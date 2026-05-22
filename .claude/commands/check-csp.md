Audit all external domains used in the Jinja2 templates against the Content Security Policy in `netlify.toml`.

Steps:

1. Grep `templates/` recursively for all `https://` URLs. Look for:
   - `src="https://` (scripts, iframes, images)
   - `href="https://` (stylesheets, links)
   - `fetch(` and API call patterns
   - `url(https://` in CSS

2. Extract the hostname (scheme + domain only) from each URL found.

3. Read the CSP `Content-Security-Policy` header value from `netlify.toml`.

4. Map each external hostname to the correct CSP directive:
   - `<script src>` → `script-src`
   - `<link rel="stylesheet">` → `style-src`
   - Font URLs → `font-src`
   - `<iframe src>` → `frame-src`
   - `fetch()` / XHR / API calls → `connect-src`
   - `<img src>` → `img-src`

5. Report three things:
   - **Missing**: domains used in templates but absent from the CSP (will break in production)
   - **Covered**: domains present in both (all good)
   - **Unused**: domains in CSP not found in any template (cleanup candidates)

6. End with a one-line summary: "X covered, Y missing, Z unused."
