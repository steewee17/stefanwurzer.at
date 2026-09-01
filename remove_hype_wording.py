import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/externe-ki-agenten/index.html
deep_file = os.path.join(base_dir, "ki-mitarbeiter", "externe-ki-agenten", "index.html")
with open(deep_file, 'r', encoding='utf-8') as f:
    deep_content = f.read()

deep_content = deep_content.replace(
    '<div class="t-text">Kein Hype, sondern handfeste, praxiserprobte Prozess-Architektur.</div>',
    '<div class="t-text">Keine leeren Versprechen, sondern handfeste, praxiserprobte Prozess-Architektur.</div>'
)

with open(deep_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(deep_content)
print("Updated externe-ki-agenten index.html")

# 2. Update ki-befaehigung.html
bef_file = os.path.join(base_dir, "ki-befaehigung.html")
with open(bef_file, 'r', encoding='utf-8') as f:
    bef_content = f.read()

bef_content = bef_content.replace(
    '<span class="ey">Die Realität des KI-Hypes</span>',
    '<span class="ey">Philosophie & Haltung</span>'
)

with open(bef_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(bef_content)
print("Updated ki-befaehigung.html")
