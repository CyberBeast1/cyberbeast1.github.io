meta-title:Title Is Home 
meta-desc:This is HomePage desctiption
meta-author:Cyber

This is a home page of my static site generator  
in this you just have to write normal text in `content/` folder  
and run `python build.py` and it will build  
everything and give final files in `output/` directory

## Posts
---
<!-- posts -->
<div class="posts-container">
<article class="post-card">
          <h3 class="post-title">
            <a href="/about">Title Is About</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified(Cyber):</span>
            <time class="post-date">2026-01-28 22:01:35.412504</time> <br>
            <span>1 mins read</span>
          </div>

          <p class="post-desc">
            Little bit about me and this project
          </p>
        </article>
<article class="post-card">
          <h3 class="post-title">
            <a href="/blog/second_post">Title Is Second Post</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified(Cyber):</span>
            <time class="post-date">2026-01-27 22:03:16.781676</time> <br>
            <span>2 mins read</span>
          </div>

          <p class="post-desc">
            Testing various markdown sytax
          </p>
        </article>
<article class="post-card">
          <h3 class="post-title">
            <a href="/blog/first-post">Title Is First Post</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified(Cyber):</span>
            <time class="post-date">2026-01-28 22:44:41.863921</time> <br>
            <span>1 mins read</span>
          </div>

          <p class="post-desc">
            This is 1st post desctiption
          </p>
        </article>
<article class="post-card">
          <h3 class="post-title">
            <a href="/blog/sub-blog/third-post"> Title Is Third Post</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified( Cyber):</span>
            <time class="post-date">2026-01-28 18:06:25.735132</time> <br>
            <span>2 mins read</span>
          </div>

          <p class="post-desc">
             Desc of 3rd post
          </p>
        </article>
</div>
<!-- end posts -->


## Final Thoughts
Post links are dynamically generated based on folder content  
including `<!-- posts -->` and `<!-- end posts -->` is *important*  
as that is searched and content is added inside that block
