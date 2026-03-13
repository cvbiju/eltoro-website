import asyncio
from playwright.async_api import async_playwright
import json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://eltorobattalion.org/gallery/")
        # Scroll to bottom to trigger lazy loading
        for i in range(10):
            await page.evaluate("window.scrollBy(0, 1000)")
            await page.wait_for_timeout(500)
        
        # Get all images within the gallery container
        images = await page.evaluate('''() => {
            const imgs = document.querySelectorAll('.elementor-gallery-item img, .gallery-item img, .e-gallery-image');
            return Array.from(imgs).map(img => {
                if (img.style.backgroundImage) {
                    return img.style.backgroundImage.replace(/url\(['"]?(.*?)['"]?\)/i, '$1');
                }
                return img.src || img.getAttribute('data-src');
            });
        }''')
        
        # also check specific elementor widgets
        print(f"Found {len(images)} gallery images")
        for img in images[:10]:
            print(img)
            
        await browser.close()

asyncio.run(main())
