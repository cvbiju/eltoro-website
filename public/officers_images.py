import urllib.request
from bs4 import BeautifulSoup

url = "https://eltorobattalion.org/meet-the-officers/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')

print("--- Image Tags ---")
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'data:image' not in src and 'wp-content/plugins' not in src and 'logo' not in src.lower():
        print(f"SRC: {src}")
