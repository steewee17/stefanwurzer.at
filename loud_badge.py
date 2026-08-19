import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Mittelstand -> KMU
content = content.replace(
    'Meine Mission: KI für den Mittelstand greifbar',
    'Meine Mission: KI für KMU greifbar'
)

# 2. Role 
content = content.replace(
    '<div class="human-role">KI-Experte & Prozess-Architekt</div>',
    '<div class="human-role">KI & Prozess-Architekt</div>'
)

# 3. Make badge louder
old_badge = ".agent-badge { font-size: 11px; font-weight: 600; background: var(--gold-pale); color: var(--bg); padding: 4px 8px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--sans); }"
new_badge = ".agent-badge { font-size: 11px; font-weight: 600; background: var(--dark); color: var(--gold); padding: 4px 8px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--sans); }"
content = content.replace(old_badge, new_badge)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
