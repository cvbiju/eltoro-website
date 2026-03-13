with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the thumbnailLink parsing with a hardcoded drive.google.com/thumbnail URL
import re

text = re.sub(
    r'const highResThumb = file\.thumbnailLink\.replace\([^,]+,\s*\'=s\d+\'\);',
    'const highResThumb = `https://drive.google.com/thumbnail?id=${file.id}&sz=w600`;',
    text
)

text = re.sub(
    r'const highResUrl = file\.webContentLink \|\| file\.thumbnailLink\.replace\([^,]+,\s*\'=s\d+\'\);',
    'const highResUrl = `https://drive.google.com/thumbnail?id=${file.id}&sz=w2048`;',
    text
)

text = re.sub(
    r'const thumbUrl = file\.thumbnailLink\.replace\([^,]+,\s*\'=s\d+\'\);',
    'const thumbUrl = `https://drive.google.com/thumbnail?id=${file.id}&sz=w1024`;',
    text
)

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated URL format")
