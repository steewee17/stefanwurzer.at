import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<div class="agent-role">Leitung Personal & KI-Organisation</div>',
    '<div class="agent-role">Personal & KI-Organisation</div>'
)

content = content.replace(
    '<div class="agent-role">Leitung Finanzen & Steuern</div>',
    '<div class="agent-role">Finanzen & Steuern</div>'
)

content = content.replace(
    '<div class="agent-role">Leitung Marketing & Positionierung</div>',
    '<div class="agent-role">Marketing & Positionierung</div>'
)

content = content.replace(
    '<div class="agent-role">Leitung Webentwicklung & IT</div>',
    '<div class="agent-role">Webentwicklung & IT</div>'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
