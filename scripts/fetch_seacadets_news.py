"""Fetch content from seacadets.org and write JSON files for the News page.

Outputs:
  public/seacadets-news.json      — latest 5 news posts from the RSS feed
  public/seacadets-magazines.json — Seafarer Magazine archive from the REST API

Enriched fields (original_link, description, image) are preserved from the
existing JSON so that enrich_news_articles.py doesn't need to re-scrape
articles that have already been processed.

Run manually: python3 scripts/fetch_seacadets_news.py
Run by GitHub Actions: .github/workflows/fetch-news.yml (nightly)
"""
import html as htmllib
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ETBNewsBot/1.0)"}

RSS_URL = "https://www.seacadets.org/feed/"
MAGAZINES_API = "https://www.seacadets.org/wp-json/wp/v2/pages?slug=seafarer-magazines&_fields=content"
NEWSROOM_API = "https://www.seacadets.org/wp-json/wp/v2/pages?slug=newsroom&_fields=content"

NEWS_OUTPUT = REPO_ROOT / "public" / "seacadets-news.json"
MAGAZINES_OUTPUT = REPO_ROOT / "public" / "seacadets-magazines.json"
ANNUAL_REPORTS_OUTPUT = REPO_ROOT / "public" / "seacadets-annual-reports.json"

MAX_NEWS = 5


# ── helpers ──────────────────────────────────────────────────────────────────

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def strip_html(text):
    return re.sub(r"<[^>]+>", "", text or "").strip()


def decode(text):
    return htmllib.unescape(text or "")


# ── fetch news ───────────────────────────────────────────────────────────────

def fetch_news():
    # Load existing JSON to preserve enriched fields (original_link, description, image)
    # keyed by seacadets.org permalink so enrichment work is never repeated.
    enrichment_cache = {}
    if NEWS_OUTPUT.exists():
        try:
            existing = json.loads(NEWS_OUTPUT.read_text())
            enrichment_cache = {item["link"]: item for item in existing.get("items", [])}
        except (json.JSONDecodeError, KeyError):
            pass

    root = ET.fromstring(fetch(RSS_URL))
    items = []
    for item in root.find("channel").findall("item")[:MAX_NEWS]:
        pub_date = item.findtext("pubDate", "")
        try:
            dt = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
            formatted = dt.strftime("%B %d, %Y")
        except ValueError:
            formatted = pub_date

        raw_link = (item.findtext("link", "") or "").strip()
        link = raw_link.split("?")[0] if "?" in raw_link else raw_link

        cached = enrichment_cache.get(link, {})
        items.append({
            "title": decode(strip_html(item.findtext("title", ""))),
            "link": link,
            # original_link: set by enrich_news_articles.py; null until then.
            # Falls back to seacadets.org permalink in the template.
            "original_link": cached.get("original_link", None),
            "date": formatted,
            "description": cached.get("description", ""),
            "image": cached.get("image", ""),
        })

    return {"updated": datetime.now(timezone.utc).strftime("%B %d, %Y"), "items": items}


# ── fetch magazines ──────────────────────────────────────────────────────────

def fetch_magazines():
    data = json.loads(fetch(MAGAZINES_API))
    content_html = decode(data[0]["content"]["rendered"])

    # Build div-ID → PDF URL map from jQuery click handlers
    # Pattern: jQuery("#SeafarerMagazine-4480").on("click", ... window.open("URL.pdf" ...
    pdf_map = {
        m.group(1): m.group(2)
        for m in re.finditer(
            r'jQuery\("#(SeafarerMagazine-\d+)"\)\.on\("click".*?window\.open\("([^"]+\.pdf)"',
            content_html,
            re.DOTALL,
        )
    }

    # Parse each magazine div: id → cover URL + title
    magazines = []
    for m in re.finditer(
        r'<div id="(SeafarerMagazine-\d+)"[^>]+class="SeafarerMagazine"[^>]*>.*?'
        r'background-image:\s*url\([\'"]?([^\'")\s]+)[\'"]?\).*?'
        r'<h3[^>]*>(.*?)</h3>',
        content_html,
        re.DOTALL | re.IGNORECASE,
    ):
        div_id = m.group(1)
        cover_url = m.group(2)
        title = decode(strip_html(m.group(3))).strip()
        pdf_url = pdf_map.get(div_id)

        if pdf_url:
            magazines.append({"title": title, "cover": cover_url, "pdf": pdf_url})

    return {"updated": datetime.now(timezone.utc).strftime("%B %d, %Y"), "magazines": magazines}


# ── fetch annual reports ─────────────────────────────────────────────────────

def fetch_annual_reports():
    data = json.loads(fetch(NEWSROOM_API))
    content_html = decode(data[0]["content"]["rendered"])

    # Build div-ID → PDF URL map from jQuery click handlers
    # Pattern: jQuery("#AnnualReport-4474").on("click", ... window.open("URL.pdf" ...
    pdf_map = {
        m.group(1): m.group(2)
        for m in re.finditer(
            r'jQuery\("#(AnnualReport-\d+)"\)\.on\("click".*?window\.open\("([^"]+\.pdf)"',
            content_html,
            re.DOTALL,
        )
    }

    # Parse each report div: id → cover URL + title
    reports = []
    for m in re.finditer(
        r'<div id="(AnnualReport-\d+)"[^>]+class="AnnualReport"[^>]*>.*?'
        r'background-image:\s*url\([\'"]?([^\'")\s]+)[\'"]?\).*?'
        r'<h3[^>]*>(.*?)</h3>',
        content_html,
        re.DOTALL | re.IGNORECASE,
    ):
        div_id = m.group(1)
        cover_url = m.group(2)
        title = decode(strip_html(m.group(3))).strip()
        pdf_url = pdf_map.get(div_id)

        if pdf_url:
            reports.append({"title": title, "cover": cover_url, "pdf": pdf_url})

    return {"updated": datetime.now(timezone.utc).strftime("%B %d, %Y"), "reports": reports}


# ── main ─────────────────────────────────────────────────────────────────────

news = fetch_news()
NEWS_OUTPUT.write_text(json.dumps(news, indent=2))
unenriched = sum(1 for i in news["items"] if not i.get("original_link"))
print(f"Wrote {len(news['items'])} news items → {NEWS_OUTPUT}  ({unenriched} need enrichment)")

magazines = fetch_magazines()
MAGAZINES_OUTPUT.write_text(json.dumps(magazines, indent=2))
print(f"Wrote {len(magazines['magazines'])} magazines → {MAGAZINES_OUTPUT}")

reports = fetch_annual_reports()
ANNUAL_REPORTS_OUTPUT.write_text(json.dumps(reports, indent=2))
print(f"Wrote {len(reports['reports'])} annual reports → {ANNUAL_REPORTS_OUTPUT}")
