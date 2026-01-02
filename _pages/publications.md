---
layout: default
title: Publications
permalink: /publications/
author_profile: false
---

<section class="section section--publications" id="full-list">
  <h2>Publications</h2>
  <div id="full-list-container" class="pubs" aria-label="all publications by year"></div>
  <p class="pubs__source">Auto-generated from <a href="https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>. (* equal contribution)</p>
</section>

<style>
  :root { --accent: #e74c3c; }
  .pubs .pub-card { border-left:4px solid var(--accent); border-radius:10px; box-shadow:0 1px 3px rgba(0,0,0,.06); padding:1rem 1.25rem; margin-bottom:1rem; background:#fff; }
  .pub-card h3 { margin:0 0 .25rem; font-weight:700; line-height:1.25; }
  .pub-card h3 a { color:#000; }
  .pub-card .authors { color:#555; font-size:.95em; }
  .pub-card .venue { color:#666; font-style:italic; font-size:.95em; }
  .tags { display:inline-flex; gap:.35rem; margin-left:.5rem; flex-wrap:wrap; }
  .tag { background:rgba(231,76,60,.12); color:#e74c3c; border:1px solid rgba(231,76,60,.35); padding:.05rem .45rem; border-radius:999px; font-size:.8rem; }
  .pubs__year { margin:1.2rem 0 .5rem; color:#0C2340; }
  @media (max-width:680px){ .pubs__header { flex-direction:column; align-items:flex-start; } }
</style>

<script>
  // Load auto-generated YAML (compiled to site.data) via Liquid → baked HTML dataset
  const allPubs = {% assign pubs = site.data.publications | jsonify %} {{ pubs }};

  function boldSelf(name){
    return name.replace(/(^|,\s*)(Kehan Guo)(?=,|$)/g, '$1<u>$2<\/u>');
  }
  function truncateAuthors(list){
    if (list.length <= 10) return list;
    return [...list.slice(0,6), '…', list[list.length-1]];
  }
  function renderTags(tags){
    if (!tags || !tags.length) return '';
    return '<span class="tags">' + tags.map(t=>`<span class="tag">${t}</span>`).join('') + '</span>';
  }
  function authorHTML(authors){
    const shown = truncateAuthors(authors);
    return shown.map(a=> {
      if (a === '…') return '…';
      if (a.includes('Kehan Guo')) return `<u>${a}</u>`;
      return a;
    }).join(', ');
  }
  function cardHTML(p){
    const title = p.url ? `<a href="${p.url}" target="_blank" rel="noopener">${p.title}</a>` : p.title;
    return `<article class="pub-card" aria-label="publication">
      <h3>${title}</h3>
      <div class="authors">${authorHTML(p.authors||[])}</div>
      <div class="venue">${p.venue || ''}${p.year?` '${String(p.year).slice(-2)}`:''}${renderTags(p.tags)}</div>
    </article>`;
  }
  function byYear(pubs){
    const groups = {};
    (pubs||[]).forEach(p=>{ const y = p.year||'Other'; (groups[y]=groups[y]||[]).push(p); });
    return Object.keys(groups).sort((a,b)=>b-a).map(y=>({year:y, items:groups[y]}));
  }

  // Render full list grouped by year
  const fullEl = document.getElementById('full-list-container');
  byYear(allPubs).forEach(g=>{
    const h = document.createElement('h3'); h.className = 'pubs__year'; h.textContent = g.year; fullEl.appendChild(h);
    const wrap = document.createElement('div'); wrap.className = 'pubs';
    wrap.innerHTML = g.items.map(cardHTML).join('');
    fullEl.appendChild(wrap);
  });
</script>


