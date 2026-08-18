import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<li><i data-lucide="check-circle-2"></i> Vorbereitung der doppelten Buchhaltung für den Steuerberater.</li>',
    '<li><i data-lucide="check-circle-2"></i> Laufende Vorbereitung der Buchhaltung für den Steuerberater.</li>'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
