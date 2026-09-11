import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")

with open(ma_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire uc-grid with the 6-card symmetrical grid
old_grid_start = """    <div class="uc-grid">
      <!-- UC 1: Propstack -->"""

old_grid_end = """      <!-- UC 5: Externe KI-Agenten (Yin-Yang Dark Card) -->
      <div class="uc-card uc-card-dark fu d5" style="background:var(--dark); border:1px solid var(--border-gold); display:flex; flex-direction:column;">
        <div class="uc-head" style="background:rgba(255,255,255,0.04); border-bottom:1px solid rgba(184,150,46,0.25); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-light);margin-bottom:8px">B2B Einkauf / Vertrieb</div>
            <div class="uc-title" style="font-size:15px;color:#ffffff;">Der Erstkontakt-Agent</div>
          </div>
          <span style="font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; background:var(--gold); color:var(--dark); padding:3px 7px; border-radius:3px;">Outside-In</span>
        </div>
        <div class="uc-body" style="display:flex; flex-direction:column; flex:1;">
          <div class="uc-problem" style="color:rgba(255,255,255,0.65);">Wenn ein Einkäufer heute seinen KI-Agenten beauftragt, Anbieter zu screenen und Termine einzuholen, wird Ihre Website nur gelesen &ndash; nicht angesprochen.</div>
          <div class="uc-result" style="color:rgba(255,255,255,0.9); border-left:2px solid var(--gold); margin-bottom:16px;">Eine Schnittstelle macht Verfügbarkeit, Kapazität und Intake direkt für fremde KIs auslösbar. <strong style="color:var(--gold-light);">Termin vor der Konkurrenz.</strong></div>
          <a href="/ki-mitarbeiter/externe-ki-agenten/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center; margin-top:auto; background:var(--gold); color:var(--dark); font-weight:600;">System-Architektur ansehen →</a>
        </div>
      </div>
    </div>"""

new_grid = """    <div class="uc-grid">
      <!-- UC 1: Propstack -->
      <div class="uc-card fu d1">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">Immobilien (Case Study: Propstack)</div>
          <div class="uc-title" style="font-size:15px;">Der KI-Makler-Assistent</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Manuelles Befüllen von ÖVI-Formularen und die Datenpflege im CRM fressen täglich wertvolle Vertriebszeit.</div>
          <div class="uc-result" style="margin-bottom:16px;">Ein Agent nimmt Daten via Chat/Sprache entgegen, generiert rechtsgültige PDFs und pflegt sie lückenlos in Propstack ein. <strong>Zero-Click CRM.</strong></div>
          <a href="/ki-mitarbeiter/propstack-agent/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>

      <!-- UC 2: B2B Industrie (MICADO) -->
      <div class="uc-card fu d2">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">B2B Industrie (Case Study: MICADO)</div>
          <div class="uc-title" style="font-size:15px;">Der B2B Lead Finder</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Vertriebler verschwenden Tage mit manueller Lead-Recherche in Branchenverzeichnissen und mühsamer Vorqualifizierung ins CRM.</div>
          <div class="uc-result" style="margin-bottom:16px;">Der Flow identifiziert relevante Industrie-Entscheider für die Kernbereiche von MICADO, qualifiziert sie nach ICP und übergibt sie ansprechbereit ans CRM. <strong>Fokus auf den persönlichen Abschluss.</strong></div>
          <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>

      <!-- UC 3: Premium Nische (METEK) -->
      <div class="uc-card fu d3">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">Premium Nische (Case Study: METEK)</div>
          <div class="uc-title" style="font-size:15px;">Die Multimodale Lead Engine</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Exklusive Nischen lassen sich nicht nach Standard-Kriterien filtern: Wer plant und baut wirklich Luxus-Chalets und 5-Sterne-Resorts?</div>
          <div class="uc-result" style="margin-bottom:16px;">Eine maßgeschneiderte KI bewertet die visuelle Ästhetik von Websites und analysiert Fachmagazine nach Architekten. <strong>Präzise Nischenansprache.</strong></div>
          <a href="/ki-mitarbeiter/case-premium-leads/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>

      <!-- UC 4: Management Reporting -->
      <div class="uc-card fu d4">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">Management</div>
          <div class="uc-title" style="font-size:15px;">Automatisierte Datenaggregation</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Die Recherche und Zusammenführung von Marktdaten und ERP-Exporten für Geschäftsberichte ist extrem zeitaufwendig.</div>
          <div class="uc-result">Ein Automatisierungs-Flow holt externe API-Daten und ERP-Exporte, strukturiert diese und bereitet ein Management-Briefing vor. <strong>Datenbasis auf Knopfdruck.</strong></div>
        </div>
      </div>

      <!-- UC 5: Listen-Verteilung -->
      <div class="uc-card fu d5">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">Logistik / Vertrieb</div>
          <div class="uc-title" style="font-size:15px;">Der Listen-Koordinator</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Das manuelle Filtern, Zerschneiden und Versenden von großen Lager- und Preislisten an das Vertriebsteam ist monoton und fehleranfällig.</div>
          <div class="uc-result">Der Agent splittet wöchentliche Master-Exporte automatisch nach Vertriebsregion auf und versendet die Teil-Listen an die jeweiligen Agenten. <strong>Fehlerfreie Verteilung.</strong></div>
        </div>
      </div>

      <!-- UC 6: Externe KI-Agenten (Yin-Yang Dark Card) -->
      <div class="uc-card uc-card-dark fu d6" style="background:var(--dark); border:1px solid var(--border-gold); display:flex; flex-direction:column;">
        <div class="uc-head" style="background:rgba(255,255,255,0.04); border-bottom:1px solid rgba(184,150,46,0.25); display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-light);margin-bottom:8px">B2B Einkauf / Vertrieb</div>
            <div class="uc-title" style="font-size:15px;color:#ffffff;">Der Erstkontakt-Agent</div>
          </div>
          <span style="font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em; background:var(--gold); color:var(--dark); padding:3px 7px; border-radius:3px;">Outside-In</span>
        </div>
        <div class="uc-body" style="display:flex; flex-direction:column; flex:1;">
          <div class="uc-problem" style="color:rgba(255,255,255,0.65);">Wenn ein Einkäufer heute seinen KI-Agenten beauftragt, Anbieter zu screenen und Termine einzuholen, wird Ihre Website nur gelesen &ndash; nicht angesprochen.</div>
          <div class="uc-result" style="color:rgba(255,255,255,0.9); border-left:2px solid var(--gold); margin-bottom:16px;">Eine Schnittstelle macht Verfügbarkeit, Kapazität und Intake direkt für fremde KIs auslösbar. <strong style="color:var(--gold-light);">Termin vor der Konkurrenz.</strong></div>
          <a href="/ki-mitarbeiter/externe-ki-agenten/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center; margin-top:auto; background:var(--gold); color:var(--dark); font-weight:600;">System-Architektur ansehen →</a>
        </div>
      </div>
    </div>"""

# Find and replace
import re
pattern = re.escape(old_grid_start) + r".*?" + re.escape(old_grid_end)
if old_grid_start in content and "Der Erstkontakt-Agent" in content:
    # Let's do exact slice replacement
    idx_start = content.find('<div class="uc-grid">')
    idx_end = content.find('</div>\n  </div>\n</section>\n\n<!-- FORMULAR -->', idx_start)
    if idx_start != -1 and idx_end != -1:
        content = content[:idx_start] + new_grid + content[idx_end + len('</div>'):]

with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Updated ki-mitarbeiter/index.html with symmetrical 6-card grid including METEK")
