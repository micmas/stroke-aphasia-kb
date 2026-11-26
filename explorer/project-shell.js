/* Shared project navigation and a theme preference across aphasia-kb.app sites. */
(() => {
  const key = 'calmar-theme';
  const valid = value => ['light', 'dark', 'system'].includes(value);
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  function read() {
    const cookie = document.cookie.split('; ').find(item => item.startsWith(`${key}=`))?.split('=')[1];
    if (valid(cookie)) return cookie;
    try { const value = localStorage.getItem(key); if (valid(value)) return value; } catch {}
    return 'system';
  }
  let preference = read();
  let select;
  function apply() {
    const theme = preference === 'system' ? (media.matches ? 'dark' : 'light') : preference;
    document.documentElement.dataset.theme = theme;
    document.documentElement.dataset.bsTheme = theme;
    if (select) select.value = preference;
  }
  function save(value) {
    preference = value;
    try { localStorage.setItem(key, value); } catch {}
    if (location.hostname === 'aphasia-kb.app' || location.hostname.endsWith('.aphasia-kb.app')) {
      document.cookie = `${key}=${value}; Domain=aphasia-kb.app; Path=/; Max-Age=31536000; SameSite=Lax; Secure`;
    }
    apply();
  }
  apply();
  media.addEventListener('change', apply);
  window.addEventListener('pageshow', () => { preference = read(); apply(); });
  window.addEventListener('focus', () => { preference = read(); apply(); });
  window.addEventListener('storage', event => { if (event.key === key) { preference = read(); apply(); } });
  function mount() {
    if (document.querySelector('.project-nav')) return;
    const nav = document.createElement('nav');
    nav.className = 'project-nav';
    nav.setAttribute('aria-label', 'Project websites');
    const link = (label, url, className) => {
      const a = document.createElement('a'); a.textContent = label; a.href = url;
      if (className) a.className = className;
      if (new URL(url).hostname === location.hostname) a.setAttribute('aria-current', 'location');
      return a;
    };
    const chapter = /^\/(aphasia|dysphagia|practice)(?:\/|$)/.exec(location.pathname)?.[1]
      || (location.hostname === 'review.stroke-kb.app' ? 'practice' : null)
      || (location.pathname.startsWith('/dysphagia-search') ? 'dysphagia'
        : /(^|\.)dysphagia-kb\.app$/.test(location.hostname) ? 'dysphagia'
        : /(^|\.)aphasia-kb\.app$/.test(location.hostname) && !location.hostname.startsWith('calmar.') ? 'aphasia' : null);
    const isReview = location.hostname.startsWith('review.') || location.pathname.includes('/screening/');
    const group = (title, items) => {
      const details = document.createElement('details'); details.className = 'project-menu';
      const summary = document.createElement('summary'); summary.textContent = title;
      const children = document.createElement('div'); children.className = 'project-menu-items';
      for (const [text, url, active] of items) {
        const a = link(text, url); a.removeAttribute('aria-current');
        if (active) { a.classList.add('project-home'); a.setAttribute('aria-current', 'location'); }
        children.append(a);
      }
      details.append(summary, children);
      details.addEventListener('toggle', () => {
        if (details.open) for (const other of nav.querySelectorAll('.project-menu')) if (other !== details) other.open = false;
      });
      return details;
    };
    nav.append(group('Stroke KB', [
      ['Stroke KB home', 'https://stroke-kb.app/', !chapter && location.hostname === 'stroke-kb.app'],
      ['Aphasia KB', 'https://aphasia-kb.app/', chapter === 'aphasia' && !isReview],
      ['Dysphagia KB', 'https://dysphagia-kb.app/', chapter === 'dysphagia' && !isReview],
      ['Practice & lived experience', 'https://stroke-kb.app/practice/', chapter === 'practice' && !isReview],
    ]), group('Review portal', [
      ['Aphasia', 'https://review.aphasia-kb.app/welcome/', chapter === 'aphasia' && isReview],
      ['Dysphagia', 'https://review.dysphagia-kb.app/', chapter === 'dysphagia' && isReview],
      ['Practice & lived experience', 'https://review.stroke-kb.app/', chapter === 'practice' && isReview],
    ]));
    document.addEventListener('click', event => {
      for (const menu of nav.querySelectorAll('.project-menu')) if (!menu.contains(event.target)) menu.open = false;
    });
    nav.addEventListener('keydown', event => {
      if (event.key === 'Escape') for (const menu of nav.querySelectorAll('.project-menu[open]')) {
        menu.open = false; menu.querySelector('summary').focus();
      }
    });
    const links = document.createElement('div'); links.className = 'project-links';
    links.append(link('CALMaR examples', 'https://calmar.aphasia-kb.app/'), link('Open webapp ↗', 'https://webapps.neurodesk.org/calmar/'), link('Non-commercial use', 'https://aphasia-kb.app/licensing.html'));
    const label = document.createElement('label'); label.className = 'project-theme'; label.append('Theme');
    select = document.createElement('select'); select.setAttribute('aria-label', 'Colour theme');
    for (const [value, text] of [['system', 'System'], ['light', 'Light'], ['dark', 'Dark']]) {
      const option = document.createElement('option'); option.value = value; option.textContent = text; select.append(option);
    }
    select.value = preference; select.addEventListener('change', () => save(select.value));
    label.append(select); nav.append(links, label);
    document.body.prepend(nav);
    if (document.querySelector('.navbar.fixed-top')) document.body.classList.add('project-qc');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount);
  else mount();
})();
