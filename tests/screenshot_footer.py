import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        await page.goto("http://localhost:8000/index.html", wait_until="networkidle")
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="index_local_footer.png")
        
        await browser.close()
        print("Footer screenshot taken.")

asyncio.run(main())
