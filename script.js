const { baseUrl } = window.APP_CONFIG;

console.log("hi");
const theme_toggle = document.getElementById('theme-toggle');
const theme_switch = document.getElementById('theme-switch');
const root = document.documentElement;


document.addEventListener('DOMContentLoaded', () => {
  // if theme found them update theme and UI and state for checkbox
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    root.dataset.theme = savedTheme;
    changeToggle(savedTheme);
  }
  // same for bg audio
  const audio = document.getElementById('bg-music');
  console.log(audio)
  if (!audio) return;

  if (localStorage.getItem('bg-music') === 'on') {
    audio.volume = 0.3;
    audio.play().catch(() => {
       // browser blocked it until user interacts — expected
    });
  }
  // add copy button to code blocks
  document.querySelectorAll("pre > code").forEach((codeBlock) => {
    console.log(codeBlock);
    const pre = codeBlock.parentNode;

    const button = document.createElement("button");
    button.className = "copy-btn";
    button.textContent = "Copy";

    button.addEventListener("click", async () => {
      await navigator.clipboard.writeText(codeBlock.innerText);
      button.textContent = "Copied!";
      setTimeout(() => (button.textContent = "Copy"), 1500);
    });

    pre.appendChild(button);
  });
});


function changeToggle(next){
  if(next === 'dark'){
    theme_toggle.checked = false;
    theme_switch.textContent = "Day";
  } else{
    theme_toggle.checked = true;
    theme_switch.textContent = "Night";
  }
}

theme_toggle.addEventListener('change', ()=>{
  const theme = theme_toggle.checked ? "light" : "dark";
  root.dataset.theme = theme;
  localStorage.setItem('theme', theme);
  theme_switch.textContent = theme_toggle.checked ? "Night" : "Day";
});

document.addEventListener('keydown', (e) =>{
  const tag = e.target.tagName;
  if (tag === 'INPUT' || tag === 'TEXTAREA' || event.target.isContentEditable) return;

  if (event.shiftKey && event.key.toLowerCase() === 'm') {
    const audio = document.getElementById('bg-music');
    if (!audio) return;

    if (audio.paused) {
      audio.muted=false;
      audio.volume = 0.3; // sane default
      audio.play();
      localStorage.setItem('bg-music', 'on');
    } else {
      audio.pause();
      localStorage.setItem('bg-music', 'off');
    }
  }

  if(e.shiftKey && e.key.toLowerCase() === 't'){
    e.preventDefault();
    console.log('Shift + T pressed');
    current_theme = root.dataset.theme;
    const next = current_theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    localStorage.setItem('theme', next);
    changeToggle(next);
  }
})


async function loadPosts() {
  console.log("Loading posts...");

    const res = await fetch(`${baseUrl}/pages.json`, {
      cache: "no-store"
    });

    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }

    const posts = await res.json();

    posts.sort((a, b) => {
      return Date.parse(b.date) - Date.parse(a.date);
    });

    return posts;
}

function createPaginationControls(containerClass) {
  console.log(containerClass);
  const container = document.getElementsByClassName(containerClass)[0];
  if(!container) return;
  // makeing idempotent: redendering don't stack garbage
  container.innerHTML = '';
  console.log("Creating pagination");
  const controls = document.createElement('div');
  controls.className = 'pagination-controls';

  const prevBtn = document.createElement('button');
  prevBtn.textContent = '<--';

  const info = document.createElement('p');
  info.textContent = `${current_page}/${TOTAL_PAGES}`;
  info.className = 'icon-text'


  const nextBtn = document.createElement('button');
  nextBtn.textContent = '-->';

  prevBtn.onclick = () => {
    if (current_page > 1) {
      current_page -= 1;
      renderPosts(POSTS_LIST, current_page, PAGE_SIZE);
      createPaginationControls('posts-pagination');

    }
  };

  nextBtn.onclick = () => {
    if (current_page < TOTAL_PAGES) {
      current_page += 1;
      renderPosts(POSTS_LIST, current_page, PAGE_SIZE);
      createPaginationControls('posts-pagination');

    }
  };

  controls.append(prevBtn, info, nextBtn);
  container.appendChild(controls);
 
}

