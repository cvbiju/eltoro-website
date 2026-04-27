import glob
import os

target_name = "Suzy Wetrs"
replacement_name = "Suzy Werts"

html_files = glob.glob('public/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_name in content:
        content = content.replace(target_name, replacement_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed spelling in: {file_path}")

print("Done.")
