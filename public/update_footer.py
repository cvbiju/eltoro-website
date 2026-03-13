import glob
import os

footer_old = """
                <!-- Column 3: Contact Us -->
                <div class="col-span-1">
                    <h3 class="font-heading text-xl text-white mb-6 uppercase tracking-wider border-b-2 border-brandRed pb-2 inline-block">Contact Us</h3>
                    
                    <div class="mb-6">
                        <p class="text-white font-bold mb-1">ENS Zane Chang, Admin Officer</p>
                        <p class="text-sm"><i class="fas fa-envelope text-brandRed w-5"></i> <a href="mailto:zchang@seacadets.org" class="hover:text-white">zchang@seacadets.org</a></p>
                        <p class="text-sm"><i class="fas fa-phone text-brandRed w-5"></i> 415-993-0799</p>
                    </div>
                    
                    <div>
                        <p class="text-white font-bold mb-1">INST Cesar Franco, Recruitment</p>
                        <p class="text-sm"><i class="fas fa-envelope text-brandRed w-5"></i> <a href="mailto:c.franco@seacadets.org" class="hover:text-white">c.franco@seacadets.org</a></p>
                        <p class="text-sm"><i class="fas fa-phone text-brandRed w-5"></i> 949-759-2265</p>
                    </div>
                </div>

                <!-- Column 4: Follow Us -->
                <div class="col-span-1">
                    <h3 class="font-heading text-xl text-white mb-6 uppercase tracking-wider border-b-2 border-brandRed pb-2 inline-block">Follow Us</h3>
                    <div class="flex space-x-4 mb-8">
                        <a href="#" class="w-10 h-10 bg-gray-800 rounded flex items-center justify-center text-white hover:bg-brandRed transition-colors"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-10 h-10 bg-gray-800 rounded flex items-center justify-center text-white hover:bg-brandRed transition-colors"><i class="fab fa-instagram"></i></a>
                        <a href="http://www.seacadets.org/" target="_blank" class="w-10 h-10 bg-gray-800 rounded flex items-center justify-center text-white hover:bg-brandRed transition-colors"><i class="fas fa-anchor"></i></a>
                    </div>
                    
                    <h3 class="font-heading text-xl text-white mb-4 uppercase tracking-wider">Parents Info</h3>
                    <a href="https://www.gofundme.com/manage/el-toro-battalion-ts-vammen/" target="_blank" class="btn-red w-full block text-center mb-4">Make a Donation</a>
                </div>
"""

footer_new = """
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
                        <!-- Precise colors and sizing for social icons -->
                        <a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fab fa-instagram"></i></a>
                        <a href="http://www.seacadets.org/" target="_blank" class="w-12 h-12 bg-[#1b2532] flex items-center justify-center text-white hover:bg-brandRed transition-colors rounded-sm text-xl"><i class="fas fa-anchor"></i></a>
                    </div>
                    
                    <h3 class="font-heading text-2xl font-semibold text-white mb-6 uppercase tracking-wider">Parents Info</h3>
                    <a href="https://www.gofundme.com/manage/el-toro-battalion-ts-vammen/" target="_blank" class="btn-red w-full flex justify-center py-4 text-center">MAKE A DONATION</a>
                </div>
"""

html_files = glob.glob("/Users/bchandr1/Documents/my-agy-projects/ETB/public/**/*.html", recursive=True)

success_count = 0
for file in html_files:
    if "compare_report" in file:
        continue # Skip the report files
        
    with open(file, 'r') as f:
        content = f.read()
        
    if footer_old in content:
        new_content = content.replace(footer_old, footer_new)
        with open(file, 'w') as f:
            f.write(new_content)
        success_count += 1
        print(f"Updated footer in: {os.path.basename(file)}")
    else:
        # Fallback if whitespace is slightly different
        print(f"Footer pattern not found matching exactly in {os.path.basename(file)}, skipping.")

print(f"\\nSuccessfully updated {success_count} files.")
