import glob
import re

html_files = glob.glob('public/*.html')

# 1. Regex to patch target="_blank"
def patch_anchor_tags(html_content):
    # Matches <a ... target="_blank" ... >
    # We want to add rel="noopener noreferrer" if it's not already there.
    def add_rel(match):
        tag = match.group(0)
        if 'rel="noopener noreferrer"' not in tag:
            # Inject rel attribute right before the closing >
            return tag[:-1] + ' rel="noopener noreferrer">'
        return tag

    # regex to find <a href="..." target="_blank" class="..."> 
    # taking into account attribute ordering variations
    pattern = re.compile(r'<a[^>]+target="_blank"[^>]*>')
    return pattern.sub(add_rel, html_content)


# Run loop over all files
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = patch_anchor_tags(content)
    
    # 2. Patch enrollment.html for honeypot
    if file_path == "public/enrollment.html":
        target_input = '<input type="hidden" name="access_key" value="0fbe9077-aea2-4c34-af94-000cd7678747">'
        honeypot_input = '<!-- Web3Forms Honeypot -->\n                                <input type="checkbox" name="botcheck" class="hidden" style="display: none;">\n                                '
        
        if honeypot_input not in new_content:
            new_content = new_content.replace(target_input, target_input + '\n                                ' + honeypot_input)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched security issues in: {file_path}")

print("Done.")
