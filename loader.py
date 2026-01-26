import os
from os.path import isdir
from pathlib import Path
from page import Page
import shutil
import markdown
from pygments.formatters import HtmlFormatter, html
from markdown.extensions.codehilite import CodeHiliteExtension


class CustomHtmlFormatter(HtmlFormatter):
    '''
    This class is to add language name class to code tag
    '''
    def __init__(self, lang_str='', **options):
        # options['style'] = 'monokai' # only useful when internal pygment cdn link is wokring but its not so my setup manually makes pygment.css using pygmentize -S dracula -f html -a .codehilite > pygment.css and uses that
        super().__init__(**options)
        # lang_str has the value {lang_prefix}{lang}
        # specified by the CodeHilite's options
        self.lang_str = lang_str

    def _wrap_code(self, source):
        yield 0, f'<code class="{self.lang_str}">'
        yield from source
        yield 0, '</code>'


def list_files(directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(os.path.join(root, file))
            # print(file_path)
            # print(file_path.suffix.lower() == '.md')
            if file_path.suffix.lower() == '.md':
                found_files.append(file_path)
    return found_files

def get_output_path(file_path):
    # ./content/index.md -> ./output/index.html
    # ./content/about.md -> ./output/about/index.html
    # ./content/blog/first-post.md -> ./output/blog/first-post.html
    output_path = file_path.replace('content', 'output').split('/')
    # print("output_path: ", '/'.join(output_path))
    if '/'.join(output_path) == 'output/index.md':
        output_path[-1] = output_path[-1].replace('md','html')
    else:
        file_name = output_path.pop(-1)
        output_path.append(file_name.split('.')[0])
        output_path.append('index.html')
    output_path = '/'.join(output_path)
    # print(f"OUTPUT_PATH: {file_path} -> {output_path}")
    return str(output_path)

def get_url(output_path):
    original_path = output_path
    output_path = output_path.split('/')
    output_path.remove("output")

    output_path.pop(-1) # remove index.html
    url = '/' + '/'.join(output_path)

    # print(f"get_url: {original_path} -> {url}")
    return url

def load_file(source_path):
    output_path = get_output_path(source_path)
    url = get_url(output_path)

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # logic for getting meta data
    meta_data = [line for line in content.split('\n') if line.__contains__("meta-")]
    content = [line for line in content.split('\n') if line not in meta_data]
    content = "\n".join(content)
    data = {}

    for mdata in meta_data:
        key = mdata.split(':')[0][5:]
        value = mdata.split(':')[1]
        if not value:
            continue
        if value.__contains__(','):
            value = value.split(', ')
        data[key] = value

    # markdowm fragment conversion
    body_content = markdown.markdown(content, extensions=["md4mathjax", "extra", "smarty", CodeHiliteExtension(pygments_formatter=CustomHtmlFormatter)])
    # md4mathjax extension is causing some issue its adding &lsquo for ' and that is giving error in rendering so i am replacing them manually
    body_content = body_content.replace('&lsquo;', "'").replace('&rsquo;', "'")
    body_content = body_content.replace('&ldquo;', "\"").replace('&rdquo;', "\"")

    # Example of modifying the generated HTML to replace task list syntax
    body_content = body_content.replace(
        '<li>[x]', '<li><input type="checkbox" checked disabled>'
    ).replace(
        '<li>[ ]', '<li><input type="checkbox" disabled>'
    )

    page = Page(source_path,output_path,url,data,content,body_content)

    # print(page)
    return page

def load_files(directory_path):
    files = list_files(directory_path)
    pages = []
    for file_path in files:
        page = load_file(str(file_path))
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

if __name__ == '__main__':
    # Specify the directory you want to list files for
    directory_path = './content'
    # files = list_files(directory_path)
    # print(files)

    # for file in files:
        # out = get_output_path(str(file))
        # get_url(out)

    # load_file(str(files[0]))
    pages = load_files(directory_path)
    print(pages[0].meta['title'])
    print(pages[1].meta['title'])
    print(pages[2].meta['title'])

    copy_static_files(['./static/','./theme/static/'],'./output')

