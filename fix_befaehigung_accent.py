import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
bef_file = os.path.join(base_dir, "ki-befaehigung.html")

with open(bef_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_text = '<br><em>Nicht umgekehrt.</em></h1>'
new_text = '<br>Nicht umgekehrt.</h1>'

content = content.replace(old_text, new_text)

with open(bef_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Removed em tags from 'Nicht umgekehrt.' in ki-befaehigung.html")
