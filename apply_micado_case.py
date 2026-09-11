import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/b2b-lead-finder/index.html
finder_file = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html")
with open(finder_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Page Header / Hero Section
old_hero = """<!-- PAGE HEADER -->
<section class="ph">
  <div class="orb orb-h1" aria-hidden="true"></div>
  <div class="phi">
    <div>
      <span class="ey">Mehr qualifizierte Leads</span>
      <div class="rule"></div>
      <h1>Der B2B Lead Finder:<br><em>Fokussierte Vertriebszeit.</em></h1>
      <p class="hsub">Der Engpass im B2B-Vertrieb ist selten der Markt – sondern die Zeit für manuelle Lead-Recherche. Der B2B Lead Finder liefert jeden Morgen geprüfte, angereicherte Wunschkunden direkt in Ihr CRM. Bereit für die persönliche Ansprache, 100 % DSGVO-konform.</p>
      <div class="hctag">
        <a href="#anfrage" class="btn">Pilotprojekt anfragen →</a>
      </div>
    </div>
    
    <!-- GRAPHIC -->
    <div class="fu d1" style="display:flex;align-items:center;justify-content:center;">
      <div style="width:100%;max-width:550px;transition:transform 0.4s cubic-bezier(0.1, 0, 0.2, 1);" onmouseover="this.style.transform='translateY(-6px)'" onmouseout="this.style.transform='translateY(0)'">
        <div class="glass-card" style="padding:40px;">
          <h3 style="font-family:var(--display);font-size:24px;color:var(--dark);margin-bottom:16px;">Vertriebler sollen verkaufen. <br>Nicht kopieren.</h3>
          <p style="font-size:15px;color:var(--text);line-height:1.6;margin-bottom:24px;">Gegenüberstellung im B2B-Vertrieb:</p>
          
          <div style="display:flex;flex-direction:column;gap:16px;">
            <div style="padding:16px;border-left:2px solid var(--muted);background:var(--bg-sec);">
              <div style="font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Manueller Blindflug</div>
              <div style="font-size:14px;color:var(--text);">Stundenlange Recherche in Datenbanken, viele irrelevante Leads und manuelles Eintragen ins CRM.</div>
            </div>
            
            <div style="padding:16px;border-left:2px solid var(--gold);background:#FAF8F3;">
              <div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Der B2B Lead Finder</div>
              <div style="font-size:14px;color:var(--dark);">Der Vertriebler öffnet morgens sein CRM und findet exakt qualifizierte Leads, fertig für das persönliche Anschreiben.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

new_hero = """<!-- PAGE HEADER -->
<section class="ph">
  <div class="orb orb-h1" aria-hidden="true"></div>
  <div class="phi">
    <div>
      <span class="ey">Case Study: <a href="https://www.micado.at" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">MICADO SMART ENGINEERING GmbH</a></span>
      <div class="rule"></div>
      <h1>Der B2B Lead Finder:<br><em>Wunschkunden im Smart Engineering.</em></h1>
      <p class="hsub">Wie skaliert ein spezialisierter Industrie-Zulieferer seinen Vertrieb über die drei Kernbereiche Vorrichtungs- & Werkzeugbau, Automatisierung und Produktentwicklung? Die MICADO SMART ENGINEERING GmbH nutzt den B2B Lead Finder, um qualifizierte Industrie-Entscheider in der DACH-Region und weltweit automatisiert zu identifizieren und ansprechbereit ins CRM zu übergeben.</p>
      <div class="hctag">
        <a href="#anfrage" class="btn">Pilotprojekt anfragen →</a>
      </div>
    </div>
    
    <!-- GRAPHIC -->
    <div class="fu d1" style="display:flex;align-items:center;justify-content:center;">
      <div style="width:100%;max-width:550px;transition:transform 0.4s cubic-bezier(0.1, 0, 0.2, 1);" onmouseover="this.style.transform='translateY(-6px)'" onmouseout="this.style.transform='translateY(0)'">
        <div class="glass-card" style="padding:40px;">
          <h3 style="font-family:var(--display);font-size:24px;color:var(--dark);margin-bottom:16px;">Präzision im <br>Industrie-Vertrieb.</h3>
          <p style="font-size:15px;color:var(--text);line-height:1.6;margin-bottom:24px;">Gegenüberstellung im B2B-Vertrieb:</p>
          
          <div style="display:flex;flex-direction:column;gap:16px;">
            <div style="padding:16px;border-left:2px solid var(--muted);background:var(--bg-sec);">
              <div style="font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Manueller Blindflug</div>
              <div style="font-size:14px;color:var(--text);">Der Vertrieb verbringt wertvolle Zeit mit dem mühsamen Durchforsten von Verzeichnissen und Plattformen nach den richtigen technischen Ansprechpartnern.</div>
            </div>
            
            <div style="padding:16px;border-left:2px solid var(--gold);background:#FAF8F3;">
              <div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Der B2B Lead Finder (MICADO-Setup)</div>
              <div style="font-size:14px;color:var(--dark);">Vollautomatische Vorqualifizierung nach Fertigungstiefe, Branchenfokus und exakter Entscheider-Rolle (z. B. Leiter Vorrichtungsbau oder Automation) – sauber im CRM.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

content = content.replace(old_hero, new_hero)

# Step 1 update in Maschinenraum
old_step1 = """          <p class="step-desc">Ein Automatisierungs-Flow übernimmt die gezielte Suche nach Account-Listen (z. B. in professionellen Business-Netzwerken) und extrahiert diese vollautomatisch (URL zu CSV).</p>"""
new_step1 = """          <p class="step-desc">Ein Automatisierungs-Flow übernimmt die gezielte Suche nach Account-Listen passender Fertigungs- und Industriebetriebe. Am Praxisbeispiel von MICADO: Strukturierte Segmentierung nach den drei Kernbereichen (Vorrichtungs- & Werkzeugbau, Automatisierung, Produktentwicklung) in der DACH-Region und internationalen Schlüsselmärkten.</p>"""

content = content.replace(old_step1, new_step1)

with open(finder_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("Updated ki-mitarbeiter/b2b-lead-finder/index.html with MICADO Case Study")

# 2. Update ki-mitarbeiter/index.html (Card 4)
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

old_card4 = """      <!-- UC 4: B2B Vertrieb -->
      <div class="uc-card fu d4">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">B2B Vertrieb</div>
          <div class="uc-title" style="font-size:15px;">Der B2B Lead Finder</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Vertriebler verschwenden Stunden mit manueller Lead-Recherche in externen Datenbanken und mühsamer Copy-Paste-Arbeit ins CRM.</div>
          <div class="uc-result" style="margin-bottom:16px;">Ein Automatisierungs-Flow sucht Leads, eine KI qualifiziert diese strikt nach Wunschkundenprofil (ICP), reichert Kontaktdaten an und legt sie mundgerecht im CRM ab. <strong>Fokus auf den persönlichen Abschluss.</strong></div>
          <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>"""

new_card4 = """      <!-- UC 4: B2B Vertrieb (MICADO Case Study) -->
      <div class="uc-card fu d4">
        <div class="uc-head">
          <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">B2B Vertrieb (Case Study: MICADO)</div>
          <div class="uc-title" style="font-size:15px;">Der B2B Lead Finder</div>
        </div>
        <div class="uc-body">
          <div class="uc-problem">Vertriebler verschwenden Tage mit manueller Lead-Recherche in Branchenverzeichnissen und mühsamer Vorqualifizierung ins CRM.</div>
          <div class="uc-result" style="margin-bottom:16px;">Der Flow identifiziert relevante Industrie-Entscheider für die Kernbereiche von MICADO, qualifiziert sie nach ICP und übergibt sie ansprechbereit ans CRM. <strong>Fokus auf den persönlichen Abschluss.</strong></div>
          <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>"""

ma_content = ma_content.replace(old_card4, new_card4)

with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ma_content)
print("Updated ki-mitarbeiter/index.html (Card 4) with MICADO Case Study reference")

# 3. Update llms.txt & ai.txt
llms_file = os.path.join(base_dir, "llms.txt")
with open(llms_file, 'r', encoding='utf-8') as f:
    llms_content = f.read()

llms_content = llms_content.replace(
    '  - *Standard B2B Finder:* "Der B2B Lead Finder". An automated lead engine that handles sourcing, AI-based ICP qualification, and direct CRM push.',
    '  - *Standard B2B Finder (MICADO Case Study):* "Der B2B Lead Finder" for MICADO SMART ENGINEERING GmbH (Vorrichtungs- & Werkzeugbau, Automatisierung, Produktentwicklung). Sourcing, AI-based ICP qualification, and direct CRM push for technical industrial decision-makers.'
)

with open(llms_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(llms_content)
print("Updated llms.txt")

ai_file = os.path.join(base_dir, "ai.txt")
with open(ai_file, 'r', encoding='utf-8') as f:
    ai_content = f.read()

ai_content = ai_content.replace(
    '- "B2B Lead Finder": Automatisierte Recherche und KI-Qualifizierung (ICP) mit CRM-Push.',
    '- "B2B Lead Finder (Case Study: MICADO)": Automatisierte Recherche und KI-Qualifizierung (ICP) von Industrie-Entscheidern für MICADO SMART ENGINEERING GmbH (Vorrichtungsbau, Automation, Produktentwicklung).'
)

with open(ai_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ai_content)
print("Updated ai.txt")