function createSearchForPosts(containerClass) {
  console.log("Creating search");
  const container = document.getElementsByClassName(containerClass)[0];
  if (!container) return;
  // makeing idempotent: redendering don't stack garbage
  container.innerHTML = '';

  const wrapper = document.createElement('div');
  wrapper.className = 'post-search';

  const input = document.createElement('input');
  input.type = 'search';
  input.placeholder = 'Search by title or tag...';
  input.autocomplete = 'off';

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();

    if (!query) {
      FILTERED_POSTS = POSTS_LIST;
    } else {
      FILTERED_POSTS = POSTS_LIST.filter(post =>
        (post.title || '')
          .toLowerCase()
          .includes(query) ||
        (post.tags || [])
          .some(tag => tag.toLowerCase().includes(query))
      );
    }

    current_page = 1;
    TOTAL_PAGES = Math.max(
      1,
      Math.ceil(FILTERED_POSTS.length / PAGE_SIZE)
    );
    console.log(FILTERED_POSTS)
    
    renderPosts(FILTERED_POSTS, current_page, PAGE_SIZE);
    createPaginationControls('posts-pagination');

  });


  wrapper.appendChild(input);
  container.prepend(wrapper);

}


function renderPosts(posts, current_page, page_size){
  console.log("Rendering posts");
    const container = document.querySelector(".posts-list");
    if (!container) return;
    // Clear container (idempotent)
    container.innerHTML = "";

  if (!Array.isArray(posts) || posts.length === 0) {
    // data is null, undefined, not an array, or empty
    container.innerHTML = `
      <p class="error">
        Nothing to show here.
      </p>
    `;
    return;
  }
  const start_idx = (current_page - 1) * page_size;
  const end_idx = start_idx + page_size;

  const pagePosts = posts.slice(start_idx, end_idx);

  if (!Array.isArray(pagePosts) || pagePosts.length === 0) {
    // data is null, undefined, not an array, or empty
    container.innerHTML = `
      <p class="error">
        You came too far.
      </p>
    `;
  
    return;
  }
 
  
    // Optional: newest first
  pagePosts
      .forEach(post => {
        container.appendChild(renderPost(post));
    });
  

}

function renderPost(data) {
  const article = document.createElement("article");
  article.className = "post-card";

  const title = (data.title || "Untitled").trim();
  const author = (data.author || "unknown").trim();
  const desc = (data.desc || "").trim();
  const url = data.url || "#";
  const mins = data.estimate_read_time ?? "?";
  const date = formatDate(data.date);

  article.innerHTML = `
    <h3 class="post-title">
      <a href="${url}">${escapeHTML(title)}</a>
    </h3>

    <div class="post-meta">
      <span class="post-author">
        Last Modified (${escapeHTML(author)}):
      </span>
      <time class="post-date">${date}</time><br>
      <span>${mins} mins read</span>
    </div>

    <p class="post-desc">
      ${escapeHTML(desc)}
    </p>
  `;

  return article;
}

function formatDate(dateStr) {
  if (!dateStr) return "Unknown";
  const d = new Date(dateStr);
  return isNaN(d)
    ? "Invalid date"
    : d.toLocaleDateString(undefined, {
        year: "numeric",
        month: "short",
        day: "numeric"
      });
}

// Basic XSS protection (cheap, effective)
function escapeHTML(str) {
  return str.replace(/[&<>"']/g, m => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;"
  }[m]));
}

const PAGE_SIZE = 2;
const POSTS_LIST = await loadPosts();
let FILTERED_POSTS = POSTS_LIST;
let TOTAL_PAGES = Math.max(
      1,
      Math.ceil(FILTERED_POSTS.length / PAGE_SIZE)
    );
let current_page = 1;
let current_theme = 'dark'

renderPosts(POSTS_LIST, current_page, PAGE_SIZE);

createSearchForPosts('posts-search');
createPaginationControls('posts-pagination');

console.log(POSTS_LIST)
console.log(TOTAL_PAGES)





