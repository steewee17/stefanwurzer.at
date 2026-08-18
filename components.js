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
      { href: '/ki-mitarbeiter/', label: 'KI-Mitarbeiter' },
    ];

    const navLinks = links.map(l => {
      const active = path.startsWith(l.href) && l.href !== '/' ? ' class="active"' : '';
      return `<a href="${l.href}"${active}>${l.label}</a>`;
    }).join('\n      ');

    this.innerHTML = `
      <style>
        @media(max-width:640px) {
          #nav .nl { display: none; }
          #nav .nl.open { 
            display: flex !important; 
            flex-direction: column; 
            position: fixed; 
            top: 64px; 
            left: 0; 
            right: 0; 
            background: #fff; 
            padding: 20px 40px 28px; 
            border-bottom: 1px solid var(--border); 
            box-shadow: 0 8px 24px rgba(0,0,0,.08); 
            gap: 4px; 
            z-index: 199; 
          }
          #nav .ham { display: flex !important; }
        }
      </style>
      <nav id="nav">
        <div class="ni">
          <a href="${logoHref}" class="logo">
            <img src="/logo_stefanwurzer_innovationservice.svg" alt="Stefan Wurzer innovationservice" width="152" height="38" style="display:block">
          </a>
          <div class="nl">
            ${navLinks}
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
            <p class="fdesc">KI-Integration und Prozessautomatisierung für KMU.<br>Fokus auf Team-Befähigung und autonome KI-Mitarbeiter.</p>
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
              <a href="/ki-mitarbeiter/case-premium-leads/">Case Study</a>
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
