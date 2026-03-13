import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        await page.goto("http://localhost:8000/gallery.html", wait_until="networkidle")
        await page.evaluate("window.scrollTo(0, 500)")
        await page.wait_for_timeout(2000)
        
        await page.screenshot(path="compare_report/gallery_local.png", full_page=True)
        
        await browser.close()
        print("Gallery screenshot generated.")

asyncio.run(main())
