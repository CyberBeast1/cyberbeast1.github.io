#!/home/cyber_monarch/Documents/Code/Python/.venv/bin/python
from loader import load_pages, copy_static_files
from renderer import render_page, save_page 
import os
import json

config = json.load(open('./config.json'))
os.makedirs(config['OUTPUT_DIR'], exist_ok=True)

pages = load_pages(config['DIR_PATH'])

for page in pages:
    rendered_html = render_page(page, config['THEME_DIR'], config['BASE_URL'])
    output_page_dir = os.path.dirname(page.output_path)

    # create parent dirs of output html page if not exist
    if not os.path.exists(output_page_dir):
        os.makedirs(output_page_dir)

    save_page(page.output_path, rendered_html)
    print(f"BUILT 🎉 - {page.source_path} -> {page.output_path}")

copy_static_files(config['STATIC_DIRS_PATH'], config['OUTPUT_DIR'])
print(f"Copied STATIC FILES {config['STATIC_DIRS_PATH']} -> {config['OUTPUT_DIR']}")
print("🥳 Successfully compiled your blog 📃")
print("Output Saved in ", config['OUTPUT_DIR'] + "\n## run: xdg-open ./output/index.html OR\ncd output && python -m http.server 8000")
