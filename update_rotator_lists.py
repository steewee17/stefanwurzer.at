import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Startseite (index.html)
index_file = os.path.join(base_dir, "index.html")
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

old_index = 'data-words=\'["vereinen.", "befähigen.", "verbinden.", "skalieren."]\''
new_index = 'data-words=\'["vereinen.", "befähigen.", "verbinden.", "skalieren.", "orchestrieren.", "stärken."]\''

index_content = index_content.replace(old_index, new_index)
with open(index_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(index_content)
print("Updated index.html rotator words")

# 2. /ki-befaehigung/ (ki-befaehigung.html)
bef_file = os.path.join(base_dir, "ki-befaehigung.html")
with open(bef_file, 'r', encoding='utf-8') as f:
    bef_content = f.read()

old_bef = 'data-words=\'["entlastet.", "befähigt.", "motiviert.", "weiterbringt."]\''
new_bef = 'data-words=\'["entlastet.", "befähigt.", "motiviert.", "weiterbringt.", "vernetzt.", "souverän macht."]\''

bef_content = bef_content.replace(old_bef, new_bef)
with open(bef_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(bef_content)
print("Updated ki-befaehigung.html rotator words")

# 3. /ki-mitarbeiter/ (ki-mitarbeiter/index.html)
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

old_ma = 'data-words=\'["Ihre Lead-Recherche.", "Ihre CRM-Pflege.", "Ihre Datenanalyse.", "Ihre Angebotserstellung."]\''
new_ma = 'data-words=\'["Ihre Lead-Recherche.", "Ihre CRM-Pflege.", "Ihre Datenanalyse.", "Ihre Angebotserstellung.", "Ihren Kundenservice.", "Ihr Projektmanagement."]\''

ma_content = ma_content.replace(old_ma, new_ma)
with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ma_content)
print("Updated ki-mitarbeiter/index.html rotator words")

# 4. /kontakt/ (kontakt/index.html) — Add 5. "zum konkreten Fahrplan."
kontakt_file = os.path.join(base_dir, "kontakt", "index.html")
with open(kontakt_file, 'r', encoding='utf-8') as f:
    kontakt_content = f.read()

old_kontakt = 'data-words=\'["zum Punkt.", "zu mehr Klarheit.", "zu neuen Ideen.", "zur passenden Lösung."]\''
new_kontakt = 'data-words=\'["zum Punkt.", "zu mehr Klarheit.", "zu neuen Ideen.", "zur passenden Lösung.", "zum konkreten Fahrplan."]\''

kontakt_content = kontakt_content.replace(old_kontakt, new_kontakt)
with open(kontakt_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(kontakt_content)
print("Updated kontakt/index.html rotator words")

print("All updates successfully written.")
