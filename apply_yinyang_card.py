import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")

with open(ma_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous uc-card-wide with the new Yin-Yang card
old_card5 = """      <!-- UC 5: Externe KI-Agenten (Outside-In) -->
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

new_card5 = """      <!-- UC 5: Externe KI-Agenten (Yin-Yang Dark Card) -->
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
      </div>"""

content = content.replace(old_card5, new_card5)

# Clean up CSS if uc-card-wide is not needed anymore
old_css = """  .uc-card-wide .uc-body { display: grid; grid-template-columns: 1fr 1.2fr auto; gap: 20px; align-items: center; }
  @media(max-width:900px){
    .uc-grid{grid-template-columns:1fr}
    .uc-card-wide .uc-body { grid-template-columns: 1fr; gap: 16px; }
    .form-wrap{grid-template-columns:1fr;gap:40px}
  }"""

new_css = """  @media(max-width:900px){
    .uc-grid{grid-template-columns:1fr}
    .form-wrap{grid-template-columns:1fr;gap:40px}
  }"""

content = content.replace(old_css, new_css)

with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Updated Card 5 to Yin-Yang dark card in ki-mitarbeiter/index.html")
