import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

pattern = r'<section class="section" style="padding-top: 80px; padding-bottom: 80px;">\s*<div class="c">\s*<!-- DATENHOHEIT & KONTROLLE \(Andrei\) -->.*?</section>'

perfect_html = """<section class="section" style="padding-top: 80px; padding-bottom: 80px;">
  <div class="c">
    <!-- DATENHOHEIT & KONTROLLE (Andrei) -->
    <div class="fu d2" style="text-align: center; max-width: 800px; margin: 0 auto;">
      <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:16px;">Kontrollierte Autonomie & Datenhoheit</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:24px;">
        Unsere digitalen Experten arbeiten nach dem strikten <strong>Least-Privilege-Prinzip</strong>: Jeder Agent hat nur Zugriff auf die Daten und Systeme, die er für seine spezifische Aufgabe zwingend benötigt. System-Prompts und Langzeitgedächtnisse liegen sicher auf europäischen Servern. Die eigentlichen KI-Modelle dienen lediglich als austauschbare Motoren – so garantieren wir 100% Datenkontrolle und absolute Unabhängigkeit von einzelnen Anbietern.
      </p>
      <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="display:inline-flex;">Genau dieses Prinzip setzen wir für Kunden um <i data-lucide="arrow-right" style="width:16px;height:16px;margin-left:4px;"></i></a>
    </div>
  </div>
</section>"""

content = re.sub(pattern, perfect_html, content, flags=re.DOTALL)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
