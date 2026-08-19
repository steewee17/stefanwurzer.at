import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<div class="agent-role">Head of People & AI-Organisation</div>',
    '<div class="agent-role">Leitung Personal & KI-Organisation</div>'
)

content = content.replace(
    '<div class="agent-role">Head of Finance, Tax & Corporate Strategy</div>',
    '<div class="agent-role">Leitung Finanzen & Steuern</div>'
)

content = content.replace(
    '<div class="agent-role">Head of Marketing & Brand Positioning</div>',
    '<div class="agent-role">Leitung Marketing & Positionierung</div>'
)

content = content.replace(
    '<div class="agent-role">Head of Web Engineering & Deployment</div>',
    '<div class="agent-role">Leitung Webentwicklung & IT</div>'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
