import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. /ki-befaehigung/ — Use the strong, unique 4-liner (Team empowerment verbs)
bef_file = os.path.join(base_dir, "ki-befaehigung.html")
with open(bef_file, 'r', encoding='utf-8') as f:
    bef_content = f.read()

old_bef = '<h1>KI, die passt.<br>Echtes Praxis-Know-how für <span class="rotator-wrap" data-words=\'["Ihren Vertrieb.", "Ihre Projektteams.", "Ihre Verwaltung.", "Ihr gesamtes Team."]\'><em class="rotator-word in">Ihren Vertrieb.</em></span></h1>'
new_bef = '<h1>KI, die passt.<br>Abläufe stärkt.<br>Teams <span class="rotator-wrap" data-words=\'["entlastet.", "befähigt.", "motiviert.", "weiterbringt."]\'><em class="rotator-word in">entlastet.</em></span><br><em>Nicht umgekehrt.</em></h1>'

bef_content = bef_content.replace(old_bef, new_bef)
with open(bef_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(bef_content)
print("Updated ki-befaehigung.html to unique 4-liner rotator")

# 2. /ki-mitarbeiter/ — Concrete tasks: Lead-Recherche, CRM-Pflege, Datenanalyse, Angebotserstellung
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

old_ma = '<h1>Delegieren statt klicken.<br>Unterstützung für <span class="rotator-wrap" data-words=\'["den Vertrieb.", "das Marketing.", "die Angebotserstellung.", "Verwaltungsaufgaben.", "Recht & Steuern."]\'><em class="rotator-word in">den Vertrieb.</em></span></h1>'
new_ma = '<h1>Delegieren statt klicken.<br>Autonome Unterstützung für <span class="rotator-wrap" data-words=\'["Ihre Lead-Recherche.", "Ihre CRM-Pflege.", "Ihre Datenanalyse.", "Ihre Angebotserstellung."]\'><em class="rotator-word in">Ihre Lead-Recherche.</em></span></h1>'

ma_content = ma_content.replace(old_ma, new_ma)
with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ma_content)
print("Updated ki-mitarbeiter/index.html to concrete task rotator")

# 3. /team/ — Structured scaling: Zwei, Drei, Vier, Fünf, Sechs und mehr Experten.
team_file = os.path.join(base_dir, "team", "index.html")
with open(team_file, 'r', encoding='utf-8') as f:
    team_content = f.read()

old_team = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><span class="rotator-wrap" data-words=\'["Sechs digitale Experten.", "Sieben digitale Experten.", "Acht digitale Experten.", "Stetig neue Experten."]\'><em class="rotator-word in">Sechs digitale Experten.</em></span></h1>'
new_team = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><span class="rotator-wrap" data-words=\'["Zwei digitale Experten.", "Drei digitale Experten.", "Vier digitale Experten.", "Fünf digitale Experten.", "Sechs und mehr Experten."]\'><em class="rotator-word in">Zwei digitale Experten.</em></span></h1>'

team_content = team_content.replace(old_team, new_team)
with open(team_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(team_content)
print("Updated team/index.html to structured count rotator")

print("All refinements applied cleanly.")
