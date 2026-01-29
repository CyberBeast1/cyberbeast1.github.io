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

❌ What will never work with md4mathjax (now proven)

You can confidently stop trying:

- aligned
- align
- cases
- \\ for vertical breaks
- spacing arguments
- delimiter changes

The DOM evidence shows they are stripped before MathJax runs.

Final mental model (this one sticks)

Think in layers:

1. Markdown decides what text survives
2. md4mathjax wraps surviving math
3. MathJax typesets whatever it receives

In your setup:

- Layer 1 destroys line breaks
- Layer 3 never had a chance

\[
\begin{aligned}
A &= B + C \\
  &= D + E \\
  &= F
\end{aligned}
\]

retry above

$$
\begin{aligned}
A &= B + C \\
  &= D + E \\
  &= F
\end{aligned}
$$


Inline math: $E = mc^2$

$$
\int_0^\infty e^{-x} dx = 1
$$

visual breaks in formula


$$
\begin{aligned}
A &= B + C \\
  &= D + E \\
  &= F
\end{aligned}
$$



$$
\begin{aligned}
f(x) &= ax^2 + bx + c \\
g(x) &= dx^2 + ex + f
\end{aligned}
$$

$$
\begin{aligned}
S &= a + b + c + d \\
  &\phantom{=} + e + f + g
\end{aligned}
$$

---

$$
\begin{aligned}
f(x) = a_1 x^n + a_2 x^{n-1} + a_3 x^{n-2} \\
\quad + a_4 x^{n-3} + a_5
\end{aligned}
$$

To haunt students in there dreams.

$$
\begin{aligned}
\mathcal{Z}
&=
\int_{0}^{\infty}
\sum_{n=1}^{\infty}
\frac{(-1)^{n+1}}{n^{s}}
\left(
\det\!\left[
\exp\!\left(
-\tfrac{1}{2}
(\mathbf{x}-\boldsymbol{\mu})^\top
\Sigma^{-1}
(\mathbf{x}-\boldsymbol{\mu})
\right)
\right]
\right)^{\!1/n}
\\
&\qquad \times
\prod_{k=1}^{n}
\left(
\frac{\partial^{k}}{\partial x^{k}}
\left[
\frac{1}{\Gamma(\alpha)}
\int_{0}^{\infty}
t^{\alpha-1} e^{-t}
\log\!\left(
1 + \frac{x^{2}}{t^{\beta}}
\right)
\, dt
\right]
\right)
\\
&\qquad \times
\exp\!\left(
i \oint_{\mathcal{C}}
\frac{z^{2} + \zeta(s)}{z^{3} - 1}
\, dz
\right)
\, dx
\end{aligned}
$$

$$
\mathcal{Z}
=
\int_0^\infty
\sum_{n=1}^\infty
\frac{(-1)^{n+1}}{n^s}
\left(\cdots\right)^{1/n}
$$

$$
\times
\prod_{k=1}^n
\left(
\frac{\partial^k}{\partial x^k}
\left[\cdots\right]
\right)
$$

$$
\times
\exp\!\left(
i \oint_\mathcal{C}
\frac{z^2 + \zeta(s)}{z^3 - 1}
\, dz
\right)
\, dx
$$


---

## Final Thoughts

Markdown is deceptively simple and wonderfully messy. but fun to quickly note things

