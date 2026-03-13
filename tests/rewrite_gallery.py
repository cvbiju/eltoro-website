import urllib.request
import re

url = "https://eltorobattalion.org/gallery/"
req = urllib.request.Request(url, headers={'User-Agent': Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
except Exception as e:
    import urllib.request as ur
    req = ur.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = ur.urlopen(req).read().decode('utf-8')

# Find all gallery images
images = re.findall(r'data-thumbnail="([^"]+)"', html)
# ensure uniqueness
unique_images = []
for img in images:
    if img not in unique_images and 'gallery-img' in img:
        unique_images.append(img)

print(f"Found {len(unique_images)} gallery images.")

grid_html = ""
for i, img_url in enumerate(unique_images):
    grid_html += f'''
                <div class="relative group overflow-hidden bg-gray-200 cursor-pointer shadow-md fade-in hover:shadow-xl transition-all duration-300 rounded" style="padding-bottom: 100%;">
                    <img src="{img_url}" alt="Gallery Image {i+1}" class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500 will-change-transform" loading="lazy" onclick="openStaticLightbox({i})">
                    <div class="absolute inset-0 bg-brandBlack/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center backdrop-blur-sm pointer-events-none">
                        <i class="fas fa-search-plus text-white text-3xl transform scale-50 group-hover:scale-100 transition-transform duration-300"></i>
                    </div>
                </div>'''

# array string for JS
js_array = "const staticImages = [" + ", ".join([f"'{img}'" for img in unique_images]) + "];"

new_script = f'''
    <script>
        {js_array}
        
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxClose = document.getElementById('lightbox-close');
        const lightboxPrev = document.getElementById('lightbox-prev');
        const lightboxNext = document.getElementById('lightbox-next');
        const lightboxLoading = document.getElementById('lightbox-loading');
        
        let currentIndex = 0;

        function openStaticLightbox(index) {{
            currentIndex = index;
            lightbox.classList.remove('hidden');
            lightbox.classList.add('flex');
            void lightbox.offsetWidth;
            lightbox.classList.remove('opacity-0');
            
            updateLightbox();
            document.body.style.overflow = 'hidden';
        }}

        function updateLightbox() {{
            lightboxImg.classList.add('opacity-0', 'scale-95');
            lightboxLoading.classList.remove('hidden');
            
            const imgUrl = staticImages[currentIndex];
            const tmpImg = new Image();
            tmpImg.onload = () => {{
                lightboxImg.src = tmpImg.src;
                lightboxLoading.classList.add('hidden');
                setTimeout(() => {{
                    lightboxImg.classList.remove('opacity-0', 'scale-95');
                    lightboxImg.classList.add('opacity-100', 'scale-100');
                }}, 50);
            }};
            tmpImg.src = imgUrl;
            
            lightboxPrev.style.display = currentIndex > 0 ? 'block' : 'none';
            lightboxNext.style.display = currentIndex < staticImages.length - 1 ? 'block' : 'none';
        }}

        function closeLightbox() {{
            lightbox.classList.add('opacity-0');
            setTimeout(() => {{
                lightbox.classList.add('hidden');
                lightbox.classList.remove('flex');
                lightboxImg.src = '';
                document.body.style.overflow = '';
            }}, 300);
        }}

        function showPrev() {{ if (currentIndex > 0) openStaticLightbox(currentIndex - 1); }}
        function showNext() {{ if (currentIndex < staticImages.length - 1) openStaticLightbox(currentIndex + 1); }}

        lightboxClose.addEventListener('click', closeLightbox);
        lightboxPrev.addEventListener('click', showPrev);
        lightboxNext.addEventListener('click', showNext);
        lightbox.addEventListener('click', (e) => {{ if (e.target === lightbox) closeLightbox(); }});
        
        document.addEventListener('keydown', (e) => {{
            if (!lightbox.classList.contains('hidden')) {{
                if (e.key === 'Escape') closeLightbox();
                else if (e.key === 'ArrowLeft') showPrev();
                else if (e.key === 'ArrowRight') showNext();
            }}
        }});

        // Unhide grid natively
        document.addEventListener('DOMContentLoaded', () => {{
            document.getElementById('loading-spinner').classList.add('hidden');
            const grid = document.getElementById('gallery-grid');
            grid.classList.remove('hidden');
            grid.classList.add('animate-fade-in');
        }});
    </script>
'''

with open('../public/gallery.html', 'r') as f:
    content = f.read()

import re
# Replace the empty grid with populated grid
content = re.sub(
    r'<div id="gallery-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 hidden">[\s\S]*?</div>',
    f'<div id="gallery-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 hidden">\n{grid_html}\n            </div>',
    content
)

# Replace the old scripts with static scripts
content = re.sub(
    r'<script>\s*const FOLDER_ID[\s\S]*?</script>',
    new_script,
    content
)

with open('../public/gallery.html', 'w') as f:
    f.write(content)
print("Gallery HTML updated with static images!")
