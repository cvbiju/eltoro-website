import re

with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/live_enrollment.html", "r") as f:
    content = f.read()

# The container with the requirements text
req_start = content.find("REQUIREMENTS TO JOIN")
req_container_start = content.rfind("<div", 0, req_start)
req_container_start = content.rfind("<div", 0, req_container_start) # go up to the wrapper

# The form is wrapped in a container that has the background color
form_container_start = content.find('<div class="elementor-element elementor-element-9f38bbd')
form_container_end = content.find('<div data-elementor-type="footer"')

form_html_raw = content[form_container_start:form_container_end]

# Clean up elementor classes, but preserve inputs
# We can just inject the raw HTML and let the browser render it if we include the CSS, 
# OR we can just keep the raw HTML because it uses standard inputs.
# Wait, let's just use the raw HTML and add Tailwind classes for styling to match the visual.

# Actually, the user wants the form to be exactly like the live site.
# The live site form has: Family Information, Family Primary Contact, Cadet Information, School, Home Address, Questionnaire.
# Let's extract all the labels and inputs and build a clean Tailwind CSS form.

import json
from bs4 import BeautifulSoup

soup = BeautifulSoup(form_html_raw, 'html.parser')

inputs = []
for field in soup.find_all(class_='elementor-field-group'):
    # some are HTML separators
    if 'elementor-field-type-html' in field['class']:
        text = field.get_text(strip=True)
        inputs.append({'type': 'heading', 'text': text})
        continue
    
    label = field.find('label')
    if label:
        label_text = label.get_text(strip=True)
    else:
        label_text = ""
        
    input_tag = field.find(['input', 'select'])
    if input_tag:
        inputs.append({
            'type': input_tag.name,
            'input_type': input_tag.get('type', ''),
            'placeholder': input_tag.get('placeholder', ''),
            'name': input_tag.get('name', ''),
            'label': label_text,
            'required': input_tag.has_attr('required'),
            'options': [opt.get_text(strip=True) for opt in input_tag.find_all('option')] if input_tag.name == 'select' else []
        })

print(json.dumps(inputs, indent=2))
