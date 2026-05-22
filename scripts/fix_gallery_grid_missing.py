with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I accidentally deleted the entire grid div. It should sit right before the error message and loading spinner
grid_html = '''
            <div id="gallery-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4" style="display: grid !important;">
                <!-- Images will be injected here via JS -->
            </div>
'''
text = text.replace('<div id="error-message"', grid_html + '            <div id="error-message"')

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored missing #gallery-grid div")
