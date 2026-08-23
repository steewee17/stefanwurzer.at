import os

team_html = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Team & KI-Agenten | Stefan Wurzer</title>
<meta name="description" content="Lernen Sie das Team hinter stefanwurzer innovationservice kennen: Ein menschlicher Prozess-Architekt und drei hochspezialisierte autonome KI-Agenten.">
<meta name="keywords" content="KI Agenten, Team, KI-Mitarbeiter, Stefan Wurzer, Automatisierung, KMU">
<link rel="stylesheet" href="/style.css">
<script src="https://unpkg.com/lucide@latest"></script>
<script src="/components.js" defer></script>
<style>
/* Team-spezifisches CSS */
.team-hero { text-align: center; margin-bottom: 64px; }
.human-card { display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 700px; margin: 0 auto 64px; background: var(--bg-warm); padding: 40px; border-radius: 12px; border: 1px solid var(--border); }
.human-img { width: 140px; height: 140px; border-radius: 50%; object-fit: cover; margin-bottom: 24px; border: 2px solid var(--gold); }
.human-name { font-family: var(--display); font-size: 28px; color: var(--dark); margin-bottom: 4px; }
.human-role { font-size: 14px; font-weight: 600; color: var(--gold); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px; }
.human-desc { font-size: 15px; color: var(--text); line-height: 1.6; }

.agent-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 32px; }
.agent-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; transition: transform 0.3s ease, border-color 0.3s ease; display: flex; flex-direction: column; }
.agent-card:hover { transform: translateY(-4px); border-color: var(--gold-pale); box-shadow: 0 12px 40px rgba(184, 150, 46, 0.08); }
.agent-img-wrap { width: 100%; aspect-ratio: 4/3; overflow: hidden; border-bottom: 1px solid var(--border); background: var(--bg-sec); }
.agent-img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(20%) contrast(1.1); transition: filter 0.3s ease; }
.agent-card:hover .agent-img { filter: grayscale(0%); }
.agent-content { padding: 32px 24px; flex-grow: 1; display: flex; flex-direction: column; }
.agent-name { font-family: var(--display); font-size: 24px; color: var(--dark); margin-bottom: 4px; display: flex; align-items: center; justify-content: space-between; }
.agent-badge { font-size: 11px; font-weight: 600; background: var(--gold-pale); color: var(--bg); padding: 4px 8px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--sans); }
.agent-role { font-size: 13px; font-weight: 600; color: var(--gold); margin-bottom: 16px; }
.agent-pate { font-size: 12px; color: var(--muted); margin-bottom: 24px; font-style: italic; }
.agent-section-title { font-size: 11px; font-weight: 600; color: var(--dark); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-top: 20px; }
.agent-list { list-style: none; padding: 0; margin: 0; }
.agent-list li { font-size: 13px; color: var(--text); line-height: 1.5; margin-bottom: 8px; display: flex; align-items: flex-start; gap: 8px; }
.agent-list li i { color: var(--gold); width: 14px; height: 14px; flex-shrink: 0; margin-top: 2px; }
.agent-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.agent-tag { font-size: 11px; color: var(--text); background: var(--bg-warm); padding: 4px 8px; border-radius: 4px; border: 1px solid var(--border); }
</style>
<link rel="icon" href="/favicon.ico" sizes="32x32">
</head>
<body>

<site-nav></site-nav>

