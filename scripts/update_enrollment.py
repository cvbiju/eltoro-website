import re

with open("public/enrollment.html", "r") as f:
    html = f.read()

new_main = """<!-- Main Content -->
    <main class="flex-grow bg-gray-50">
        
        <!-- Premium Hero Header -->
        <div class="relative bg-[radial-gradient(circle_at_center,_#2a2a2a_0%,_#000000_100%)] text-white py-20 text-center border-b-[6px] border-brandRed overflow-hidden shadow-2xl">
            <div class="absolute inset-0 bg-[linear-gradient(135deg,_rgba(190,30,46,0.15)_0%,_transparent_60%)] pointer-events-none"></div>
            <!-- Decorative Hexagons/grid could go here, but keeping it clean -->
            <div class="absolute right-0 top-0 opacity-10 pointer-events-none translate-x-1/4 -translate-y-1/4 transform scale-150">
                <i class="fas fa-file-signature text-9xl"></i>
            </div>
            <div class="max-w-7xl mx-auto px-4 relative z-10">
                <h1 class="font-heading text-5xl md:text-6xl font-bold tracking-[0.2em] uppercase drop-shadow-lg">Enrollment</h1>
                <p class="mt-4 text-gray-300 max-w-2xl mx-auto text-lg font-light tracking-wide">Join the El Toro Battalion. Challenge yourself, build leadership, and become part of a legacy.</p>
            </div>
        </div>

        <div class="bg-gray-50 py-16">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                
                <!-- Enrollment Video -->
                <div class="w-full max-w-4xl mx-auto mb-20">
                    <div class="shadow-2xl rounded-2xl overflow-hidden relative border-8 border-white bg-white group" style="padding-top: 56.25%;">
                        <div class="absolute inset-0 z-0 bg-brandBlack flex items-center justify-center">
                            <i class="fas fa-circle-notch fa-spin text-4xl text-brandRed"></i>
                        </div>
                        <iframe class="absolute top-0 left-0 w-full h-full z-10 opacity-0 transition-opacity duration-1000" onload="this.classList.remove('opacity-0')" src="https://www.youtube.com/embed/YpL9qZN_18E" title="El Toro Battalion Enrollment Video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    </div>
                </div>

                <!-- Gamified Requirements Checklist -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-20 items-start">
                    <div class="col-span-1 lg:col-span-4 lg:sticky lg:top-32">
                        <h2 class="text-4xl font-heading uppercase font-bold text-brandBlack mb-4">Requirements to Join</h2>
                        <p class="text-gray-500 mb-6 text-lg leading-relaxed">Applicants for the USNLCC (10-13) and USNSCC (13-17) must meet the following baseline criteria.</p>
                        <div class="hidden lg:block w-32 h-1 bg-brandRed rounded-full mb-8"></div>
                    </div>
                    
                    <div class="col-span-1 lg:col-span-8">
                        <div class="space-y-6 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-300 before:to-transparent">
                            
                            <!-- Requirement 1 -->
                            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-brandRed text-white shadow shadow-red-500/50 shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 transform group-hover:scale-110 transition-transform">
                                    <i class="fas fa-heartbeat"></i>
                                </div>
                                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-white rounded-xl shadow border border-gray-100 group-hover:shadow-lg transition-shadow border-l-4 border-brandRed flex flex-col">
                                    <div class="flex items-center mb-2">
                                        <h3 class="font-heading font-bold text-xl uppercase text-brandBlack m-0">Physical Examination</h3>
                                    </div>
                                    <p class="text-sm text-gray-500 leading-relaxed">A medical examination similar to a high school sports physical is required. No one will be denied admission due to a medical disability (waivers/accommodations available).</p>
                                </div>
                            </div>

                            <!-- Requirement 2 -->
                            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-brandRed text-white shadow shadow-red-500/50 shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 transform group-hover:scale-110 transition-transform">
                                    <i class="fas fa-graduation-cap"></i>
                                </div>
                                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-white rounded-xl shadow border border-gray-100 group-hover:shadow-lg transition-shadow border-l-4 border-brandRed flex flex-col">
                                    <div class="flex items-center mb-2">
                                        <h3 class="font-heading font-bold text-xl uppercase text-brandBlack m-0">Education</h3>
                                    </div>
                                    <p class="text-sm text-gray-500 leading-relaxed">Applicants must be enrolled in school (public, private, or sanctioned home school) and maintain satisfactory scholastic standing. A recent report card is required.</p>
                                </div>
                            </div>

                            <!-- Requirement 3 -->
                            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-brandRed text-white shadow shadow-red-500/50 shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 transform group-hover:scale-110 transition-transform">
                                    <i class="fas fa-balance-scale"></i>
                                </div>
                                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-white rounded-xl shadow border border-gray-100 group-hover:shadow-lg transition-shadow border-l-4 border-brandRed flex flex-col">
                                    <div class="flex items-center mb-2">
                                        <h3 class="font-heading font-bold text-xl uppercase text-brandBlack m-0">Moral Character</h3>
                                    </div>
                                    <p class="text-sm text-gray-500 leading-relaxed">Applicants must possess good moral character: unmarried, drug-free, and absolutely free of any felony convictions.</p>
                                </div>
                            </div>

                            <!-- Requirement 4 -->
                            <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                                <div class="flex items-center justify-center w-10 h-10 rounded-full border border-white bg-brandRed text-white shadow shadow-red-500/50 shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 transform group-hover:scale-110 transition-transform">
                                    <i class="fas fa-user-friends"></i>
                                </div>
                                <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-white rounded-xl shadow border border-gray-100 group-hover:shadow-lg transition-shadow border-l-4 border-brandRed flex flex-col">
                                    <div class="flex items-center mb-2">
                                        <h3 class="font-heading font-bold text-xl uppercase text-brandBlack m-0">Parental Involvement</h3>
                                    </div>
                                    <p class="text-sm text-gray-500 leading-relaxed">Parental support is crucial for drill attendance, transportation, and enforcing personal appearance standards (particularly haircuts & styling).</p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>

                <!-- Pre-Form Anchor -->
                <div id="enrollment-form-section" class="scroll-mt-32"></div>

                <!-- Multi-Step Application Form -->
                <div class="max-w-4xl mx-auto mt-24">
                    <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-gray-200">
                        <!-- Form Header with Progress -->
                        <div class="bg-[#1a1a1a] p-8 border-b-4 border-brandRed relative">
                            <h2 class="text-white text-center text-3xl font-heading font-bold tracking-widest uppercase mb-6">Application Form</h2>
                            
                            <!-- Stepper Container -->
                            <div class="flex justify-between items-center max-w-xl mx-auto relative px-2">
                                <!-- Progress Bar Background -->
                                <div class="absolute left-8 right-8 top-1/2 -translate-y-1/2 h-1 bg-gray-700 z-0"></div>
                                <!-- Active Progress Bar -->
                                <div id="progress-bar-fill" class="absolute left-8 top-1/2 -translate-y-1/2 h-1 bg-brandRed z-0 transition-all duration-500 w-0"></div>
                                
                                <!-- Step 1 Indicator -->
                                <div class="step-indicator relative z-10 flex flex-col items-center" data-target="1">
                                    <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm border-2 border-brandRed bg-brandRed text-white transition-colors duration-300">1</div>
                                    <span class="absolute -bottom-6 text-xs font-bold text-white uppercase tracking-wider whitespace-nowrap">Family</span>
                                </div>
                                
                                <!-- Step 2 Indicator -->
                                <div class="step-indicator relative z-10 flex flex-col items-center" data-target="2">
                                    <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm border-2 border-gray-600 bg-gray-800 text-gray-400 transition-colors duration-300">2</div>
                                    <span class="absolute -bottom-6 text-xs text-gray-400 uppercase tracking-wider whitespace-nowrap hidden sm:block">Cadet</span>
                                </div>
                                
                                <!-- Step 3 Indicator -->
                                <div class="step-indicator relative z-10 flex flex-col items-center" data-target="3">
                                    <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm border-2 border-gray-600 bg-gray-800 text-gray-400 transition-colors duration-300">3</div>
                                    <span class="absolute -bottom-6 text-xs text-gray-400 uppercase tracking-wider whitespace-nowrap hidden sm:block">Review</span>
                                </div>
                            </div>
                        </div>

                        <div class="p-8 lg:p-12">
                            <form action="https://api.web3forms.com/submit" method="POST" id="enrollmentForm" class="elementor-form">
                                <input type="hidden" name="access_key" value="0fbe9077-aea2-4c34-af94-000cd7678747">
                                <input type="hidden" name="subject" value="New message from El Toro Battalion Enrollment Form">
                                <input type="hidden" name="redirect" value="https://web3forms.com/success">
                                <input type="checkbox" name="botcheck" class="hidden" style="display: none;">

                                <!-- STEP 1: Family Info -->
                                <div id="form-step-1" class="form-step transition-opacity duration-300">
                                    <h3 class="text-2xl font-heading font-bold text-brandBlack mb-6 uppercase border-l-4 border-brandRed pl-3">Family Primary Contact</h3>
                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6">
                                        <div class="relative">
                                            <input type="text" name="form_fields[fname_family]" placeholder="First Name *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">First Name *</label>
                                        </div>
                                        <div class="grid grid-cols-3 gap-4">
                                            <div class="relative col-span-1">
                                                <input type="text" name="form_fields[minitial_family]" placeholder="M.I. *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">M.I. *</label>
                                            </div>
                                            <div class="relative col-span-2">
                                                <input type="text" name="form_fields[lname_family]" placeholder="Last Name *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Last Name *</label>
                                            </div>
                                        </div>
                                        <div class="relative">
                                            <input type="email" name="form_fields[email_family]" placeholder="Email *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Email *</label>
                                        </div>
                                        <div class="relative">
                                            <input type="tel" name="form_fields[phone_family]" placeholder="Phone Number (Cell) *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Phone Number (Cell) *</label>
                                        </div>
                                        <div class="relative md:col-span-2">
                                            <input type="text" name="form_fields[street_family]" placeholder="Street Address *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Street Address *</label>
                                        </div>
                                        <div class="relative">
                                            <input type="text" name="form_fields[city_family]" placeholder="City *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">City *</label>
                                        </div>
                                        <div class="grid grid-cols-2 gap-4">
                                            <div class="relative">
                                                <select name="form_fields[state_family]" required class="w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent appearance-none">
                                                    <option value="" disabled selected>State *</option>
                                                    <option value="California">California</option>
                                                    <option value="Nevada">Nevada</option>
                                                    <option value="Texas">Texas</option>
                                                </select>
                                                <i class="fas fa-caret-down absolute right-3 top-4 text-gray-400 pointer-events-none"></i>
                                            </div>
                                            <div class="relative">
                                                <input type="text" name="form_fields[zip_family]" placeholder="Zip Code *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Zip Code *</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- STEP 2: Cadet Info -->
                                <div id="form-step-2" class="form-step hidden opacity-0 transition-opacity duration-300">
                                    <h3 class="text-2xl font-heading font-bold text-brandBlack mb-6 uppercase border-l-4 border-brandRed pl-3">Cadet Demographics</h3>
                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6 mb-8">
                                        <div class="relative">
                                            <input type="text" name="form_fields[fname_cadet]" placeholder="First Name *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Cadet First Name *</label>
                                        </div>
                                        <div class="grid grid-cols-3 gap-4">
                                            <div class="relative col-span-1">
                                                <input type="text" name="form_fields[minitial_cadet]" placeholder="M.I. *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">M.I. *</label>
                                            </div>
                                            <div class="relative col-span-2">
                                                <input type="text" name="form_fields[lname_cadet]" placeholder="Last Name *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Cadet Last Name *</label>
                                            </div>
                                        </div>
                                        <div class="relative grid grid-cols-2 gap-4">
                                            <div class="col-span-1">
                                                <input type="text" name="form_fields[gender_cadet]" placeholder="Gender *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Gender *</label>
                                            </div>
                                            <div class="col-span-1">
                                                <input type="text" name="form_fields[ethnicity_cadet]" placeholder="Ethnicity *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 pl-1 border-gray-200 md:ml-4 -border -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Ethnicity *</label>
                                            </div>
                                        </div>                                        
                                        <div class="relative">
                                            <input type="date" name="form_fields[dob_cadet]" required class="w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm">Birthdate *</label>
                                        </div>
                                        <div class="md:col-span-2 pt-2 border-t border-gray-100 mt-2">
                                            <label class="block text-gray-800 font-semibold mb-3">Citizenship *</label>
                                            <div class="flex space-x-8">
                                                <label class="inline-flex items-center text-gray-600 cursor-pointer group hover:text-brandBlack"><input type="radio" name="form_fields[citizenship]" value="US Citizen" class="form-radio text-brandRed w-5 h-5 mr-3 focus:ring-brandRed" required> U.S Citizen</label>
                                                <label class="inline-flex items-center text-gray-600 cursor-pointer group hover:text-brandBlack"><input type="radio" name="form_fields[citizenship]" value="Legal Resident" class="form-radio text-brandRed w-5 h-5 mr-3 focus:ring-brandRed" required> Legal Resident</label>
                                            </div>
                                        </div>
                                    </div>
                                    <h3 class="text-2xl font-heading font-bold text-brandBlack mb-6 uppercase border-l-4 border-brandRed pl-3 mt-8">School Information</h3>
                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6">
                                        <div class="grid grid-cols-2 gap-4 relative md:col-span-2">
                                            <div>
                                                <input type="text" name="form_fields[grade_cadet]" placeholder="Grade *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">Grade *</label>
                                            </div>
                                            <div class="relative">
                                                <input type="text" name="form_fields[gpa_cadet]" placeholder="School GPA *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                                <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">GPA *</label>
                                            </div>
                                        </div>
                                        <div class="relative">
                                            <input type="text" name="form_fields[school_name]" placeholder="School Name *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">School Name *</label>
                                        </div>
                                        <div class="relative">
                                            <input type="text" name="form_fields[school_address]" placeholder="School Address *" required class="peer w-full border-b-2 border-gray-200 py-3 text-gray-800 focus:outline-none focus:border-brandRed transition-colors bg-transparent placeholder-transparent">
                                            <label class="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:top-3 peer-focus:-top-3.5 peer-focus:text-sm peer-focus:text-brandRed">School Address *</label>
                                        </div>
                                    </div>
                                </div>

                                <!-- STEP 3: Final Review -->
                                <div id="form-step-3" class="form-step hidden opacity-0 transition-opacity duration-300">
                                    <h3 class="text-2xl font-heading font-bold text-brandBlack mb-6 uppercase border-l-4 border-brandRed pl-3">Questionnaire</h3>
                                    
                                    <div class="bg-gray-50 p-6 rounded-lg mb-8 border border-gray-200">
                                        <div class="mb-6 relative">
                                            <label class="block text-gray-800 font-semibold mb-2">Community Profile</label>
                                            <select name="form_fields[community]" class="w-full border border-gray-300 bg-white rounded py-3 px-4 focus:outline-none focus:border-brandRed focus:ring-1 focus:ring-brandRed transition-all appearance-none cursor-pointer">
                                                <option value="" disabled selected>Select Community Profile...</option>
                                                <option value="Inner City">Inner City</option>
                                                <option value="Urban">Urban</option>
                                                <option value="Suburban">Suburban</option>
                                                <option value="Rural">Rural</option>
                                                <option value="Other">Other</option>
                                                <option value="Decline to state">Decline to state</option>
                                            </select>
                                            <i class="fas fa-caret-down absolute right-4 top-11 text-gray-400 pointer-events-none"></i>
                                        </div>

                                        <div>
                                            <label class="block text-gray-800 font-semibold mb-4">Have you ever been charged with or convicted of a criminal offense? *</label>
                                            <div class="bg-white p-4 border border-gray-200 rounded flex space-x-8">
                                                <label class="inline-flex items-center text-gray-700 cursor-pointer font-bold"><input type="radio" name="form_fields[criminal]" value="Yes" class="form-radio text-brandRed w-5 h-5 mr-3 focus:ring-brandRed" required> YES</label>
                                                <label class="inline-flex items-center text-gray-700 cursor-pointer font-bold"><input type="radio" name="form_fields[criminal]" value="No" class="form-radio text-brandRed w-5 h-5 mr-3 focus:ring-brandRed" required> NO</label>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="bg-red-50 border-l-4 border-brandRed p-5 rounded">
                                        <h4 class="font-bold text-brandRed mb-1"><i class="fas fa-info-circle mr-2"></i> Almost Done</h4>
                                        <p class="text-sm text-gray-700">By submitting this form, you acknowledge that all information provided is accurate and you understand the requirements for joining the El Toro Battalion. A commanding officer will be in touch shortly.</p>
                                    </div>
                                </div>

                                <!-- Form Controls Navigation -->
                                <div class="mt-10 pt-6 border-t border-gray-200 flex justify-between items-center">
                                    <button type="button" id="form-prev" class="px-6 py-3 border-2 border-gray-300 text-gray-600 font-bold uppercase tracking-widest hover:border-gray-800 hover:text-gray-800 transition-colors hidden rounded">Back</button>
                                    
                                    <div class="ml-auto">
                                        <button type="button" id="form-next" class="bg-brandBlack text-white uppercase text-sm font-bold tracking-widest px-10 py-3.5 hover:bg-brandRed hover:shadow-lg transition-all rounded">Next Step <i class="fas fa-arrow-right ml-2 text-xs"></i></button>
                                        
                                        <button type="submit" id="form-submit" class="bg-brandRed text-white uppercase text-sm font-bold tracking-widest px-10 py-3.5 hover:bg-brandRedHover hover:shadow-[0_0_15px_rgba(190,30,46,0.5)] transition-all hidden rounded"><i class="fas fa-paper-plane mr-2"></i> Submit Application</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </main>
"""

