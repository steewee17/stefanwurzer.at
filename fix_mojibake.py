import os
import glob

def fix_encoding(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # The file has utf-8 bytes read and written as cp1252 by powershell, resulting in garbled text.
    # Wait, if powershell read it as ANSI (cp1252) and then wrote it back as UTF-8, then what was an actual UTF-8 byte sequence like b'\xc3\xa4' (ä) was treated as two ANSI characters Ã (0xC3) and ¤ (0xA4). Then powershell wrote out those two characters as UTF-8, resulting in b'\xc3\x83\xc2\xa4'.
    
    try:
        # Convert it back
        # Read as utf-8 (which gives us the double encoded characters like Ã¤)
        text = content.decode('utf-8')
        # Encode as cp1252 to get the original utf-8 bytes
        original_bytes = text.encode('cp1252')
        # Decode as utf-8 to get the proper text
        fixed_text = original_bytes.decode('utf-8')
        
        with open(filepath, 'w', encoding='utf-8') as f:
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
