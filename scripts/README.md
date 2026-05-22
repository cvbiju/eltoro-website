# Scripts

Utility and migration scripts from the WordPress-to-static migration.

**Most scripts in this directory are obsolete.** They were written to patch the old flat HTML files directly and do not work with the Jinja2 template system. For content changes, edit `templates/pages/` and run `python3 build.py` from the repo root.

---

## Still Useful

| Script | Purpose |
|---|---|
| `serve_local.py` | Starts a local HTTP server on :8000 for previewing `public/` |
| `trim_video.py` | Trims/converts video files (useful for the hero background video) |
| `tmp_rembg.py` | Removes backgrounds from images using `rembg` |
| `screenshot_pages.py` | Takes screenshots of all pages for visual regression review |

---

## Obsolete (WordPress Migration Artifacts)

These were one-off scripts that patched the old flat HTML files. They are not needed now that all pages are generated from Jinja2 templates.

**Enrollment form scripts**: `fix_enrollment.py`, `build_enrollment_form.py`, `extract_enrollment.py`, `parse_form.py`, `update_enrollment.py`

**Gallery scripts**: `fix_gallery_css_columns.py`, `fix_gallery_css_override.py`, `fix_gallery_dynamic.py`, `fix_gallery_grid_missing.py`, `fix_gallery_html.py`, `fix_gallery_layout.py`, `fix_gallery_referrer.py`, `fix_gallery_script.py`, `fix_gallery_thumbnail_url.py`, `fix_gallery_thumbnail_url2.py`, `fix_gallery_thumbnail_url3.py`, `revert_gallery.py`, `rewrite_gallery.py`, `update_gallery.py`, `get_live_gallery.py`

**Page-specific patchers**: `update_about_us.py`, `build_about_us_fixed.py`, `update_cadet_mess.py`, `update_grooming.py`, `update_index.py`, `update_parents.py`, `update_physical_fitness.py`, `fix_images.py`, `fix_parents_footer.py`, `fix_phone.py`, `fix_social_links.py`, `fix_social_links_regex.py`, `fix_suzy.py`, `lighten_shadows.py`, `officers_images.py`, `about_images.py`

**Footer patchers**: `update_footer.py`, `update_footer_layout.py`, `update_footer_names.py`, `update_footer_robust.py`, `update_footer_text.py`

**Security patches**: `patch_low_security.py`, `patch_medium_security.py` (applied to flat HTML; superceded by netlify.toml headers)

**Migration tools**: `extract_html.py`, `compare_pages.py`, `screenshot_drive.py`, `screenshot_drive_fixed.py`

---

These obsolete scripts can be deleted once it's confirmed that no historical reference is needed.
