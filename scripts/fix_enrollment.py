import re

with open("public/enrollment.html", "r") as f:
    html = f.read()

# Remove the incorrectly placed validateCurrentStep block
bad_block = re.search(r'        function validateCurrentStep\(\) \{.*?\n        \}\n', html, re.DOTALL)
if bad_block:
    html = html.replace(bad_block.group(0), '')

# Define the correct Multi-Step JS
multi_step_js = """<script>
    // Multi-Step Form Logic
    document.addEventListener('DOMContentLoaded', function() {
        const steps = document.querySelectorAll('.form-step');
        const indicators = document.querySelectorAll('.step-indicator');
        const nextBtn = document.getElementById('form-next');
        const prevBtn = document.getElementById('form-prev');
        const submitBtn = document.getElementById('form-submit');
        const progressBar = document.getElementById('progress-bar-fill');
        let currentStep = 0;

        function updateForm() {
            steps.forEach((step, index) => {
                if(index === currentStep) {
                    step.classList.remove('hidden');
                    setTimeout(() => step.classList.remove('opacity-0'), 50);
                } else {
                    step.classList.add('hidden', 'opacity-0');
                }
            });

            const progress = (currentStep / (steps.length - 1)) * 100;
            progressBar.style.width = `${progress}%`;

            indicators.forEach((indicator, index) => {
                const circle = indicator.querySelector('div');
                const text = indicator.querySelector('span');
                if (index <= currentStep) {
                    circle.className = 'w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm border-2 border-brandRed bg-brandRed text-white transition-colors duration-300';
                    text.classList.add('text-white');
                    text.classList.remove('text-gray-400');
                } else {
                    circle.className = 'w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm border-2 border-gray-600 bg-gray-800 text-gray-400 transition-colors duration-300';
                    text.classList.remove('text-white');
                    text.classList.add('text-gray-400');
                }
            });

            if (currentStep === 0) {
                prevBtn.classList.add('hidden');
                nextBtn.classList.remove('hidden');
                submitBtn.classList.add('hidden');
            } else if (currentStep === steps.length - 1) {
                prevBtn.classList.remove('hidden');
                nextBtn.classList.add('hidden');
                submitBtn.classList.remove('hidden');
            } else {
                prevBtn.classList.remove('hidden');
                nextBtn.classList.remove('hidden');
                submitBtn.classList.add('hidden');
            }
        }

        function validateCurrentStep() {
            const currentStepEl = steps[currentStep];
            const inputs = currentStepEl.querySelectorAll('input[required], select[required]');
            let isValid = true;
            let firstInvalid = null;
            
            inputs.forEach(input => {
                input.classList.remove('border-red-500', 'border-b-red-500'); // clear UI errors
                
                if (!input.checkValidity()) {
                    input.classList.add('border-b-[3px]', 'border-b-red-500', 'bg-red-50', 'bg-opacity-50'); // Highlight error field visually with stronger borders
                    if (!firstInvalid) firstInvalid = input;
                    isValid = false;
                }
            });
            
            if (firstInvalid) {
                firstInvalid.reportValidity();
            }
            return isValid;
        }

        nextBtn.addEventListener('click', function() {
            if(validateCurrentStep()) {
                currentStep++;
                updateForm();
                document.getElementById('enrollment-form-section').scrollIntoView({behavior: 'smooth'});
            }
        });

        prevBtn.addEventListener('click', function() {
            currentStep--;
            updateForm();
            document.getElementById('enrollment-form-section').scrollIntoView({behavior: 'smooth'});
        });

        // Initialize Form
        updateForm();
        
        // Remove error classes on input
        document.querySelectorAll('input, select').forEach(el => {
            el.addEventListener('input', () => {
                el.classList.remove('border-b-[3px]', 'border-b-red-500', 'bg-red-50', 'bg-opacity-50');
            });
        });
    });
</script>

"""

# Re-inject it properly before the final web3forms script
html = html.replace("<script>\n    const form = document.getElementById('enrollmentForm');", multi_step_js + "<script>\n    const form = document.getElementById('enrollmentForm');")

with open("public/enrollment.html", "w") as f:
    f.write(html)
