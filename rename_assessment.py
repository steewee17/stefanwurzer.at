import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "2. Das Assessment Center"
replacement = "2. Der Härtetest"

if target in content:
    content = content.replace(target, replacement)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
