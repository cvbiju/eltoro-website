import re

with open("public/cadet-mess.html", "r") as f:
    html = f.read()

new_main = """<!-- Main Content -->
<main class="flex-grow bg-gray-50">
    <!-- Hero Header -->
    <div class="relative bg-[radial-gradient(circle_at_center,_#2a2a2a_0%,_#000000_100%)] text-white py-20 text-center border-b-4 border-brandRed overflow-hidden">
        <div class="absolute inset-0 bg-[linear-gradient(135deg,_rgba(190,30,46,0.2)_0%,_transparent_50%)] pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10">
            <h1 class="font-heading text-5xl md:text-6xl font-bold tracking-[0.2em] uppercase">Cadet Mess</h1>
        </div>
    </div>

    <div class="py-16">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <!-- 3 Column Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10 mb-16">
                <!-- Card 1 -->
                <div class="flex flex-col items-center text-center group bg-white p-6 rounded-xl shadow-md border-t-4 border-brandRed hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                    <div class="w-full flex-grow flex items-center h-48 justify-center overflow-hidden mb-6">
                        <img src="./assets/images/Sea-Cadet.jpg" alt="Sea Cadet Family Handbook" class="w-auto h-auto max-h-48 object-contain">
                    </div>
                    <h3 class="font-heading text-xl font-bold uppercase text-brandBlack mb-6 mt-0">Sea Cadet Family Handbook</h3>
                    <a href="./assets/images/Sea-Cadet-Family-Handbook.pdf" target="_blank" class="mt-auto inline-flex items-center justify-center bg-brandRed hover:bg-brandRedHover text-white py-3 px-8 w-full text-sm font-bold tracking-widest shadow transition">
                        <i class="fas fa-file-pdf mr-2"></i> Open PDF
                    </a>
                </div>
                <!-- Card 2 -->
                <div class="flex flex-col items-center text-center group bg-white p-6 rounded-xl shadow-md border-t-4 border-brandRed hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                    <div class="w-full flex-grow flex items-center h-48 justify-center overflow-hidden mb-6">
                        <img src="./assets/images/Code-of-Conduct.png" alt="Sea Cadet Oath & Cadet Code of Conduct" class="w-auto h-auto max-h-48 object-contain">
                    </div>
                    <h3 class="font-heading text-xl font-bold uppercase text-brandBlack mb-6 mt-0">Oath & Code of Conduct</h3>
                    <a href="./assets/images/Code-of-Conduct.png" target="_blank" class="mt-auto inline-flex items-center justify-center bg-brandRed hover:bg-brandRedHover text-white py-3 px-8 w-full text-sm font-bold tracking-widest shadow transition">
                        <i class="fas fa-file-pdf mr-2"></i> Open PDF
                    </a>
                </div>
                <!-- Card 3 -->
                <div class="flex flex-col items-center text-center group bg-white p-6 rounded-xl shadow-md border-t-4 border-brandRed hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                    <div class="w-full flex-grow flex items-center h-48 justify-center overflow-hidden mb-6">
                        <img src="./assets/images/Core-Values.png" alt="Sea Cadet Core Values" class="w-auto h-auto max-h-48 object-contain">
                    </div>
                    <h3 class="font-heading text-xl font-bold uppercase text-brandBlack mb-6 mt-0">Sea Cadet Core Values</h3>
                    <a href="./assets/images/Core-Values.png" target="_blank" class="mt-auto inline-flex items-center justify-center bg-brandRed hover:bg-brandRedHover text-white py-3 px-8 w-full text-sm font-bold tracking-widest shadow transition">
                        <i class="fas fa-file-pdf mr-2"></i> Open PDF
                    </a>
                </div>
            </div>
            
            <!-- 3 Buttons Row -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-24">
                <a href="./general-knowledge.html" class="group relative overflow-hidden bg-white hover:bg-brandBlack border border-gray-200 hover:border-brandBlack flex flex-col items-center text-center py-10 px-6 rounded-xl shadow-md transition-all duration-300 rounded-sm">
                    <div class="w-16 h-16 bg-gray-50 group-hover:bg-gray-800 rounded-full flex items-center justify-center mb-4 transition-colors">
                        <i class="fas fa-book-open text-brandRed font-bold text-2xl"></i>
                    </div>
                    <h3 class="font-heading text-xl text-brandBlack group-hover:text-white uppercase tracking-widest font-bold mb-2 transition-colors">General Knowledge</h3>
                    <p class="text-sm text-gray-500 group-hover:text-gray-400">Top 6, Sailor's Creed, Oath & more</p>
                </a>
                
                <a href="./physical-fitness.html" class="group relative overflow-hidden bg-white hover:bg-brandBlack border border-gray-200 hover:border-brandBlack flex flex-col items-center text-center py-10 px-6 rounded-xl shadow-md transition-all duration-300 rounded-sm">
                    <div class="w-16 h-16 bg-gray-50 group-hover:bg-gray-800 rounded-full flex items-center justify-center mb-4 transition-colors">
                        <i class="fas fa-running text-brandRed font-bold text-2xl"></i>
                    </div>
                    <h3 class="font-heading text-xl text-brandBlack group-hover:text-white uppercase tracking-widest font-bold mb-2 transition-colors">Physical Fitness</h3>
                    <p class="text-sm text-gray-500 group-hover:text-gray-400">PRT Standards, Levels & Guides</p>
                </a>

                <a href="./grooming-uniform.html" class="group relative overflow-hidden bg-white hover:bg-brandBlack border border-gray-200 hover:border-brandBlack flex flex-col items-center text-center py-10 px-6 rounded-xl shadow-md transition-all duration-300 rounded-sm">
                    <div class="w-16 h-16 bg-gray-50 group-hover:bg-gray-800 rounded-full flex items-center justify-center mb-4 transition-colors">
                        <i class="fas fa-tshirt text-brandRed font-bold text-2xl"></i>
                    </div>
                    <h3 class="font-heading text-xl text-brandBlack group-hover:text-white uppercase tracking-widest font-bold mb-2 transition-colors">Grooming & Uniform</h3>
                    <p class="text-sm text-gray-500 group-hover:text-gray-400">Hair Policies, Uniform Manuals</p>
                </a>
            </div>
            
            <!-- Content Area - Cadet Expectations -->
            <div class="mb-20">
                <div class="text-center mb-10">
                    <h2 class="text-4xl font-heading uppercase text-brandBlack font-bold border-b-4 border-brandRed inline-block pb-2">Pillars of Conduct</h2>
                    <p class="text-gray-500 mt-4 max-w-2xl mx-auto">Cadet Expectations. Adhering to these pillars ensures unit cohesion, professional growth, and personal development.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <!-- HONOR -->
                    <div class="bg-white p-8 rounded-xl shadow-lg border-l-4 border-brandRed hover:shadow-xl transition-shadow">
                        <div class="flex items-center mb-6">
                            <i class="fas fa-medal text-brandRed text-4xl mr-4"></i>
                            <h4 class="text-2xl font-heading tracking-widest text-brandBlack font-bold m-0 uppercase">Honor</h4>
                        </div>
                        <p class="mb-6 text-gray-600 text-sm leading-relaxed border-b border-gray-100 pb-4">Cadets will conduct themselves honorably at all times by being completely truthful, polite, and considerate to all people and showing proper military bearing.</p>
                        <h5 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Cadets will act responsibly through:</h5>
                        <ul class="space-y-3 text-sm text-gray-700">
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Arriving on time (15 minutes before start).</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Reading the Plan of the Day / Month in advance.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Maintaining proper grooming & wearing the uniform with pride.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Safeguarding their Sea Cadet ID cards, no “gear adrift.”</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Remaining in good standing academically at school.</span></li>
                        </ul>
                    </div>

                    <!-- RESPECT -->
                    <div class="bg-white p-8 rounded-xl shadow-lg border-l-4 border-brandRed hover:shadow-xl transition-shadow">
                        <div class="flex items-center mb-6">
                            <i class="fas fa-handshake text-brandRed text-4xl mr-4"></i>
                            <h4 class="text-2xl font-heading tracking-widest text-brandBlack font-bold m-0 uppercase">Respect</h4>
                        </div>
                        <p class="mb-6 text-gray-600 text-sm leading-relaxed border-b border-gray-100 pb-4">Cadets will be respectful by saying "Yes, sir/ma'am" or "No, sir/ma'am" when addressing adults.</p>
                        <ul class="space-y-3 text-sm text-gray-700">
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Cadets will obey the orders of those placed in authority over them.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Follow all military courtesies and unit policies.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Abide strictly by the Cadet Code of Conduct.</span></li>
                        </ul>
                    </div>

                    <!-- COMMITMENT -->
                    <div class="bg-white p-8 rounded-xl shadow-lg border-l-4 border-brandRed hover:shadow-xl transition-shadow">
                        <div class="flex items-center mb-6">
                            <i class="fas fa-anchor text-brandRed text-4xl mr-4"></i>
                            <h4 class="text-2xl font-heading tracking-widest text-brandBlack font-bold m-0 uppercase">Commitment</h4>
                        </div>
                        <h5 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Cadets will demonstrate commitment by:</h5>
                        <ul class="space-y-3 text-sm text-gray-700">
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Maintaining or exceeding the minimum unit drill attendance of 75% per quarter.</span></li>
                            <li class="flex items-start"><i class="fas fa-shield-alt text-gray-400 mt-1 mr-3"></i> <span class="italic text-gray-500 text-xs">Note: A pattern of poor attendance may result in dismissal.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Completing online advancement courses on time.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Attending at least one (NSCC) summer/winter training per year.</span></li>
                        </ul>
                    </div>

                    <!-- SERVICE -->
                    <div class="bg-white p-8 rounded-xl shadow-lg border-l-4 border-brandRed hover:shadow-xl transition-shadow">
                        <div class="flex items-center mb-6">
                            <i class="fas fa-hands-helping text-brandRed text-4xl mr-4"></i>
                            <h4 class="text-2xl font-heading tracking-widest text-brandBlack font-bold m-0 uppercase">Service</h4>
                        </div>
                        <p class="mb-6 text-gray-600 text-sm leading-relaxed border-b border-gray-100 pb-4">Cadets will serve and support each other through positive interactions.</p>
                        <ul class="space-y-3 text-sm text-gray-700">
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Building one another up with encouragement.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Maintaining an environment free of cursing, inappropriate jokes, or demeaning comments.</span></li>
                            <li class="flex items-start"><i class="fas fa-check text-brandRed mt-1 mr-3"></i> <span>Striving to complete 30 hours of community service for every year enrolled.</span></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- COTC's Top 6 Spotlight -->
            <div class="mt-20">
                <div class="bg-gray-900 rounded-2xl shadow-2xl relative overflow-hidden">
                    <div class="absolute inset-0 bg-[linear-gradient(45deg,_rgba(190,30,46,0.2)_0%,_transparent_100%)] pointer-events-none"></div>
                    <div class="grid grid-cols-1 md:grid-cols-2">
                        <div class="p-10 md:p-16 flex flex-col justify-center relative z-10">
                            <h2 class="text-4xl font-heading uppercase font-bold text-white mb-6">COTC’s Top 6</h2>
                            <p class="mb-10 text-lg font-medium text-gray-400 leading-relaxed max-w-lg">Violating COTC’s Top 6 will be grounds for severe consequences: demotion in rank, termination from the unit, termination from the USNSCC program, Captain’s Mast, and more.</p>
                            
                            <ul class="space-y-4 mb-8">
                                <li class="text-white font-heading text-xl uppercase tracking-wider flex items-center bg-gray-800 bg-opacity-50 p-3 rounded"><i class="fas fa-ban text-brandRed mr-4"></i> 1. No Discrimination</li>
                                <li class="text-white font-heading text-xl uppercase tracking-wider flex items-center bg-gray-800 bg-opacity-50 p-3 rounded"><i class="fas fa-ban text-brandRed mr-4"></i> 2. No Hazing</li>
                                <li class="text-white font-heading text-xl uppercase tracking-wider flex items-center bg-gray-800 bg-opacity-50 p-3 rounded"><i class="fas fa-ban text-brandRed mr-4"></i> 3. No Sexual Harassment</li>
                                <li class="text-white font-heading text-xl uppercase tracking-wider flex items-center bg-gray-800 bg-opacity-50 p-3 rounded"><i class="fas fa-ban text-brandRed mr-4"></i> 4. No Fraternization</li>
                                <li class="text-white font-heading text-xl uppercase tracking-wider flex items-center bg-gray-800 bg-opacity-50 p-3 rounded"><i class="fas fa-ban text-brandRed mr-4"></i> 5. No Cadet-to-Cadet Contact</li>
                                <li class="text-white font-heading text-xl uppercase tracking-wider flex items-center bg-gray-800 bg-opacity-50 p-3 rounded"><i class="fas fa-ban text-brandRed mr-4"></i> 6. No Substance Abuse</li>
                            </ul>
                            
                            <div>
                                <a href="./general-knowledge.html" class="inline-flex items-center text-white bg-brandRed hover:bg-brandRedHover px-8 py-4 font-bold tracking-widest text-sm transition shadow-lg">
                                    READ MORE
                                </a>
                            </div>
                        </div>
                        <div class="relative min-h-[400px]">
                            <img src="./assets/images/455997308_18279201460239783_7897856532944536242_n.jpg" alt="NSCC Cadets Spotlight" class="absolute inset-0 w-full h-full object-cover object-center grayscale hover:grayscale-0 transition-all duration-700">
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</main>
"""

new_html = re.sub(r"<!-- Main Content -->.*?<!-- Footer mirroring the live site 4-columns -->", new_main + "\n<!-- Footer mirroring the live site 4-columns -->", html, flags=re.DOTALL)

with open("public/cadet-mess.html", "w") as f:
    f.write(new_html)
