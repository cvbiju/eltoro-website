import re

with open("public/gallery.html", "r") as f:
    html = f.read()

# 1. Update the Main Section to include Hero Header and Grid
new_main = """<main id="content" class="site-main flex-grow bg-gray-50" role="main">
    
    <!-- Premium Hero Header -->
    <div class="relative bg-[radial-gradient(circle_at_center,_#2a2a2a_0%,_#000000_100%)] text-white py-20 text-center border-b-[6px] border-brandRed overflow-hidden shadow-2xl">
        <div class="absolute inset-0 bg-[linear-gradient(135deg,_rgba(190,30,46,0.15)_0%,_transparent_60%)] pointer-events-none"></div>
        <div class="absolute left-0 top-0 opacity-10 pointer-events-none -translate-x-1/4 -translate-y-1/4 transform scale-150">
            <i class="fas fa-camera text-9xl"></i>
        </div>
        <div class="max-w-7xl mx-auto px-4 relative z-10">
            <h1 class="font-heading text-5xl md:text-6xl font-bold tracking-[0.2em] uppercase drop-shadow-lg">Gallery</h1>
            <p class="mt-4 text-gray-300 max-w-2xl mx-auto text-lg font-light tracking-wide">Explore moments of leadership, teamwork, and discipline from the El Toro Battalion.</p>
        </div>
    </div>

    <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div id="gallery-grid" class="gap-6 text-center" style="display: flex !important; flex-wrap: wrap; justify-content: center; width: 100% !important; clear: both;">
            <!-- Images will be injected here via JS -->
        </div>
        
        <div id="loading-spinner" class="flex flex-col justify-center items-center py-32 space-y-4">
            <div class="relative w-20 h-20">
                <div class="absolute inset-0 rounded-full border-4 border-gray-200"></div>
                <div class="absolute inset-0 rounded-full border-4 border-brandRed border-t-transparent animate-spin"></div>
            </div>
            <p class="text-gray-500 font-heading tracking-widest uppercase animate-pulse">Loading Training Archives...</p>
        </div>
        
        <div id="error-message" class="hidden text-center py-20">
            <div class="inline-block bg-white border-l-4 border-brandRed text-gray-800 p-8 rounded-xl shadow-xl max-w-lg">
                <i class="fas fa-exclamation-triangle text-4xl text-brandRed mb-4"></i>
                <h3 class="font-heading text-2xl font-bold uppercase mb-2">Connection Error</h3>
                <p id="error-text" class="text-gray-500">Failed to load gallery images.</p>
            </div>
        </div>
    </div>
</main>"""

html = re.sub(r'<main id="content".*?</main>', new_main, html, flags=re.DOTALL)


