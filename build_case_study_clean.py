import os

f = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html"
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Head/Meta
c = c.replace('<title>Die automatisierte B2B-Lead-Pipeline | Stefan Wurzer</title>', '<title>Case Study: Premium B2B Lead-Generierung (METEK) | Stefan Wurzer</title>')
import re
c = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Case Study: Wie die METEK GmbH durch multimodale KI-Analyse (Semantik & visuelle Ästhetik) exklusive Architektur-Leads für den Premium-Innenausbau identifiziert.">', c)
c = re.sub(r'<meta name="keywords" content="[^"]*">', '<meta name="keywords" content="Case Study, B2B Vertrieb, Lead Pipeline, Lead Engine, Luxussegment, Architektur, KI-Analyse, METEK GmbH">', c)
c = c.replace('"name": "Die automatisierte B2B-Lead-Pipeline | Stefan Wurzer"', '"name": "Case Study: Premium B2B Lead-Generierung (METEK) | Stefan Wurzer"')
c = c.replace('https://www.stefanwurzer.at/ki-mitarbeiter/b2b-lead-pipeline/', 'https://www.stefanwurzer.at/ki-mitarbeiter/case-premium-leads/')
c = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Case Study: KI-Qualifizierung im Premium-Segment">', c)
c = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Wie eine KI architektonische Ästhetik und semantische Fachartikel bewertet, um exklusive B2B-Kunden zu identifizieren.">', c)

# Header section
c = c.replace('<span class="ey">Mehr qualifizierte Leads</span>', '<span class="ey">Case Study: METEK GmbH</span>')
c = c.replace('<h1>Die B2B-Lead-Pipeline:<br><em>Fokussierte Vertriebszeit.</em></h1>', '<h1>KI-Qualifizierung im<br><em>Premium-Segment.</em></h1>')
c = c.replace('Viele B2B-Teams kennen ihre Zielkunden. Was fehlt, ist ein verlässlicher Prozess, der daraus täglich bearbeitbare Kontakte macht. Lösen Sie den manuellen Recherche-Engpass mit einer durchgängigen Workflow-Lösung: vom ICP bis zur CRM-Übergabe.', 'Wie identifiziert man hochspezialisierte Architekten für den gehobenen Innenausbau (Luxus), die man nicht einfach "ergoogeln" kann? Diese Case Study zeigt, wie die METEK GmbH durch eine Kombination aus semantischer Textanalyse, Medien-Recherche und visueller Ästhetik-Bewertung ihren Vertrieb revolutioniert.')
c = c.replace('Vertriebler sollen verkaufen. <br>Nicht kopieren.', 'Die Architektur-<br>Stecknadel.')
c = c.replace('Gegenüberstellung im B2B-Vertrieb:', 'Jeder findet ein Architekturbüro im Netz. Aber wer findet das Büro, das exklusiv Luxus-Chalets und 5-Sterne-Resorts plant? Standard-Datenbanken kapitulieren hier.')
c = c.replace('<div style="font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Manueller Blindflug</div>', '<div style="font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Die manuelle Lösung</div>')
c = c.replace('Stundenlange Recherche in Datenbanken, viele irrelevante Leads und manuelles Eintragen ins CRM.', 'Stundenlange, manuelle Inspektion von Architekten-Websites und Portfolio-Prüfung durch den Vertrieb.')
c = c.replace('<div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Agentic Lead Generation</div>', '<div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Die KI-Lösung</div>')
c = c.replace('<div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Die B2B-Lead-Pipeline</div>', '<div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">Die KI-Lösung</div>')
c = c.replace('Der Vertriebler öffnet morgens sein CRM und findet exakt qualifizierte Leads, fertig für das persönliche Anschreiben.', 'Ein multimodales KI-System bewertet die Ästhetik der Website und durchsucht Fachmagazine nach dem Architekten.')

# Steps Section
c = c.replace('So funktioniert der <br><em>Prozess.</em>', 'Die Analyse-<br><em>Architektur.</em>')
c = c.replace('Qualität statt Masse. Wir bauen ein hochintelligentes Research-System, das dem Menschen nur die absolut relevantesten Leads auf dem Silbertablett serviert.', 'Die KI berechnet aus drei komplementären Analysen einen aggregierten LeadScore (1-10) für das CRM.')

c = c.replace('Sourcing (Die Datenquelle)', 'Semantische Textanalyse (40%)')
c = c.replace('Ein Automatisierungs-Flow übernimmt die gezielte Suche nach Account-Listen (z. B. in professionellen Business-Netzwerken) und extrahiert diese vollautomatisch (URL zu CSV).', 'Ein GPT-gestütztes Modul analysiert die Website-Texte auf Begriffe wie „maßgeschneidert“, „architektonisch anspruchsvoll“ oder „Luxusimmobilien“. Auch narrative Struktur und Länge fließen in die Bewertung ein.')

c = c.replace('Daten-Upload & Strukturierung', 'Umfeldanalyse (35%)')
c = c.replace('Die rohen Leads werden nicht mühsam in Excel gepflegt, sondern landen sicher, DSGVO-konform und strukturiert in einer eigenen, dedizierten Datenbank (einer sicheren Datenbank).', 'Ein KI-Recherchemodul (Perplexity) durchsucht das Netz nach Erwähnungen in Presseartikeln und Fachportalen. Maßgeblich ist, ob das Architekturbüro im Kontext hochwertiger Hotel- oder Interior-Projekte genannt wird.')

