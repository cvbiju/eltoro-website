with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# drop all the 106 images we just injected
text = re.sub(
    r'<div id="gallery-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 hidden">[\s\S]*?</div>(\s*)<div id="error-message"',
    r'<div id="gallery-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 hidden">\n                <!-- Images will be injected here via JS -->\n            </div>\g<1><div id="error-message"',
    text
)

# Replace script using literal replacement
start_marker = '<script>'
end_marker = '</script>'
start_idx = text.rfind(start_marker)

new_script = '''<script>
        const FOLDER_ID = '1Y0uWE60pYLVFaOKMQLIeYzUdCa25cD66';
        const API_KEY = 'AIzaSyBQKSzsRbkW5HFs9TFY46Zb8CvnOslC1kU';
        const API_URL = `https://www.googleapis.com/drive/v3/files?q='${FOLDER_ID}'+in+parents+and+mimeType+contains+'image/'&key=${API_KEY}&fields=files(id,name,mimeType,thumbnailLink,webContentLink)&pageSize=200`;

        const galleryGrid = document.getElementById('gallery-grid');
        const loadingSpinner = document.getElementById('loading-spinner');
        const errorMessage = document.getElementById('error-message');
        const errorText = document.getElementById('error-text');

        let imageList = [];
        let currentIndex = 0;

        async function fetchImages() {
            try {
                const response = await fetch(API_URL);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                
                if (data.files && data.files.length > 0) {
                    imageList = data.files.filter(file => file.thumbnailLink);
                    renderGallery(imageList);
                } else {
                    showError('No images found in the specified gallery folder.');
                }
            } catch (error) {
                console.error('Error fetching images:', error);
                showError('Failed to load gallery images. Note: Google Drive API blocks direct origin access via local IP depending on project settings. Try running through localhost directly.');
            }
        }

        function renderGallery(images) {
            loadingSpinner.classList.add('hidden');
            galleryGrid.innerHTML = '';
            galleryGrid.classList.remove('hidden');
            galleryGrid.classList.add('animate-fade-in');

            images.forEach((file, index) => {
                const highResThumb = file.thumbnailLink.replace(/=s\\d+$/, '=s600');
                
                const imgContainer = document.createElement('div');
                imgContainer.className = 'relative group overflow-hidden bg-gray-200 cursor-pointer shadow-md fade-in hover:shadow-xl transition-all duration-300 rounded';
                imgContainer.style.paddingBottom = '100%'; 
                
                imgContainer.innerHTML = `
                    <img src="${highResThumb}" alt="${file.name}" class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500 will-change-transform" loading="lazy">
                    <div class="absolute inset-0 bg-brandBlack/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center backdrop-blur-sm pointer-events-none">
                        <i class="fas fa-search-plus text-white text-3xl transform scale-50 group-hover:scale-100 transition-transform duration-300"></i>
                    </div>
                `;
                
                imgContainer.addEventListener('click', () => openLightbox(index));
                galleryGrid.appendChild(imgContainer);
            });
        }

        function showError(msg) {
            loadingSpinner.classList.add('hidden');
            errorMessage.classList.remove('hidden');
            errorText.textContent = msg;
        }

        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxClose = document.getElementById('lightbox-close');
        const lightboxPrev = document.getElementById('lightbox-prev');
        const lightboxNext = document.getElementById('lightbox-next');
        const lightboxLoading = document.getElementById('lightbox-loading');

        function openLightbox(index) {
            currentIndex = index;
            lightbox.classList.remove('hidden');
            lightbox.classList.add('flex');
            void lightbox.offsetWidth;
            lightbox.classList.remove('opacity-0');
            updateLightboxImage();
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            lightbox.classList.add('opacity-0');
            setTimeout(() => {
                lightbox.classList.add('hidden');
                lightbox.classList.remove('flex');
                lightboxImg.src = '';
                document.body.style.overflow = '';
            }, 300);
        }

        function updateLightboxImage() {
            lightboxImg.classList.add('opacity-0', 'scale-95');
            lightboxLoading.classList.remove('hidden');
            
            const file = imageList[currentIndex];
            const highResUrl = file.webContentLink || file.thumbnailLink.replace(/=s\\d+$/, '=s2048');
            
            const tmpImg = new Image();
            tmpImg.onload = () => {
                lightboxImg.src = tmpImg.src;
                lightboxLoading.classList.add('hidden');
                setTimeout(() => {
                    lightboxImg.classList.remove('opacity-0', 'scale-95');
                    lightboxImg.classList.add('opacity-100', 'scale-100');
                }, 50);
            };
            tmpImg.onerror = () => {
                const thumbUrl = file.thumbnailLink.replace(/=s\\d+$/, '=s1024');
                lightboxImg.src = thumbUrl;
                lightboxLoading.classList.add('hidden');
                setTimeout(() => {
                    lightboxImg.classList.remove('opacity-0', 'scale-95');
                    lightboxImg.classList.add('opacity-100', 'scale-100');
                }, 50);
            };
            tmpImg.src = highResUrl;
            
            lightboxPrev.style.display = currentIndex > 0 ? 'block' : 'none';
            lightboxNext.style.display = currentIndex < imageList.length - 1 ? 'block' : 'none';
        }

        function showPrev() {
            if (currentIndex > 0) {
                currentIndex--;
                updateLightboxImage();
            }
        }

        function showNext() {
            if (currentIndex < imageList.length - 1) {
                currentIndex++;
                updateLightboxImage();
            }
        }

        lightboxClose.addEventListener('click', closeLightbox);
        lightboxPrev.addEventListener('click', showPrev);
        lightboxNext.addEventListener('click', showNext);
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (!lightbox.classList.contains('hidden')) {
                if (e.key === 'Escape') closeLightbox();
                else if (e.key === 'ArrowLeft') showPrev();
                else if (e.key === 'ArrowRight') showNext();
            }
        });

        document.addEventListener('DOMContentLoaded', fetchImages);
    </script>'''

text = text[:start_idx] + new_script

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Reverted to Original Google Drive API Setup")
