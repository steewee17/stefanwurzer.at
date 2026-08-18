import os
import re

# 1. Update index.html FAQ
f_idx = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\index.html"
with open(f_idx, 'r', encoding='utf-8') as file:
    c = file.read()

new_faq = """      <div class="fi"><button class="fb" onclick="faq(this)">Funktioniert KI-Qualifizierung auch für hochkomplexe, exklusive B2B-Nischen? <span class="fic">+</span></button><div class="fa"><div class="fai">Ja. Moderne KI-Systeme filtern nicht nur nach Standard-Daten wie Umsatz oder Branche. In unserer <a href="/ki-mitarbeiter/case-premium-leads/" style="color:var(--gold);text-decoration:underline;">Case Study (Premium-Segment)</a> zeigen wir, wie eine KI die <strong>visuelle Ästhetik</strong> von Architektur-Websites bewertet, semantische Fachsprache analysiert und in Branchenmagazinen recherchiert, um exklusive Wunschkunden zu identifizieren. Solche Prozesse qualifizieren Leads auf einem Niveau, das zuvor nur teuren Fachexperten vorbehalten war.</div></div></div>\n"""

# Insert the new FAQ right before the closing </div> of the flist
c = re.sub(r'(      </div>\n    </div>\n  </div>\n</section>\n\n<!-- SCHNITTSTELLEN)', r'' + new_faq + r'\1', c)

with open(f_idx, 'w', encoding='utf-8') as file:
    file.write(c)

# 2. Update components.js footer
f_comp = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\components.js"
with open(f_comp, 'r', encoding='utf-8') as file:
    comp = file.read()

footer_link = """                <a href="${faqHref}">Häufige Fragen</a>
                <span class="fdot">·</span>
                <a href="/ki-mitarbeiter/case-premium-leads/">Anwendungsfall (Case Study)</a>
                <span class="fdot">·</span>
                <a href="/kontakt">Kontakt</a>"""

comp = re.sub(r'                <a href="\$\{faqHref\}">Häufige Fragen</a>\s*<span class="fdot">·</span>\s*<a href="/kontakt">Kontakt</a>', footer_link, comp)

with open(f_comp, 'w', encoding='utf-8') as file:
    file.write(comp)
