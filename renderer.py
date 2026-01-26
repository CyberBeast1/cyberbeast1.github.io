from loader import load_files 
from jinja2 import Environment, FileSystemLoader
import re

def apply_base_url(html: str, base_url: str) -> str:
    if not base_url:
        return html

    def repl(match):
        attr = match.group(1)
        url = match.group(2)

        # already absolute (http, https)
        if url.startswith("http"):
            return match.group(0)

        return f'{attr}="{base_url}{url}"'

    pattern = re.compile(r'(href|src)="(/[^"]*)"')
    return pattern.sub(repl, html)

def render_page(page,theme_dir, base_url):
    env = Environment(loader=FileSystemLoader(theme_dir))
    template = env.get_template('page.html')
   
    html = template.render(page=page, base_url=base_url)
    html = apply_base_url(html, base_url)

    return html

def save_page(output_path, rendered_html):
    with open(output_path, 'w') as f:
        f.write(rendered_html)
