# Project State: stefanwurzer.at (KI-Automatisierung & KMU Enablement)

> [!NOTE]
> Dieses Dokument spiegelt den aktuellen, finalisierten Stand der Website wider. Es dokumentiert die radikale Neupositionierung hin zu harter technologischer KMU-Befähigung, das moderne Design-Upgrade (Glassmorphism) und die strategische Ausrichtung auf "Evergreen"-Probleme im B2B-Umfeld.

## 1. Strategische Kernpositionierung: Befähigung statt Agentur-Blackbox
Die Website und Kommunikation wurden vollständig von abstrakten Consulting-Phrasen ("AEO Report", "Conversion Infrastructure") befreit. Der Fokus liegt nun zu 100 % auf nachvollziehbarer technologischer Umsetzung für den Mittelstand (KMU).

- **Agentic Systems Expertise:** Positionierung als souveräner Experte für "Agentic Feedback Loops" und "Geschlossene IT-Systeme". Keine leeren Chatbot-Versprechen (Open-Loop), sondern garantierte "Kontrollierte Autonomie".
- **Lösung von Dauerproblemen ("Evergreen Problem"):** Das zentrale Argumentarium wurde massiv geschärft. KI-Lösungen werden nicht mehr nur als Einmal-Projekte verkauft, sondern als "permanenter Motor", der Dauerprobleme löst (z.B. Neukundengewinnung/Lead-Pipeline, die ein Unternehmensleben lang benötigt wird). 
- **Qualität statt Masse (Kein Spam):** Harte Abgrenzung von toxischen Begriffen wie "Kaltakquise" oder "Spam-Bots". Der Fokus liegt auf der *vorherigen* Recherche und strengen Qualifizierung nach Wunschkundenprofil (ICP) – das unterstreicht den Premium-Anspruch.
- **Das 2-Säulen-Portfolio:**
  - *KI-Befähigung:* Das Fundament (Infrastruktur, Automation, Eigene Agenten) für Unternehmen, die intern Wissen aufbauen wollen.
  - *KI-Mitarbeiter:* Der "Done-for-you"-Ansatz. KI-Agenten, die über APIs (z. B. n8n) direkt an Fachsysteme (ERP/CRM) andocken und Workflows autonom abarbeiten.

## 2. Seitenarchitektur & Content (Live-Stand)
- **Startseite (`/`):** Runderneuert. Starker Fokus auf den Endnutzen ("Delegieren statt klicken"). 
  - *Neu:* Ein auffälliger, dunkler "Featured"-Banner pusht den konkreten Use-Case "B2B Vertrieb auf Autopilot" prominent auf der Startseite.
  - *Neu:* FAQ-Sektion adressiert proaktiv Bedenken ("Ist das ein Massen-Mailing-Tool? -> Nein, präzise Lead-Engine").
- **KI-Befähigung (`/ki-befaehigung/`):** Fokus auf die Probleme der Nutzer. Integration von anonymisierten Praxisbeispielen (Sitzungsprotokolle, Excel-Abgleich, ERP-Exporte).
- **KI-Mitarbeiter (`/ki-mitarbeiter/`):** Branchenübergreifende Case-Studies im Grid-Layout (CRM-Intake, n8n Reporting, B2B Vertrieb). 
- **Digitale Akquise (`/ki-mitarbeiter/digitale-akquise/`):** Eine komplett neue, dedizierte Deep-Dive-Landingpage (Hub-and-Spoke-Modell) für das erste **produktisierte System**: den KI-Sales-Researcher. Präsentiert den 5-stufigen "Maschinenraum" (Sourcing, DB, KI-Qualifizierung via Claude, Enrichment, CRM-Push in HubSpot/Pipedrive/Freshworks) in einem edlen Glassmorphism-UI.
- **Kontakt (`/kontakt/`):** Das Formular-Dropdown wurde radikal verschlankt und auf die Kernleistungen fokussiert (Systemcheck, KI-Mitarbeiter, Befähigung). Die "Über mich"-Prinzipien wurden als klares "Architektur-Fundament für KI-Systeme" neu vertextet.

## 3. Visuelles Design & UI-System
Das gesamte visuelle Erlebnis wurde auf ein einheitliches "Premium Tech"-Level gehoben.
- **Glassmorphism:** Formulare, Kontakt-Karten, Praxisbeispiel-Boxen und die Architektur-Schritte der Akquise-Seite wurden in ein edles Glass-Design überführt (`backdrop-filter: blur`, zarte transparente Verläufe, helle Rahmen und weiche Hover-Schatten). Das signalisiert technologische Marktführerschaft.
- **Bewusste 2D-Mikrointeraktionen:** Um Unschärfen beim Text-Rendering (Anti-Aliasing-Verlust bei 3D-CSS auf Windows-Rechnern) zu vermeiden, wurden statische 3D-Kipp-Effekte bei HTML-Text durch sanfte 2D-Hover-Elevation (`translateY`) ersetzt. 
- **Subtile Leuchteffekte:** Einsatz von sanft pulsierenden, asymmetrischen `.orb`-Elementen im Hintergrund, um den Bereichen räumliche Tiefe zu verleihen.

## 4. AEO & SEO (Answer Engine Optimization)
- **Strukturierte Daten (JSON-LD):** Die Startseite, sowie die Landingpages funken nun explizit B2B-Konzepte in die `knowsAbout`- und `description`-Arrays der Schema.org-Daten: "Agentic Systems", "Lead Generation", "B2B Vertrieb Automatisierung", "n8n API Integration".
- **Meta-Tags:** Alle Titel und Beschreibungen wurden messerscharf auf die neuen Keywords getrimmt. KI-Suchmaschinen (Perplexity, ChatGPT Search) erkennen nun sofort die tiefe technische Expertise abseits von reinem Coaching.
- **Sitemap:** Die `sitemap.xml` wurde um alle neuen Landingpages ergänzt (Zuletzt aktualisiert am 28.07.2026).

## 5. Offene Potenziale & Zukünftige Roadmap
- **Weitere Use Cases produktisieren:** Nach dem Vorbild der "Digitalen Akquise" könnten weitere Boxen aus dem KI-Mitarbeiter-Grid (z.B. Dokumenten-Parsing, intelligentes E-Mail-Routing) eigene vertikale Landingpages erhalten, sobald diese Prozesse standardisiert verkauft werden sollen.
- **Agent-Knowledge Update:** Die Supabase-Datenbank (Knowledge Base) des nativen "KI-Chat-Agenten" (`agent-widget.js`), falls dieser weiter aktiv im Einsatz ist, muss zwingend mit dem neuen, verschlankten Content-Scrape der Website aktualisiert werden, damit der Agent die neue "Evergreen Problem" Positionierung übernimmt.
