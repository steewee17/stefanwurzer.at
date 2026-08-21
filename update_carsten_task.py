import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "<li><i data-lucide=\"check-circle-2\"></i> Aufbereitung bereinigter Lead-Listen für die direkte Vertriebsansprache.</li>"
replacement = "<li><i data-lucide=\"check-circle-2\"></i> Aufbereitung bereinigter Lead-Listen für die direkte Vertriebsansprache und automatisierte Übergabe an das CRM-System.</li>"

content = content.replace(target, replacement)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
