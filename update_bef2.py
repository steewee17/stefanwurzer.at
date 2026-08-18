import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-befaehigung.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'sowie die Offenheit, Fehler im System offen zu korrigieren',
    'sowie die Bereitschaft, Fehler im System konstruktiv zu korrigieren'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
