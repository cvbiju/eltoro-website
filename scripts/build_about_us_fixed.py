import re

# Read base HTML (index.html is a good source for the accurate header/footer)
with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/index.html", "r") as f:
    orig = f.read()

# Extract header and footer
header_match = re.search(r'(<header.*?</header>)', orig, re.DOTALL)
header_html = header_match.group(1) if header_match else ""

footer_match = re.search(r'(<footer.*?</footer>)', orig, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""

# Extract <head>
head_match = re.search(r'(<head>.*?</head>)', orig, re.DOTALL)
head_html = head_match.group(1) if head_match else ""

about_custom_css = """
<style>
    body { font-family: 'Montserrat', sans-serif; }
    h1, h2, h3, h4, h5, h6, .nav-item { font-family: 'Oswald', sans-serif; text-transform: uppercase; }
    .header-bg { background-color: #000000; border-bottom: 2px solid #1a1a1a; }
    
    .dropdown:hover .dropdown-menu { display: block; }
    .dropdown-menu {
        display: none; position: absolute; background-color: #1a1a1a; min-width: 250px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.5); z-index: 100; border-top: 3px solid #BE1E2E;
    }
    .dropdown-menu a {
        color: #ffffff; padding: 12px 20px; text-decoration: none; display: block;
        font-size: 0.9rem; border-bottom: 1px solid #333; transition: background 0.3s, padding-left 0.3s;
        font-family: 'Montserrat', sans-serif; text-transform: none; font-weight: 500;
    }
    .dropdown-menu a:hover { background-color: #BE1E2E; padding-left: 25px; }
    
    .nav-link { position: relative; padding-bottom: 5px; }
    .nav-link::after { content: ''; position: absolute; width: 0; height: 2px; bottom: 0; left: 0; background-color: #BE1E2E; transition: width 0.3s; }
    .nav-link:hover::after { width: 100%; }
    
    .btn-red { background-color: #BE1E2E; color: white; padding: 12px 24px; font-family: 'Oswald', sans-serif; text-transform: uppercase; font-weight: 600; letter-spacing: 1px; transition: background 0.3s; }
    .btn-red:hover { background-color: #9A1623; }
    
    /* Hero Section */
    .hero-section {
        background-color: #000;
        background-image: url('/assets/images/2D6A5D5F-1AEB-4402-A62E-0083B7651C8D.jpeg'); /* Same as home */
        background-position: center 30%;
        background-size: cover;
        background-blend-mode: overlay;
        background-color: rgba(0, 0, 0, 0.6);
        min-height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
    }
    .hero-section h1 { font-size: 5rem; font-weight: 700; letter-spacing: 2px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }

    .btn-red-outline {
        background-color: #BE1E2E;
        color: white;
        padding: 5px 20px;
        margin-top: 5px;
        display: inline-block;
        font-weight: bold;
        transition: 0.3s;
    }
    .btn-red-outline:hover { background-color: #000; }
</style>
"""
# Replace styles in head
head_html = re.sub(r'<style>.*?</style>', about_custom_css, head_html, flags=re.DOTALL)
head_html = head_html.replace("<title>El Toro Battalion</title>", "<title>About Us | El Toro Battalion</title>")

# Build content
content_html = """
    <main class="flex-grow">
        <!-- Hero -->
        <div class="hero-section w-full relative">
            <h1 class="text-center">About Us</h1>
        </div>

        <!-- Section 1: Per Ardua -->
        <div class="bg-white py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-[40px] font-bold mb-4 font-heading text-black leading-tight">‘Per Ardua, Ad Alta’</h2>
                    <p class="text-gray-600 italic mb-6">"Through hard work, great things are achieved"</p>
                    <p class="text-gray-700 mb-6 leading-relaxed"><strong>El Toro Battalion</strong> is located in Irvine, California. Our goal is to instill discipline, pride, motivation, self-reliance, and self-respect in our cadets. It is through exciting training evolutions and proper training that we accomplish this.</p>
                    <p class="text-gray-700 leading-relaxed"><strong>El Toro Battalion</strong> is active year around. Our weekend drill dates change monthly. Please refer to our Unit Calendar for the Plan of the Month (POM)</p>
                </div>
                <div class="flex justify-center">
                    <img src="/assets/images/SCCNewLogo7-1.png" alt="Battalion Logo" class="w-full max-w-[500px]">
                </div>
            </div>
        </div>

        <!-- Section 2: Unit History -->
        <div class="bg-[#f4f4f4] py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                <div class="flex justify-center">
                    <img src="/assets/images/image-asset.jpg" alt="Aerial Base" class="w-full max-w-[600px] shadow-lg">
                </div>
                <div>
                    <h2 class="text-[32px] font-bold mb-4 font-heading text-black">UNIT HISTORY</h2>
                    <p class="text-gray-700 leading-relaxed"><strong>El Toro Battalion</strong> was initially the Trieste 2 Division. In 2004, we became a Seabee Battalion. We also changed our name to honor the men and women that served on the El Toro Air Station. Trieste had long been a successful unit in the U.S. Naval Sea Cadets Corps, and now as <strong>El Toro Battalion</strong>, we have continued to provide a high quality youth program for the Orange County community.</p>
                </div>
            </div>
        </div>

        <!-- Section 3: USNSCC info -->
        <div class="bg-[#BE1E2E] py-16 text-center text-white">
            <div class="max-w-5xl mx-auto px-4">
                <h2 class="text-[32px] font-bold mb-6 font-heading">UNITED STATES NAVAL SEA CADET CORPS (USNSCC)</h2>
                <p class="mb-4 leading-relaxed font-sans text-white/90">On September 10, 1962, Congress federally incorporated the US Naval Sea Cadet Corps under Public Law 87-655 (36 USC 1541) after recognizing the importance and benefits of the NSCC. For more information please visit <a href="http://www.seacadets.org" class="underline hover:text-gray-200" target="_blank">www.seacadets.org</a>.</p>
                <p class="mb-8 leading-relaxed font-sans text-white/90">Since 1958, the United States Naval Sea Cadet Corps has been committed to providing American youth with a drug-and alcohol-free environment to foster their leadership abilities, broaden their horizons through hands-on training, and guide them to become mature young adults.</p>
                <img src="/assets/images/image-asset.png" alt="NSCC Eagle Logo" class="w-32 mx-auto">
            </div>
        </div>

        <!-- Section 4: Sponsors & Links -->
        <div class="bg-white py-16 text-center">
            <div class="max-w-5xl mx-auto px-4">
                <div class="mb-8">
                    <h4 class="font-bold text-black text-xl mb-1">Sponsored by American Legion Post 291</h4>
                    <a href="http://www.al291.com" target="_blank" class="btn-red-outline">www.al291.com</a>
                </div>
                
                <div class="mb-8">
                    <h4 class="font-bold text-black text-xl mb-1">Proud friends of the NRA</h4>
                    <a href="http://www.friendsofnra.org" target="_blank" class="btn-red-outline">www.friendsofnra.org</a>
                </div>
                
                <div class="mb-12">
                    <h4 class="font-bold text-black text-xl mb-1">For Donations</h4>
                    <a href="https://www.gofundme.com/manage/el-toro-battalion-ts-vammen/" target="_blank" class="btn-red-outline">https://www.gofundme.com/manage/el-toro-battalion-ts-vammen/</a>
                </div>

                <!-- 2-col image grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16 items-center">
                    <div><img src="/assets/images/image-asset1.png" alt="Marina" class="w-full shadow-md"></div>
                    <div><img src="/assets/images/image-asset-1.png" alt="Friends of NRA" class="w-full shadow-md" onerror="this.src='/assets/images/image-asset.png'"></div>
                </div>

                <div class="flex flex-col items-center justify-center pt-8 border-t border-gray-200">
                    <h2 class="text-[28px] font-bold mb-6 font-heading text-black max-w-4xl leading-tight">Air Force Association's Cyberpatriot National Youth Cyber Education Program Participant</h2>
                    <img src="/assets/images/image-asset-1.jpg" alt="Cyberpatriot" class="w-48 shadow-lg rounded-full border-4 border-[#224466]">
                </div>
            </div>
        </div>
    </main>
"""

javascript = """
    <!-- Mobile Menu Script -->
    <script>
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {
            var menu = document.getElementById('mobile-menu');
            var icon = this.querySelector('i');
            menu.classList.toggle('hidden');
            if (menu.classList.contains('hidden')) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            } else {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            }
        });
    </script>
"""

full_html = f"<!DOCTYPE html>\n<html lang=\"en\">\n{head_html}\n<body class=\"bg-white text-gray-800 flex flex-col min-h-screen\">\n{header_html}\n{content_html}\n{footer_html}\n{javascript}\n</body>\n</html>"

with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/about-us.html", "w") as f:
    f.write(full_html)

print("about-us.html rebuilt successfully with precision grid.")
