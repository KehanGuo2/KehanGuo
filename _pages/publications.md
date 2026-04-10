---
layout: default
title: Publications
permalink: /publications/
author_profile: true
---

## Publications

<p style="font-size:0.93em; color:#4a4a5a; margin-bottom:1.5rem;">Full list from <a href="https://scholar.google.com/citations?user=t8iRCLUAAAAJ&hl=en">Google Scholar</a>. (* equal contribution)</p>

<div id="pub-list"></div>

<script>
const allPubs = {{ site.data.publications | jsonify }};

function boldSelf(name) {
  if (name.includes('Kehan Guo')) return '<strong>' + name + '</strong>';
  return name;
}

function truncateAuthors(list) {
  if (list.length <= 10) return list;
  return [...list.slice(0, 6), '...', list[list.length - 1]];
}

function renderLinks(p) {
  let links = '';
  if (p.url) links += ' <a href="' + p.url + '">[Paper]</a>';
  if (p.code) links += ' &nbsp;<a href="' + p.code + '">[Code]</a>';
  if (p.dataset) links += ' &nbsp;<a href="' + p.dataset + '">[Dataset]</a>';
  if (p.oracle) links += ' &nbsp;<a href="' + p.oracle + '">[Oracle]</a>';
  return links;
}

function renderTags(tags) {
  if (!tags || !tags.length) return '';
  return tags.map(function(t) {
    var norm = String(t || '').trim().toLowerCase();
    if (norm === 'spotlight') return ' <strong>Spotlight.</strong>';
    return ' <span style="color:#00369f; font-weight:600;">' + t + '</span>';
  }).join('');
}

function cardHTML(p) {
  var authors = truncateAuthors(p.authors || []).map(boldSelf).join(', ');
  var title = p.url ? '<a href="' + p.url + '">' + p.title + '</a>' : p.title;
  var venue = (p.venue || '') + ', ' + p.year + '.' + renderTags(p.tags) + renderLinks(p);
  return '<div class="pub-entry">' +
    '<div class="pub-title">' + title + '</div>' +
    '<div class="pub-authors">' + authors + '</div>' +
    '<div class="pub-venue"><em>' + venue + '</em></div>' +
    '</div>';
}

function byYear(pubs) {
  var groups = {};
  (pubs || []).forEach(function(p) {
    var y = p.year || 'Other';
    if (!groups[y]) groups[y] = [];
    groups[y].push(p);
  });
  return Object.keys(groups).sort(function(a, b) { return b - a; }).map(function(y) {
    return { year: y, items: groups[y] };
  });
}

var container = document.getElementById('pub-list');
byYear(allPubs).forEach(function(g) {
  var h = document.createElement('h3');
  h.style.cssText = 'color:#0C2340; margin:1.5rem 0 0.5rem; font-size:1.15em;';
  h.textContent = g.year;
  container.appendChild(h);
  var wrap = document.createElement('div');
  wrap.innerHTML = g.items.map(cardHTML).join('');
  container.appendChild(wrap);
});
</script>
