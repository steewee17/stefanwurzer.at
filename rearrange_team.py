import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Soften the "Big-Five" wording
old_big_five = "Hier definieren wir Befugnisse und das <strong>Big-Five-Persönlichkeitsprofil</strong>."
new_wording = "Hier definieren wir Befugnisse und eine <strong>individuelle Verhaltens-Persona</strong>."
content = content.replace(old_big_five, new_wording)

# 2. Move "Datenhoheit & Kontrolle"
datenhoheit_html = """    <!-- DATENHOHEIT & KONTROLLE (Andrei) -->
    <div class="fu d2" style="background: var(--bg-warm); border: 1px solid var(--border); border-radius: 12px; padding: 40px; margin-bottom: 64px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
      <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:16px;">Kontrollierte Autonomie & Datenhoheit</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:24px;">
        Unsere digitalen Experten arbeiten nach dem strikten <strong>Least-Privilege-Prinzip</strong>: Jeder Agent hat nur Zugriff auf die Daten und Systeme, die er für seine spezifische Aufgabe zwingend benötigt. System-Prompts und Langzeitgedächtnisse liegen sicher auf europäischen Servern. Die eigentlichen KI-Modelle dienen lediglich als austauschbare Motoren – so garantieren wir 100% Datenkontrolle und absolute Unabhängigkeit von einzelnen Anbietern.
      </p>
      <a href="/ki-mitarbeiter/" class="btn" style="display:inline-flex;">Genau dieses Prinzip setzen wir für Kunden um <i data-lucide="arrow-right" style="width:16px;height:16px;margin-left:4px;"></i></a>
    </div>"""

# Remove from current location
content = content.replace(datenhoheit_html, "")

# Insert it right before the "PLATZHALTER ZUKUNFT" section, which is just below the grid.
# The grid ends with:
#       </div>
#
#       <!-- PLATZHALTER ZUKUNFT -->
#       <div class="fu" style="text-align:center; margin-top: 48px;">

target_insert = """      <!-- PLATZHALTER ZUKUNFT -->
      <div class="fu" style="text-align:center; margin-top: 48px;">
        <p style="font-size:14px; color:var(--muted); font-style:italic;">* Dieses Organigramm wächst dynamisch. Weitere KI-Mitarbeiter befinden sich aktuell im Onboarding.</p>
      </div>"""

replacement_insert = datenhoheit_html + "\n\n" + target_insert

content = content.replace(target_insert, replacement_insert)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
