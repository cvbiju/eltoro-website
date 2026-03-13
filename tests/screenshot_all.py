import asyncio
from playwright.async_api import async_playwright
import os

pages = [
    ("", "index"),
    ("about-us/", "about-us"),
    ("about-us/meet-the-officers/", "meet-the-officers"),
    ("cadet-mess/", "cadet-mess"),
    ("cadet-mess/general-knowledge/", "general-knowledge"),
    ("cadet-mess/physical-fitness/", "physical-fitness"),
    ("cadet-mess/grooming-uniform/", "grooming-uniform"),
    ("parents/", "parents"),
    ("calendar/", "calendar"),
    ("gallery/", "gallery"),
    ("enrollment/", "enrollment"),
    ("programs/", "programs")
]

live_base = "https://eltorobattalion.org/"
local_base = "http://localhost:8000/"
out_dir = "screenshots"
os.makedirs(out_dir, exist_ok=True)

html_out = "<html><head><style>body{font-family:sans-serif;} .row{display:flex;margin-bottom:50px;} .col{flex:1;padding:10px;} img{max-width:100%; border:1px solid #ccc;}</style></head><body><h1>Page Comparisons</h1>"

async def take_screenshot(page_obj, url, filename):
    print(f"Loading {url}...")
    try:
        await page_obj.goto(url, wait_until="networkidle", timeout=30000)
        await page_obj.wait_for_timeout(2000) # Give extra time for fonts/images
        await page_obj.screenshot(path=filename, full_page=True)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Failed {url}: {e}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page_obj = await context.new_page()
        
        global html_out
        
        for live_path, local_name in pages:
            live_url = live_base + live_path
            local_url = local_base + local_name + ".html"
            
            live_file = f"{out_dir}/{local_name}_live.png"
            local_file = f"{out_dir}/{local_name}_local.png"
            
            await take_screenshot(page_obj, live_url, live_file)
            await take_screenshot(page_obj, local_url, local_file)
            
            html_out += f"<h2>{local_name.upper()}</h2><div class='row'>"
            html_out += f"<div class='col'><h3>Live ({live_url})</h3><img src='{local_name}_live.png' loading='lazy'></div>"
            html_out += f"<div class='col'><h3>Local ({local_url})</h3><img src='{local_name}_local.png' loading='lazy'></div>"
            html_out += "</div><hr>"
            
        await browser.close()
        
        with open(f"{out_dir}/report.html", "w") as f:
            html_out += "</body></html>"
            f.write(html_out)
        print("Done! Open tests/screenshots/report.html to view side-by-side comparisons.")

asyncio.run(main())
