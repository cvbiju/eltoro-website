import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        await page.goto("http://localhost:8000/about-us.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="../public/compare_report/about-us_local.png", full_page=True)

        await page.goto("http://localhost:8000/meet-the-officers.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="../public/compare_report/meet-the-officers_local.png", full_page=True)
        
        await browser.close()
        print("Screenshots taken.")

asyncio.run(main())
