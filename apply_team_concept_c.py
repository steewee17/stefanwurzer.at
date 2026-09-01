import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
team_file = os.path.join(base_dir, "team", "index.html")

with open(team_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_h1 = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><span class="rotator-wrap" data-words=\'["Zwei digitale Experten.", "Drei digitale Experten.", "Vier digitale Experten.", "Fünf digitale Experten.", "Sechs und mehr Experten."]\'><em class="rotator-word in">Zwei digitale Experten.</em></span></h1>'
new_h1 = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein hybrides Kernteam.<br>Maximale Schlagkraft durch <span class="rotator-wrap" data-words=\'["kontrollierte Autonomie.", "spezialisierte Fachagenten.", "stabile Feedback-Loops.", "maßgeschneiderte Workflows."]\'><em class="rotator-word in">kontrollierte Autonomie.</em></span></h1>'

content = content.replace(old_h1, new_h1)

with open(team_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Updated team/index.html to Concept C")
