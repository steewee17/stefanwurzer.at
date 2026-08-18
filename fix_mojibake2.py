import os

def fix_encoding(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # Strip BOM if present
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
    
    try:
        text = content.decode('utf-8')
        original_bytes = text.encode('cp1252')
        fixed_text = original_bytes.decode('utf-8')
        
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(fixed_text)
        print(f"Fixed {filepath}")
    except Exception as e:
        print(f"Skipping {filepath} - {e}")

files = [
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\propstack-agent\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\b2b-lead-pipeline\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\kontakt\index.html'
]

for f in files:
    fix_encoding(f)
