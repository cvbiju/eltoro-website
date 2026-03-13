with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '<div id="gallery-grid"' in line:
        new_lines.append(line)
        new_lines.append('                <!-- Images will be injected here via JS -->\n')
        new_lines.append('            </div>\n')
        skip = True
        continue
    if skip and '</div>' in line and 'id="error-message"' in ''.join(lines[lines.index(line):lines.index(line)+2]):
        skip = False
        new_lines.append(line)
        continue
    if not skip:
        new_lines.append(line)

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
