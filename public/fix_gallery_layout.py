with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

grid_html = '''    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div id="gallery-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4" style="display: grid !important;">
            <!-- Images will be injected here via JS -->
        </div>
        <div id="loading-spinner" class="flex justify-center items-center py-20">
            <i class="fas fa-circle-notch fa-spin text-4xl text-brandRed"></i>
        </div>
        <div id="error-message" class="hidden text-center py-20">
            <div class="inline-block bg-red-100 border-l-4 border-brandRed text-red-700 p-4 rounded shadow">
                <p class="font-bold flex items-center justify-center"><i class="fas fa-exclamation-triangle mr-2"></i> Error</p>
                <p id="error-text">Failed to load gallery images.</p>
            </div>
        </div>
    </div>
    <script>'''

text = text.replace('    <script>', grid_html)

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored layout!")
