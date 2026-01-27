from loader import load_pages, copy_static_files
from renderer import render_page, save_page 
import os

DIR_PATH = './content'
THEME_DIR = './theme'
STATIC_DIRS_PATH = ['./static', './theme/static/']
OUTPUT_DIR = './output/'
BASE_URL = 'file:///home/cyber_monarch/Documents/Code/Python/staticSiteGen/site/output' # change to empty string when deploying

files = load_pages(DIR_PATH)

# print(files[0].output_path)


for file in files:
    rendered_html = render_page(file, THEME_DIR, BASE_URL)
    output_file_dir = os.path.dirname(file.output_path)

    # create parent dirs of output html file if not exist
    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)

    save_page(file.output_path, rendered_html)
    print(f"BUILT 🎉 - {file.source_path} -> {file.output_path}")

copy_static_files(STATIC_DIRS_PATH, OUTPUT_DIR)
print(f"Copied STATIC FILES {STATIC_DIRS_PATH} -> {OUTPUT_DIR}")
print("🥳 Successfully compiled your blog 📃")
print("Output Saved in ", OUTPUT_DIR + "\n## run: xdg-open ./output/index.html")
