import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the text from its current position
target_text = """
    <!-- PLATZHALTER ZUKUNFT -->
    <div class="fu" style="text-align:center; margin-top: 48px;">
      <p style="font-size:14px; color:var(--muted); font-style:italic;">* Dieses Organigramm wächst dynamisch. Weitere KI-Mitarbeiter befinden sich aktuell im Onboarding.</p>
    </div>"""

if target_text in content:
    content = content.replace(target_text, '')

# 2. Insert it before the HR PROCESS rule
insert_target = "    <!-- HR PROCESS / ONBOARDING -->"
if insert_target in content:
    content = content.replace(insert_target, target_text + "\n    \n" + insert_target)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
