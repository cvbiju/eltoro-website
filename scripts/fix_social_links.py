import os
import glob

# The old links look like:
# <a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-facebook-f"></i></a>
# <a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-instagram"></i></a>

target_dir = "/Users/bchandr1/Documents/my-agy-projects/ETB/public"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

fb_old = '<a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-facebook-f"></i></a>'
fb_new = '<a href="https://www.facebook.com/eltoro.battalion/" target="_blank" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-facebook-f"></i></a>'

ig_old = '<a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-instagram"></i></a>'
ig_new = '<a href="https://www.instagram.com/eltorobattalion/" target="_blank" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-instagram"></i></a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if fb_old in content or ig_old in content:
        content = content.replace(fb_old, fb_new)
        content = content.replace(ig_old, ig_new)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {os.path.basename(file)}")
