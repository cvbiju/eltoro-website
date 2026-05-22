import os
import glob
import re

target_dir = "/Users/bchandr1/Documents/my-agy-projects/ETB/public"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

fb_pattern = r'<a href="#"([^>]*?)><i class="fab fa-facebook-f"></i></a>'
fb_new = r'<a href="https://www.facebook.com/eltoro.battalion/" target="_blank"\1><i class="fab fa-facebook-f"></i></a>'

ig_pattern = r'<a href="#"([^>]*?)><i class="fab fa-instagram"></i></a>'
ig_new = r'<a href="https://www.instagram.com/eltorobattalion/" target="_blank"\1><i class="fab fa-instagram"></i></a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if re.search(fb_pattern, content):
        content = re.sub(fb_pattern, fb_new, content)
        modified = True
    
    if re.search(ig_pattern, content):
        content = re.sub(ig_pattern, ig_new, content)
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {os.path.basename(file)}")