new_html = re.sub(r"<!-- Hero Section -->.*?<!-- Footer mirroring the live site 4-columns -->", new_main + "\n    <!-- Footer mirroring the live site 4-columns -->", html, flags=re.DOTALL)

# Insert the Multi-step JS
multi_step_js = """
<script>
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
            // Update visibility of steps
            steps.forEach((step, index) => {
                if(index === currentStep) {
                    step.classList.remove('hidden');
                    // Slight delay for fade in effect
                    setTimeout(() => step.classList.remove('opacity-0'), 50);
                } else {
                    step.classList.add('hidden', 'opacity-0');
                }
            });

            // Update Progress Bar (0%, 50%, 100%)
            const progress = (currentStep / (steps.length - 1)) * 100;
            progressBar.style.width = `${progress}%`;

            // Update Indicators
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

            // Update Buttons
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
            inputs.forEach(input => {
                if (!input.checkValidity()) {
                    input.reportValidity();
                    isValid = false;
                }
            });
            return isValid;
        }

        nextBtn.addEventListener('click', function() {
            if(validateCurrentStep()) {
                currentStep++;
                updateForm();
                // Scroll to top of form section smoothly
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
    });
</script>
"""

new_html = re.sub(r"    <script>\n        const form = document", multi_step_js + "\n    <script>\n        const form = document", new_html)

with open("public/enrollment.html", "w") as f:
    f.write(new_html)
