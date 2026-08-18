$file = "c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\b2b-lead-pipeline\index.html"
$content = Get-Content $file -Raw -Encoding UTF8

# Head and Meta
$content = $content -replace '<title>B2B Digitale Akquise & Lead Generation \| Stefan Wurzer</title>', '<title>Die automatisierte B2B-Lead-Pipeline | Stefan Wurzer</title>'
$content = $content -replace '<meta name="description" content="Der KI-Sales-Researcher: Automatisierte Lead-Recherche, KI-Qualifizierung nach Ihrem Wunschkundenprofil und nahtlose CRM-Übergabe für den B2B Vertrieb.">', '<meta name="description" content="Die B2B-Lead-Pipeline: Automatisierte Lead-Recherche, Qualifizierung nach Ihrem Wunschkundenprofil (ICP) und nahtlose CRM-Übergabe für den B2B-Vertrieb.">'
$content = $content -replace '<meta name="keywords" content="B2B Vertrieb Automatisierung, Lead Generation, Digitale Akquise, KI-Sales-Researcher, KI-Mitarbeiter, HubSpot Automatisierung, Pipedrive Automatisierung">', '<meta name="keywords" content="B2B Vertrieb Automatisierung, Lead Pipeline, Lead Engine, Lead Generation, B2B-Lead-Pipeline, KI-Mitarbeiter, HubSpot Automatisierung, Pipedrive Automatisierung">'
$content = $content -replace '"name": "B2B Digitale Akquise & Lead Generation \| Stefan Wurzer"', '"name": "Die automatisierte B2B-Lead-Pipeline | Stefan Wurzer"'
$content = $content -replace '<meta property="og:title" content="B2B Digitale Akquise & Lead Generation \| Stefan Wurzer">', '<meta property="og:title" content="Die automatisierte B2B-Lead-Pipeline | Stefan Wurzer">'
$content = $content -replace '<meta property="og:description" content="Der KI-Sales-Researcher: Wie ein maßgeschneiderter KI-Agent Ihre B2B-Akquise revolutioniert.">', '<meta property="og:description" content="Die B2B-Lead-Pipeline: Wie automatisierte Datenprozesse Ihren Vertriebsengpass lösen.">'

# H1 and Intro
$content = $content -replace '<h1>Der KI-Sales-Researcher:<br><em>Volle Pipeline.</em></h1>', '<h1>Die B2B-Lead-Pipeline:<br><em>Fokussierte Vertriebszeit.</em></h1>'
$content = $content -replace '<span class="ey">B2B Vertrieb auf Autopilot</span>', '<span class="ey">Mehr qualifizierte Leads</span>'
$content = $content -replace 'Die Neukundengewinnung ist ein Problem, das nie verschwindet. Lösen Sie es mit einem System, das nie schläft. Von der automatisierten Recherche über die KI-Qualifizierung nach Ihrem Wunschkundenprofil \(ICP\) bis zur nahtlosen CRM-Übergabe.', 'Viele B2B-Teams kennen ihre Zielkunden. Was fehlt, ist ein verlässlicher Prozess, der daraus täglich bearbeitbare Kontakte macht. Lösen Sie den manuellen Recherche-Engpass mit einer durchgängigen Workflow-Lösung: vom ICP bis zur CRM-Übergabe.'
$content = $content -replace 'Agentic Lead Generation', 'Die B2B-Lead-Pipeline'

# Form and specific text
$content = $content -replace '<span class="ey">Akquise Automatisieren</span>', '<span class="ey">Pipeline Automatisieren</span>'
$content = $content -replace 'diesen Akquise-Agenten auf', 'diesen Lead-Prozess auf'
$content = $content -replace "leistung: 'KI-Sales-Researcher \\(Akquise\\)'", "leistung: 'B2B-Lead-Pipeline'"
$content = $content -replace 'Die Neukundengewinnung nachhaltig.', 'Die Lead-Gewinnung nachhaltig.'

Set-Content -Path $file -Value $content -NoNewline -Encoding UTF8
