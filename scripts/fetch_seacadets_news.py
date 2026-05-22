"""Fetch content from seacadets.org and write JSON files for the News page.

Outputs:
  public/seacadets-news.json      — latest 5 news posts from the RSS feed
  public/seacadets-magazines.json — Seafarer Magazine archive from the REST API

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

NEWS_OUTPUT = REPO_ROOT / "public" / "seacadets-news.json"
MAGAZINES_OUTPUT = REPO_ROOT / "public" / "seacadets-magazines.json"

MAX_NEWS = 5


# ── helpers ──────────────────────────────────────────────────────────────────

def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "").strip()


def decode(text: str) -> str:
    return htmllib.unescape(text or "")


def clean_description(text: str) -> str:
    text = decode(strip_html(text))
    text = re.sub(r"The post .+ appeared first on .+\.\s*$", "", text, flags=re.DOTALL).strip()
    return text


def truncate(text: str, length: int = 220) -> str:
    return text[:length].rstrip() + "…" if len(text) > length else text




# ── fetch news ───────────────────────────────────────────────────────────────

def fetch_news() -> dict:
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

        items.append({
            "title": decode(strip_html(item.findtext("title", ""))),
            "link": link,
            "date": formatted,
            "description": truncate(clean_description(item.findtext("description", ""))),
        })

    return {"updated": datetime.now(timezone.utc).strftime("%B %d, %Y"), "items": items}


# ── fetch magazines ──────────────────────────────────────────────────────────

def fetch_magazines() -> dict:
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


# ── main ─────────────────────────────────────────────────────────────────────

news = fetch_news()
NEWS_OUTPUT.write_text(json.dumps(news, indent=2))
print(f"Wrote {len(news['items'])} news items → {NEWS_OUTPUT}")

magazines = fetch_magazines()
MAGAZINES_OUTPUT.write_text(json.dumps(magazines, indent=2))
print(f"Wrote {len(magazines['magazines'])} magazines → {MAGAZINES_OUTPUT}")
