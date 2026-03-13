with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

text = re.sub(
    r'const highResThumb = `https://drive\.google\.com/uc\?export=view&id=\$\{file\.id\}`;',
    'const highResThumb = `https://www.googleapis.com/drive/v3/files/${file.id}?alt=media&key=${API_KEY}`;',
    text
)

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated URL format to alt=media")
