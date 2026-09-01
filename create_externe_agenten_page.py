import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
target_dir = os.path.join(base_dir, "ki-mitarbeiter", "externe-ki-agenten")
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = """<!DOCTYPE html>
<html lang="de">
<head>
<!-- Cookie Consent: Klaro -->
<script defer src="/klaro-config.js"></script>
<script defer src="https://cdn.kiprotect.com/klaro/v0.7/klaro.js"></script>

<!-- Google tag (gtag.js) — loads only after consent via Klaro -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'analytics_storage': 'denied'
  });
  gtag('js', new Date());
  gtag('config', 'G-XL6E22PCJC');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XL6E22PCJC"></script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Der Erstkontakt-Agent: Externe KI-Agenten anbinden | Stefan Wurzer</title>
<meta name="description" content="Machine-to-Machine im B2B: Machen Sie Ihr Unternehmen direkt für fremde KI-Agenten erreichbar und handlungsfähig. Verfügbarkeit, Kapazität und Intake ohne Umwege.">
<meta name="keywords" content="Externe KI-Agenten, B2B Einkauf Automatisierung, Agentic Systems, WebMCP, Machine-to-Machine, CRM Intake, n8n Prozess-Architektur">
<meta name="author" content="Stefan Wurzer">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.stefanwurzer.at/ki-mitarbeiter/externe-ki-agenten/">
<link rel="alternate" hreflang="de-AT" href="https://www.stefanwurzer.at/ki-mitarbeiter/externe-ki-agenten/">
<link rel="alternate" hreflang="de" href="https://www.stefanwurzer.at/ki-mitarbeiter/externe-ki-agenten/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.stefanwurzer.at/ki-mitarbeiter/externe-ki-agenten/">
<meta property="og:title" content="Der Erstkontakt-Agent: Externe KI-Agenten anbinden | Stefan Wurzer">
<meta property="og:description" content="Machine-to-Machine im B2B-Vertrieb: Machen Sie Ihre Systeme für fremde KI-Agenten ansprechbar und handlungsfähig.">
<meta property="og:locale" content="de_AT">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Der Erstkontakt-Agent: Externe KI-Agenten anbinden | Stefan Wurzer",
  "url": "https://www.stefanwurzer.at/ki-mitarbeiter/externe-ki-agenten/",
  "description": "Architektur und Schnittstellen für externe KI-Agenten im B2B-Einkauf und Vertrieb. Strukturierte Workflows für Terminbuchung, Kapazitätsprüfung und qualifizierten Intake.",
  "publisher": {
    "@type": "Person",
    "name": "Stefan Wurzer"
  }
}</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Instrument+Sans:wght@400;500;600&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet"></noscript>
<link rel="stylesheet" href="/style.css?v=4">
<script defer src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<style>
  .step-grid { display: flex; flex-direction: column; gap: 24px; max-width: 800px; margin: 40px auto 0; }
  .step-card { display: grid; grid-template-columns: 80px 1fr; gap: 24px; align-items: flex-start; padding: 32px; border: 1px solid var(--border); border-radius: 8px; background: var(--bg); }
  .step-num { width: 44px; height: 44px; border-radius: 50%; background: var(--bg-sec); color: var(--gold); border: 1px solid var(--border-gold); display: flex; align-items: center; justify-content: center; font-family: var(--display); font-size: 20px; font-weight: 600; }
  .step-title { font-family: var(--display); font-size: 20px; font-weight: 600; color: var(--dark); margin-bottom: 8px; }
  .step-desc { font-size: 14px; color: var(--text); line-height: 1.65; }
  
  .glass-card { background: rgba(255,255,255,0.7); backdrop-filter: blur(8px); border: 1px solid rgba(232,228,220,0.8); border-radius: 12px; }
  
  /* MATRIX TABLE */
  .matrix-table-wrap { width: 100%; overflow-x: auto; margin-top: 32px; border-radius: 8px; border: 1px solid var(--border); background: var(--bg); }
  .matrix-table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
  .matrix-table th { background: var(--bg-warm); padding: 16px 20px; font-weight: 600; color: var(--dark); border-bottom: 1px solid var(--border); font-family: var(--body); }
  .matrix-table td { padding: 18px 20px; border-bottom: 1px solid var(--border); color: var(--text); vertical-align: top; line-height: 1.6; }
  .matrix-table tr:last-child td { border-bottom: none; }
  .matrix-type { font-weight: 600; color: var(--dark); }
  .matrix-badge { display: inline-block; font-size: 11px; font-weight: 600; color: var(--gold); background: var(--gold-pale); padding: 2px 8px; border-radius: 4px; border: 1px solid var(--border-gold); margin-bottom: 4px; }

  @media(max-width:900px){
    .phi{grid-template-columns:1fr;gap:48px}
    .form-wrap{grid-template-columns:1fr;gap:40px}
    .step-card{grid-template-columns:1fr;gap:16px;}
    .step-num{margin-bottom:8px;}
  }
</style>
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon.png">
<link rel="apple-touch-icon" href="/thumbnail_sw.jpg">
<meta property="og:image" content="https://www.stefanwurzer.at/og-img_sw.jpg">
<meta name="twitter:image" content="https://www.stefanwurzer.at/og-img_sw.jpg">
</head>
<body>

<site-nav></site-nav>

<!-- PAGE HEADER -->
<section class="ph">
  <div class="orb orb-h1" aria-hidden="true"></div>
  <div class="phi">
    <div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <span class="ey" style="margin-bottom:0">B2B Einkauf & Vertrieb</span>
        <span style="font-size:11px;font-weight:600;color:var(--muted);background:var(--bg-sec);border:1px solid var(--border);padding:2px 8px;border-radius:4px;">Stand: September 2026</span>
      </div>
      <div class="rule"></div>
      <h1>Der Erstkontakt-Agent:<br><em>Für fremde KIs erreichbar.</em></h1>
      <p class="hsub">Wenn Einkäufer heute autonome KI-Agenten beauftragen, um Anbieter zu screenen und Termine einzuholen, wird Ihre Website meist nur passiv gelesen. Wir machen Ihre Prozess-Infrastruktur direkt ansprechbar und handlungsfähig – Machine-to-Machine, ohne manuelle Reibungsverluste.</p>
      <div class="hctag">
        <a href="#anfrage" class="btn">Systemcheck vereinbaren →</a>
      </div>
    </div>
    
    <!-- GRAPHIC -->
    <div class="fu d1" style="display:flex;align-items:center;justify-content:center;">
      <div style="width:100%;max-width:550px;transition:transform 0.4s cubic-bezier(0.1, 0, 0.2, 1);" onmouseover="this.style.transform='translateY(-6px)'" onmouseout="this.style.transform='translateY(0)'">
        <div class="glass-card" style="padding:40px;">
          <h3 style="font-family:var(--display);font-size:24px;color:var(--dark);margin-bottom:16px;">Vom passiven Lesen <br>zur echten Aktion.</h3>
          <p style="font-size:15px;color:var(--text);line-height:1.6;margin-bottom:24px;">Gegenüberstellung im digitalen Erstkontakt:</p>
          
          <div style="display:flex;flex-direction:column;gap:16px;">
            <div style="padding:16px;border-left:2px solid var(--muted);background:var(--bg-sec);">
              <div style="font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Klassische Website (Passiv)</div>
              <div style="font-size:14px;color:var(--text);">Fremde KIs scannen unstrukturierten Text. Anfragen landen in überfüllten Postfächern, die Terminabstimmung dauert Tage.</div>
            </div>
            
            <div style="padding:16px;border-left:2px solid var(--gold);background:#FAF8F3;">
              <div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Machine-to-Machine (Aktiv)</div>
              <div style="font-size:14px;color:var(--dark);">Einkaufs-Agenten sprechen definierte Schnittstellen direkt an. Qualifizierte Termine und Daten landen sofort fehlerfrei im CRM.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DER RAHMEN & PARADIGMENWECHSEL -->
<section class="sec" style="background:var(--bg-warm);">
  <div class="wrap">
    <div class="fu" style="text-align:center;margin-bottom:48px;max-width:720px;margin-left:auto;margin-right:auto;">
      <span class="ey">Paradigmenwechsel</span>
      <div class="rule c"></div>
      <h2>Vom Klick-Web zum<br><em>handlungsorientierten Netzwerk.</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin-top:20px;">
        Entscheider recherchieren im B2B-Umfeld immer seltener manuell durch endlose Unterseiten. Sie beauftragen spezialisierte Agenten (ChatGPT, Perplexity oder interne Firmen-KIs), um den Markt zu scannen, Zertifizierungen zu prüfen und konkrete Termine vorzubereiten.
      </p>
    </div>

    <div class="fu d1 glass-card" style="padding:36px; max-width:850px; margin:0 auto; border:1px solid var(--border);">
      <h3 style="font-size:19px; color:var(--dark); margin-bottom:12px;">Warum Chat-Widgets der falsche Ansatz sind</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:16px;">
        Aufgesetzte Chat-Fenster auf Websites werden von anfragenden KIs und Menschen gleichermaßen gemieden. Die eigentliche Schnittstelle für die nächste Generation des B2B-Geschäfts liegt nicht in bunten Popups, sondern eine Ebene tiefer: <strong>im Maschinenraum Ihrer Datenflüsse und APIs</strong>.
      </p>
      <p style="font-size:14px; color:var(--muted); line-height:1.6; margin:0; border-left:2px solid var(--gold); padding-left:14px;">
        <strong>Unsere Positionierung:</strong> Wir behaupten nicht, das Rad neu erfunden zu haben. Unsere Kunden gehören schlicht zu den ca. 1 % der Macher im Mittelstand, die aktiv handeln und ihre Systeme vorbereiten, während der Großteil des Marktes noch abwartet.
      </p>
    </div>
  </div>
</section>

<!-- DAS 3-SCHICHTEN-MODELL -->
<section class="sec">
  <div class="wrap">
    <div class="fu" style="text-align:center;margin-bottom:60px;max-width:650px;margin-left:auto;margin-right:auto;">
      <span class="ey">System-Architektur</span>
      <div class="rule c"></div>
      <h2>Das 3-Schichten-Modell<br><em>für Agent-Readiness.</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin-top:16px;">
        Ein funktionierender KI-Intake ist kein Marketing-Gimmick, sondern solide Prozess-Architektur. Das System gliedert sich in drei klare Ebenen:
      </p>
    </div>

    <div class="step-grid">
      <!-- Schicht 1 -->
      <div class="step-card fu">
        <div class="step-num">1</div>
        <div>
          <h3 class="step-title">Schicht 1: Auffindbarkeit (Discovery)</h3>
          <p class="step-desc">
            Der externe Agent erkennt in Sekunden, wer Sie sind und welche Leistungen Sie anbieten. Dies geschieht über strukturierte Semantik (Semantic Web, maschinenlesbare Schemata und offene Manifeste). <em>Diese Schicht ist vergleichsweise leicht zu implementieren.</em>
          </p>
        </div>
      </div>

      <!-- Schicht 2 -->
      <div class="step-card fu d1">
        <div class="step-num">2</div>
        <div>
          <h3 class="step-title">Schicht 2: Regelwerk & Fähigkeiten (Permissions)</h3>
          <p class="step-desc">
            Der externe Agent erfährt verbindlich, welche Aktionen er auslösen darf (z. B. Verfügbarkeitsabfrage, Terminbuchung oder Angebots-Intake) und welche Datenformate erwartet werden. Strikte Leitplanken nach dem Least-Privilege-Prinzip schützen interne Daten.
          </p>
        </div>
      </div>

      <!-- Schicht 3 -->
      <div class="step-card fu d2" style="border:1px solid var(--gold);box-shadow:0 8px 32px rgba(184,150,46,.08);background:var(--bg-warm);">
        <div class="step-num" style="background:var(--gold);color:#fff;border-color:var(--gold);">3</div>
        <div>
          <h3 class="step-title" style="color:var(--dark);">Schicht 3: Ausführung & Integration (The Gateway)</h3>
          <p class="step-desc">
            <strong>Hier liegt die eigentliche Wertschöpfung.</strong> Sichere Backend-Webhooks (z. B. über n8n / REST-Schnittstellen) fangen die eingehende Payload ab, validieren Dubletten, prüfen Kalender oder Fertigungskapazitäten und übergeben den Datensatz lückenlos in Ihr CRM oder ERP. <em>Das ist der eigentliche Prozess-Engineering-Teil.</em>
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DIE BEWERTUNGSMATRIX -->
<section class="sec" style="background:var(--bg-warm);">
  <div class="wrap">
    <div class="fu" style="text-align:center;margin-bottom:40px;max-width:700px;margin-left:auto;margin-right:auto;">
      <span class="ey">Entscheidungs-Matrix</span>
      <div class="rule c"></div>
      <h2>Welcher Prozess stiftet<br><em>für Sie den größten Wert?</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin-top:16px;">
        Nicht jeder Prozess muss sofort vollautomatisiert werden. Entscheidend ist die Struktur Ihrer Leistungen und wie viele Variablen den Preis bestimmen:
      </p>
    </div>

    <div class="matrix-table-wrap fu d1">
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width:25%;">Prozess-Typ</th>
            <th style="width:40%;">Was der externe Agent erhält</th>
            <th style="width:35%;">Wann wirtschaftlich sinnvoll</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="matrix-badge">E-Commerce / Handel</span>
              <div class="matrix-type">Katalog & Festpreis</div>
            </td>
            <td>Verbindlicher Preis, Rabattstaffeln oder Optionsbündel in Echtzeit.</td>
            <td>Wenige, vorab bekannte Parameter (Stückzahl, Maße, Material, Lagerbestand).</td>
          </tr>
          <tr>
            <td>
              <span class="matrix-badge">Industrie & Fertigung</span>
              <div class="matrix-type">Verfügbarkeit & Kapazität</div>
            </td>
            <td>Sofortige Zusage zu Lieferfenster, Fertigungsslot oder Termin.</td>
            <td>Auch bei mittlerer Komplexität; Schnelligkeit der Rückmeldung schlägt Preisgenauigkeit.</td>
          </tr>
          <tr>
            <td>
              <span class="matrix-badge">B2B Beratung & Projekt</span>
              <div class="matrix-type">Qualifizierter Intake</div>
            </td>
            <td>Vollständiger, strukturierter Projektdatensatz statt vager Kontaktmail.</td>
            <td>Individuelle, beratungsintensive Leistungen ohne automatisch berechenbaren Preis.</td>
          </tr>
          <tr>
            <td>
              <span class="matrix-badge">Compliance & Ausschreibung</span>
              <div class="matrix-type">Trust & Zertifikate</div>
            </td>
            <td>Strukturierte Nachweise (ISO, DSGVO-Standards, ESG/Lieferkette).</td>
            <td>Vorauswahl-Phase in Großkonzern-Beschaffung, bevor verhandelt wird.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- FAUSTREGEL -->
    <div class="fu d2" style="max-width:800px;margin:32px auto 0;background:var(--bg);border:1px solid var(--border-gold);border-radius:8px;padding:24px;">
      <div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Die Faustregel für Entscheider</div>
      <p style="font-size:14px;color:var(--dark);line-height:1.65;margin:0;">
        <strong>Wenige & vorab bekannte Variablen?</strong> → Katalog, Verfügbarkeit und Preisslot direkt automatisieren.<br>
        <strong>Viele & situationsabhängige Variablen?</strong> → Der strukturierte Intake und die qualifizierte Vorarbeit sind der Hebel, nicht der Preis.
      </p>
    </div>
  </div>
</section>

<!-- REALER BELEG & TREND -->
<section class="sec">
  <div class="wrap">
    <div class="fu" style="text-align:center;max-width:700px;margin:0 auto;">
      <span class="ey">Markt-Entwicklung</span>
      <div class="rule c"></div>
      <h2 style="margin-bottom:20px;">Der Trend ist <em>messbar.</em></h2>
      <p style="font-size:15px;color:var(--text);line-height:1.75;">
        Branchenanalysen (u. a. von Cloudflare und Gartner) dokumentieren eine rapide Verschiebung: Der Anteil an automatisiertem Datenverkehr durch KI-Systeme und autonome Recherche-Bots wächst kontinuierlich. Unternehmen, die ihre digitale Infrastruktur frühzeitig auf strukturierte Maschinenlesbarkeit und Webhook-Gateways ausrichten, sichern sich den schnellsten Zugang zu Neugeschäft.
      </p>
    </div>
  </div>
</section>

<!-- FORMULAR -->
<section class="sec" id="anfrage" style="background:var(--bg-warm);">
  <div class="wrap form-wrap">
    
    <div class="form-left fu">
      <span class="ey">Systemcheck</span>
      <div class="rule"></div>
      <h2>Machen Sie Ihr Unternehmen<br><em>anschlussfähig.</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin:24px 0 32px">Lassen Sie uns in einem 30-minütigen Systemcheck prüfen, welche Schnittstellen für Ihr CRM/ERP den größten Hebel bieten, um externe KI-Agenten sicher und kontrolliert anzubinden.</p>
      
      <div class="t-item">
        <div class="t-icon"><i data-lucide="shield-check"></i></div>
        <div class="t-text">Sicherheit an erster Stelle: 100 % Datenkontrolle & Least-Privilege-Prinzip.</div>
      </div>
      <div class="t-item">
        <div class="t-icon"><i data-lucide="network"></i></div>
        <div class="t-text">Direkte Anbindung an bestehende CRM- & ERP-Systeme.</div>
      </div>
      <div class="t-item">
        <div class="t-icon"><i data-lucide="crosshair"></i></div>
        <div class="t-text">Kein Hype, sondern handfeste Prozess-Architektur mit n8n.</div>
      </div>
    </div>

    <div class="form-right fu d1">
      <div class="glass-card" style="padding:40px;">
        <h3 style="font-family:var(--display);font-size:22px;font-weight:600;color:var(--dark);margin-bottom:6px">Systemcheck anfragen</h3>
        <p style="font-size:14px;color:var(--muted);margin-bottom:24px;margin-top:6px">Ich melde mich in der Regel innerhalb von 24 Stunden.</p>
        <div class="fg2">
          <div class="fg" style="margin-bottom:0"><label for="f-name" class="fl">Name *</label><input type="text" class="fi2" id="f-name" placeholder="Ihr Name" required></div>
          <div class="fg" style="margin-bottom:0"><label for="f-email" class="fl">E-Mail *</label><input type="email" class="fi2" id="f-email" placeholder="Ihre E-Mail-Adresse" required></div>
        </div>
        <div style="height:20px"></div>
        <div class="fg">
          <label for="f-firma" class="fl">Unternehmen</label>
          <input type="text" class="fi2" id="f-firma" placeholder="Ihr Unternehmen">
        </div>
        <div class="fg" style="margin-bottom:0">
          <label for="f-nachricht" class="fl">Nachricht <span style="font-weight:400;text-transform:none;letter-spacing:0">(optional)</span></label>
          <textarea class="fta" id="f-nachricht" placeholder="Welche Prozesse oder Systeme möchten Sie anbinden?"></textarea>
        </div>
        <div style="height:20px"></div>
        <button class="btn" style="width:100%" onclick="submitContactForm('stefanwurzer.at/externe-ki-agenten')">Systemcheck anfragen →</button>
        <div class="fs" id="f-status"></div>
      </div>
    </div>
    
  </div>
</section>

<site-footer></site-footer>

<script defer src="/components.js?v=4"></script>
<script>
const LW = 'https://steewee.app.n8n.cloud/webhook/stefanwurzer-lead';

document.addEventListener('DOMContentLoaded', () => { if (window.lucide) lucide.createIcons(); });

const io = new IntersectionObserver(e => e.forEach(x => { if (x.isIntersecting) x.target.classList.add('vis'); }), { threshold: .12 });
document.querySelectorAll('.fu').forEach(el => io.observe(el));

async function submitContactForm(source) {
  const name = document.getElementById('f-name').value.trim();
  const email = document.getElementById('f-email').value.trim();
  const firma = document.getElementById('f-firma').value.trim();
  const nachricht = document.getElementById('f-nachricht').value.trim();
  const st = document.getElementById('f-status');
  if (!name || !email) { st.className = 'fs er'; st.style.display = 'block'; st.textContent = 'Bitte Name und E-Mail angeben.'; return; }
  try {
    const res = await fetch(LW, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, company: firma, message: nachricht, leistung: 'Externe KI-Agenten (Erstkontakt)', source })
    });
    if (res.ok) {
      st.className = 'fs ok'; st.style.display = 'block';
      st.textContent = 'Anfrage erhalten — ich melde mich innerhalb von 24 Stunden.';
      ['f-name','f-email','f-firma','f-nachricht'].forEach(id => document.getElementById(id).value = '');
    } else { throw new Error(); }
  } catch {
    st.className = 'fs er'; st.style.display = 'block';
    st.textContent = 'Fehler beim Senden. Bitte direkt unter info@stefanwurzer.at melden.';
  }
}
</script>
</body>
</html>
"""

with open(target_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html_content)

print(f"Created deep page at {target_file}")
