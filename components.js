// stefanwurzer.at — Global Web Components
// Nav and footer are defined here once and used on all pages.
// To update logo, nav links, or footer: edit this file only.

class SiteNav extends HTMLElement {
  connectedCallback() {
    const path = window.location.pathname;
    const isHome = path === '/' || path === '/index.html';
    const logoHref = isHome ? '#' : '/';
    const kontaktHref = '/kontakt';

    const links = [
      { href: '/ki-befaehigung.html', label: 'KI-Befähigung' },
      { href: '/x402/', label: 'x402' },
      { href: '/team/', label: 'Team' },
    ];

    const isAgentenActive = path.startsWith('/ki-agenten/');
    const agentenActiveCls = isAgentenActive ? ' active' : '';

    this.innerHTML = `
      <style>
        .nav-drop {
          position: relative;
          display: inline-flex;
          align-items: center;
        }
        .nav-drop::after {
          content: '';
          position: absolute;
          top: 100%;
          left: 0;
          right: 0;
          height: 12px;
        }
        .nav-drop-btn {
          display: inline-flex;
          align-items: center;
          gap: 4px;
        }
        .nav-drop-menu {
          position: absolute;
          top: calc(100% + 6px);
          left: 0;
          width: 210px;
          background: #ffffff;
          border: 1px solid var(--border);
          border-radius: 8px;
          box-shadow: 0 10px 28px rgba(0,0,0,.08);
          padding: 6px;
          opacity: 0;
          visibility: hidden;
          transform: translateY(6px);
          transition: opacity .18s ease, transform .18s ease, visibility .18s;
          z-index: 250;
          display: flex;
          flex-direction: column;
          gap: 2px;
        }
        .nav-drop:hover .nav-drop-menu,
        .nav-drop:focus-within .nav-drop-menu {
          opacity: 1;
          visibility: visible;
          transform: translateY(0);
        }
        .drop-item {
          font-size: 13px !important;
          font-weight: 500 !important;
          color: var(--dark) !important;
          padding: 8px 12px !important;
          border-radius: var(--r) !important;
          text-decoration: none !important;
          transition: color .15s, background .15s !important;
          display: block !important;
        }
        .drop-item:hover {
          color: var(--gold) !important;
          background: var(--gold-pale) !important;
        }
        .drop-div {
          height: 1px;
          background: var(--border);
          margin: 4px 6px;
        }
        .drop-all {
          font-size: 12.5px !important;
          font-weight: 600 !important;
          color: var(--gold) !important;
          padding: 8px 12px !important;
          text-decoration: none !important;
          border-radius: var(--r) !important;
          display: block !important;
          transition: background .15s !important;
        }
        .drop-all:hover {
          background: var(--gold-pale) !important;
        }
        @media(max-width:800px) {
          .nl { display: none !important; }
          .nl.open { 
            display: flex !important; 
            flex-direction: column !important; 
            position: fixed !important; 
            top: 64px !important; 
            left: 0 !important; 
            right: 0 !important; 
            background: #fff !important; 
            padding: 20px 40px 28px !important; 
            border-bottom: 1px solid var(--border) !important; 
            box-shadow: 0 8px 24px rgba(0,0,0,.08) !important; 
            gap: 8px !important; 
            z-index: 999 !important; 
          }
          .ham { display: flex !important; }
          .nav-drop {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            width: 100%;
          }
          .nav-drop-btn {
            width: 100%;
          }
          .nav-drop-menu {
            position: static;
            opacity: 1;
            visibility: visible;
            transform: none;
            box-shadow: none;
            border: none;
            background: transparent;
            padding: 0 0 4px 12px;
            margin-left: 8px;
            border-left: 2px solid var(--border-gold);
            width: 100%;
          }
          .drop-item { padding: 6px 10px !important; font-size: 13px !important; }
          .drop-all { padding: 6px 10px !important; }
        }
      </style>
      <nav id="nav">
        <div class="ni">
          <a href="${logoHref}" class="logo">
            <img src="/logo_stefanwurzer_innovationservice.svg" alt="Stefan Wurzer innovationservice" width="152" height="38" style="display:block">
          </a>
          <div class="nl">
            <a href="/ki-befaehigung.html"${path.startsWith('/ki-befaehigung.html') ? ' class="active"' : ''}>KI-Befähigung</a>
            <div class="nav-drop">
              <a href="/ki-agenten/" class="nav-drop-btn${agentenActiveCls}">
                KI-Agenten
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="margin-left:2px"><path d="m6 9 6 6 6-6"/></svg>
              </a>
              <div class="nav-drop-menu">
                <a href="/ki-agenten/website-agent/" class="drop-item">Website-Agent</a>
                <a href="/ki-agenten/b2b-lead-finder/" class="drop-item">B2B Lead Finder</a>
                <a href="/ki-agenten/propstack-agent/" class="drop-item">CRM-Agent</a>
                <div class="drop-div"></div>
                <a href="/ki-agenten/" class="drop-all">Alle Agenten im Überblick</a>
              </div>
            </div>
            <a href="/x402/"${path.startsWith('/x402/') ? ' class="active"' : ''}>x402</a>
            <a href="/team/"${path.startsWith('/team/') ? ' class="active"' : ''}>Team</a>
            <a href="${kontaktHref}">Kontakt</a>
          </div>
          <button class="ham" onclick="toggleNav()" aria-label="Menü">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1A1A1A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
          </button>
        </div>
      </nav>`;

    // Scroll shadow
    window.addEventListener('scroll', () => {
      const nav = document.getElementById('nav');
      if (nav) nav.classList.toggle('sc', window.scrollY > 20);
    }, { passive: true });
  }
}

