import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<p class="human-desc">Meine Mission: KI für KMU greifbar und sicher nutzbar zu machen. Ich pflege den direkten Kontakt zu unseren Kunden, stelle strategische Weichen und orchestriere unsere digitalen Agenten. Alles, was Routine ist, wird delegiert.</p>'
replacement = '<p class="human-desc">Mein Ziel ist es, den KI-Anlaufprozess in Ihrem Unternehmen deutlich zu verkürzen. Durch die <strong>KI-Befähigung</strong> Ihres Teams und die Entwicklung eigener <strong>KI-Mitarbeiter</strong> wandeln wir erste theoretische Experimente in echte operative Entlastung um. Wie effizient das in der Praxis funktioniert, zeige ich am besten am eigenen Unternehmen: Ich fokussiere mich auf Prozess-Architektur und Kundenkontakt &ndash; die administrative Routine übernimmt mein digitales Kernteam. Dürfen wir uns vorstellen?</p>'

if target not in content:
    # fallback for encoding
    target = '<p class="human-desc">Meine Mission: KI fǬr KMU greifbar und sicher nutzbar zu machen. Ich pflege den direkten Kontakt zu unseren Kunden, stelle strategische Weichen und orchestriere unsere digitalen Agenten. Alles, was Routine ist, wird delegiert.</p>'

content = content.replace(target, replacement)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
