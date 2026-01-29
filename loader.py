import os
from datetime import datetime
from pathlib import Path
from page import Page
import shutil
import markdown
from pygments.formatters import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension
import re
import math
import json

# local to include index.html in end or url and deploy for not(for production)
config = json.load(open('./config.json'))
url_type = config["URL_TYPE"]

class CustomHtmlFormatter(HtmlFormatter):
    '''
    This class is to add language name class to code tag
    '''
    def __init__(self, lang_str='', **options):
        super().__init__(**options)
        self.lang_str = lang_str

    def _wrap_code(self, source):
        yield 0, f'<code class="{self.lang_str}">'
        yield from source
        yield 0, '</code>'


def list_files(directory):
    found_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(os.path.join(root, file))
            if file_path.suffix.lower() == '.md':
                found_files.append(file_path)
    return found_files

def get_output_path(file_path):
    output_path = file_path.replace('content', 'output').split('/')
    if '/'.join(output_path) in ('output/index.md', 'output/404.md'):
        output_path[-1] = output_path[-1].replace('md','html')
    else:
        file_name = output_path.pop(-1)
        output_path.append(file_name.split('.')[0])
        output_path.append('index.html')
    output_path = '/'.join(output_path)
    return str(output_path)

def get_url(output_path):
    output_path = output_path.split('/')
    output_path.remove("output")
    output_path.pop(-1) # remove index.html
    url = '/' + '/'.join(output_path)

    return url

def extract_meta_data(source_path, content):
    '''
    content: markdown content
    '''
    meta_data = [line for line in content.split('\n') if line.__contains__("meta-")]
    removed_meta_content = [line for line in content.split('\n') if line not in meta_data]
    removed_meta_content = "\n".join(removed_meta_content)
    data = {}

    for mdata in meta_data:
        key = mdata.split(':')[0][5:]
        value = mdata.split(':')[1]
        if not value:
            continue
        if value.__contains__(','):
            value = value.split(', ')
        data[key] = value

    mtime = os.path.getmtime(source_path)
    data["date"] = str(datetime.fromtimestamp(mtime))
    data['url'] = get_url(get_output_path(str(source_path)))

    words = count_md_words(source_path)
    etr = estimate_read_time(words, 200)
    data['words'] = words
    data['estimate_read_time'] = etr

    return data, removed_meta_content


def convert_md_to_html(content):
    '''
    content: markdown content
    '''
    body_content = markdown.markdown(content, extensions=["toc","md4mathjax", "extra", "smarty", CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)])
    body_content = body_content.replace('&lsquo;', "'").replace('&rsquo;', "'")
    body_content = body_content.replace('&ldquo;', "\"").replace('&rdquo;', "\"")

    # generating HTML to replace task list syntax
    body_content = body_content.replace(
        '<li>[x]', '<li><input type="checkbox" checked disabled>'
    ).replace(
        '<li>[ ]', '<li><input type="checkbox" disabled>'
    )

    return body_content


def load_page(source_path):
    output_path = get_output_path(source_path)
    url = get_url(output_path)

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    data, removed_meta_content = extract_meta_data(source_path, content)
    # print("In load_pages: meta_data\n", data)
    # print("### In load_pages: removed_meta_content ###")
    # print(removed_meta_content)
    body_content = convert_md_to_html(removed_meta_content)

    page = Page(source_path,output_path,url,data,removed_meta_content,body_content)

    # print(page)
    return page

def generate_pages_json_file(files):
    json_data = []

    posts_snippets_links = [file_path for file_path in files if str(file_path) not in ('content/index.md' ,'content/about.md', 'content/404.md')]
    for posts_snippets_link in posts_snippets_links:
        with open(str(posts_snippets_link), 'r', encoding='utf-8') as f:
            content = f.read()

        data, _ = extract_meta_data(posts_snippets_link, content)
        # ----- here i am constructing json data to page.json
        json_data.append(data)
        # -----

    # ----- here i am writeing json data to page.json
    json_file = open('./output/pages.json', 'w')
    json.dump(json_data, json_file, sort_keys=True, indent=4) 
    # -----



def load_pages(directory_path):
    files = list_files(directory_path)
    pages = []
    for file_path in files:

        if str(file_path) == 'content/index.md':
            print("Found Home page index.html! Generating links")
            # generated post links and add to index.md before rendering step
            generate_pages_json_file(files)

        page = load_page(str(file_path))
        pages.append(page)
    return pages

def copy_static_files(static_folders_list, dest_folder):
    for static_folder in static_folders_list:
        if not os.path.exists(static_folder):
            raise ValueError("Static Directory doesn not Exists!")

        for file in os.listdir(static_folder):
            source = os.path.join(static_folder, file)
            destination = os.path.join(dest_folder, file)

            if os.path.isdir(source):
               shutil.copytree(source,destination,dirs_exist_ok=True)
            else:
                shutil.copy2(source,destination)
            # print(f'Copied {source} -> {destination}')

def count_md_words(path: str) -> int:
    text = Path(path).read_text(encoding="utf-8")

    # 1. Remove meta / front-matter (everything before first ---)
    text = re.sub(r"\A.*?\n---\n", "", text, flags=re.S)

    # 2. Remove fenced code blocks ``` ```
    text = re.sub(r"```.*?```", "", text, flags=re.S)

    # 3. Remove inline code `code`
    text = re.sub(r"`[^`]*`", "", text)

    # 4. Remove images ![alt](url)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)

    # 5. Replace links [text](url) → text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # 6. Remove task list checkboxes "- [ ]" or "- [x]"
    text = re.sub(r"-\s*\[[ xX]\]\s*", "", text)

    # 7. Remove markdown symbols
    text = re.sub(r"[#>*_~\-]+", " ", text)

    # 8. Collapse whitespace
    text = re.sub(r"\s+", " ", text)

    # 9. Count words
    words = re.findall(r"\b[A-Za-z0-9']+\b", text)
    return len(words)

def estimate_read_time(word_count: int, reading_speed_wpm: int) -> int:
    return max(1, math.ceil(word_count / reading_speed_wpm))

if __name__ == '__main__':
    # Specify the directory you want to list files for
    directory_path = './content'
    files = list_files(directory_path)
    # for file in files:
        # print(file)
        # if str(file) == 'content/index.md':
            # print(1)

    # load_pages(directory_path)
    # print("meta of index.md")
    # with open('content/index.md', 'r', encoding='utf-8') as f:
        # content = f.read()

    # print(extract_meta_data(content))
    # for file in files:
        # out = get_output_path(str(file))
        # get_url(out)

    load_page(str(files[0]))

    words = count_md_words("./content/about.md")
    print(f"For {words} words")
    print(estimate_read_time(words, 200), end = " ")
    print("min read")
    # pages = load_pages(directory_path)
    # print(pages[0].meta['title'])
    # print(pages[1].meta['title'])
    # print(pages[2].meta['title'])


   #  print(pages[1].source_path)
   # 
   #  print(pages[0].url)
   #  print(pages[1].url)
   #  print(pages[2].url)

    # copy_static_files(['./static/','./theme/static/'],'./output')

