import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
files_to_check = [
    os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html"),
    os.path.join(base_dir, "index.html"),
    os.path.join(base_dir, "ki-mitarbeiter", "index.html")
]

replacements = [
    ("Die B2B Lead Finder", "Der B2B Lead Finder"),
    ("die B2B Lead Finder", "den B2B Lead Finder"), # e.g. "Ist der B2B Lead Finder..." (Ist is nominative so "der", but I'll fix this manually if needed)
]

for f in files_to_check:
    replace_in_file(f, replacements)
