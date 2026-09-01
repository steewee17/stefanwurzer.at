import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/index.html
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

# Subtitle update
old_subtitle = "<p>Konkrete Anwendungsfälle, wie moderne KI-Agenten Fachsysteme (CRMs, ERPs) steuern und Workflows eigenständig abarbeiten.</p>"
new_subtitle = "<p>Konkrete Anwendungsfälle, wie moderne KI-Agenten Fachsysteme (CRMs, ERPs) steuern, Workflows eigenständig abarbeiten – und wie Ihr Unternehmen selbst für externe KI-Agenten erreichbar und handlungsfähig wird.</p>"
ma_content = ma_content.replace(old_subtitle, new_subtitle)

# Responsive CSS update for uc-card-wide
old_css = """  @media(max-width:900px){
    .uc-grid{grid-template-columns:1fr}
    .form-wrap{grid-template-columns:1fr;gap:40px}
  }"""

new_css = """  .uc-card-wide .uc-body { display: grid; grid-template-columns: 1fr 1.2fr auto; gap: 20px; align-items: center; }
  @media(max-width:900px){
    .uc-grid{grid-template-columns:1fr}
    .uc-card-wide .uc-body { grid-template-columns: 1fr; gap: 16px; }
    .form-wrap{grid-template-columns:1fr;gap:40px}
  }"""
ma_content = ma_content.replace(old_css, new_css)

# Card 5 insertion after Card 4
card5_html = """
      <!-- UC 5: Externe KI-Agenten (Outside-In) -->
      <div class="uc-card uc-card-wide fu d5" style="grid-column: 1 / -1; border: 1px solid var(--border-gold); background: var(--bg); margin-top: 8px;">
        <div class="uc-head" style="background: var(--bg-warm); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
          <div>
            <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:4px">B2B Einkauf / Vertrieb (Außenanbindung)</div>
            <div class="uc-title" style="font-size:16px;">Der Erstkontakt-Agent</div>
          </div>
          <span style="font-size:10px; font-weight:600; text-transform:uppercase; letter-spacing:0.1em; background:var(--gold-pale); color:var(--gold); padding:3px 8px; border-radius:4px; border:1px solid var(--border-gold);">Outside-In</span>
        </div>
        <div class="uc-body">
          <div class="uc-problem" style="margin-bottom:0;">Wenn ein Einkäufer heute seinen KI-Agenten beauftragt, drei Anbieter zu finden und Termine oder Angebote einzuholen, wird Ihre Website nur gelesen – nicht angesprochen.</div>
          <div class="uc-result" style="margin-bottom:0;">Eine strukturierte Schnittstelle macht Verfügbarkeit, Kapazität oder Anfrage-Intake direkt für fremde KI-Agenten auslösbar. <strong>Termin vor der Konkurrenz, ganz ohne menschliches Zutun.</strong></div>
          <a href="/ki-mitarbeiter/externe-ki-agenten/" class="btn" style="padding:10px 16px; font-size:12px; white-space:nowrap; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>"""

target_card4_end = """          <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="padding:10px 16px; font-size:12px; width:100%; justify-content:center;">System-Architektur ansehen →</a>
        </div>
      </div>"""

replacement_card4_and_5 = target_card4_end + card5_html

ma_content = ma_content.replace(target_card4_end, replacement_card4_and_5)

with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ma_content)
print("Updated ki-mitarbeiter/index.html with Card 5 and new subtitle")

# 2. Update sitemap.xml
sitemap_file = os.path.join(base_dir, "sitemap.xml")
with open(sitemap_file, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_sitemap_entry = """  <url>
    <loc>https://www.stefanwurzer.at/ki-mitarbeiter/externe-ki-agenten/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/kontakt/</loc>"""

sitemap_content = sitemap_content.replace("  <url>\n    <loc>https://www.stefanwurzer.at/kontakt/</loc>", new_sitemap_entry)

with open(sitemap_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with /ki-mitarbeiter/externe-ki-agenten/")
