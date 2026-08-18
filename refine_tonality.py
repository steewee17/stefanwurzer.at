import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Refine section title
content = content.replace(
    'Wie wir digitale Kollegen "einstellen"',
    'Der Onboarding-Prozess für digitale Agenten'
)

# Refine Card 1 (Rollenprofil)
content = content.replace(
    'Das verhindert generisches "KI-Sprech" und sorgt dafür, dass sich der Agent nahtlos in die Tonalität einfügt. Harte No-Go-Listen definieren absolute rote Linien.',
    'Dies verhindert austauschbare Floskeln und stellt sicher, dass sich die Kommunikation nahtlos in die Unternehmenssprache einfügt. Klare No-Go-Listen definieren dabei strikte Compliance-Vorgaben.'
)

# Refine Card 2 (Assessment Center)
content = content.replace(
    'In einer isolierten Umgebung testen Hacker-KIs den Neuzugang: Sie versuchen, Sicherheitslücken zu finden, Halluzinationen zu provozieren oder ein PR-Desaster auszulösen. Nur wer standhält, wird übernommen.',
    'In einer isolierten Umgebung prüfen spezialisierte Audit-Agenten das System auf Belastbarkeit: Sie simulieren Stresstests, um Sicherheitslücken aufzudecken, Halluzinationen zu provozieren oder Richtlinienverstöße zu erzwingen. Nur Systeme, die diesen Härtetest fehlerfrei bestehen, werden freigegeben.'
)

# Refine Card 3 (Probezeit)
content = content.replace(
    'Ein Sprachmodell allein ist nur ein Gehirn im Glas.',
    'Ein isoliertes Sprachmodell generiert lediglich Text.'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
