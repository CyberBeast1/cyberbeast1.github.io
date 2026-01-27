meta-title:Title Is Second Post
meta-desc:Testing various markdown sytax
meta-author:Cyber
meta-tags:markdown, demo, test, parser, second post
# Heading Level 1

## Heading Level 2

### Heading Level 3

#### Heading Level 4

##### Heading Level 5

###### Heading Level 6

---

About link: [OpenAI](/)

## Paragraphs & Line Breaks

This is a normal paragraph. Markdown collapses  
multiple spaces and respects  
manual line breaks using two spaces at the end of a line.

This is a new paragraph..

---

## Emphasis

*Italic text*  
_Italic text (underscore)_  

**Bold text**  
__Bold text (underscore)__  

***Bold + Italic***  
___Bold + Italic___  

~~Strikethrough~~

---

## Blockquotes

> This is a blockquote.
>
> > Nested blockquote.
> >
> > > Deeply nested blockquote.

---

## Lists

### Unordered List

- Item A
- Item B
  - Subitem B1
  - Subitem B2
    - Sub-subitem
- Item C

### Ordered List

1. First item
2. Second item
   1. Nested ordered item
   2. Another nested item
3. Third item

### Task List (GFM)

- [x] Completed task
- [ ] Incomplete task
- [ ] Another task

---

## Code

### Inline Code

Use `printf()` in C or `console.log()` in JavaScript.

### Fenced Code Blocks

```c
#include <stdio.h>

int main() {
    printf("Hello, Markdown!\n");
    return 0;
}
```

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```zsh
gcc main.c -O2 -Wall -o app
./app
```

---

## Horizontal Rules

---
***
___

---

## Links

- Inline link: [OpenAI](https://openai.com)
- Reference-style link: [GitHub][github-link]

[github-link]: https://github.com

---

## Images

![Alt text](/images/coder.jpg "Image Title")

![Alt text](/images/eye.gif "Anime Waifu")
<!-- ![Alt text](https://via.placeholder.com/300x150 "Image Title") -->

---

## Tables (GFM)

| Language | Type       | Speed |
|----------|------------|-------|
| C        | Compiled   | Fast  |
| Python  | Interpreted| Medium|
| Java    | JVM        | Fast  |

---

## Footnotes

This sentence has a footnote.[^1]

[^1]: This is a simple footnote.

---

## HTML Inside Markdown

<div style="border:1px solid #888; padding:10px; border-radius:6px;">
<strong>HTML block</strong> inside Markdown.
</div>

---

## Emoji

🔥 🚀 🧠 💻 📦

---

## Math

Inline math: $E = mc^2$

$$
\int_0^\infty e^{-x} dx = 1
$$

---

## Final Thoughts

Markdown is deceptively simple and wonderfully messy.

