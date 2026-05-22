import urllib.request
from bs4 import BeautifulSoup
import re

pages = [
    ("", "index.html"),
    ("about-us/", "about-us.html"),
    ("about-us/meet-the-officers/", "meet-the-officers.html"),
    ("cadet-mess/", "cadet-mess.html"),
    ("cadet-mess/general-knowledge/", "general-knowledge.html"),
    ("cadet-mess/physical-fitness/", "physical-fitness.html"),
    ("cadet-mess/grooming-uniform/", "grooming-uniform.html"),
    ("parents/", "parents.html"),
    ("calendar/", "calendar.html"),
    ("gallery/", "gallery.html"),
    ("enrollment/", "enrollment.html"),
    ("programs/", "programs.html")
]

live_base = "https://eltorobattalion.org/"
local_base = "http://localhost:8000/"

def get_text(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Remove nav, footer, scripts to focus strictly on body content
        for sel in ["nav", "footer", "script", "style", "header"]:
            for el in soup.find_all(sel):
                el.decompose()

        text = soup.get_text(separator=' ', strip=True)
        # Normalize whitespace
        text = re.sub(r'\\s+', ' ', text)
        return text
    except Exception as e:
        return f"ERROR: {e}"

print("Starting page comparison...")
for live_path, local_file in pages:
    live_url = live_base + live_path
    local_url = local_base + local_file
    
    live_text = get_text(live_url)
    local_text = get_text(local_url)
    
    if "ERROR" in live_text or "ERROR" in local_text:
        print(f"[{local_file}] -> Failed to load one of the pages. Live/Local sizes: {len(live_text)} / {len(local_text)}")
        continue
        
    # very basic length diff to spot massive missing sections
    diff = abs(len(live_text) - len(local_text))
    percent = (diff / max(len(live_text), 1)) * 100
    
    if percent > 15:
         print(f"[{local_file}] -> ⚠️ Significant mismatch: Live ({len(live_text)} chars) vs Local ({len(local_text)} chars). Difference: {percent:.1f}%")
    else:
         print(f"[{local_file}] -> ✅ Content length matches closely (within {percent:.1f}% deviation).")

print("Done.")
