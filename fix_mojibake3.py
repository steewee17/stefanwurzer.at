import os

def fix_direct(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()
    
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
        
    text = content.decode('utf-8')
    
    # Replace broken characters
    replacements = {
        'Ã¤': 'ä',
        'Ã¶': 'ö',
        'Ã¼': 'ü',
        'ÃŸ': 'ß',
        'Ã„': 'Ä',
        'Ã–': 'Ö',
        'Ãœ': 'Ü',
        'â€“': '–',
        'â€ž': '„',
        'â€œ': '“',
        'â€': '”',
        'â€™': '’',
        'Ã©': 'é',
        'Â': ''
    }
    
    for k, v in replacements.items():
        text = text.replace(k, v)
        
    # Also manual fix for  if there are any
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
    text = text.replace('VI', 'ÖVI')
    text = text.replace('Expos', 'Exposé')
    text = text.replace('vollstndig', 'vollständig')
    text = text.replace('Reibungsverluste', 'Reibungsverluste')
    text = text.replace('Grundberzeugung', 'Grundüberzeugung')
    text = text.replace('Durchfhrung', 'Durchführung')
    text = text.replace('Prozessverstndnis', 'Prozessverständnis')
    text = text.replace('unzhligen', 'unzähligen')
    text = text.replace('lsst', 'lässt')
    text = text.replace('rcken', 'rücken')
    text = text.replace('gefllt', 'gefüllt')
    text = text.replace('Kufer', 'Käufer')
    text = text.replace('Geschftsberichte', 'Geschäftsberichte')
    text = text.replace('Zusammenfhrung', 'Zusammenführung')
    text = text.replace('Auftrge', 'Aufträge')
    text = text.replace('hchster', 'höchster')
    text = text.replace('Schlssel', 'Schlüssel')
    text = text.replace('zurck', 'zurück')
    text = text.replace('Bro', 'Büro')
    text = text.replace('Expos-Erstellung', 'Exposé-Erstellung')
    text = text.replace('mageschneiderten', 'maßgeschneiderten')
    text = text.replace('rechtsgltige', 'rechtsgültige')
    text = text.replace('Untersttzung', 'Unterstützung')
    text = text.replace('Zustzlich', 'Zusätzlich')
    text = text.replace('ber', 'über')

    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
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
    fix_direct(f)
