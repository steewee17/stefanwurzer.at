import os
import re

f = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\b2b-lead-pipeline\index.html"
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('Dynamisches <em>Zielbild.</em>', 'Der messbare <em>Effekt.</em>')
c = c.replace('<div class="fu d1" style="background:var(--gold); border-radius:12px; padding:40px; text-align:center;">', '<div class="fu d1 glass-card" style="text-align:center; padding:40px; max-width:800px; margin:0 auto; border:1px solid var(--gold);">')
c = c.replace('<a href="/ki-mitarbeiter/case-premium-leads/" class="btn" style="background:var(--dark); color:var(--gold); border-color:var(--dark);">Zur Case Study →</a>', '<a href="/ki-mitarbeiter/case-premium-leads/" class="btn" style="display:inline-flex;">Zur Case Study →</a>')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
