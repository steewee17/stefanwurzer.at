import os
import re

def fix_file(filepath):
    # Read the file as utf-8, but it might have been saved as Windows-1252 containing utf-8 bytes
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # Let's decode it. If it was double-encoded, we can fix it.
    try:
        text = content.decode('utf-8')
    except:
        text = content.decode('windows-1252', errors='ignore')
        
    # Fix broken characters
    replacements = {
        'Ã¤': 'ä',
        'Ã¶': 'ö',
        'Ã¼': 'ü',
        'ÃŸ': 'ß',
        'Ã„': 'Ä',
        'Ã–': 'Ö',
        'Ãœ': 'Ü',
        '': 'ä' # Just a placeholder, might need manual replace if it's the replacement char
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
        
    # Since  is lossy, we need to manually fix known words
    text = text.replace('Qualitt', 'Qualität')
    text = text.replace('Quantitt', 'Quantität')
    text = text.replace('przise', 'präzise')
    text = text.replace('fr', 'für')
    text = text.replace('grozgiger', 'großzügiger')
    text = text.replace('Weiraum', 'Weißraum')
    text = text.replace('sthetik', 'Ästhetik')
    text = text.replace('berladene', 'überladene')
    text = text.replace('mageschneidert', 'maßgeschneidert')
    text = text.replace('Mnchen', 'München')
    text = text.replace('unpersnliche', 'unpersönliche')
    text = text.replace('bergabe', 'Übergabe')
    text = text.replace('Sulen', 'Säulen')
    text = text.replace('geprft', 'geprüft')
    text = text.replace('Lsung', 'Lösung')
    text = text.replace('zuknftige', 'zukünftige')
    text = text.replace('mhsamer', 'mühsamer')
    text = text.replace('Tglich', 'Täglich')
    text = text.replace('tglich', 'täglich')
    text = text.replace('durchgngige', 'durchgängige')
    text = text.replace('gefllten', 'gefüllten')
    text = text.replace('lckenlos', 'lückenlos')
    text = text.replace('groen', 'großen')
    text = text.replace('fehleranfllig', 'fehleranfällig')
    text = text.replace('wchentliche', 'wöchentliche')
    text = text.replace('persnlichen', 'persönlichen')
    text = text.replace('Ermdung', 'Ermüdung')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

files = [
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\propstack-agent\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\b2b-lead-pipeline\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html',
    r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\kontakt\index.html'
]

for f in files:
    fix_file(f)