# 2. Update the Lightbox Layout
old_lightbox = r'<div id="lightbox" class="fixed inset-0 z-\[60\] bg-brandBlack/95 hidden items-center justify-center opacity-0 transition-opacity duration-300 backdrop-blur-sm">.*?</div>'
new_lightbox = """<!-- Enhanced Premium Lightbox -->
    <div id="lightbox" class="fixed inset-0 z-[60] bg-black/95 hidden items-center justify-center opacity-0 transition-all duration-500 backdrop-blur-md">
        
        <!-- Controls Header -->
        <div class="absolute top-0 left-0 right-0 h-24 bg-gradient-to-b from-black/80 to-transparent z-[70] flex justify-between items-center px-8 pointer-events-none">
            <div class="flex items-center space-x-3 pointer-events-auto">
                <img src="./assets/images/new-logo-navy.png" alt="Logo" class="h-10 opacity-70">
                <div class="hidden md:block border-l border-white/20 pl-3">
                    <p class="text-white/70 font-heading tracking-widest uppercase text-sm">El Toro Battalion</p>
                </div>
            </div>
            <button id="lightbox-close" class="pointer-events-auto text-white/50 hover:text-brandRed hover:rotate-90 transition-all duration-300 text-4xl p-2 focus:outline-none overflow-hidden" aria-label="Close Lightbox">
                <i class="fas fa-times drop-shadow-md"></i>
            </button>
        </div>

        <!-- Navigation Areas -->
        <button id="lightbox-prev" class="absolute left-0 top-0 bottom-0 w-1/6 md:w-32 flex items-center justify-start pl-4 md:pl-8 group text-white/10 hover:text-white transition-colors duration-300 z-[70] focus:outline-none" aria-label="Previous Image">
            <div class="w-16 h-16 rounded-full flex items-center justify-center bg-black/20 group-hover:bg-brandRed transition-all duration-300 transform group-hover:-translate-x-2 backdrop-blur-sm">
                <i class="fas fa-chevron-left text-3xl drop-shadow-lg"></i>
            </div>
        </button>
        
        <button id="lightbox-next" class="absolute right-0 top-0 bottom-0 w-1/6 md:w-32 flex items-center justify-end pr-4 md:pr-8 group text-white/10 hover:text-white transition-colors duration-300 z-[70] focus:outline-none" aria-label="Next Image">
            <div class="w-16 h-16 rounded-full flex items-center justify-center bg-black/20 group-hover:bg-brandRed transition-all duration-300 transform group-hover:translate-x-2 backdrop-blur-sm">
                <i class="fas fa-chevron-right text-3xl drop-shadow-lg"></i>
            </div>
        </button>
        
        <div class="relative w-full h-full flex items-center justify-center p-4 md:p-16">
            <div id="lightbox-loading" class="absolute inset-0 flex items-center justify-center">
                <div class="relative w-16 h-16">
                    <div class="absolute inset-0 rounded-full border-4 border-white/10"></div>
                    <div class="absolute inset-0 rounded-full border-4 border-brandRed border-t-transparent animate-spin"></div>
                </div>
            </div>
            <img id="lightbox-img" src="" alt="Gallery View" class="max-h-[85vh] max-w-[90vw] object-contain shadow-[0_0_50px_rgba(0,0,0,0.8)] transition-all duration-500 transform scale-90 opacity-0 rounded-sm">
        </div>
        
        <!-- Image Counter Footer -->
        <div class="absolute bottom-6 left-1/2 -translate-x-1/2 z-[70] bg-black/50 backdrop-blur-md px-6 py-2 rounded-full border border-white/10">
            <p class="text-white/70 font-sans text-sm"><span id="lightbox-counter-current" class="font-bold text-white">1</span> / <span id="lightbox-counter-total">1</span></p>
        </div>
    </div>"""

html = re.sub(old_lightbox, new_lightbox, html, flags=re.DOTALL)


# 3. Update JS Logic to integrate JS changes
# Fix imgContainer HTML and counter text
old_js_inject = r"imgContainer\.innerHTML = `.*?`;"
new_js_inject = """imgContainer.innerHTML = `
                    <div class="absolute inset-0 bg-gray-200 animate-pulse skeleton-loader z-0"></div>
                    <img src="${highResThumb}" alt="${file.name}" class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-[1.03] transition-transform duration-700 ease-out z-10" loading="lazy" referrerpolicy="no-referrer" crossorigin="anonymous" onload="this.previousElementSibling.remove()">
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-20 pointer-events-none"></div>
                    <div class="absolute inset-0 flex items-center justify-center bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-20 pointer-events-none">
                        <div class="w-16 h-16 rounded-full bg-brandRed text-white flex items-center justify-center transform scale-50 group-hover:scale-100 transition-transform duration-500 shadow-xl">
                            <i class="fas fa-expand text-2xl"></i>
                        </div>
                    </div>
                `;"""
html = re.sub(old_js_inject, new_js_inject, html, flags=re.DOTALL)

# Add Counter update to updateLightboxImage
html = html.replace("lightboxLoading.classList.remove('hidden');", """lightboxLoading.classList.remove('hidden');
            document.getElementById('lightbox-counter-current').textContent = currentIndex + 1;
            document.getElementById('lightbox-counter-total').textContent = imageList.length;""")

with open("public/gallery.html", "w") as f:
    f.write(html)
