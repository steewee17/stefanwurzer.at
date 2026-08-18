import os

f_comp = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\components.js"
with open(f_comp, 'r', encoding='utf-8') as f:
    comp = f.read()

comp = comp.replace(
    "{ href: '/ki-mitarbeiter/', label: 'KI-Mitarbeiter' },",
    "{ href: '/ki-mitarbeiter/', label: 'KI-Mitarbeiter' },\n        { href: '/team/', label: 'Team' },"
)

with open(f_comp, 'w', encoding='utf-8') as f:
    f.write(comp)
