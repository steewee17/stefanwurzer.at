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
      { href: '/markt', label: 'Markt' },
      { href: '/planung', label: 'Planung' },
      { href: '/umsetzung', label: 'Umsetzung' },
    ];

    const navLinks = links.map(l => {
      const active = path.startsWith(l.href) ? ' class="active"' : '';
      return `<a href="${l.href}"${active}>${l.label}</a>`;
    }).join('\n      ');

    this.innerHTML = `
      <nav id="nav">
        <div class="ni">
          <a href="${logoHref}" class="logo">
            <img src="/logo_stefanwurzer_innovationservice.svg" alt="Stefan Wurzer innovationservice" height="38" style="display:block">
          </a>
          <div class="nl">
            ${navLinks}
            <a href="${kontaktHref}" class="cta">Kontakt aufnehmen</a>
          </div>
          <button class="ham" onclick="toggleNav()" aria-label="Menü">
            <span></span><span></span><span></span>
          </button>
        </div>
      </nav>`;

    // Scroll shadow
    window.addEventListener('scroll', () => {
      const nav = document.getElementById('nav');
      if (nav) nav.classList.toggle('sc', window.scrollY > 20);
    });
  }
}

class SiteFooter extends HTMLElement {
  connectedCallback() {
    const path = window.location.pathname;
    const isHome = path === '/' || path === '/index.html';

    const extraLinks = isHome
      ? `<span class="fdot">·</span>
        <a href="#faq">Häufige Fragen</a>
        <span class="fdot">·</span>
        <a href="/kontakt">Kontakt</a>`
      : `<span class="fdot">·</span>
        <a href="/">Zurück zur Hauptseite</a>`;

    this.innerHTML = `
      <footer>
        <div class="wrap">
          <div class="foot">
            <p class="fdesc">Marktanalyse, Planung und Umsetzung digitaler Systeme für KMU.<br>Fokus auf Sichtbarkeit, Anfragen, Prozesse und Datennutzung.</p>
            <div class="fbrand"><span>© 2026 Stefan Wurzer</span></div>
            <div class="flinks">
              <a href="https://www.wkoecg.at/Ecg.aspx?FirmaID=f18d9b7a-0310-436a-a9f0-1f35002ee26a" target="_blank" rel="noopener">Impressum</a>
              <span class="fdot">·</span>
              <a href="/datenschutz">Datenschutz</a>
              <span class="fdot">·</span>
              <a href="/agb">AGB</a>
              ${extraLinks}
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
  const isOpen = nl.style.position === 'fixed';
  if (isOpen) {
    nl.removeAttribute('style');
  } else {
    Object.assign(nl.style, {
      display: 'flex',
      flexDirection: 'column',
      position: 'fixed',
      top: '64px',
      left: '0',
      right: '0',
      background: '#fff',
      padding: '20px 40px 28px',
      borderBottom: '1px solid var(--border)',
      boxShadow: '0 8px 24px rgba(0,0,0,.08)',
      gap: '4px',
      zIndex: '199',
    });
  }
}
