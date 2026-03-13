import glob
import os

footer_old = """
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
"""

footer_new = """
                <!-- Column 3: Contact Us -->
                <div class="col-span-1">
                    <h3 class="font-heading text-xl text-white mb-6 uppercase tracking-wider border-b-2 border-brandRed pb-2 inline-block">Contact Us</h3>
                    
                    <div class="mb-6">
                        <p class="text-white font-bold mb-2 text-lg">Commanding Officer: Suzy Wetrs</p>
                        <p class="text-base text-gray-300 mb-1"><i class="fas fa-envelope text-brandRed w-6 text-lg"></i> <a href="mailto:swerts@seacadets.org" class="hover:text-white">swerts@seacadets.org</a></p>
                        <p class="text-base text-gray-300"><i class="fas fa-phone text-brandRed w-6 text-lg"></i> 310-613-1586</p>
                    </div>
                    
                    <div>
                        <p class="text-white font-bold mb-2 text-lg">Executive Officer: Biju Chandrasekharan</p>
                        <p class="text-base text-gray-300 mb-1"><i class="fas fa-envelope text-brandRed w-6 text-lg"></i> <a href="mailto:v.chandrasekharan@seacadets.org" class="hover:text-white">v.chandrasekharan@seacadets.org</a></p>
                        <p class="text-base text-gray-300"><i class="fas fa-phone text-brandRed w-6 text-lg"></i> 949-774-8468</p>
                    </div>
                </div>
"""

html_files = glob.glob("/Users/bchandr1/Documents/my-agy-projects/ETB/public/**/*.html", recursive=True)

success_count = 0
for file in html_files:
    if "compare_report" in file or "live_" in file or "dump" in file:
        continue
        
    with open(file, 'r') as f:
        content = f.read()
        
    # Strip whitespace to match reliably
    if footer_old.strip() in content:
        new_content = content.replace(footer_old.strip(), footer_new.strip())
        with open(file, 'w') as f:
            f.write(new_content)
        success_count += 1
        print(f"Updated names in: {os.path.basename(file)}")
    else:
        # Fallback regex for minor indent differences
        import re
        pattern = re.compile(r'<!-- Column 3: Contact Us -->.*?(?=<!-- Column 4: Follow Us -->)', re.DOTALL)
        if pattern.search(content):
            new_content = pattern.sub(footer_new.strip() + "\\n\\n                ", content)
            with open(file, 'w') as f:
                f.write(new_content)
            success_count += 1
            print(f"Updated names via regex in: {os.path.basename(file)}")

print(f"\\nSuccessfully updated names in {success_count} files.")