# Step 3 highlight removal
c = c.replace('class="step-card glass-card fu d2" style="border:1px solid var(--gold);box-shadow:0 8px 32px rgba(184,150,46,.1);"', 'class="step-card glass-card fu d2"')
c = c.replace('class="step-icon" style="background:var(--gold);color:#fff;"', 'class="step-icon"')
c = c.replace('class="step-num" style="background:var(--gold);color:#fff;border-color:var(--gold);"', 'class="step-num"')

c = c.replace('KI-Qualifizierung (Das Gehirn)', 'Visuelle Analyse (25%)')
c = c.replace('<strong>Hier passiert die Magie.</strong> Ein intelligentes KI-Sprachmodell analysiert jeden einzelnen Lead über API und bewertet ihn präzise anhand Ihres spezifischen Ideal Customer Profiles (ICP). Irrelevante Leads werden gnadenlos aussortiert, ohne dass ein Mensch Zeit damit verschwendet.', 'Parallel zur Textauswertung bewertet ein Vision-Modell die Ästhetik der Website (Typografie, großzügiger Weißraum, Bildsprache, Studiofotografie). Baukasten-Optik oder überladene Designs werden abgewertet.')

c = c.replace('Anreicherung (Data Enrichment)', 'Aggregation: Der LeadScore')
c = c.replace('Valide E-Mail-Adressen, Telefonnummern und weitere Firmendaten der qualifizierten Leads werden über zertifizierte Schnittstellen angereichert.', 'Die drei Teilergebnisse werden gewichtet und zu einem LeadScore von 1 bis 10 zusammengeführt. Zusätzlich generiert die KI eine textbasierte Begründung für den Score.')

c = c.replace('CRM-Übergabe', 'Nahtlose CRM-Übergabe')
c = c.replace('Die perfekten, qualifizierten und angereicherten Leads werden direkt in Ihr CRM (wie HubSpot, Pipedrive, Freshsales oder Propstack) gepusht. Ihr Sales-Team sieht sofort, warum der Lead relevant ist.', 'Die qualifizierten Leads werden mitsamt der Analysebegründung vollautomatisiert ins Pipedrive-CRM der METEK GmbH übergeben. Der Vertrieb startet den Tag mit einer priorisierten Arbeitsliste.')

# Outcome Section
# Remove cross-link banner from case study page
c = re.sub(r'<!-- CASE STUDY CROSS LINK -->.*?</section>', '', c, flags=re.DOTALL)

c = c.replace('Der messbare <em>Effekt.</em>', 'Das <em>Ergebnis.</em>')
c = c.replace('Kontrollierte Autonomie: Die KI baut die Pipeline, der Mensch schließt ab.', 'Höchste Lead-Qualität und drastische Zeitersparnis.')
c = c.replace('Dieses System ist keine unpersönliche Massen-Maschine. Es ist eine präzise "Lead Engine", die sicherstellt, dass Vertriebler ihre wertvolle Zeit zu 100% in hochindividuelle, datengetriebene Kundengespräche investieren können.', 'Während die manuelle Recherche bislang extrem zeitintensiv war, analysiert das System nun hunderte potenzielle Leads pro Woche – ohne zusätzlichen Personalbedarf. Der Vertrieb fokussiert sich ausschließlich auf die Anbahnung bei den relevantesten Top-Kandidaten.')
c = c.replace('<strong>Ein permanenter Motor für Ihr Wachstum.</strong> Die meisten geschäftlichen Probleme löst man einmal. Die Notwendigkeit für neue Kunden bleibt, solange Ihr Unternehmen existiert. Diese Lead-Engine ist kein einmaliges IT-Projekt, sondern ein immerwährendes System, das Tag für Tag, Monat für Monat kontinuierlich Ihre Pipeline füllt.', 'Ein Paradigmenwechsel im B2B-Vertrieb: Weg von reaktiver Recherche und Zufallsansprache hin zu systematisch vorbereiteten, priorisierten Kontakten mit extrem hoher inhaltlicher Relevanz.')

# Form Section
c = c.replace('<span class="ey">Pipeline Automatisieren</span>', '<span class="ey">Ihre Nische erschließen</span>')
c = c.replace('<h2>Bereit für eine<br><em>volle Pipeline?</em></h2>', '<h2>Suchen Sie nach<br><em>unsichtbaren Leads?</em></h2>')
c = c.replace('Lassen Sie uns in 30 Minuten analysieren, wie wir diesen Lead-Prozess auf Ihre spezifische Branche und Ihr CRM anpassen können.', 'Wenn Standard-Lead-Listen für Ihre Branche nicht ausreichen, bauen wir die Intelligenz, die Sie brauchen. Lassen Sie uns Ihren Prozess besprechen.')

c = c.replace("leistung: 'B2B-Lead-Pipeline'", "leistung: 'Case Study (Premium Leads)'")

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

print("Applied case study changes correctly.")
