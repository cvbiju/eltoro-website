from bs4 import BeautifulSoup
import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will use a simple substring replace for the CSS adding if BeautifulSoup strips self-closing tags
soup = BeautifulSoup(html, 'html.parser')

# Define the scroll observer script to inject at the bottom
scroll_script = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.remove('opacity-0', 'translate-y-10', 'scale-95');
                        entry.target.classList.add('opacity-100', 'translate-y-0', 'scale-100');
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            document.querySelectorAll('.animate-on-scroll').forEach((elem, index) => {
                // Add staggered delay based on DOM order for sibling groups
                elem.style.transitionDelay = `${(index % 4) * 150}ms`;
                observer.observe(elem);
            });
        });
    </script>
"""

# Let's cleanly inject without breaking formatting by using string replacement.
# 1. Inject script before </body>
html = html.replace('</body>', f'{scroll_script}\n</body>')

# 2. Add custom styles for the button glow
style_block = """
        /* Pulsating Button glow */
        .btn-red-pulse {
            position: relative;
        }
        .btn-red-pulse::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            border-radius: 4px;
            box-shadow: 0 0 15px 2px rgba(190, 30, 46, 0.6);
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
            pointer-events: none;
        }
        .btn-red-pulse:hover::before {
            opacity: 1;
            animation: pulse-glow 1.5s infinite;
        }
        @keyframes pulse-glow {
            0% { box-shadow: 0 0 15px 2px rgba(190, 30, 46, 0.6); }
            50% { box-shadow: 0 0 25px 5px rgba(190, 30, 46, 0.8); }
            100% { box-shadow: 0 0 15px 2px rgba(190, 30, 46, 0.6); }
        }
"""
html = html.replace('</style>', f'{style_block}\n    </style>')

# 3. Add classes to elements
# Let's convert Who We Are Image and Text
html = html.replace('id="who-we-are-image" src="./assets/images/model-3_70.jpg" alt="Who We Are" class="w-full h-auto shadow-lg"', 
                    'id="who-we-are-image" src="./assets/images/model-3_70.jpg" alt="Who We Are" class="animate-on-scroll opacity-0 translate-y-10 transition-all duration-[800ms] ease-out w-full h-auto shadow-lg"')
html = html.replace('<div class="w-full md:w-1/2 text-left">', 
                    '<div class="animate-on-scroll opacity-0 translate-y-10 transition-all duration-[800ms] ease-out w-full md:w-1/2 text-left">')

# 4. What We Do cards
html = html.replace('class="flex flex-col"', 'class="flex flex-col animate-on-scroll opacity-0 translate-y-10 transition-all duration-700 ease-out"')
html = html.replace('class="flex flex-col mt-0 md:mt-12"', 'class="flex flex-col mt-0 md:mt-12 animate-on-scroll opacity-0 translate-y-10 transition-all duration-700 ease-out"')
html = html.replace('class="flex flex-col mt-0 md:mt-24"', 'class="flex flex-col mt-0 md:mt-24 animate-on-scroll opacity-0 translate-y-10 transition-all duration-700 ease-out"')

# 5. Resources blocks
html = html.replace('class="flex flex-col items-center w-full sm:w-[45%] lg:w-[22%]"', 'class="flex flex-col items-center w-full sm:w-[45%] lg:w-[22%] animate-on-scroll opacity-0 scale-95 transition-all duration-700 ease-out"')

# 6. Update Buttons
html = html.replace('btn-red inline-block text-[20px]', 'btn-red btn-red-pulse inline-block text-[20px]')

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html!")
