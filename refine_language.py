import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-befaehigung.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Commodity -> austauschbarer Standard
content = content.replace(
    'Die Technologie – ob das neueste Flaggschiff-Modell oder Open-Source – ist mittlerweile austauschbare Commodity.',
    'Die Technologie – ob das neueste Flaggschiff-Modell oder Open-Source – ist mittlerweile ein austauschbarer Standard.'
)

# 2. Positive Framing for Processes
content = content.replace(
    'Eine KI kann nur so präzise agieren, wie der zugrunde liegende Prozess definiert ist. Wenn die Übergabepunkte, Qualitätskriterien und Datenflüsse im Unternehmen chaotisch sind, skaliert ein KI-Agent lediglich das Chaos in Rekordzeit.',
    'Eine KI entfaltet ihr wahres Potenzial erst, wenn der zugrunde liegende Prozess klar strukturiert ist. Sobald Übergabepunkte, Qualitätskriterien und Datenflüsse sauber definiert sind, wird aus einfacher Automatisierung eine spürbare Entlastung für das gesamte Team.'
)

# 3. Use Case & Keks -> Anwendungsfall & Routine
content = content.replace(
    'Wer stattdessen vom konkreten <strong>Use Case</strong> ausgeht – <em>"Welche Aufgaben gehen den Leuten im Alltag eigentlich total auf den Keks?"</em> – und diese gezielt automatisiert, liefert keinen bloßen "Tech-Stack", sondern operative Transformation mit messbarem ROI.',
    'Wer stattdessen beim konkreten <strong>Anwendungsfall</strong> ansetzt – <em>"Welche Aufgaben binden im Alltag die meiste wertvolle Zeit?"</em> – und exakt diese Routine gezielt automatisiert, liefert nicht einfach nur neue Software, sondern operative Transformation mit messbarem Mehrwert.'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
