import glob
import re

html_files = glob.glob('public/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replacement of the exact phone number string
    if "310-613-1586" in content:
        content = content.replace("310-613-1586", "310-415-0781")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated phone number in: {file_path}")

print("Done.")
