import os

f_comp = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\components.js"
with open(f_comp, 'r', encoding='utf-8') as file:
    comp = file.read()

comp = comp.replace('<a href="/ki-mitarbeiter/case-premium-leads/">Case Study (Premium-Leads)</a>', '<a href="/ki-mitarbeiter/case-premium-leads/">Case Study</a>')

with open(f_comp, 'w', encoding='utf-8') as file:
    file.write(comp)
