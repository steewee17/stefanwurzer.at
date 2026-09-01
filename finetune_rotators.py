import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update components.js: slower interval (4200ms) and smoother transition
comp_file = os.path.join(base_dir, "components.js")
with open(comp_file, 'r', encoding='utf-8') as f:
    comp_content = f.read()

comp_content = comp_content.replace(
    'setInterval(() => {\n        wordEl.classList.remove(\'in\');\n        wordEl.classList.add(\'out\');\n\n        setTimeout(() => {\n          currentIndex = (currentIndex + 1) % words.length;\n          wordEl.textContent = words[currentIndex];\n          wordEl.classList.remove(\'out\');\n          wordEl.classList.add(\'init\');\n\n          // Trigger reflow\n          void wordEl.offsetWidth;\n\n          wordEl.classList.remove(\'init\');\n          wordEl.classList.add(\'in\');\n        }, 350);\n      }, 3000);',
    'setInterval(() => {\n        wordEl.classList.remove(\'in\');\n        wordEl.classList.add(\'out\');\n\n        setTimeout(() => {\n          currentIndex = (currentIndex + 1) % words.length;\n          wordEl.textContent = words[currentIndex];\n          wordEl.classList.remove(\'out\');\n          wordEl.classList.add(\'init\');\n\n          // Trigger reflow\n          void wordEl.offsetWidth;\n\n          wordEl.classList.remove(\'init\');\n          wordEl.classList.add(\'in\');\n        }, 450);\n      }, 4200);'
)

with open(comp_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(comp_content)
print("Updated timing in components.js")

# 2. Update style.css transition timing
style_file = os.path.join(base_dir, "style.css")
with open(style_file, 'r', encoding='utf-8') as f:
    style_content = f.read()

style_content = style_content.replace(
    'transition: opacity 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);',
    'transition: opacity 0.45s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);'
)

with open(style_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(style_content)
print("Updated style.css transition")

# 3. Update /ki-mitarbeiter/ (remove "Autonome" so it fits smoothly)
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

old_ma = '<h1>Delegieren statt klicken.<br>Autonome Unterstützung für <span class="rotator-wrap" data-words=\'["den Vertrieb.", "das Marketing.", "die Angebotserstellung.", "Verwaltungsaufgaben.", "Recht & Steuern."]\'><em class="rotator-word in">den Vertrieb.</em></span></h1>'
new_ma = '<h1>Delegieren statt klicken.<br>Unterstützung für <span class="rotator-wrap" data-words=\'["den Vertrieb.", "das Marketing.", "die Angebotserstellung.", "Verwaltungsaufgaben.", "Recht & Steuern."]\'><em class="rotator-word in">den Vertrieb.</em></span></h1>'

ma_content = ma_content.replace(old_ma, new_ma)
with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ma_content)
print("Updated ki-mitarbeiter/index.html H1")

# 4. Update /kontakt/ (Move "Direkt" into line 1)
kontakt_file = os.path.join(base_dir, "kontakt", "index.html")
with open(kontakt_file, 'r', encoding='utf-8') as f:
    kontakt_content = f.read()

old_kontakt = '<h1>30 Minuten.<br>Direkt <span class="rotator-wrap" data-words=\'["zum Punkt.", "zu mehr Klarheit.", "zu neuen Ideen.", "zur passenden Lösung."]\'><em class="rotator-word in">zum Punkt.</em></span></h1>'
new_kontakt = '<h1>30 Minuten. Direkt<br><span class="rotator-wrap" data-words=\'["zum Punkt.", "zu mehr Klarheit.", "zu neuen Ideen.", "zur passenden Lösung."]\'><em class="rotator-word in">zum Punkt.</em></span></h1>'

kontakt_content = kontakt_content.replace(old_kontakt, new_kontakt)
with open(kontakt_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(kontakt_content)
print("Updated kontakt/index.html H1")

# 5. Update /team/ (Add dynamic count rotator)
team_file = os.path.join(base_dir, "team", "index.html")
with open(team_file, 'r', encoding='utf-8') as f:
    team_content = f.read()

old_team_h1 = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><em>Sechs digitale Experten.</em></h1>'
new_team_h1 = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><span class="rotator-wrap" data-words=\'["Sechs digitale Experten.", "Sieben digitale Experten.", "Acht digitale Experten.", "Stetig neue Experten."]\'><em class="rotator-word in">Sechs digitale Experten.</em></span></h1>'

if old_team_h1 in team_content:
    team_content = team_content.replace(old_team_h1, new_team_h1)
    with open(team_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(team_content)
    print("Updated team/index.html H1")
else:
    print("Could not match old team H1, please check")

print("All adjustments complete.")
