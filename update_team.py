import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Headline
content = content.replace(
    'Ein Mensch.<br><em>Drei Maschinen.</em>',
    'Ein Mensch.<br><em>Drei digitale Experten.</em>'
)

# 2. Dogfood Subtitle
content = content.replace(
    'Lernen Sie das Team kennen, das "Eat your own dogfood" wörtlich nimmt. Wir verkaufen nicht nur autonome KI-Systeme – wir werden von ihnen operativ betrieben.',
    'Wir nutzen modernste autonome Agenten tagtäglich selbst, um unser Unternehmen maximal effizient und schlank zu führen. Lernen Sie das Team kennen.'
)

# 3. Human Role & Desc
content = content.replace(
    '<div class="human-role">Der Mensch (CEO & Prozess-Architekt)</div>',
    '<div class="human-role">KI-Experte & Prozess-Architekt</div>'
)
content = content.replace(
    'Meine Aufgabe: Die Vision vorgeben, den direkten menschlichen Kontakt zu unseren Kunden pflegen, strategische Weichen stellen und die KI-Agenten orchestrieren. Alles, was Routine ist, delegiere ich konsequent an mein maschinelles Team.',
    'Meine Mission: KI für den Mittelstand greifbar und sicher nutzbar zu machen. Ich pflege den direkten Kontakt zu unseren Kunden, stelle strategische Weichen und orchestriere unsere digitalen Agenten. Alles, was Routine ist, wird delegiert.'
)

# 4. Maschinelles Kernteam -> Digitale Experten
content = content.replace(
    '<h2 style="font-family:var(--display); font-size:32px; color:var(--dark);">Das maschinelle Kernteam</h2>',
    '<h2 style="font-family:var(--display); font-size:32px; color:var(--dark);">Unser KI-Kernteam</h2>'
)

# 5. CSS aspect-ratio 4/3 -> 3/4 for portraits
content = content.replace(
    'aspect-ratio: 4/3;',
    'aspect-ratio: 3/4;'
)

# 6. Jakob GmbH Secret
content = content.replace(
    '<li><i data-lucide="check-circle-2"></i> Begleitung des Übergangs vom Einzelunternehmen zur Solo-GmbH per 01.01.2027.</li>\n            ',
    ''
)
content = content.replace(
    '<li><i data-lucide="check-circle-2"></i> Steuerung steuer- & SVS-optimierter Schnittstellen (GF-Bezug, Miete etc.).</li>',
    '<li><i data-lucide="check-circle-2"></i> Kontinuierliche Optimierung steuer- und SVS-relevanter Kennzahlen.</li>'
)

# 7. David stefanwurzer innovationservice
content = content.replace(
    '<li><i data-lucide="check-circle-2"></i> Positionierung und Content-Strategie für stefanwurzer innovationservice.</li>',
    '<li><i data-lucide="check-circle-2"></i> Verantwortung für die strategische Positionierung und den Content.</li>'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
