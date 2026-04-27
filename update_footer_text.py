import glob
import os

target_string1 = "Since 1958, the USNSCC has been committed to providing American youth with a drug-and alcohol-free environment..."
target_string2 = "Since 1958, we have been committed to providing American youth with a drug-and alcohol-free environment to foster leadership abilities, broaden horizons through hands-on training, and guide them to become mature young adults."
target_string3 = "Since 1958, the United States Naval Sea Cadet Corps has been committed to providing American youth with a drug-and alcohol-free environment to foster their leadership abilities, broaden their horizons through hands-on training, and guide them to become mature young adults."

replacement = "Since 1958, the Naval Sea Cadet Corps has been committed to providing American youth with a drug and alcohol free environment to foster their leadership abilities, broaden their horizons through hands-on training and guide them to becoming mature young adults."

html_files = glob.glob('public/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(target_string1, replacement)
    new_content = new_content.replace(target_string2, replacement)
    new_content = new_content.replace(target_string3, replacement)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

print("Done.")
