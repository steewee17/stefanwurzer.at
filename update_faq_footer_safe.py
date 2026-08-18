import os

# 1. Update index.html FAQ
f_idx = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\index.html"
with open(f_idx, 'r', encoding='utf-8') as file:
    c = file.read()

target_str = '<div class="fi"><button class="fb" onclick="faq(this)">Ist die B2B-Lead-Pipeline nur ein weiteres Massen-Mailing-Tool?'
new_faq = '        <div class="fi"><button class="fb" onclick="faq(this)">Funktioniert KI-Qualifizierung auch für hochkomplexe, exklusive B2B-Nischen? <span class="fic">+</span></button><div class="fa"><div class="fai">Ja. Moderne KI-Systeme filtern nicht nur nach Standard-Daten wie Umsatz oder Branche. In unserer <a href="/ki-mitarbeiter/case-premium-leads/" style="color:var(--gold);text-decoration:underline;">Case Study (Premium-Segment)</a> zeigen wir, wie eine KI die <strong>visuelle Ästhetik</strong> von Architektur-Websites bewertet, semantische Fachsprache analysiert und in Branchenmagazinen recherchiert, um exklusive Wunschkunden zu identifizieren. Solche Prozesse qualifizieren Leads auf einem Niveau, das zuvor nur teuren Fachexperten vorbehalten war.</div></div></div>\n        '

c = c.replace(target_str, new_faq + target_str)

with open(f_idx, 'w', encoding='utf-8') as file:
    file.write(c)

# 2. Update components.js footer
f_comp = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\components.js"
with open(f_comp, 'r', encoding='utf-8') as file:
    comp = file.read()

target_footer = '<a href="${faqHref}">Häufige Fragen</a>\n                <span class="fdot">·</span>\n                <a href="/kontakt">Kontakt</a>'
new_footer = '<a href="${faqHref}">Häufige Fragen</a>\n                <span class="fdot">·</span>\n                <a href="/ki-mitarbeiter/case-premium-leads/">Anwendungsfall (Case Study)</a>\n                <span class="fdot">·</span>\n                <a href="/kontakt">Kontakt</a>'

comp = comp.replace(target_footer, new_footer)

with open(f_comp, 'w', encoding='utf-8') as file:
    file.write(comp)

print("Updated FAQ and footer successfully.")
