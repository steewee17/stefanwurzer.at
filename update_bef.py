import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-befaehigung.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Risikoappetit
content = content.replace(
    'den "Risikoappetit", Fehler',
    'die Offenheit, Fehler'
)

# Replace Mittelstand with KMU
content = content.replace(
    'oft im Mittelstand:',
    'oft in KMU:'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
