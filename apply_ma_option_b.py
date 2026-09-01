import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")

with open(ma_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_h1 = '<h1>Delegieren statt klicken.<br>Unterstützung für <span class="rotator-wrap" data-words=\'["Ihre Lead-Recherche.", "Ihre CRM-Pflege.", "Ihre Datenanalyse.", "Ihre Angebotserstellung.", "Ihren Kundenservice.", "Ihr Projektmanagement."]\'><em class="rotator-word in">Ihre Lead-Recherche.</em></span></h1>'
new_h1 = '<h1>Delegieren statt klicken.<br>Unterstützung in <span class="rotator-wrap" data-words=\'["Lead-Recherche.", "CRM-Pflege.", "Datenanalyse.", "Angebotserstellung.", "Kundenservice.", "Projektmanagement."]\'><em class="rotator-word in">Lead-Recherche.</em></span></h1>'

content = content.replace(old_h1, new_h1)

with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Updated ki-mitarbeiter/index.html to Option B")
