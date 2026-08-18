import re

f = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html"
with open(f, 'r', encoding='utf-8', errors='replace') as file:
    content = file.read()

content = re.sub(r'Das Problem:\s*<br>Subjektive Qualit.t\.', 'Die Architektur-<br>Stecknadel.', content)
content = re.sub(r'Herk.mmliche Lead-Datenbanken liefern nur Standard-Metriken \(Umsatz, Mitarbeiter\)\. Sie verraten aber nicht, ob ein Architekturb.ro "Premium" baut\.', 'Jeder findet ein Architekturbüro im Netz. Aber wer findet das Büro, das exklusiv Luxus-Chalets und 5-Sterne-Resorts plant? Standard-Datenbanken kapitulieren hier.', content)
content = re.sub(r'Der 3-S.ulen-\s*<br><em>Algorithmus\.</em>', 'Die Analyse-<br><em>Architektur.</em>', content)

with open(f, 'w', encoding='utf-8') as file:
    file.write(content)
