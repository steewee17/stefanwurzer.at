import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
deep_file = os.path.join(base_dir, "ki-mitarbeiter", "externe-ki-agenten", "index.html")

with open(deep_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace trust item "Kein Hype, sondern handfeste Prozess-Architektur mit n8n."
content = content.replace(
    '<div class="t-text">Kein Hype, sondern handfeste Prozess-Architektur mit n8n.</div>',
    '<div class="t-text">Kein Hype, sondern handfeste, praxiserprobte Prozess-Architektur.</div>'
)

# 2. Replace Schicht 3 text mentioning "(z. B. über n8n / REST-Schnittstellen und WebMCP-Konzepte)"
content = content.replace(
    'Sichere Backend-Webhooks (z. B. über n8n / REST-Schnittstellen und WebMCP-Konzepte) fangen die eingehende Payload ab',
    'Sichere Backend-Webhooks und standardisierte Schnittstellen (APIs) fangen die eingehende Payload ab'
)

with open(deep_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Removed tech stack mentions from ki-mitarbeiter/externe-ki-agenten/index.html")
