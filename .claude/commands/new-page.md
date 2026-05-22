Scaffold a new page for the El Toro Battalion website.

1. Ask the user for:
   - **Page slug** (e.g. `sea-trials`) — used for the filename and URL path
   - **Page title** (e.g. `Sea Trials`) — shown in the hero header and browser tab
   - **Brief description** — one sentence about the page's purpose

2. Create `templates/pages/{slug}.html` using this starter template:

```html
{% extends "_base.html" %}
{% block page_title %}{Page Title} | El Toro Battalion{% endblock %}
{% block main_attrs %}class="flex-grow bg-gray-50"{% endblock %}
{% block content %}
    <!-- Hero Header -->
    <div class="relative bg-[radial-gradient(circle_at_center,_#2a2a2a_0%,_#000000_100%)] text-white py-20 text-center border-b-4 border-brandRed overflow-hidden">
        <div class="absolute inset-0 bg-[linear-gradient(135deg,_rgba(190,30,46,0.2)_0%,_transparent_50%)] pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10">
            <h1 class="font-heading text-5xl md:text-6xl font-bold tracking-[0.2em] uppercase">{Page Title}</h1>
        </div>
    </div>

    <div class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Page content here -->
        </div>
    </div>
{% endblock %}
```

3. Add a nav link in `templates/_base.html` — both the desktop dropdown and the mobile menu.
   Follow the existing pattern for other pages in each menu.

4. Run `python3 build.py` and confirm `public/{slug}.html` was created.

5. If the page uses any external domain not already in the CSP (see CLAUDE.md), add it to
   the `[[headers]]` block in `netlify.toml` before pushing.
