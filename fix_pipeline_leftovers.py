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

# 1. Product page
replacements_product = [
    ("Die automatisierte B2B-Lead-Pipeline", "Der automatisierte B2B Lead Finder"),
    ("B2B-Lead-Pipeline", "B2B Lead Finder"),
    ("Die B2B-Lead-Pipeline", "Der B2B Lead Finder"),
    ("Unsere standardisierte B2B-Pipeline", "Unser standardisierter B2B Lead Finder"),
]
replace_in_file(os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html"), replacements_product)

# 2. Homepage
replacements_home = [
    ("Die B2B-Lead-Pipeline", "Der B2B Lead Finder"),
    ("die B2B-Lead-Pipeline", "der B2B Lead Finder"),
]
replace_in_file(os.path.join(base_dir, "index.html"), replacements_home)

# 3. KI-Mitarbeiter page
replacements_ki = [
    ("Die B2B-Lead-Pipeline", "Der B2B Lead Finder"),
    ("die B2B-Lead-Pipeline", "der B2B Lead Finder"),
]
replace_in_file(os.path.join(base_dir, "ki-mitarbeiter", "index.html"), replacements_ki)

print("Done.")
