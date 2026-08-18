import os
import re

f_comp = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\components.js"
with open(f_comp, 'r', encoding='utf-8', errors='replace') as file:
    comp = file.read()

comp = re.sub(r'(<a href="\$\{faqHref\}">[^<]+</a>\s*<span class="fdot">[^<]+</span>\s*)(<a href="/kontakt">)', r'\1<a href="/ki-mitarbeiter/case-premium-leads/">Case Study (Premium-Leads)</a>\n              <span class="fdot">·</span>\n              \2', comp)

# Fix the mojibake in components.js too while we are at it
comp = comp.replace('Hufige Fragen', 'Häufige Fragen')
comp = comp.replace(' 2026', '© 2026')
comp = comp.replace('fr KMU', 'für KMU')
comp = comp.replace('Befhigung', 'Befähigung')

with open(f_comp, 'w', encoding='utf-8') as file:
    file.write(comp)
