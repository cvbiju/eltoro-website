import re
with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/parents.html", "r") as f:
    orig = f.read()

correct_footer = """
    <!-- Footer mirroring the live site 4-columns -->
    <footer class="bg-brandBlack text-gray-300 pt-16 pb-8 border-t border-gray-800 mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-10 scroll-mt-24">
                
                <!-- Column 1: Logo and Address -->
                <div class="col-span-1">
                    <img src="/assets/images/SCCNewLogo7-1.png" alt="El Toro Logo" class="w-32 mb-6">
                    <h3 class="font-heading text-xl text-white mb-4 uppercase tracking-wider">El Toro Battalion</h3>
                    <p class="text-sm leading-loose mb-2"><i class="fas fa-map-marker-alt text-brandRed w-5"></i> Irvine, CA</p>
                    <p class="text-sm leading-loose mb-2">Since 1958, the USNSCC has been committed to providing American youth with a drug-and alcohol-free environment...</p>
                </div>
                
                <!-- Column 2: Quick Links -->
                <div class="col-span-1">
                    <h3 class="font-heading text-xl text-white mb-6 uppercase tracking-wider border-b-2 border-brandRed pb-2 inline-block">Quick Links</h3>
                    <ul class="space-y-3 text-sm font-semibold">
                        <li><a href="/" class="hover:text-brandRed transition-colors">> Home</a></li>
                        <li><a href="/about-us.html" class="hover:text-brandRed transition-colors">> About Us</a></li>
                        <li><a href="/programs.html" class="hover:text-brandRed transition-colors">> Programs</a></li>
                        <li><a href="/enrollment.html" class="hover:text-brandRed transition-colors">> Enrollment</a></li>
                        <li><a href="/gallery.html" class="hover:text-brandRed transition-colors">> Gallery</a></li>
                        <li><a href="/calendar.html" class="hover:text-brandRed transition-colors">> Calendar</a></li>
                    </ul>
                </div>

                <!-- Column 3: Contact Us -->
                <div class="col-span-1">
                    <h3 class="font-heading text-xl text-white mb-6 uppercase tracking-wider border-b-2 border-brandRed pb-2 inline-block">Contact Us</h3>
                    
                    <div class="mb-6">
                        <p class="text-white font-bold mb-2 text-lg">ENS Zane Chang, Admin Officer</p>
                        <p class="text-base text-gray-300 mb-1"><i class="fas fa-envelope text-brandRed w-6 text-lg"></i> <a href="mailto:zchang@seacadets.org" class="hover:text-white">zchang@seacadets.org</a></p>
                        <p class="text-base text-gray-300"><i class="fas fa-phone text-brandRed w-6 text-lg"></i> 415-993-0799</p>
                    </div>
                    
                    <div>
                        <p class="text-white font-bold mb-2 text-lg">INST Cesar Franco, Recruitment</p>
                        <p class="text-base text-gray-300 mb-1"><i class="fas fa-envelope text-brandRed w-6 text-lg"></i> <a href="mailto:c.franco@seacadets.org" class="hover:text-white">c.franco@seacadets.org</a></p>
                        <p class="text-base text-gray-300"><i class="fas fa-phone text-brandRed w-6 text-lg"></i> 949-759-2265</p>
                    </div>
                </div>

                <!-- Column 4: Follow Us -->
                <div class="col-span-1">
                    <h3 class="font-heading text-xl text-white mb-6 uppercase tracking-wider border-b-2 border-brandRed pb-2 inline-block">Follow Us</h3>
                    <div class="flex space-x-3 mb-10">
                        <a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-instagram"></i></a>
                        <a href="http://www.seacadets.org/" target="_blank" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fas fa-anchor"></i></a>
                    </div>
                    
                    <h3 class="font-heading text-2xl font-semibold text-white mb-6 uppercase tracking-wider">Parents Info</h3>
                    <a href="https://www.gofundme.com/manage/el-toro-battalion-ts-vammen/" target="_blank" class="btn-red w-full flex justify-center py-4 text-center rounded-none font-bold tracking-widest text-lg">MAKE A DONATION</a>
                </div>
                
            </div>
            
            <div class="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500">
                <p>&copy; 2026 El Toro Battalion. All Rights Reserved.</p>
                <p class="mt-4 md:mt-0">U.S. Naval Sea Cadet Corps</p>
            </div>
        </div>
    </footer>
"""

orig = re.sub(r'<!-- Footer mirroring the live site 4-columns -->.*</footer>', correct_footer, orig, flags=re.DOTALL)

with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/parents.html", "w") as f:
    f.write(orig)

print("parents.html footer fixed.")
