"""Enrich news articles with original source URLs and article descriptions.

For each item in seacadets-news.json that is missing original_link:
  1. Fetch og:description and og:image from the seacadets.org page <head>
     (server-rendered Yoast meta tags — no browser needed).
  2. Use Playwright (headless Chromium) to render the Divi page and extract
     the first outbound link pointing to the original news source.

Results are written back to seacadets-news.json in place. The fetch script
preserves these fields on subsequent runs, so Playwright only runs once
per unique article.

Run manually: python3 scripts/enrich_news_articles.py
  (requires: pip3 install playwright && python3 -m playwright install chromium)
Run by GitHub Actions: .github/workflows/fetch-news.yml (conditionally)
"""
import html as htmllib
import json
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
NEWS_JSON = REPO_ROOT / "public" / "seacadets-news.json"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ETBNewsBot/1.0)"}

# Domains that are never the "original article" source — skip links to these
# even if they appear in the Divi-rendered body.
SKIP_DOMAINS = [
    "seacadets.org",
    "facebook.com", "twitter.com", "x.com", "instagram.com",
    "youtube.com", "linkedin.com",
    "qgiv.com", "secure.qgiv.com",
    "googletagmanager.com", "google.com", "googleapis.com",
    "hotjar.com", "monsterinsights.com", "analytify.io",
    "peeayecreative.com", "gravatar.com",
    "wordpress.org", "wordpress.com",
]


# ── og: meta (fast, no Playwright) ───────────────────────────────────────────

def fetch_og_meta(url):
    """Return og:description and og:image from the page <head>."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        print(f"    [og fetch failed: {exc}]")
        return {"description": "", "image": ""}

    def find_meta(prop):
        # Handle both attribute orderings Yoast may emit.
        # Use [\"'] character class (double-quoted f-string) to avoid raw-string escaping issues.
        q = r"""["']"""
        p = re.escape(prop)
        m = re.search(
            rf'property={q}{p}{q}[^>]*?content={q}(.*?){q}',
            html,
        ) or re.search(
            rf'content={q}(.*?){q}[^>]*?property={q}{p}{q}',
            html,
        )
        return htmllib.unescape(m.group(1)).strip() if m else ""

    return {
        "description": find_meta("og:description"),
        "image": find_meta("og:image"),
    }


# ── Playwright extraction ─────────────────────────────────────────────────────

# Injected into the rendered page to locate the best outbound article link.
_FIND_LINK_JS = """() => {
    const skipDomains = """ + json.dumps(SKIP_DOMAINS) + """;

    const isExternal = href => {
        if (!href || !href.startsWith('http')) return false;
        return !skipDomains.some(d => href.includes(d));
    };

    // Exclude links that live inside nav, header, or footer chrome.
    const isChrome = el => !!el.closest(
        'header, #top-header, #main-header, #et-navigation, ' +
        'footer, #footer-widgets, #footer-bottom, .et_pb_footer_bottom_bar, ' +
        '.et_pb_menu, nav'
    );

    const candidates = Array.from(document.querySelectorAll('a[href]'))
        .filter(el => isExternal(el.href) && !isChrome(el));

    if (!candidates.length) return null;

    // Prefer a link whose visible text signals "read more" / "original story".
    const keywords = ['read', 'original', 'source', 'story', 'article', 'full', 'here', 'click', 'visit'];
    const priority = candidates.find(el => {
        const t = el.textContent.toLowerCase().trim();
        return keywords.some(k => t.includes(k));
    });

    return (priority || candidates[0]).href;
}"""


def extract_original_url(page, url):
    """Navigate to a seacadets.org post and return the first outbound article link."""
    from playwright.sync_api import TimeoutError as PWTimeout
    try:
        page.goto(url, wait_until="networkidle", timeout=30000)
    except PWTimeout:
        # networkidle can hang on analytics scripts; domcontentloaded is enough
        # for Divi to finish injecting its content modules.
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=20000)
            page.wait_for_timeout(3000)
        except PWTimeout:
            print("    [timeout loading page]")
            return None

    return page.evaluate(_FIND_LINK_JS)


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    data = json.loads(NEWS_JSON.read_text())
    items = data["items"]

    unenriched = [item for item in items if not item.get("original_link")]
    if not unenriched:
        print("All articles already enriched — nothing to do.")
        return

    print(f"Enriching {len(unenriched)} article(s)…")

    # ── Step 1: og: meta via plain HTTP (fast) ────────────────────────────────
    for item in unenriched:
        meta = fetch_og_meta(item["link"])

        # Only use og:description if it adds information beyond the title.
        # seacadets.org sometimes sets og:description == og:title for thin posts.
        desc = meta["description"]
        if desc and desc.strip().lower() != item["title"].strip().lower():
            if not item.get("description"):
                item["description"] = desc

        if meta["image"] and not item.get("image"):
            item["image"] = meta["image"]

        print(f"  og: fetched — {item['title'][:70]}")

    # ── Step 2: Playwright for original article URLs ──────────────────────────
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright not installed. Run: pip3 install playwright && python3 -m playwright install chromium", file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        )
        page = context.new_page()

        # Block images, fonts, and media — we only need the DOM for link extraction.
        page.route(
            "**/*.{png,jpg,jpeg,gif,webp,svg,ico,woff,woff2,ttf,eot,mp4,webm}",
            lambda route: route.abort(),
        )

        for item in unenriched:
            print(f"  Playwright → {item['link']}")
            original = extract_original_url(page, item["link"])
            if original:
                item["original_link"] = original
                print(f"    ✓ original: {original}")
            else:
                # Fall back to the newsroom index — the individual permalinks render blank
                # (Divi JS required), so the newsroom listing is a better destination.
                item["original_link"] = "https://www.seacadets.org/newsroom/sea-cadets-in-the-news/"
                print(f"    ! no outbound link found; falling back to newsroom index")

        browser.close()

    NEWS_JSON.write_text(json.dumps(data, indent=2))
    print(f"\nWrote enriched JSON → {NEWS_JSON}")


if __name__ == "__main__":
    main()
