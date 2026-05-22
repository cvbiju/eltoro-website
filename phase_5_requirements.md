# Phase 5: Functional & Content Requirements

Based on an extensive competitive analysis of the National USNSCC Headquarters site, alongside peer divisions (Seal Beach, Escondido, South Bay, Monroe, and Gunfighter), I have formulated a business requirements document for the next phase of the El Toro Battalion web migration.

## Competitive Analysis Summary

While our recent modernizations have elevated the El Toro Battalion site aesthetically beyond its peers, several peer sites excel significantly in **functional self-service** and **localized storytelling**. 

Peer units place a heavy emphasis on turning their websites into operational hubs (managing requisition forms, linking out to official DOD/National portals, and showcasing local integration).

## Proposed Requirements for Implementation

Here are the grouped functional and content requirements recommended for Phase 5.

### 1. Digital Requisition & Service Forms (Operations)
Currently, cadets likely request gear or sign off on renewals using paper forms or email. We can digitalize this logistics pipeline (similar to Monroe and Escondido):
- **REQ-1.1:** Develop a `cadet-requests.html` hub.
- **REQ-1.2:** Implement a **Uniform & Ribbon Requisition Form** (using Web3Forms like our enrollment page) so cadets can officially request replacement covers, ranks, or ribbons.
- **REQ-1.3:** Implement a **Color Guard Request Form** for local businesses and civic organizations to easily invite the ETB Color Guard to present colors at events.
- **REQ-1.4:** Implement a **Cadet Renewal / Admin Form** to streamline annual re-enrollment logistics.

### 2. External Portal Integrations (Cadet Resources)
HQ, Gunfighter, and Escondido prominently feature the national mandatory management tools. Our site currently fails to link prominently to them.
- **REQ-2.1:** Create a dedicated "Cadet Portal" or "Quick Links" floating dashboard.
- **REQ-2.2:** Add direct, highly visible SSO jumps to **The Quarterdeck** (Administrative records).
- **REQ-2.3:** Add direct jumps to **Polaris** (Advancement Coursework).
- **REQ-2.4:** Build out visual **Rank Insignia & Ribbon Charts** to gamify advancement and give cadets an easy visual reference.

### 3. Program Clarification (UX/Content)
South Bay and HQ explicitly differentiate the junior and senior programs on their landing pages to help parents immediately self-select. 
- **REQ-3.1:** Currently, ETB relies on the general "Programs" page. We need to explicitly demarcate **Navy League Cadet Corps (NLCC)** (Ages 10-13) vs. **Naval Sea Cadet Corps (NSCC)** (Ages 14-18) natively on the Home Page and Enrollment flows.
- **REQ-3.2:** Explicitly link or host the official *NSCC Parent Handbook PDF* in the Parents section (mirroring Escondido).

### 4. Community & Legacy (Storytelling)
Monroe and Escondido maximize their local community ties to increase donations and enrollment.
- **REQ-4.1:** Establish a **"Wall of Service" / Alumni Page**. List former ETB cadets who have officially enlisted in the armed services, entered ROTC, or attended Service Academies to prove the program's ROI to prospective parents.
- **REQ-4.2:** Establish a **Testimonials Section** from current parents and Cadets. Let the community sell the program.
- **REQ-4.3:** Deepen the "About Us" history block. Specifically outline the connection/history of the **El Toro Marine Base** namesake.

## Phase 5 Prioritization

Of the requirements listed above, I recommend prioritizing **Group 1 (Requisition Forms)** and **Group 2 (External Portal Integrations)**. These will transition the site from being a pure "Digital Brochure" into an actual **Operational Tool** that the commanding officers and cadets rely on day-to-day.

*** 

### User Review Required
Please review the gathered requirements above. Let me know which specific group or requirement number you would like to tackle first, or if there are any additional operational bottlenecks you want to solve!
