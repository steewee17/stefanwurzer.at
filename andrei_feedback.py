import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Header & Add Datenhoheit Section
target_header = """    <!-- AGENTEN HEADER -->
    <div class="fu d2" style="text-align:center; margin-bottom:48px;">
      <h2 style="font-family:var(--display); font-size:32px; color:var(--dark);">Unser KI-Kernteam</h2>
      <p style="font-size:15px; color:var(--text);">Nach dem Least-Privilege-Prinzip strukturiert und mit klar abgegrenzten Verantwortlichkeiten.</p>
    </div>"""

replacement_header = """    <!-- DATENHOHEIT & KONTROLLE (Andrei) -->
    <div class="fu d2" style="background: var(--bg-warm); border: 1px solid var(--border); border-radius: 12px; padding: 40px; margin-bottom: 64px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
      <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:16px;">Kontrollierte Autonomie & Datenhoheit</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:24px;">
        Unsere digitalen Experten arbeiten nach dem strikten <strong>Least-Privilege-Prinzip</strong>: Jeder Agent hat nur Zugriff auf die Daten und Systeme, die er für seine spezifische Aufgabe zwingend benötigt. System-Prompts und Langzeitgedächtnisse liegen sicher auf europäischen Servern. Die eigentlichen KI-Modelle dienen lediglich als austauschbare Motoren – so garantieren wir 100% Datenkontrolle und absolute Unabhängigkeit von einzelnen Anbietern.
      </p>
      <a href="/ki-mitarbeiter/" class="btn" style="display:inline-flex;">Genau dieses Prinzip setzen wir für Kunden um <i data-lucide="arrow-right" style="width:16px;height:16px;margin-left:4px;"></i></a>
    </div>

    <!-- AGENTEN HEADER -->
    <div class="fu" style="text-align:center; margin-bottom:48px;">
      <h2 style="font-family:var(--display); font-size:32px; color:var(--dark);">Unser KI-Kernteam</h2>
    </div>"""

content = content.replace(target_header, replacement_header)

# 2. Update the Assessment Center text
target_audit = "In einer isolierten Umgebung prüfen spezialisierte Audit-Agenten das System auf Belastbarkeit: Sie simulieren Stresstests, um Sicherheitslücken aufzudecken, Halluzinationen zu provozieren oder Richtlinienverstöße zu erzwingen. Nur Systeme, die diesen Härtetest fehlerfrei bestehen, werden freigegeben."
replacement_audit = "In einer isolierten Umgebung durchläuft das System rigorose Stresstests auf Belastbarkeit. Wir provozieren gezielt Halluzinationen und versuchen, Richtlinienverstöße zu erzwingen, um Schwachstellen aufzudecken. Nur Systeme, die diesen Härtetest fehlerfrei bestehen, werden für die Produktivumgebung freigegeben."

content = content.replace(target_audit, replacement_audit)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
