with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# The Elementor CSS is too aggressive, overriding the style.display = 'grid' due to specificity.
# We will rip out the Elementor CSS completely for the gallery tag, and let Tailwind handle it.

text = text.replace('class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 hidden"', 'class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4" style="display: grid !important;"')

text = text.replace('galleryGrid.style.display = \'grid\';', 'galleryGrid.style.setProperty("display", "grid", "important");')

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Forced CSS Grid via inline !important")