<section class="sec" style="padding-top:140px; padding-bottom: 80px;">
  <div class="wrap">
    
    <div class="team-hero fu">
      <span class="ey">Über uns</span>
      <div class="rule c"></div>
      <h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><em>Drei Maschinen.</em></h1>
      <p style="font-size:18px;color:var(--text);max-width:600px;margin:0 auto;line-height:1.6;">Lernen Sie das Team kennen, das "Eat your own dogfood" wörtlich nimmt. Wir verkaufen nicht nur autonome KI-Systeme – wir werden von ihnen operativ betrieben.</p>
    </div>

    <!-- MENSCH -->
    <div class="human-card fu d1">
      <img src="/portrait_sw.jpg" alt="Stefan Wurzer" class="human-img">
      <div class="human-name">Stefan Wurzer</div>
      <div class="human-role">Der Mensch (CEO & Prozess-Architekt)</div>
      <p class="human-desc">Meine Aufgabe: Die Vision vorgeben, den direkten menschlichen Kontakt zu unseren Kunden pflegen, strategische Weichen stellen und die KI-Agenten orchestrieren. Alles, was Routine ist, delegiere ich konsequent an mein maschinelles Team.</p>
    </div>

    <div class="rule c" style="margin: 80px auto;"></div>

    <!-- AGENTEN HEADER -->
    <div class="fu d2" style="text-align:center; margin-bottom:48px;">
      <h2 style="font-family:var(--display); font-size:32px; color:var(--dark);">Das maschinelle Kernteam</h2>
      <p style="font-size:15px; color:var(--text);">Nach dem Least-Privilege-Prinzip strukturiert und mit klar abgegrenzten Verantwortlichkeiten.</p>
    </div>

    <!-- AGENTEN GRID -->
    <div class="agent-grid fu d3">
      
      <!-- KURT -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="kurt.jpg" alt="Kurt - Head of HR" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">Kurt <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Head of People & AI-Organisation</div>
          <div class="agent-pate">Namenspate: Kurt Lewin (Pionier der Organisationspsychologie)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Konzeption, "Recruiting" und Onboarding neuer KI-Mitarbeiter.</li>
            <li><i data-lucide="check-circle-2"></i> Formulierung und Wartung von Systemprompts.</li>
            <li><i data-lucide="check-circle-2"></i> Überwachung des Organigramms und Schnittstellen-Design.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">docx (Rollenprofile)</span>
            <span class="agent-tag">session-librarian</span>
            <span class="agent-tag">weekly-review-planning</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">A2A (Agent-Koordination)</span>
            <span class="agent-tag">Clarifying Questions</span>
            <span class="agent-tag">File Operations</span>
            <span class="agent-tag">Memory</span>
          </div>
        </div>
      </div>

      <!-- JAKOB -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="jakob.jpg" alt="Jakob - CFO" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">Jakob <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Finanzen & Steuern</div>
          <div class="agent-pate">Namenspate: Jakob Fugger (Pionier der kaufmännischen Buchführung & Finanzorganisation)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Autonome Vorbereitung und Strukturierung der laufenden Buchhaltung direkt im Dateisystem.</li>
            <li><i data-lucide="check-circle-2"></i> Vorausschauende Berechnung, Planung und Optimierung von SVS-Beiträgen und Nachbemessungen.</li>
            <li><i data-lucide="check-circle-2"></i> Erstellung strukturierter Prüfdossiers und Vorbereitungen für den Steuerberater.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">xlsx (Liquiditäts- & SVS-Planung)</span>
            <span class="agent-tag">docx (Vertrags- & Dokumentenentwürfe)</span>
            <span class="agent-tag">pdf (Bescheid- & Belegprüfung)</span>
            <span class="agent-tag">RIS & Findok (Rechtsquellen-Verifikation)</span>
            <span class="agent-tag">GSVG- & Abgaben-Controlling</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">Dateisystem (Direkte Ordner-Kollaboration)</span>
            <span class="agent-tag">Web-Recherche (RIS, Findok, SVS.at)</span>
            <span class="agent-tag">Aufgaben- & Fristenplanung</span>
            <span class="agent-tag">Strukturiertes Langzeitgedächtnis</span>
          </div>
        </div>
      </div>

      <!-- DAVID -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="david.jpg" alt="David - Head of Marketing" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">David <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Head of Marketing & Brand Positioning</div>
          <div class="agent-pate">Namenspate: David Ogilvy (Vater des modernen Werbetextens)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Positionierung und Content-Strategie für stefanwurzer innovationservice.</li>
            <li><i data-lucide="check-circle-2"></i> Erstellung zielgruppenrelevanter B2B-Texte (LinkedIn, Whitepaper, Blog).</li>
            <li><i data-lucide="check-circle-2"></i> Wahrung einer fundierten Tonalität ohne Buzzword-Floskeln.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">humanizer (Schärfung)</span>
            <span class="agent-tag">docx (Fachartikel)</span>
            <span class="agent-tag">baoyu-infographic</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">A2A (Budget/Rollen-Abstimmung)</span>
            <span class="agent-tag">File Operations (Website-Drafts)</span>
            <span class="agent-tag">Web Search (Markttrends)</span>
            <span class="agent-tag">Memory</span>
          </div>
        </div>
      </div>

    </div>
    
    <!-- PLATZHALTER ZUKUNFT -->
    <div class="fu" style="text-align:center; margin-top: 48px;">
      <p style="font-size:14px; color:var(--muted); font-style:italic;">* Dieses Organigramm wächst dynamisch. Weitere KI-Mitarbeiter befinden sich aktuell im Onboarding.</p>
    </div>

  </div>
</section>

<site-footer></site-footer>

<script>
  lucide.createIcons();
  
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('vis');
        obs.unobserve(e.target);
      }
    });
  }, {threshold:0.1});
  document.querySelectorAll('.fu').forEach(el => obs.observe(el));
</script>
</body>
</html>
"""

with open(r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html', 'w', encoding='utf-8') as f:
    f.write(team_html)
    
# Update components.js to include "Team" in nav
f_comp = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\components.js"
with open(f_comp, 'r', encoding='utf-8') as f:
    comp = f.read()

nav_target = '<a href="/ki-mitarbeiter" class="${p === \'/ki-mitarbeiter\' ? \'active\' : \'\'}">KI-Mitarbeiter</a>'
nav_replacement = '<a href="/ki-mitarbeiter" class="${p === \'/ki-mitarbeiter\' ? \'active\' : \'\'}">KI-Mitarbeiter</a>\n          <a href="/team" class="${p.startsWith(\'/team\') ? \'active\' : \'\'}">Team</a>'
comp = comp.replace(nav_target, nav_replacement)

with open(f_comp, 'w', encoding='utf-8') as f:
    f.write(comp)
    
