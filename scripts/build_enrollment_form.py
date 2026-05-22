import json
import re

form_data = [
  {"type": "heading_h2", "text": "Family Information"},
  {"type": "input", "input_type": "text", "placeholder": "First Name", "name": "form_fields[name]", "label": "", "required": True, "span": "col-span-12 md:col-span-5"},
  {"type": "input", "input_type": "text", "placeholder": "Middle Initial", "name": "form_fields[field_1cf390f]", "label": "", "required": False, "span": "col-span-12 md:col-span-2"},
  {"type": "input", "input_type": "text", "placeholder": "Last Name", "name": "form_fields[field_1084ea3]", "label": "", "required": True, "span": "col-span-12 md:col-span-5"},
  {"type": "input", "input_type": "text", "placeholder": "Email", "name": "form_fields[field_b25a55a]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "number", "placeholder": "Phone Number (Cell)", "name": "form_fields[field_3566503]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Street Address", "name": "form_fields[field_b8453d7]", "label": "", "required": False, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Street Address (Cont)", "name": "form_fields[field_820fb1f]", "label": "", "required": False, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "City", "name": "form_fields[field_01b6e75]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "select", "input_type": "", "placeholder": "", "name": "form_fields[field_c1c2157]", "label": "", "required": True, "options": ["Select any one State", "Alabama", "Alaska", "Arizona", "California", "Colorado", "Florida", "Georgia", "Hawaii", "Nevada", "New York", "Texas", "Washington"], "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Zip Code", "name": "form_fields[field_7091af9]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "heading_h2", "text": "Family Primary Contact"},
  {"type": "input", "input_type": "text", "placeholder": "First Name", "name": "form_fields[field_5611738]", "label": "", "required": True, "span": "col-span-12 md:col-span-5"},
  {"type": "input", "input_type": "text", "placeholder": "Middle Initial", "name": "form_fields[field_b1b81de]", "label": "", "required": True, "span": "col-span-12 md:col-span-2"},
  {"type": "input", "input_type": "text", "placeholder": "Last Name", "name": "form_fields[field_18ef4a7]", "label": "", "required": True, "span": "col-span-12 md:col-span-5"},
  {"type": "input", "input_type": "email", "placeholder": "Email", "name": "form_fields[field_dc6244e]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "tel", "placeholder": "Phone Number (Cell)", "name": "form_fields[field_d3ec0e2]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Street Address", "name": "form_fields[field_15fee43]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Street Address (Cont)", "name": "form_fields[field_2fc05bd]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "City", "name": "form_fields[field_6151eeb]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "select", "input_type": "", "placeholder": "", "name": "form_fields[field_4387fc1]", "label": "", "required": True, "options": ["Select any one State", "California", "Texas", "Nevada"], "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Zip Code", "name": "form_fields[field_dfcf2bf]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "heading", "text": "Cadet Information"},
  {"type": "heading_h2", "text": "Demographic Information"},
  {"type": "input", "input_type": "text", "placeholder": "First Name", "name": "form_fields[name]", "label": "", "required": True, "span": "col-span-12 md:col-span-5"},
  {"type": "input", "input_type": "text", "placeholder": "Middle Initial", "name": "form_fields[field_1cf390f]", "label": "", "required": True, "span": "col-span-12 md:col-span-2"},
  {"type": "input", "input_type": "text", "placeholder": "Last Name", "name": "form_fields[field_1084ea3]", "label": "", "required": True, "span": "col-span-12 md:col-span-5"},
  {"type": "input", "input_type": "text", "placeholder": "Gender", "name": "form_fields[field_836f7e0]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "email", "placeholder": "Cadet Unique Email Address", "name": "form_fields[field_b25a55a]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "radio", "placeholder": "", "name": "form_fields[field_5d26368]", "label": "Citizenship", "required": True, "options": ["U.S Citizen", "Legal Resident"], "span": "col-span-12"},
  {"type": "input", "input_type": "date", "placeholder": "Birthdate", "name": "form_fields[field_a270caf]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Ethnicity", "name": "form_fields[field_1f6d6d1]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "tel", "placeholder": "Primary Phone number", "name": "form_fields[field_7107711]", "label": "", "required": False, "span": "col-span-12 md:col-span-12"},
  {"type": "input", "input_type": "number", "placeholder": "Cadet Phone Number (Cell)", "name": "form_fields[field_3566503]", "label": "", "required": False, "span": "col-span-12 md:col-span-12"},
  {"type": "heading_h2", "text": "School"},
  {"type": "input", "input_type": "text", "placeholder": "Grade", "name": "form_fields[field_2884188]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "School GPA", "name": "form_fields[field_e9cb9c3]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "School Name", "name": "form_fields[field_8929269]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "School Address", "name": "form_fields[field_624ab20]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "heading_h2", "text": "Home Address"},
  {"type": "input", "input_type": "text", "placeholder": "Street Address", "name": "form_fields[field_b8453d7]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Street Address (Cont)", "name": "form_fields[field_820fb1f]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "City", "name": "form_fields[field_01b6e75]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "select", "input_type": "", "placeholder": "", "name": "form_fields[field_c1c2157]", "label": "", "required": True, "options": ["Select any one State", "California", "Nevada", "Texas"], "span": "col-span-12 md:col-span-6"},
  {"type": "input", "input_type": "text", "placeholder": "Zip Code", "name": "form_fields[field_7091af9]", "label": "", "required": True, "span": "col-span-12 md:col-span-6"},
  {"type": "heading_h2", "text": "Questionaire"},
  {"type": "select", "input_type": "", "placeholder": "", "name": "form_fields[field_9e03d79]", "label": "", "required": False, "options": ["Select Any one Community Profile", "Inner City", "Urban", "Suburban", "Rural", "Other", "Decline to state"], "span": "col-span-12"},
  {"type": "input", "input_type": "radio", "placeholder": "", "name": "form_fields[field_643a067]", "label": "Have you ever been charged with or convicted of a criminal offense?", "required": True, "options": ["Yes", "No"], "span": "col-span-12"}
]

# Slice out the hidden first form (indices 0 to 10 are hidden or duplicate)
# Index 0 is {"type": "heading_h2", "text": "Family Information"} which we will manually add
form_data = form_data[11:]

# The entire section has a burgundy background
form_html = """
        <div class="bg-[#B42041] py-16 relative w-full">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <h2 class="text-white text-center text-4xl font-heading font-bold mb-10 tracking-wide" style="text-transform: none !important; color: white !important;">Family Information</h2>
                <div class="bg-white rounded-lg shadow-xl p-8 lg:p-12 mb-8">
                    <form action="https://api.web3forms.com/submit" method="POST" id="enrollmentForm" class="elementor-form">
                        <input type="hidden" name="access_key" value="0fbe9077-aea2-4c34-af94-000cd7678747">
                        <input type="hidden" name="subject" value="New message from El Toro Battalion Enrollment Form">
                        <input type="hidden" name="redirect" value="https://web3forms.com/success">
                        <input type="checkbox" name="botcheck" class="hidden" style="display: none;">
                        <div class="grid grid-cols-12 gap-x-6 gap-y-4">
"""

for field in form_data:
    if field['type'] == 'heading':
        # E.g. "Cadet Information" which is centered and black
        form_html += f'                            <div class="col-span-12 mt-10 mb-6">\n'
        form_html += f'                                <h3 class="text-3xl font-heading font-bold text-center text-black mb-2" style="text-transform: none !important;">{field["text"]}</h3>\n'
        form_html += f'                            </div>\n'
    elif field['type'] == 'heading_h2':
        # E.g. "Family Primary Contact", "Demographic Information" etc (Solid burgundy bar)
        form_html += f'                            <div class="col-span-12 bg-[#b41e44] text-white py-2 px-4 shadow-sm mb-2">\n'
        form_html += f'                                <h4 class="text-lg font-sans font-bold">{field["text"]}</h4>\n'
        form_html += f'                            </div>\n'
    elif field['type'] == 'input':
        span = field.get('span', 'col-span-12')
        if field['input_type'] == 'radio':
            form_html += f'                            <div class="{span} mb-2">\n'
            if field['label']:
                form_html += f'                                <label class="block text-gray-700 font-sans mb-2 font-semibold">{field["label"]} {"*" if field["required"] else ""}</label>\n'
            form_html += f'                                <div class="flex space-x-6">\n'
            for opt in field.get('options', []):
                form_html += f'                                    <label class="inline-flex items-center text-gray-700 font-sans text-sm"><input type="radio" name="{field["name"]}" class="form-radio text-brandRed mr-2" {"required" if field["required"] else ""}> {opt}</label>\n'
            form_html += f'                                </div>\n'
            form_html += f'                            </div>\n'
        else:
            required_attr = "required" if field["required"] else ""
            ast = "*" if field["required"] else ""
            placeholder = f"{field['placeholder']}"
            if field["required"]: placeholder += f" *"
            form_html += f'                            <div class="{span} mb-2">\n'
            if field['label']:
                form_html += f'                                <label class="block text-gray-700 font-sans mb-1 font-semibold">{field["label"]} {ast}</label>\n'
            form_html += f'                                <input type="{field["input_type"]}" name="{field["name"]}" placeholder="{placeholder}" {required_attr} class="w-full border-b border-gray-300 py-2 px-1 focus:outline-none focus:border-brandRed bg-transparent font-sans text-gray-800 transition-colors">\n'
            form_html += f'                            </div>\n'
    elif field['type'] == 'select':
        span = field.get('span', 'col-span-12')
        required_attr = "required" if field["required"] else ""
        ast = "*" if field["required"] else ""
        form_html += f'                            <div class="{span} mb-2 relative">\n'
        if field['label']:
            form_html += f'                                <label class="block text-gray-700 font-sans mb-1 font-semibold">{field["label"]} {ast}</label>\n'
        form_html += f'                                <select name="{field["name"]}" {required_attr} class="w-full border-b border-gray-300 py-2 px-1 focus:outline-none focus:border-brandRed bg-transparent font-sans text-gray-500 appearance-none">\n'
        for opt in field.get('options', []):
            form_html += f'                                    <option value="{opt}">{opt}</option>\n'
        form_html += f'                                </select>\n'
        form_html += f'                                <div class="absolute inset-y-0 right-0 top-2 flex items-center px-2 pointer-events-none">\n'
        form_html += f'                                    <i class="fas fa-caret-down text-gray-400 mt-2"></i>\n'
        form_html += f'                                </div>\n'
        form_html += f'                            </div>\n'

form_html += """
                            <div class="col-span-12 mt-6">
                                <button type="submit" class="bg-black text-white font-sans uppercase text-sm font-semibold px-8 py-3 hover:bg-gray-800 transition-colors">SEND</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
"""

# Read original
with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/enrollment.html", "r") as f:
    orig = f.read()

# Generate new Hero section without uppercase
hero_html = """
    <!-- Hero Section -->
    <div class="relative w-full flex items-center justify-center bg-black bg-opacity-40 bg-blend-overlay" style="min-height: 500px; padding: 100px 20px; background-image: url('https://eltorobattalion.org/wp-content/uploads/2024/09/model-3_70.jpg'); background-size: cover; background-position: center; background-repeat: no-repeat;">
        <div class="text-center px-4 w-full relative z-10">
            <h1 class="text-white font-bold font-heading tracking-wide" style="font-size: clamp(40px, 6vw, 60px);">Enrollment</h1>
        </div>
    </div>
"""

# Replace page-header
orig = re.sub(r'<div class="page-header">.*?</div>\s*</div>', hero_html, orig, flags=re.DOTALL)
orig = re.sub(r'<!-- Hero Section -->.*?</div>.*?</div>', hero_html, orig, flags=re.DOTALL)

# Inject Form
if '<div class="bg-[#B42041] py-16' in orig:
    # already replaced previously, replace it again
    orig = re.sub(r'<div class="bg-\[#B42041\] py-16.*?</div>\s*</div>\s*</div>', form_html, orig, flags=re.DOTALL)
elif '<div class="bg-[#b41e44] py-16' in orig:
    orig = re.sub(r'<div class="bg-\[#b41e44\] py-16.*?</div>\s*</div>\s*</div>', form_html, orig, flags=re.DOTALL)
elif '<div class="py-16">' in orig:
    orig = re.sub(r'<div class="py-16">.*?</div>\s*</div>\s*</div>', form_html, orig, flags=re.DOTALL)
else:
    # find <h2>Family Information</h2> and replace it
    orig = orig.replace("<h2>Family Information</h2>", form_html)

ajax_script = """
<script>
    const form = document.getElementById('enrollmentForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const submitButton = form.querySelector('button[type="submit"]');
            const originalText = submitButton.innerText;
            submitButton.innerText = "SENDING...";
            submitButton.disabled = true;

            const formData = new FormData(form);
            const object = Object.fromEntries(formData);
            const json = JSON.stringify(object);

            fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: json
            })
            .then(async (response) => {
                let json = await response.json();
                if (response.status == 200) {
                    alert("Thank you! Your enrollment application has been successfully submitted.");
                    form.reset();
                } else {
                    console.error(response);
                    alert("Something went wrong! Please try again later.");
                }
            })
            .catch(error => {
                console.error(error);
                alert("Something went wrong! Please try again later.");
            })
            .finally(() => {
                submitButton.innerText = originalText;
                submitButton.disabled = false;
            });
        });
    }
</script>
"""

# Inject AJAX script before closing body tag if not already there
if "const form = document.getElementById('enrollmentForm');" not in orig:
    orig = orig.replace("</body>", ajax_script + "\\n</body>")

with open("/Users/bchandr1/Documents/my-agy-projects/ETB/public/enrollment.html", "w") as f:
    f.write(orig)

print("Enrollment page successfully generated with hero, forms, and AJAX submission logic.")
