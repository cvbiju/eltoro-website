import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://eltorobattalion.org/about-us/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')

print("--- Background Images ---")
bg_tags = soup.find_all(style=re.compile("background-image"))
for bg in bg_tags:
    print(bg.get('style'))

print("\\n--- Image Tags ---")
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'data:image' not in src and 'wp-content/plugins' not in src:
        classes = img.get('class', '')
        print(f"SRC: {src}\\n  CLASSES: {classes}\\n  WIDTH: {img.get('width')} HEIGHT: {img.get('height')}\\n")
