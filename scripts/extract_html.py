import re

with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/live_enrollment.html", "r") as f:
    content = f.read()

# Extract Hero section:
hero_match = re.search(r'<div class="elementor-element elementor-element-7e00cc3.*?</div>\s*</div>\s*</div>', content, re.DOTALL)
hero_html = hero_match.group(0) if hero_match else ""

# Extract Content section (Requirements + Form):
# It starts at 8d58124 and ends before the footer 171
content_match = re.search(r'<div class="elementor-element elementor-element-8d58124.*?<!-- end content -->', content + "<!-- end content -->", re.DOTALL)
# wait, better to just split by <div data-elementor-type="footer"
parts = content.split('<div data-elementor-type="footer"')
content_html = parts[0].split('<div data-elementor-type="wp-page" data-elementor-id="1107" class="elementor elementor-1107" data-elementor-post-type="page">')[1]

# Instead of raw Elementor HTML which might be heavily nested and rely on thousands of lines of CSS, 
# I can build a clean Tailwind equivalent. The user wants the form to look exactly like the live site.
