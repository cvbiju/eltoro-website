with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

css_replacement = '''            if (!document.getElementById('gallery-grid-override')) {
                const style = document.createElement('style');
                style.id = 'gallery-grid-override';
                style.innerHTML = `
                    #gallery-grid { 
                        display: grid !important; 
                        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
                    }
                    @media (min-width: 768px) {
                        #gallery-grid { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; }
                    }
                    @media (min-width: 1024px) {
                        #gallery-grid { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
                    }
                `;
                document.head.appendChild(style);
            }'''

import re
text = re.sub(
    r'if \(!document\.getElementById\(\'gallery-grid-override\'\)\) \{.*?document\.head\.appendChild\(style\);\s*\}',
    css_replacement,
    text,
    flags=re.DOTALL
)

with open('/Users/bchandr1/Documents/my-agy-projects/ETB/public/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected explicit !important media queries for the grid columns.")
