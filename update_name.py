import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<div class="human-name">Stefan Wurzer</div>',
    '<div class="human-name">Stefan</div>'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
