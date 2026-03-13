import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        await page.goto("http://localhost:8000/gallery.html", wait_until="networkidle")
        await page.wait_for_timeout(3000)
        
        await page.screenshot(path="compare_report/gallery_drive_fixed.png", full_page=True)
        
        await browser.close()
        print("Captured")

asyncio.run(main())
