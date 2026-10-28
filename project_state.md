# Project State: stefanwurzer.at (KI-Agenten & KMU-Befähigung)

> [!NOTE]
> Dieses Dokument bildet den **aktuellen, verbindlichen Live-Stand der Website** ab (Stand: Oktober 2026). Es dient als Single Source of Truth für alle Agenten, Sessions und Weiterentwicklungen.

---

## 1. Strategische Kernpositionierung & Wording-Regeln

Die Website positioniert Stefan Wurzer als unabhängigen Experten für **autonome KI-Agenten, Closed-Loop-Systeme und technologische KMU-Befähigung**.

- **Primäres Einstiegsangebot: Der „7-Phasen-Prozess-Check“**
  - Auf der Website werden **keine Umsetzungs-Projekte oder Tool-Pakete von der Stange** verkauft.
  - Das exklusive Conversion-Ziel der gesamten Website ist die **Terminvereinbarung für den 7-Phasen-Prozess-Check** (offiziell gefördert unter dem Förderschwerpunkt [„Digitalisierung von Geschäftsprozessen“](https://foerderungen.wko.at/tirol/Digitalisierung), bis zu 80 % förderfähig via WKO / KMU.DIGITAL).
  - Umsetzungsleistungen (die eigentliche Systemintegration und Automatisierung) entstehen erst als organische Folgeprojekte im Beratungs- und Auswertungsgespräch des Checks („Diagnose vor Therapie“).
- **Hero-Messaging & Kernversprechen (Sieger-Kombination statt „Durchsatz“):**
  - Eyebrow: `● FÖRDERSCHWERPUNKT: DIGITALISIERUNG VON GESCHÄFTSPROZESSEN | DER 7-PHASEN-PROZESS-CHECK` (Offizieller WKO-Link, dezent und ohne territoriale Einschränkung „nur Tirol“ formuliert).
  - Headline: *„Schnellere Auftragsabwicklung. Flaschenhälse aufdecken und beseitigen.“*
  - Subline: *„Wo verliert Ihr Betrieb zwischen Vertrieb, Büro und Ausführung täglich Zeit und Marge? Im geförderten 7-Phasen-Prozess-Check identifizieren wir die Bremsen in Ihren Abläufen und verbinden Ihre bestehende Software zu einem nahtlosen Informationsfluss.“*
  - Begründung: Der Begriff *„Durchsatz“* wurde im gesamten Außenauftritt getilgt (im KMU-Umfeld zu abstrakt/industriell). Stattdessen greifen die Begriffe *„Schnellere Auftragsabwicklung“*, *„Flaschenhälse“*, *„Liegezeiten“* und *„Zeit & Marge“* unmittelbar die reale betriebliche Dringlichkeit auf.
- **Terminologie-Standard: „KI-Agenten“ statt „KI-Mitarbeiter“**
  - Sämtliche URLs, Navigationselemente, Überschriften und Fließtexte wurden von *KI-Mitarbeiter* auf **KI-Agenten** migriert.
  - Begründung: Präzisere Branchenterminologie, professionelle Abgrenzung von Hype-Begriffen und Vorbereitung auf M2M- / Agentic-Web-Standards.
- **Wording-Regel (Österreich / DACH): „KMU“ statt „Mittelstand“**
  - Der Begriff *„Mittelstand“* ist bundesdeutsches Vokabular. Für den österreichischen und regionalen DACH-Markt gilt ausnahmslos: **KMU (Kleine und mittlere Unternehmen)**, **Betriebe**, **Industrieunternehmen** oder **Zulieferer**. (Verankert in `AGENTS.md`).
- **Tonalität & Anspruch:**
  - Ingenieursnah, prägnant, rhythmisch und bodenständig.
  - Kein Agentur-Hype-Slang („Gamechanger“, „10x“, „mit n8n gebaut“). Die Technologie arbeitet im Hintergrund; im Vordergrund steht der belastbare, permanente Geschäftsnutzen (*Evergreen-Probleme lösen*).
  - Verbindliches, professionelles **„Sie / Ihr“**.
- **Das 2-Säulen-Portfolio:**
  1. **KI-Befähigung (`/ki-befaehigung/`):** Fundament, Infrastruktur, Prompting & interne Agenten-Workflows für Betriebe, die eigenes Inhouse-Know-how aufbauen wollen.
  2. **KI-Agenten (`/ki-agenten/`):** Produktisierte, API-gestützte autonome Agenten-Systeme (Done-for-you & maßgeschneidert) für Kernprozesse.

---

## 2. Seitenarchitektur & Content-Übersicht

### A. Startseite (`/`)
- **Hero & Leistungen:** Harmonische Einbindung des Website-Agenten als Speerspitze der autonomen Agenten-Systeme (organische Hinführung zum Dark-Showcase-Banner).
- **Showcase-Banner:** Prominenter Dark-Banner für **Der Website-Agent** (Souveräne Inhouse-Web-Infrastruktur für KMU: Inhalte jederzeit per Dialog anpassen, 100 % Firmeneigentum im Tresor, globale Edge-Auslieferung unter 0,5 s bei 0 € CMS-Kosten).
- **FAQ-Sektion:** 7 harmonisierte Kernfragen zu den beiden Säulen (Befähigung, Agenten-Architektur, Datenschutz, API-Integration) sowie zu digitaler Souveränität und AEO/GEO (Website-Agent) – 100 % synchron zwischen sichtbarem HTML und Schema.org `FAQPage`-Markup.

### B. KI-Befähigung (`/ki-befaehigung/`)
- Interaktiver Kurs-/Befähigungs-Konfigurator mit Live-Preisen und Phasenübersicht.
- Praxisnahe B2B-Anwendungsbeispiele (Sitzungsprotokolle, Excel-Abgleich, Web-Publishing per Dialog ohne Agentur-Tickets, Dokumentenprüfung, dezentrales Firmenwissen, Reportings).

### C. KI-Agenten Hub (`/ki-agenten/`)
- **Navigation (Globales Dropdown via `components.js`):** Schlankes 1-Spalten-Fokusmenü mit den Top 3 (*Der Website-Agent*, *B2B Lead Finder*, *CRM-Agent*) + Link zu allen Systemen.
- **Hero:** Breitere KMU-Positionierung ("Delegieren statt klicken" für Web-Publishing, Lead-Recherche & Fachsysteme).
- **Portfolio-Systeme (Direkt unter dem Hero platziert für maximale Conversion):**
  - **Cluster 1: Markt, Vertrieb & Web-Präsenz:**
    1. *Der Website-Agent* (Hervorgehobene Star-Kachel an Position 1, Inhouse-Pipeline, Dialog-Publishing, 0 € CMS)
    2. *B2B Lead Finder* (Case Study MICADO – Industrie-Entscheider)
    3. *Multimodale Lead Engine* (Case Study METEK – Ästhetik-Scoring)
    4. *Der Erstkontakt-Agent* (Outside-In / Dark-Card – als komplementäres Web-Gegenstück zum Website-Agenten)
  - **Cluster 2: Interne Prozesse & Fachsysteme:**
    5. *Der CRM-Agent* (Firmierung als übergreifender CRM-Agent, Case Study: Propstack / Zero-Click CRM)
    6. *Automatisierte Datenaggregation* (Controlling & ERP-Management-Briefing)
- **Featured Spotlight (Großes Dark-Showcase):** Der Website-Agent im zentralen Schaufenster (Inhouse-Pipeline, Firmeneigentum-Tresor, Edge-Auslieferung).
- **Architektur & Fundament:** 3-Ebenen-System der Integration & Paradigmenwechsel.
- **„Gut zu wissen“:** *Automation vs. Autonomie* & *Kontrollierte Autonomie* ans Ende direkt vor das Systemcheck-Kontaktformular positioniert.

### D. Deep-Dive Landingpages (Hub-and-Spoke unter `/ki-agenten/`)
1. **`/ki-agenten/b2b-lead-finder/`:**
   - *Case Study:* MICADO SMART ENGINEERING GmbH (Sondermaschinenbau & High-Tech).
   - 5-stufiger Maschinenraum: ICP-Definition, multimodales Web-Scraping, Qualifizierung, CRM-Übergabe.
2. **`/ki-agenten/case-premium-leads/`:**
   - *Case Study:* METEK GmbH (Architekturglas & Premium-Fassadenbau).
   - Multimodale Lead Engine mit visuellem Ästhetik-Scoring von Referenzobjekten & Architekten-Matching.
3. **`/ki-agenten/propstack-agent/`:**
   - *Case Study:* Immobilienwirtschaft & Propstack CRM.
   - Voice-to-CRM, Audio-Intake bei Objektbegehungen, automatische Exposé- und Stammdatenpflege.
4. **`/ki-agenten/externe-ki-agenten/`:**
   - *Fokus:* Der Erstkontakt-Agent für Machine-to-Machine (M2M) & WebMCP.
   - Reagiert auf die wachsende Bot-Präsenz (Cloudflare-Statistik: 57,5 % des Traffics), bietet maschinenlesbare Schnittstellen (ORF- / RIS-Austria-Konformität).
5. **`/ki-agenten/website-agent/`:**
   - *Fokus:* Der Website-Agent für souveräne Web-Infrastruktur & Inhouse-Pipeline.
   - *Hero:* Interaktive SVG-Pipeline-Visualisierung (3D-Perspektive: User-Dialog $\rightarrow$ Web-Agent Code/Gear $\rightarrow$ Live-Website mit Edge-Status) mit integriertem Inhouse-Pipeline-Header.
   - 5-stufiger Maschinenraum: 1. KI-Dialog $\rightarrow$ 2. Firmeneigener Tresor $\rightarrow$ 3. Edge-Netzwerk $\rightarrow$ 4. Live-Schaltung (< 60 s) $\rightarrow$ 5. Autonome Sofort-Indexierung via Echtzeit-Protokoll (Zero-Wait).
   - 100 % Firmeneigentum, Zero-Maintenance und native AEO/GEO-Maschinenlesbarkeit bei 0 € laufenden CMS-Infrastrukturkosten.

### E. Innovation Lab: `/x402/` (`x402/index.html`)
- Dedizierte Forschungs- und Experimentalseite für **autonome Machine-to-Machine-Payments** über den HTTP-402-Standard.
- Pay-per-Inference, autonome Agenten-Ökonomie und reine Lab-Darstellung (Grundlagenforschung & Proof of Concept ohne Community-Aufbau oder Vertriebs-CTAs).

### F. Kontakt & Impressum (`/kontakt/`, `/impressum/`, `/datenschutz/`)
- Modales Buchungs- und Anfrageformular, synchronisiert mit den Kernleistungen.
- Vollständige rechtliche Angaben und DSGVO-konforme Datenschutzerklärung.

---

## 3. Visuelles Design & UI-System
- **Glassmorphism:** Subtile Transparenzen, weiche Randbeleuchtungen (`backdrop-filter: blur`), dunkle Akzentkarten für M2M/x402.
- **Symmetrie & Baseline-Alignment:** Einheitliche Flexbox-Höhen und Button-Baselines im 6er-Grid.
- **Fokusierte Funnel:** Entfernung ablenkender Querverlinkungsboxen oberhalb von Kontakt-CTAs auf den Deep-Dive-Seiten.
- **Performance & Barrierefreiheit:**
  - Feste Bilddimensionen zur Vermeidung von Layout Shifts (CLS = 0).
  - ARIA-Labels für Klaro-Cookie-Consent-Banner und interaktive Modals.

---

## 4. Technisches Routing, SEO & AEO
- **301-Redirect-Kaskade (`_redirects`):**
  - `/ki-mitarbeiter/*` $\rightarrow$ `/ki-agenten/:splat` (301 Permanent Redirect).
  - Apex-Domain (`stefanwurzer.at/*`) $\rightarrow$ Canonical `www.stefanwurzer.at/:splat` (301!).
- **Meta-Tags & SERP-Optimierung:**
  - Alle Meta Descriptions sind auf 140–155 Zeichen kalibriert (erfüllt strenge Bing Webmaster Tools & Google Richtlinien).
- **Maschinenlesbarkeit (AEO / Agent-Readiness):**
  - `llms.txt` und `ai.txt` im Root-Verzeichnis enthalten alle aktuellen Leistungsbeschreibungen, Case Studies (MICADO, METEK, Propstack) und x402-Details im sauberen Markdown-Link-Format.
  - `sitemap.xml` und `robots.txt` sind vollständig mit allen `/ki-agenten/`- und `/x402/`-Routen synchronisiert.
- **Strukturierte Daten (JSON-LD):**
  - Schema.org-Typen `ProfessionalService`, `WebPage`, `CollectionPage`, `FAQPage` mit semantischen `knowsAbout`-Tags für Agentic Systems, B2B-Automatisierung und API-Workflows.
- **Suchmaschinen-Indexierung & IndexNow-Workflow:**
  - *Cloudflare Crawler Hints (IndexNow):* Vollautomatischer Push an Microsoft Bing und Yandex bei jedem Deployment aktiviert.
  - *Sitemap:* `https://www.stefanwurzer.at/sitemap.xml` (bei Google Search Console eingereicht).
  - *Prioritäre URLs für manuelle GSC-Prüfung:*
    1. `https://www.stefanwurzer.at/ki-agenten/website-agent/` (Erstindexierung)
    2. `https://www.stefanwurzer.at/` (Re-Indexierung: Showcase & FAQPage-Schema)
    3. `https://www.stefanwurzer.at/ki-agenten/` (Re-Indexierung: Karte 5 im Hub)
    4. `https://www.stefanwurzer.at/x402/` (Lab-Seite & M2M-Payments)

---

## 5. Strategischer Relaunch & Roadmap (In Arbeit: Der Wertschöpfungs-Prozess)

Aktuell befindet sich ein strategischer Paradigmenwechsel für die Startseite und Gesamtarchitektur in Vorbereitung (Prototypen abgesichert unter `preview-landingpage.html` und `/case-studies/index.html`, von Crawlern per `robots.txt` / noindex ausgeschlossen):

- **Ablösung des reinen KI-Fokus („KI durch die Hintertür“):**
  - Statt den Besucher mit Hype-Themen wie „KI-Befähigung“ oder isolierten „Agenten“ zu konfrontieren, wird das Unternehmen an seinen realen betriebswirtschaftlichen Schmerzpunkten abgeholt: *„Jedes Unternehmen hat 1–2 Engpässe. Wo reißt Ihre Wertschöpfungskette?“*
  - Die KI-Agenten werden nicht als Selbstzweck verkauft, sondern als modernste Problemlöser an den Schwachstellen der Kette.
  - Dach-Modell: **Der 7-Phasen-Prozess-Check** (Geförderte Geschäftsprozess-Analyse nach dem Standard der Wertschöpfungskette).
  - Geplante Ablösung der Navigation (`/ki-befaehigung/` und `/ki-agenten/`) durch die beiden großen Cluster:
    1. **Marktseitige Wertschöpfung (Phase 1 / Stufen 01–04):** Sichtbarkeit, Anfrage-Eingang, Bearbeitung & Vertrieb.
    2. **Operative Wertschöpfung (Phase 2 / Stufen 05–07):** Kundenbetreuung, Auftragsabwicklung & Betriebssteuerung.
- **Die 7 Phasen des Wertschöpfungs-Prozesses (Durchgängig deutsche 1-Wort-Begriffe):**
  - Die 7 Phasen beschreiben die betriebliche Realität jedes KMU:
    - *01 Sichtbarkeit:* Marktzugang, moderne Präsenz & Auffindbarkeit.
    - *02 Anfrage-Eingang:* Erstkontakt, Eingangskanäle & strukturierte Aufnahme.
    - *03 Anfrage-Bearbeitung:* Vorprüfung, technische Machbarkeit & ICP-Filterung.
    - *04 Vertrieb:* Abschluss, Terminnachbereitung & CRM-Synchronisation.
    - *05 Kundenbetreuung:* Kundenführung, Übergabe in die Projektbetreuung & proaktiver Informationsfluss.
    - *06 Auftragsabwicklung:* Materialfluss, Disposition, Lagerbestand & ERP-Abgleich.
    - *07 Betriebssteuerung:* Kennzahlen, Controlling & phasenübergreifende Datenaggregation.
  - **Systeme wirken phasenübergreifend (Keine 1:1-Agenten-Zuordnung):**
    - Ein entscheidendes Key Finding: Eine starre Zuteilung „1 Agent = 1 Phase“ ist fachlich falsch und fällt in die Insellösungs-Falle zurück.
    - Echte Systeme verbinden vorhandene Werkzeuge (Microsoft 365 + ERP + CRM) über Phasen hinweg zu einem durchgängigen Informationsfluss (z. B. wirkt die CRM- und Sprachintegration von Phase 02 über 03 und 04 bis zur Übergabe in 05).
    - Auf den Highway-Cards wird daher der **phasenübergreifende Informationsfluss** an den Schnittstellen hervorgehoben.
- **Reframing der Case Studies (Kausalitätsbeweis statt Menükarte):**
  - Die Case Studies sind **keine kaufbaren Einzelprodukte von der Stange**, sondern dienen als Beweis dafür, was nach der Engpass-Analyse im Check geschieht:
    - *Case 1:* **Immobilien-Vertrieb &bull; Außendienst** (*CRM- &amp; Formularwesen per Sprache* – Erfassung von unterwegs, automatisierte Formulare statt Word, keine Nacharbeit am Abend).
    - *Case 2:* **Industrie &bull; Sondermaschinenbau** (*Automatisierte B2B-Wunschkunden-Recherche* – Vorqualifizierung nach exaktem ICP statt manuellem Recherche-Blindflug).
    - *Case 3:* **Web-Infrastruktur &bull; KMU-Souveränität** (*Eigene Web-Pipeline statt Agentur-Abhängigkeit* – Dialoggeführte Änderungen im Haus ohne CMS-Wartungsverträge oder Ticket-Wartezeiten).
  - Auf der Startseite werden **keine konkreten Kundennamen (wie MICADO)** und **keine Nischen-Toolnamen (wie Propstack)** genannt.
  - Strikte Kausallogik: *Ausgangslage $\rightarrow$ Im Check aufgedeckter Engpass $\rightarrow$ Systemlösung $\rightarrow$ Betriebliche Wirkung*.
- **Visuelles Konzept & Prototyp (`preview-landingpage.html`):**
  - **Full-Width 3D-Highway (Cyber/Dark-Grid):** Vertikaler S-Kurven-Scrollfluss über die gesamte Bildschirmbreite.
  - **Durchgehender Venturi-/Flaschenhals-Kanal (`#highwayFlowSvg` & Kinetischer Licht-Puls):**
    - Statt dekorativer Einzel-Icons bilden zwei nahtlos verbundene Außenkonturen einen geschlossenen Prozesskanal von Phase 01 bis Phase 07 (mit sanftem Fade-in oben und Fade-out unten).
    - Auf freier Strecke läuft der Kanal weit und parallel; an jeder Phasen-Schnittstelle schnürt er sich exakt auf die Nadelöhr-Geometrie ein (konzentrische Darstellung im Zentrum: Punkt + kleine Nadelöhr-Ellipse + große Glow-Ellipse `.pedestal` in einheitlicher Leuchtstärke, Gold für 01–04, Cyan für 05–07).
    - Der animierte Licht-Puls (`#highwayPulse`) gleitet schnell über freie Strecken, bremst vor jeder Phasen-Engstelle spürbar ab, komprimiert und glüht im Nadelöhr kurz auf (Stau-/Reibungseffekt) und beschleunigt danach wieder in die nächste Phase.
  - **Flaschenhals-Abschluss (Textuelles Fazit ohne redundante Einzelgrafik):** Nach dem Fade-out von Phase 07 folgt direkt das textuelle Prinzip der Begrenzung (*„Wo liegt der Flaschenhals in Ihrem Betrieb?“*), da das visuelle Flaschenhals-Prinzip bereits im gesamten 7-Phasen-Flow verankert ist.
  - **Durchgängiger Dark-Canvas (Kein Schachbrett-Wechsel):** Statt harter Kontraste (weiß/dunkel) fließt die Seite auf einem einheitlichen Dark-Canvas (`#0a0c10` bis `#0d1117`) mit dezentem Dark-Glassmorphism, feinen Konturlinien (`rgba(255,255,255,0.08)`) und gezielten Gold-Akzenten.
  - **Invertiertes Logo (`logo_stefanwurzer_white.svg`):** Speziell für das Dark Theme optimierte Vektorgrafik mit reinweißem Text (`#FFFFFF`) für „stefanwurzer“ und edlem Mittelgrau (`#9CA3AF`) für „innovationservice“ (bewusst ohne Goldanteile im Schriftzug).
- **Beschlossene Navigations- & Inhalts-Architektur (Strategisches Konzeptpapier):**
  1. *Ultra-Lean Navigation:* Maximal reduziert auf nur zwei Elemente:
     - `LOGO` (links)
     - `Kontakt` (CTA-Button rechts)
     - Keine Zwischenmenüs, keine störenden Dropdowns – die Website funktioniert als geführter Gedankengang (wie ein Sales-Gespräch).
     - Dezent wandernder Datenpuls (`.nav-pulse-pixel`): Verläuft im Header zwischen Logo und Kontakt-Button als feiner Leuchtfunke, blendet sich via IntersectionObserver automatisch aus (`opacity: 0; animation-play-state: paused`), sobald der Besucher aus der Hero-Sektion nach unten scrollt (keine visuelle Ablenkung beim Lesen unterer Sektionen).
  2. *Case Studies als Kausalitätsbeweis statt Produktkatalog:*
     - Auf der Startseite verweisen 3 strukturierte B2B-Karten auf reale Problemlösungen nach dem Check.
     - Verlinkung auf die Sammelseite `/case-studies/`.
  3. *Schnittstellen & Microsoft-Hebel (Das Lösungsprinzip nach der Analyse):*
     - **Reframing im Sektions-Header:**
       - Eyebrow: `DAS LÖSUNGSPRINZIP NACH DER ANALYSE`
       - Headline: *„Bestehende Systeme verbinden statt neue Insellösungen aufzwingen.“*
       - Subline: *„Wenn wir im 7-Phasen-Prozess-Check einen Flaschenhals aufdecken, ersetzen wir nicht Ihre gewachsene Infrastruktur. Wir schließen manuelle Medienbrüche direkt zwischen Ihren vorhandenen Programmen – mit Microsoft 365 als vertrauter Steuerungs- und Informationsschicht.“*
     - Ablösung statischer Badges durch einen animierten, interaktiven System-Kosmos mit **Microsoft als zentralem betrieblichen Anker & Steuerungsebene** (Power BI, Teams, SharePoint).
     - Verbindungslinien als filigrane, runde Leuchtpunkt-Ströme (`stroke-linecap: round; stroke-dasharray: 1 8; animation: dotStream`) statt massiver Balken.
     - **Responsive Dual-Architektur (Desktop-Kosmos vs. Mobile System-Bridge):**
       - *Desktop (> 768px):* Großzügiges 2D-Netzwerk im SVG mit 9 Knoten, pulsierenden Leuchtpunkt-Strömen und dezentem Dimming unbeteiligter Systeme.
       - *Mobile (≤ 768px):* Native Mobile System-Bridge statt unleserlichem Minigraph. Oben eine daumenfreundliche, horizontal wischbare Touch-Pill-Leiste; in der Mitte ein fokussierter vertikaler Fluss (Microsoft-Anker $\rightarrow$ Leuchtpunkt-Stream $\rightarrow$ beteiligte Fachsystem-Karten in nativer 14px-Typografie); unten die strukturierte Engpass- & Wirkungskarte.
     - Demonstriert den **n-fachen Lösungsraum** über 4 exemplarische, synchron rotierende und klickbare Szenarien in reiner **Geschäfts- statt Techniksprache**:
       - *Szenario 01: Leads ohne Tipparbeit erfassen (1:1-Quick-Win)*
       - *Szenario 02: Kennzahlen auf Knopfdruck (2 Verbindungen)*
       - *Szenario 03: Aufträge & Lager synchronisieren (3 Verbindungen, Cyan)*
       - *Szenario 04: Dokumente ohne manuelle Ablage (1 Verbindung)*
  4. *Finaler CTA: Kompromisslose Ausrichtung auf das Einstiegsangebot („Hin-zu“-Framing):*
     - Ziel: **Terminvereinbarung für den 7-Phasen-Prozess-Check** (Geförderte Geschäftsprozess-Analyse).
     - Durchgängig positive „Hin-zu“-Kommunikation (was das Ergebnis ist, statt Verneinungen): *„Im 7-Phasen-Prozess-Check analysieren wir Ihre marktseitigen und operativen Informationsflüsse, lokalisieren die 1–2 entscheidenden Engpässe und liefern Ihnen einen konkreten, direkt umsetzbaren Fahrplan für Ihren Betrieb.“*
     - Unter dem Button steht fokussiert nur das einzelne Trust-Element: `✓ Offiziell WKO-gefördert (bis zu 80 %)`.
  5. *Footer-Architektur & Positionierungs-Claim:*
     - Claim: *„7-Phasen-Prozess-Check & Systemintegration für KMU. Engpässe in der marktseitigen und operativen Wertschöpfungskette aufdecken und beheben.“*
     - Links: Impressum, Datenschutz, AGB, Case Studies (`/#case-studies`), Kontakt (`/kontakt/`).
  6. *Live-Migration auf `/` (`index.html`) inkl. Begleitseiten (`/kontakt/`, `/agb/`, `/datenschutz/`, `/cookie-richtlinie/`):*
     - **Landingpage (`index.html`):** Vollständig auf das neue Dark-Theme, den 7-Phasen-Prozess-Check und das Lösungsprinzip Systemintegration migriert (inkl. Klaro Cookie Consent, Google Tag Manager `G-XL6E22PCJC`, `index, follow`, aktualisiertem `ProfessionalService` JSON-LD).
     - **`/kontakt/` (`kontakt/index.html` — Über mich & Kontakt):** Im einheitlichen Dark-Theme (`#0a0c10`) mit Ultra-Lean Navigation und neuem Global Footer gestaltet. Bewahrt das persönliche Vertrauens-Fundament (*„Über mich“* mit Porträt `/portrait_sw.jpg`, 17+ Jahre Erfahrung über die gesamte Wertschöpfungskette Marketing, Vertrieb, Planung und Produktion sowie Digital-Check-Erfahrung), kombiniert mit den 4 abgestimmten Fundament-Kacheln und dem Live-Kontaktformular (n8n-Webhook `stefanwurzer-lead` mit aktualisierten Themen-Optionen rund um den 7-Phasen-Prozess-Check und Systemintegration).
     - **Rechtliche Seiten (`/agb/index.html`, `/datenschutz/index.html`, `datenschutz.html`, `/cookie-richtlinie/index.html`):** Vollständig vom alten weißen `<site-nav>`/`components.js`-Layout gelöst und auf das neue Dark-Theme, die Ultra-Lean Navigation und den neuen Footer umgestellt. AGB § 2 (Leistungsumfang) und Datenschutzerklärung § 2 (Kontaktformular) sind inhaltlich auf den 7-Phasen-Prozess-Check und Systemintegration aktualisiert.
     - **301-Routing (`_redirects`), `sitemap.xml`, `robots.txt` & `llms.txt`:** Alle bisherigen Leistungs-, Agenten-, Team- und Lab-URLs (`/ki-befaehigung*`, `/ki-agenten*`, `/x402*`, `/team*`, `/ki-mitarbeiter*` etc.) leiten per direktem `301!` ohne Redirect-Ketten auf `/` um. Indexiert in `sitemap.xml` sind `/` und `/kontakt/`. Die Sammelseite `/case-studies/` bleibt vorerst im Hintergrund (`noindex` / `Disallow: /case-studies/`), bis weitere Cases ergänzt sind.
