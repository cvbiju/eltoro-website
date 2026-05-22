import glob
import re

target_paragraph = '<p class="text-sm leading-loose mb-2">Since 1958, the Naval Sea Cadet Corps has been committed to providing American youth with a drug and alcohol free environment to foster their leadership abilities, broaden their horizons through hands-on training and guide them to becoming mature young adults.</p>'

html_files = glob.glob('public/*.html')

new_mission_block = """
            <div class="mt-12 pt-8 border-t border-gray-800 text-center mx-auto max-w-5xl">
                <p class="text-sm leading-relaxed text-gray-400 font-light italic">"Since 1958, the Naval Sea Cadet Corps has been committed to providing American youth with a drug and alcohol free environment to foster their leadership abilities, broaden their horizons through hands-on training and guide them to becoming mature young adults."</p>
            </div>
            
            <div class="mt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500">"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the paragraph from Column 1
    if target_paragraph in content:
        content = content.replace(target_paragraph, '')
        
        # 2. Inject the new mission block and adjust the copyright row
        # The copyright row currently starts with:
        # <div class="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500">
        
        # We need to elegantly replace that div opening
        copyright_target = '<div class="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500">'
        
        if copyright_target in content:
            content = content.replace(copyright_target, new_mission_block)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated footer layout in: {file_path}")
        else:
            print(f"Could not find copyright target in {file_path}")

print("Done.")
