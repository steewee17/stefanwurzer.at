import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = "Dürfen wir uns vorstellen?</p>"
replacement = "Darf ich vorstellen:</p>"

content = content.replace(target, replacement)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
