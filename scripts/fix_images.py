import os
import re

def replace_in_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w') as f:
        f.write(content)

# Fix Meet The Officers
mto_replacements = [
    # Boyes was 13.png, Live is 5.png
    ('MIDN Phillips Boyes",\n        "image": "13.png', 'MIDN Phillips Boyes",\n        "image": "5.png'),
    ('/assets/images/13.png" alt="MIDN Phillips Boyes"', '/assets/images/5.png" alt="MIDN Phillips Boyes"'),
    
    # Chang was slazzer-edit-image-1.png, Live is WhatsApp-Image-2024-12-30-at-1.09.21-PM.jpeg
    ('ENS Zane Chang",\n        "image": "slazzer-edit-image-1.png', 'ENS Zane Chang",\n        "image": "WhatsApp-Image-2024-12-30-at-1.09.21-PM.jpeg'),
    ('/assets/images/slazzer-edit-image-1.png" alt="ENS Zane Chang"', '/assets/images/WhatsApp-Image-2024-12-30-at-1.09.21-PM.jpeg" alt="ENS Zane Chang"'),
    
    # Franco was NewProject4.png, Live is slazzer-edit-image-1.png
    ('INST Cesar Franco",\n        "image": "NewProject4.png', 'INST Cesar Franco",\n        "image": "slazzer-edit-image-1.png'),
    ('/assets/images/NewProject4.png" alt="INST Cesar Franco"', '/assets/images/slazzer-edit-image-1.png" alt="INST Cesar Franco"'),
    
    # Ginsburg had no image (user-shield), Live is NewProject4.png
    ('<div class="w-48 h-48 mx-auto rounded-full bg-brandBlack flex items-center justify-center mb-6 border-4 border-white shadow-md">\n                        <i class="fas fa-user-shield text-5xl text-white opacity-50"></i>\n                    </div>\n                    <h3 class="text-2xl font-heading font-bold text-brandBlack uppercase">WO Terry Ginsburg</h3>',
     '<img src="/assets/images/NewProject4.png" alt="WO Terry Ginsburg" class="w-48 h-48 mx-auto rounded-full object-cover mb-6 border-4 border-white shadow-md" onerror="this.src=\'/assets/images/image-asset.jpg\'">\n                    <h3 class="text-2xl font-heading font-bold text-brandBlack uppercase">WO Terry Ginsburg</h3>')
]
replace_in_file("meet-the-officers.html", mto_replacements)

# Fix About Us
about_replacements = [
    # Section 1: Logo
    ('<img src="/assets/images/SCCNewLogo7-1.png" alt="Battalion Logo" class="w-full max-w-[500px]">',
     '<img src="https://eltorobattalion.org/wp-content/uploads/2024/09/SCCNewLogo7-1.png" alt="Battalion Logo" class="w-full">'),
     
    # Section 2: Aerial
    ('<img src="/assets/images/image-asset.jpg" alt="Aerial Base" class="w-full max-w-[600px] shadow-lg">',
     '<img src="https://eltorobattalion.org/wp-content/uploads/2024/09/image-asset.jpg" alt="Aerial Base" class="w-full shadow-lg">'),
     
    # Section 3: Eagle
    ('<img src="/assets/images/image-asset.png" alt="NSCC Eagle Logo" class="w-32 mx-auto">',
     '<img src="https://eltorobattalion.org/wp-content/uploads/2024/09/image-asset.png" alt="NSCC Eagle Logo" class="w-[172px] mx-auto">'),
     
    # Section 4: Sponsors Left
    ('<img src="/assets/images/image-asset1.png" alt="Marina" class="w-full shadow-md">',
     '<img src="https://eltorobattalion.org/wp-content/uploads/2024/10/image-asset1.png" alt="Marina" class="w-full">'),
     
    # Section 4: Sponsors Right
    ('<img src="/assets/images/image-asset-1.png" alt="Friends of NRA" class="w-full shadow-md" onerror="this.src=\'/assets/images/image-asset.png\'">',
     '<img src="https://eltorobattalion.org/wp-content/uploads/2024/10/image-asset.png" alt="Friends of NRA" class="w-full">'),
     
    # Cyberpatriot
    ('<img src="/assets/images/image-asset-1.jpg" alt="Cyberpatriot" class="w-48 shadow-lg rounded-full border-4 border-[#224466]">',
     '<img src="https://eltorobattalion.org/wp-content/uploads/2024/10/image-asset-1.jpg" alt="Cyberpatriot" class="w-[240px] shadow-lg">')
]
replace_in_file("about-us.html", about_replacements)
print("Updated HTML files with exact image matching!")
