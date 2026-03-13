import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        await page.goto("https://eltorobattalion.org/about-us/", wait_until="networkidle")
        await page.screenshot(path="about-us_live-fixed.png", full_page=True)
        
        await page.goto("http://localhost:8000/about-us.html", wait_until="networkidle")
        await page.screenshot(path="about-us_local-fixed.png", full_page=True)
        
        await browser.close()
        print("Screenshots taken.")

asyncio.run(main())
