from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader("templates"), autoescape=False)
output_dir = Path("public")

for page_path in sorted(Path("templates/pages").glob("*.html")):
    template = env.get_template(f"pages/{page_path.name}")
    output = template.render()
    (output_dir / page_path.name).write_text(output, encoding="utf-8")
    print(f"  Built: {page_path.name}")

print("Build complete.")
