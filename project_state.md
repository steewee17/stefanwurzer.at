# Project State: stefanwurzer.at (7-Phasen-Prozess-Check & Systemintegration für KMU)

> [!NOTE]
> Dieses Dokument bildet den **aktuellen, verbindlichen Live-Stand der Website** ab (Stand: 28. Oktober 2026, nach dem vollständigen Dark-Theme-Relaunch). Es dient als Single Source of Truth für alle Agenten, Sessions und Weiterentwicklungen.
> Ein Git-Sicherungs-Tag des alten weißen 2-Säulen-Stands existiert unter `pre-relaunch-2026-10`.

---

## 1. Strategische Kernpositionierung & Wording-Regeln

Die Website positioniert Stefan Wurzer als Spezialisten für **Geschäftsprozessanalyse, Systemintegration und KI-gestützte Automatisierung** für KMU.

- **Primäres Einstiegsangebot: Der „7-Phasen-Prozess-Check“**
  - Auf der Website werden **keine isolierten Tool-Pakete oder Agenten von der Stange** verkauft („KI durch die Hintertür“).
  - Das exklusive Conversion-Ziel der gesamten Website ist die **Anfrage für den 7-Phasen-Prozess-Check** bzw. ein 30-minütiges Kennenlerngespräch (gefördert unter dem WKO-Förderschwerpunkt [„Digitalisierung von Geschäftsprozessen“](https://foerderungen.wko.at/tirol/Digitalisierung), bis zu 80 % förderfähig).
  - Umsetzungsleistungen (die eigentliche Systemintegration und Automatisierung) folgen organisch auf die Engpass-Diagnose im Check („Diagnose vor Therapie“).
- **Hero-Messaging & Kernversprechen:**
  - Eyebrow: `FÖRDERSCHWERPUNKT: DIGITALISIERUNG VON GESCHÄFTSPROZESSEN | DER 7-PHASEN-PROZESS-CHECK` (ohne vorangestellten Punkt, mit offiziellem WKO-Link).
  - Headline: *„Schnellere Auftragsabwicklung. Flaschenhälse aufdecken und beseitigen.“*
  - Subline: *„Wo verliert Ihr Betrieb zwischen Vertrieb, Büro und Ausführung täglich Zeit und Marge? Im geförderten 7-Phasen-Prozess-Check identifizieren wir die Bremsen in Ihren Abläufen und verbinden Ihre bestehende Software zu einem nahtlosen Informationsfluss.“*
  - **Verzicht auf „Durchsatz“:** Der Begriff *„Durchsatz“* wurde im gesamten Außenauftritt getilgt (im KMU-Alltag zu abstrakt/industriell) und durch *„Schnellere Auftragsabwicklung“*, *„Flaschenhälse“*, *„Tempo“* und *„Zeit & Marge“* ersetzt.
- **Verbindliche Wording- & Tonalitäts-Regeln (Österreich / DACH):**
  - **KMU statt Mittelstand:** Ausnahmslos **KMU (Kleine und mittlere Unternehmen)**, **Betriebe** oder **Unternehmen** verwenden (kein bundesdeutsches „Mittelstand“).
  - **KI-Agenten statt KI-Mitarbeiter:** Wo auf Agenten-Technologie Bezug genommen wird, immer **KI-Agenten** verwenden.
  - **Positive „Hin-zu“-Sprache:** Fokus auf das Ergebnis (Klarheit, nahtloser Informationsfluss, Tempo, freie Kapazitäten) statt auf negative Abgrenzungen.
  - **Ansprache & Stil:** Verbindliches, wertschätzendes **„Sie / Ihr“**; ingenieursnah, prägnant, rhythmisch und bodenständig ohne Agentur-Hype-Slang.
  - **Ein-Personen-Unternehmen vs. Partnerschaft mit dem Kunden:** Wo Stefan über sich selbst spricht (z. B. im Über-mich-Text oder Formular-Hinweis: *„Ich melde mich persönlich innerhalb von 24 Stunden“*), steht **„Ich“**. Wo die gemeinsame Analyse im Betrieb beschrieben wird (*„Im 7-Phasen-Prozess-Check analysieren wir …“*), steht das partnerschaftliche **„Wir“**.

---

## 2. Live-Seitenarchitektur & Sektionen im Detail

### A. Startseite (`/`, `index.html` & synchron `preview-landingpage.html`)
Die Startseite führt den Besucher in einem einzigen, durchgängigen Dark-Canvas (`#0a0c10` / `#0c1017`) durch 5 logisch aufeinander aufbauende Stufen:

1. **Ultra-Lean Dark Glass Navigation (`.live-nav-wrap`, Höhe `76px`):**
   - Links: Invertiertes Logo `/logo_stefanwurzer_white.svg` (`height: 40px`, Mobile `34px`).
   - Mitte (nur Desktop): Subtile Daten-Spur (`.nav-track`) mit wanderndem Leuchtpixel (`.nav-pulse-pixel`), das sich per `IntersectionObserver` automatisch pausiert/ausblendet, sobald der Nutzer aus dem Hero scrollt.
   - Rechts: Pill-Button **`Kontakt`** (`13px`, `padding: 10px 24px`), der auf allen Seiten zwingend auf die Unterseite **`/kontakt/`** verlinkt.
2. **Sektion 1 — Hero & Der 7-Phasen-Prozess-Check (3D-Highway & Sanduhr-Kanal):**
   - **Die 7 Phasen der Wertschöpfungskette:**
     - *01 • Marktzugang (Marktseitig):* **Sichtbarkeit**
     - *02 • Erstkontakt (Marktseitig):* **Anfrage-Eingang**
     - *03 • Vorprüfung (Marktseitig):* **Anfrage-Bearbeitung**
     - *04 • Abschluss (Marktseitig):* **Vertrieb**
     - *05 • Kundenführung (Operativ):* **Kundenbetreuung**
     - *06 • Produktion / Dienstleistung (Operativ):* **Auftragsabwicklung** (optisch zu 100 % einheitlich mit Phase 05 und 07, kein Sonder-Highlighting)
     - *07 • Führung & KPIs (Operativ):* **Betriebssteuerung**
   - **Phasenübergreifender Fluss:** Jede Phase zeigt die typische Engpass-Frage und darunter die Box *„Phasenübergreifender Fluss“* (keine isolierte 1:1-Tool-Zuordnung).
   - **Sanduhr-Geometrie (`#highwayFlowSvg`) & Kinetischer Licht-Puls (`#highwayPulse`):**
     - Alle 7 Knoten sitzen sowohl am Desktop als auch auf Mobile (`grid-row: 1` + `ResizeObserver`) exakt mittig auf Höhe ihrer jeweiligen Card.
     - Das SVG nutzt einen exakten 1:1-Pixelmaßstab (`flowSvg.style.height = svgH + 'px'` und `gradientUnits="userSpaceOnUse"` mit präzisen Prozent-Stops).
     - Die äußeren Sanduhr-Linien sind bei Phase 01 (oben) und Phase 07 (unten) zu 100 % symmetrisch zu ihren inneren Armen (`topFlare` / `botFlare`), bleiben über 86 % der Armlänge kräftig sichtbar und faden genau am Mittelpunkt zwischen zwei Phasen kurz und weich aus und wieder ein.
   - **Fazit unter dem Flow (`#flaschenhals`):** *„Das Prinzip der Begrenzung — Wo liegt der Flaschenhals in Ihrem Betrieb?“* mit Anker-CTA `Gespräch vereinbaren ↓` (scrollt direkt zu `#kontakt` auf derselben Seite).
3. **Sektion 2 — Das Lösungsprinzip nach der Analyse (Die betriebliche Informationsschicht):**
   - Eyebrow: `Das Lösungsprinzip nach der Analyse • Die betriebliche Informationsschicht`
   - Headline: *„Bestehende Systeme verbinden statt neue Insellösungen aufzwingen.“*
   - Mission-Subline: *„Wir beseitigen Informationsengpässe zwischen Vertrieb, Büro und operativer Leistungserbringung: Wenn im 7-Phasen-Prozess-Check ein Flaschenhals aufgedeckt wird, ersetzen wir nicht Ihre gewachsene Infrastruktur – wir verbinden Ihre vorhandenen Programme über Microsoft 365 zu einer zentralen betrieblichen Informationsschicht, damit die richtigen Informationen dort bereitstehen, wo Entscheidungen getroffen werden.“*
   - **Einheitliches Farbkonzept (Warm Gold & Schiefergrau):** Kein Blau-/Cyan-Ausreißer mehr. Inaktive Knoten sind dezent abgedunkelt, der zentrale Microsoft-Anker und die jeweils aktiven Systeme/Datenströme leuchten konsistent in warmem Gold (`--gold` / `--gold-light`).
   - **Alle 9 Knoten im Desktop-Netzwerk aktiv eingebunden:**
     - *Szenario 01 (Leads ohne Tipparbeit erfassen):* Microsoft Teams $\leftrightarrow$ `HubSpot • Salesforce` & `Branchen-CRM`.
     - *Szenario 02 (Kennzahlen auf Knopfdruck):* Microsoft Power BI $\leftrightarrow$ `SAP S/4HANA & B1`, `Odoo ERP` & `DATEV • Buchhaltung`.
     - *Szenario 03 (Aufträge & Lager synchronisieren):* Microsoft Power BI & Teams $\leftrightarrow$ `Odoo ERP`, `xentral • Weclapp` & `SQL • REST-APIs`.
     - *Szenario 04 (Dokumente ohne manuelle Ablage):* Microsoft 365 SharePoint $\leftrightarrow$ `Branchen-CRM` & `DATEV • Buchhaltung`.
   - **Mobile Darstellung (Ansatz 1 — 2×2 Grid & Zero-Layout-Shift Bridge):**
     - Auf Smartphones (`≤ 768px`) werden die 4 Szenario-Buttons als übersichtliches **2×2-Raster** dargestellt (kein horizontales Wischen).
     - Darunter zeigt die kompakte `.mobile-bridge-stage` den Microsoft-Anker und immer **exakt 2 nebeneinanderliegende Ziel-System-Chips** (`.mb-target-chip`), gefolgt von der Engpass-&-Wirkung-Box (`.scenario-desc-card` mit sauber umbrechendem `.desc-badge`). Dadurch ändert sich die Höhe beim 6,5-Sekunden-Wechsel um **0 Pixel** (kein Springen der Seite beim Lesen!).
4. **Sektion 3 — Bodenständig & Belastbar (Warum punktuelle Tools scheitern):**
   - 3 Karten im Dark-Glass-Design mit Gold-Top-Border: *01 Keine neuen Insellösungen*, *02 Kontrollierte Autonomie*, *03 100 % Datenhoheit*.
5. **Sektion 4 — Kausalitätsbeweis aus der Praxis (`#case-studies`):**
   - 3 anonymisierte Vorher-Nachher-Cases nach der Struktur *Ausgangslage $\rightarrow$ Engpass $\rightarrow$ Lösung $\rightarrow$ Wirkung*:
     1. *Immobilien-Vertrieb • Außendienst:* CRM- & Formularwesen per Sprache
     2. *Industrie • Sondermaschinenbau:* Automatisierte B2B-Wunschkunden-Recherche
     3. *Web-Infrastruktur • KMU-Souveränität:* Eigene Web-Pipeline statt Agentur-Abhängigkeit
6. **Sektion 5 — 3-Schritte-Ablauf & Eingebettetes Kontaktformular (`#kontakt`):**
   - **3-Schritte-Dreiklang „Vom Prozess-Check zur gelösten Engstelle“ (`.process-roadmap-wrap`):**
     - *Schritt 01 • Diagnose:* **7-Phasen-Prozess-Check & Potenzialbericht** (Vor-Ort- oder Online-Analyse aller 7 Phasen inkl. schriftlichem Potenzialbericht zu Engpässen, Ursachen und klaren Prioritäten; bis zu 80 % WKO-gefördert).
     - *Schritt 02 • Architektur:* **Integrationskonzept** (Konkreter technischer Bauplan für CRM, ERP, Microsoft 365 ohne Systemwechsel).
     - *Schritt 03 • Wirkung:* **Umsetzung & laufender Betrieb** (Schrittweise Implementierung, Team-Einschulung und zuverlässiger Betrieb).
   - **2-spaltiges Kontaktformular darunter:** Angebunden an den n8n-Webhook `https://steewee.app.n8n.cloud/webhook/stefanwurzer-lead` mit `source: 'stefanwurzer.at/startseite'`.
   - Links: Eyebrow `GESCHÄFTSPROZESS-ANALYSE`, Headline *„Den Flaschenhals im Betrieb aufdecken.“*, Förder-Badge `✓ WKO-gefördert (bis zu 80 %)`, Direktkontakte sowie eine persönliche **Vertrauens-Karte mit Porträt (`/thumbnail_sw.jpg`)**: *„Stefan Wurzer — 17+ Jahre Praxis in Marketing, Vertrieb, Planung & Produktion • Über mich →“* (`/kontakt/#ueber`).
   - Rechts: Formular mit reduziertem Dropdown (`#f-leistung`) mit exakt 2 klaren Optionen:
     1. `7-Phasen-Prozess-Check`
     2. `Allgemeines Kennenlerngespräch`

---

### B. Über mich & Kontakt (`/kontakt/`, `kontakt/index.html`)
- **Konsistentes Dark-Theme (`#0a0c10`)** mit identischer Ultra-Lean Navigation (`76px`) und identischem Footer.
- **Hero (`#ph`):**
  - Links: Eyebrow `Über mich & Kontakt`, Headline `30 Minuten. Direkt [zum Punkt. / zu mehr Klarheit. / zum Engpass-Check. / zur passenden Lösung. / zum konkreten Fahrplan.]`, CTA-Button `7-Phasen-Prozess-Check anfragen →` (scrollt zu `#formular`).
  - Rechts: Karte `Direkt erreichbar` mit E-Mail, Telefon, Adresse (`Unterassling 55 · 9911 Assling · Tirol`) und Punkt 4 schlicht **`WKO-zertifizierter Unternehmensberater`** (ohne Förder-Zusatz).
- **Sektion „Über mich“ (`#ueber`):**
  - Porträt `/portrait_sw.jpg` + biografischer Text (17+ Jahre Erfahrung in Handwerk, Industrie, Handel und Beratung; Marketing, Vertrieb, Planung und Produktion; Digital Check) komplett ruhig in **Regular (`font-weight: 400`)** ohne Fettdruck (`<strong>` im Fließtext entfernt).
  - Darunter die 4 Fundament-Kacheln (*7-Phasen-Prozess-Check*, *Bestehende Systeme verbinden*, *Pragmatische Umsetzung*, *Spürbare Entlastung*).
- **Sektion Kontaktformular (`#formular`):**
  - 2-spaltiges Formular (identisches Dropdown mit `7-Phasen-Prozess-Check` und `Allgemeines Kennenlerngespräch`, Webhook `source: 'stefanwurzer.at/kontakt'`) + UID/IBAN/BIC-Angaben.

---

### C. Globaler Footer & Rechtliche Seiten (`/agb/`, `/datenschutz/`, `/cookie-richtlinie/`)
- **Footer-Wording (auf allen Seiten identisch):**
  - Claim: *„7-Phasen-Prozess-Check & Systemintegration für KMU. Engpässe in der marktseitigen und operativen Wertschöpfungskette aufdecken und beheben.“*
  - Links (alle einheitlich in dezentem Grau `rgba(255,255,255,.45)` ohne goldene Eigen-Hervorhebung): `Impressum` (externer WKO-ECG-Link) · `Datenschutz` · `AGB` · `Case Studies` · `Kontakt`.
- **Rechtliche Unterseiten:**
  - `/agb/index.html`, `/datenschutz/index.html` (plus Root-Fallback `datenschutz.html`) und `/cookie-richtlinie/index.html` sind komplett auf das Dark-Theme, die `76px` Ultra-Lean Navigation und das neue Wording umgestellt.

---

## 3. Mobile-First, Typografie & Technische Leitplanken

- **Typografie-Feinschliff (Gold-Eyebrows):**
  - Alle goldenen Eyebrows, Phasen-Tags und Monospace-Labels nutzen `font-weight: 400` (Regular) und `--gold-light` (`#E0C068`) für gestochen scharfe Lesbarkeit auf dunklem Hintergrund.
- **Horizontale Fixierung auf Mobilgeräten (Zero Horizontal Scroll):**
  - Auf allen Seiten (`index.html`, `kontakt/index.html`, `agb/index.html`, `datenschutz/index.html`, `cookie-richtlinie/index.html`, `style.css`) ist `html, body, section, footer { overflow-x: clip; max-width: 100%; }` gesetzt.
  - Durch `overflow-x: clip` statt `hidden` auf `html, body` ist horizontales Wischen auf iOS Safari und Android Chrome zu 100 % unterbunden, während `position: sticky` der Navbar uneingeschränkt funktioniert.
  - Alle CSS-Grid-Kinder besitzen `min-width: 0`, Auto-Fit-Grids nutzen `minmax(min(100%, 280px), 1fr)` und Formularfelder haben auf Mobile `font-size: 16px` (verhindert den automatischen iOS-Input-Zoom).
- **SEO, GEO/AEO & Routing:**
  - **JSON-LD (`index.html`):** Kombiniertes `ProfessionalService`-Schema mit `OfferCatalog` (1. *7-Phasen-Prozess-Check*, 2. *Systemintegration & Prozessautomatisierung*) für optimale Erfassung durch Google und KI-Suchmaschinen (Perplexity, ChatGPT, Copilot).
  - **`llms.txt`, `sitemap.xml`, `robots.txt` & `_redirects`:** Vollständig mit der neuen Architektur synchronisiert. Alte URLs (`/ki-befaehigung*`, `/ki-agenten*`, `/x402*`, `/team*`, `/ki-mitarbeiter*`) leiten per direktem `301!` auf `/` um.
