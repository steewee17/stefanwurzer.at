import os

def fix_direct(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
    
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
        
    text = content.decode('utf-8')
    
    replacements = {
        'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¼': 'ü', 'ÃŸ': 'ß',
        'Ã„': 'Ä', 'Ã–': 'Ö', 'Ãœ': 'Ü', 'â€“': '–',
        'â€ž': '„', 'â€œ': '“', 'â€': '”', 'â€™': '’',
        'Ã©': 'é', 'Â': ''
    }
    
    for k, v in replacements.items():
        text = text.replace(k, v)
        
    text = text.replace('Befhigung', 'Befähigung')
    text = text.replace('Ablufe', 'Abläufe')
    text = text.replace('strkt', 'stärkt')
    text = text.replace('Gesprch', 'Gespräch')
    text = text.replace('grozgiger', 'großzügiger')
    text = text.replace('Weiraum', 'Weißraum')
    text = text.replace('drckt', 'drückt')
    text = text.replace('gefhrter', 'geführter')
    text = text.replace('Gesprche', 'Gespräche')
    text = text.replace('grYten', 'größten')
    text = text.replace('Engpsse', 'Engpässe')
    text = text.replace('Kpfen', 'Köpfen')
    text = text.replace('langjhriger', 'langjähriger')
    text = text.replace('knnen', 'können')
    text = text.replace('tglich', 'täglich')
    text = text.replace('hchste', 'höchste')
    
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)

fix_direct(r'c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-befaehigung.html')
