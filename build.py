from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import date

env = Environment(loader=FileSystemLoader("templates"), autoescape=False)
output_dir = Path("public")

BASE_URL = "https://eltorobattalion.org"

# Pages excluded from the sitemap (error page, not indexable content)
SITEMAP_EXCLUDE = {"404.html"}

pages_built = []
for page_path in sorted(Path("templates/pages").glob("*.html")):
    template = env.get_template(f"pages/{page_path.name}")
    output = template.render()
    (output_dir / page_path.name).write_text(output, encoding="utf-8")
    print(f"  Built: {page_path.name}")
    pages_built.append(page_path.name)

# Generate sitemap.xml
today = date.today().isoformat()
sitemap_pages = [p for p in pages_built if p not in SITEMAP_EXCLUDE]

def page_url(page):
    return f"{BASE_URL}/" if page == "index.html" else f"{BASE_URL}/{page}"

sitemap_entries = "\n".join(
    f"  <url>\n    <loc>{page_url(page)}</loc>\n    <lastmod>{today}</lastmod>\n  </url>"
    for page in sitemap_pages
)
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>
"""
(output_dir / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")
print(f"  Built: sitemap.xml ({len(sitemap_pages)} URLs)")

print("Build complete.")
