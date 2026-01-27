meta-title:Title Is Home 
meta-desc:This is HomePage desctiption
meta-author:Cyber
meta-tags:markdown, demo, test, parser
meta-random:

This is a home page of my static site generator  
in this you just have to write normal text in `content/` folder  
and run `python build.py` and it will build  
everything and give final files in `output/` directory

## Posts
<!-- posts -->
<article class="post-card">
          <h3 class="post-title">
            <a href="/about/index.html">Title Is About</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified(Cyber):</span>
            <time class="post-date">2026-01-27 23:43:27.701064</time><br>
            <span>1 mins read</span>
          </div>

          <p class="post-desc">
            Little bit about me and this project
          </p>
        </article>
<article class="post-card">
          <h3 class="post-title">
            <a href="/blog/second_post/index.html">Title Is Second Post</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified(Cyber):</span>
            <time class="post-date">2026-01-27 22:03:16.781676</time><br>
            <span>2 mins read</span>
          </div>

          <p class="post-desc">
            Testing various markdown sytax
          </p>
        </article>
<article class="post-card">
          <h3 class="post-title">
            <a href="/blog/first-post/index.html">Title Is First Post</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified(Cyber):</span>
            <time class="post-date">2026-01-27 23:53:55.287385</time><br>
            <span>1 mins read</span>
          </div>

          <p class="post-desc">
            This is 1st post desctiption
          </p>
        </article>
<article class="post-card">
          <h3 class="post-title">
            <a href="/blog/sub-blog/third-post/index.html"> Title Is Third Post</a>
          </h3>

          <div class="post-meta">
            <span class="post-author">Last Modified( Cyber):</span>
            <time class="post-date">2026-01-27 22:36:19.363734</time><br>
            <span>2 mins read</span>
          </div>

          <p class="post-desc">
             Desc of 3rd post
          </p>
        </article>
<!-- end posts -->
## Final Thoughts
Post links are dynamically generated based on folder content  
including `<!-- posts -->` and `<!-- end posts -->` is *important*  
as that is searched and content is added inside that block
