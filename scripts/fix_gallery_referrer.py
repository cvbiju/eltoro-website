with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Add referrerpolicy="no-referrer" to the img tag
text = text.replace('class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500 will-change-transform" loading="lazy"',
                    'class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500 will-change-transform" loading="lazy" referrerpolicy="no-referrer"')

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added referrerpolicy")
