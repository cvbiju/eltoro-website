import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        await page.goto("http://localhost:8000/physical-fitness.html", wait_until="networkidle")
        await page.evaluate("window.scrollTo(0, 300)")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="../public/compare_report/physical-fitness_local.png", full_page=True)

        await page.goto("http://localhost:8000/general-knowledge.html", wait_until="networkidle")
        await page.evaluate("window.scrollTo(0, 300)")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="../public/compare_report/general-knowledge_local.png", full_page=True)
        
        await page.goto("http://localhost:8000/grooming-uniform.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="../public/compare_report/grooming-uniform_local.png", full_page=True)

        await browser.close()
        print("Screenshots taken.")

asyncio.run(main())
