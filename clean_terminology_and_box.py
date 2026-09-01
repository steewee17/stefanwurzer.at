import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/externe-ki-agenten/index.html
deep_file = os.path.join(base_dir, "ki-mitarbeiter", "externe-ki-agenten", "index.html")
with open(deep_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_box = """    <div class="fu d1 glass-card" style="padding:36px; max-width:850px; margin:0 auto; border:1px solid var(--border);">
      <h3 style="font-size:19px; color:var(--dark); margin-bottom:12px;">Warum Chat-Widgets der falsche Ansatz sind</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:16px;">
        Aufgesetzte Chat-Fenster auf Websites werden von anfragenden KIs und Menschen gleichermaßen gemieden. Die eigentliche Schnittstelle für die nächste Generation des B2B-Geschäfts liegt nicht in bunten Popups, sondern eine Ebene tiefer: <strong>im Maschinenraum Ihrer Datenflüsse und APIs</strong>.
      </p>
      <p style="font-size:14px; color:var(--muted); line-height:1.6; margin:0; border-left:2px solid var(--gold); padding-left:14px;">
        <strong>Unsere Positionierung:</strong> Wir behaupten nicht, das Rad neu erfunden zu haben. Unsere Kunden gehören schlicht zu den ca. 1 % der Macher im Mittelstand, die aktiv handeln und ihre Systeme vorbereiten, während der Großteil des Marktes noch abwartet.
      </p>
    </div>"""

new_box = """    <div class="fu d1 glass-card" style="padding:36px; max-width:850px; margin:0 auto; border:1px solid var(--border);">
      <h3 style="font-size:19px; color:var(--dark); margin-bottom:12px;">Die Schnittstelle liegt im Backend, nicht im Chat-Fenster</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:16px;">
        Klassische Chat-Fenster auf Websites greifen zu kurz &ndash; externe KI-Agenten interagieren nicht über grafische Benutzeroberflächen, sondern über strukturierte Schnittstellen. Die reale Wertschöpfung liegt deshalb eine Ebene tiefer: <strong>im Maschinenraum Ihrer bestehenden CRM- und ERP-Systeme</strong>.
      </p>
      <p style="font-size:14px; color:var(--text); line-height:1.6; margin:0; border-left:2px solid var(--gold); padding:12px 16px; background:var(--bg-sec); border-radius:0 4px 4px 0;">
        <strong>Voraussetzung & Zielgruppe:</strong> Diese Lösung richtet sich an digital aufgestellte KMU und Industrieunternehmen mit bestehenden CRM-/ERP-Strukturen. Unsere Kunden gehören zu den Vorreitern, die ihre Systeme heute aktiv anschlussfähig machen, während der Großteil des Marktes noch abwartet.
      </p>
    </div>"""

content = content.replace(old_box, new_box)

with open(deep_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("Updated deep page content (removed Chat-Widget focus, fixed target group and Mittelstand)")

# 2. Update ki-befaehigung.html (Mittelstand -> KMU in meta description)
bef_file = os.path.join(base_dir, "ki-befaehigung.html")
with open(bef_file, 'r', encoding='utf-8') as f:
    bef_content = f.read()

bef_content = bef_content.replace(
    'content="Praxisnahe KI-Befähigung für den Mittelstand (KMU).',
    'content="Praxisnahe KI-Befähigung für KMU.'
)
with open(bef_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(bef_content)
print("Updated ki-befaehigung.html meta description")

# 3. Update ki-mitarbeiter/index.html (Mittelstand -> KMU in meta description)
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

ma_content = ma_content.replace(
    'content="Digitale Experten für den Mittelstand.',
    'content="Digitale Experten für KMU.'
)
with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ma_content)
print("Updated ki-mitarbeiter/index.html meta description")
