import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

files = [
    os.path.join(base_dir, "ki-mitarbeiter", "index.html"),
    os.path.join(base_dir, "ki-mitarbeiter.html")
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace("Ein digitaler Agent bedient Ihr CRM (wie z. B. Propstack) über offene Schnittstellen", "Ein digitaler Agent bedient Ihr CRM über offene Schnittstellen")
        
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"Updated {file_path}")
