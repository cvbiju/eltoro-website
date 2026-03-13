import xml.etree.ElementTree as ET
import os

xml_file = "/Users/bchandr1/Documents/my-agy-projects/ETB/eltorobattalion.WordPress.2026-03-10.xml"
tree = ET.parse(xml_file)
root = tree.getroot()

ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/'
}

for item in root.findall('.//item'):
    title = item.find('title')
    post_type = item.find('wp:post_type', ns)
    
    if title is not None and title.text == 'Enrollment' and post_type is not None and post_type.text == 'page':
        content = item.find('content:encoded', ns)
        if content is not None:
            with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/enrollment_dump.html", "w") as f:
                f.write(content.text or "")
            print("Found and dumped enrollment page content.")
            break
