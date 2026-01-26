from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any

@dataclass
class Page:
    source_path: Path        # content/blog/post.md
    output_path: Path        # output/blog/post/index.html
    url: str                 # /blog/post/
    meta: Dict[str, Any]     # title, tags, date, etc.
    raw_markdown: str        # original markdown
    html_content: str        # rendered markdown fragment