class SiteFooter extends HTMLElement {
  connectedCallback() {
    const path = window.location.pathname;
    const isHome = path === '/' || path === '/index.html';
    const faqHref = isHome ? '#faq' : '/#faq';

    this.innerHTML = `
      <footer>
        <div class="wrap">
          <div class="foot">
            <p class="fdesc">KI-Integration und Prozessautomatisierung für KMU.<br>Fokus auf Team-Befähigung und autonome KI-Agenten.</p>
            <div class="fbrand"><span>© 2026 Stefan Wurzer</span></div>
            <div class="flinks">
              <a href="https://www.wkoecg.at/Ecg.aspx?FirmaID=b9661af9-a80b-47ec-ab63-c89c2cf9d0b1" target="_blank" rel="noopener">Impressum</a>
              <span class="fdot">·</span>
              <a href="/datenschutz">Datenschutz</a>
              <span class="fdot">·</span>
              <a href="/agb">AGB</a>
              <span class="fdot">·</span>
              <a href="${faqHref}">Häufige Fragen</a>
              <span class="fdot">·</span>
              <a href="/ki-agenten/case-premium-leads/">Case Study</a>
              <span class="fdot">·</span>
              <a href="/kontakt">Kontakt</a>
            </div>
          </div>
        </div>
      </footer>`;
  }
}

customElements.define('site-nav', SiteNav);
customElements.define('site-footer', SiteFooter);

// Shared toggle function for mobile nav
function toggleNav() {
  const nl = document.querySelector('.nl');
  if (!nl) return;
  const isOpen = nl.classList.contains('open') || nl.style.position === 'fixed';
  if (isOpen) {
    nl.classList.remove('open');
    nl.removeAttribute('style');
  } else {
    nl.classList.add('open');
  }
}

// Word Rotator Component
function initWordRotators() {
  const rotators = document.querySelectorAll('[data-words]');
  rotators.forEach(el => {
    try {
      const raw = el.getAttribute('data-words');
      if (!raw) return;
      const words = JSON.parse(raw);
      if (!Array.isArray(words) || words.length <= 1) return;

      let currentIndex = 0;
      let wordEl = el.querySelector('.rotator-word');
      if (!wordEl) {
        wordEl = el.querySelector('em') || el;
      }
      wordEl.classList.add('rotator-word', 'in');

      setInterval(() => {
        wordEl.classList.remove('in');
        wordEl.classList.add('out');

        setTimeout(() => {
          currentIndex = (currentIndex + 1) % words.length;
          wordEl.textContent = words[currentIndex];
          wordEl.classList.remove('out');
          wordEl.classList.add('init');

          // Trigger reflow
          void wordEl.offsetWidth;

          wordEl.classList.remove('init');
          wordEl.classList.add('in');
        }, 450);
      }, 4200);
    } catch (e) {
      console.warn('WordRotator error:', e);
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initWordRotators);
} else {
  initWordRotators();
}
