import os

f = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html"
with open(f, 'r', encoding='utf-8', errors='replace') as file:
    content = file.read()

content = content.replace('Das Problem: <br>Subjektive Qualität.', 'Die Architektur-<br>Stecknadel.')
content = content.replace('Das Problem: \n<br>Subjektive Qualität.', 'Die Architektur-<br>Stecknadel.')
content = content.replace('Der 3-Säulen-<br><em>Algorithmus.</em>', 'Die Analyse-<br><em>Architektur.</em>')
content = content.replace('Der 3-Sulen-<br><em>Algorithmus.</em>', 'Die Analyse-<br><em>Architektur.</em>')
content = content.replace('Herkömmliche Lead-Datenbanken liefern nur Standard-Metriken (Umsatz, Mitarbeiter). Sie verraten aber nicht, ob ein Architekturbüro "Premium" baut.', 'Jeder findet ein Architekturbüro im Netz. Aber wer findet das Büro, das exklusiv Luxus-Chalets und 5-Sterne-Resorts plant? Standard-Datenbanken kapitulieren hier.')

with open(f, 'w', encoding='utf-8') as file:
    file.write(content)
