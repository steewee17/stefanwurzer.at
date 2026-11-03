# Project State: stefanwurzer.at (7-Phasen-Prozess-Check, Website & Automation für KMU)

> [!NOTE]
> Dieses Dokument bildet den **aktuellen, verbindlichen Live-Stand der Website** ab (Stand: 3. November 2026, inkl. der zwei konkreten Produkt-Unterseiten **Website** `/website/` und **Automation** `/automation/` sowie der erweiterten globalen Navigation). Es dient als Single Source of Truth für alle Agenten, Sessions und Weiterentwicklungen.
> Ein Git-Sicherungs-Tag des alten weißen 2-Säulen-Stands existiert unter `pre-relaunch-2026-10`.

---

## 1. Strategische Kernpositionierung & Wording-Regeln

Die Website positioniert Stefan Wurzer als Spezialisten für **Geschäftsprozessanalyse (7-Phasen-Prozess-Check), moderne KI-lesbare Websites und KI-gestützte Prozessautomatisierung & Systemintegration** für KMU.

- **Methodischer Kern & Einstiegsangebot: Der „7-Phasen-Prozess-Check“ (`/`)**
  - Das zentrale Diagnose-Format der Website ist der **7-Phasen-Prozess-Check** bzw. ein 30-minütiges Kennenlerngespräch (gefördert unter dem WKO-Förderschwerpunkt [„Digitalisierung von Geschäftsprozessen“](https://foerderungen.wko.at/tirol/Digitalisierung), bis zu 80 % förderfähig).
  - Umsetzungsleistungen folgen organisch auf die Engpass-Diagnose im Check („Diagnose vor Therapie“) oder sind für Besucher mit bereits klarem Bedarf direkt über die beiden konkreten Produktangebote zugänglich.
- **Zwei konkrete Produkt- & Umsetzungsschwerpunkte entlang der 7 Phasen:**
  1. **Angebot 01 — Website (`/website/` • Phase 01 & 02: Marktzugang & Conversion):**
     - Fokus auf **Auffindbarkeit 2.0 (Sichtbarkeit für Mensch & KI-Suchsysteme)** wie ChatGPT, Gemini, Copilot und Perplexity durch strukturierte, maschinenlesbare Daten (`JSON-LD`, `/ai`, `llms.txt`, `.well-known/ard.json`, `/compare`, `WebMCP / MCP-ready`).
     - Fokus auf **Conversion (Phase 02)** statt statischer Web-1.0-Visitenkarte sowie **Ablöse veralteter, wartungsintensiver PHP-/WordPress-Altbestände** (keine Plugin-Sicherheitsrisiken).
     - Fokus auf **Digitale Souveränität (100 % Eigentum, 0 % Agentur-Abhängigkeit):** Volle Code- und Datenhoheit im Betrieb, Änderungen in Minuten selbst im Haus durchführbar, keine monatlichen Wartungspauschalen.
  2. **Angebot 02 — Automation (`/automation/` • Phase 03 bis 07: Prozesskette & Systemintegration):**
     - Folgt der 4-stufigen Kausalitäts-Formel:  
       `Problem: Zu viel Administration` $\rightarrow$ `Ursache: Medienbrüche und Informationsverluste` $\rightarrow$ `Lösung: Büroprozesse automatisieren` $\rightarrow$ `Technologie: Microsoft 365 · CRM · ERP · KI`.
     - **Stufe 01 (Vorhandene Ressourcen ausschöpfen):** Automatisierung wiederkehrender Büroprozesse im **Microsoft-365-Ökosystem (Power Automate, SharePoint, Teams, Outlook)** ohne zusätzliche Software-Lizenzen.
     - **Stufe 02 (Integrative System-Intelligenz):** Spezialisierte KI-Agenten und Assistenten auf einer abgesicherten, vorgelagerten Server-Schicht, konkret dargestellt anhand von 4 Praxis-Modulen:
       1. *Autonomer CRM-Agent per Chat & Sprache (Phase 04 — Vertrieb & Außendienst)*
       2. *B2B-Lead-Finder & Qualifizierungs-Agent (Phase 01–03 — Marktbearbeitung & Vorprüfung)*
       3. *Dispo-Assistent zur Lagerkosten-Optimierung (Phase 06 — Lager & Auftragsabwicklung)*
       4. *Systemübergreifender Recherche-Assistent (Phase 05 & 07 — Kundenführung & Steuerung)*
- **Hero-Messaging & Kernversprechen auf der Startseite:**
  - Eyebrow: `FÖRDERSCHWERPUNKT: DIGITALISIERUNG VON GESCHÄFTSPROZESSEN | DER 7-PHASEN-PROZESS-CHECK` (mit offiziellem WKO-Link).
  - Headline: *„Schnellere Auftragsabwicklung. Flaschenhälse aufdecken und beseitigen.“*
  - Subline: *„Wo verliert Ihr Betrieb zwischen Vertrieb, Büro und Ausführung täglich Zeit und Marge? Im geförderten 7-Phasen-Prozess-Check identifizieren wir die Bremsen in Ihren Abläufen und verbinden Ihre bestehende Software zu einem nahtlosen Informationsfluss.“*
  - **Verzicht auf „Durchsatz“:** Der Begriff *„Durchsatz“* bleibt im gesamten Außenauftritt getilgt und durch *„Schnellere Auftragsabwicklung“*, *„Flaschenhälse“*, *„Tempo“* und *„Zeit & Marge“* ersetzt.
- **Verbindliche Wording- & Tonalitäts-Regeln (Österreich / DACH):**
  - **KMU statt Mittelstand:** Ausnahmslos **KMU (Kleine und mittlere Unternehmen)**, **Betriebe** oder **Unternehmen** verwenden (kein bundesdeutsches „Mittelstand“).
  - **KI-Agenten statt KI-Mitarbeiter:** Wo auf Agenten-Technologie Bezug genommen wird, immer **KI-Agenten** oder **KI-Assistenten** verwenden.
  - **Positive „Hin-zu“-Sprache:** Fokus auf das Ergebnis (Klarheit, nahtloser Informationsfluss, Tempo, freie Kapazitäten, digitale Souveränität).
  - **Ansprache & Stil:** Verbindliches, wertschätzendes **„Sie / Ihr“**; ingenieursnah, prägnant, rhythmisch und bodenständig ohne Agentur-Hype-Slang.
  - **Ein-Personen-Unternehmen vs. Partnerschaft mit dem Kunden:** Wo Stefan über sich selbst spricht (z. B. im Über-mich-Text oder Formular-Hinweis: *„Ich melde mich persönlich innerhalb von 24 Stunden“*), steht **„Ich“**. Wo die gemeinsame Analyse und Umsetzung im Betrieb beschrieben wird (*„Im 7-Phasen-Prozess-Check analysieren wir …“*), steht das partnerschaftliche **„Wir“**.

---

## 2. Live-Seitenarchitektur & Sektionen im Detail

### A. Globale Dark-Glass-Navigation (`.live-nav-wrap` auf allen Seiten)
- **Struktur:**
  - Links: Invertiertes Logo `/logo_stefanwurzer_white.svg` (`height: 40px`, Mobile `32px`), verlinkt auf `/`.
  - Mitte (`.live-nav-links`): Die 3 Kern-Navigationspunkte mit aktivem Gold-Pill-Highlight (`.live-nav-link.active` / `aria-current="page"`):
    1. **`Prozess-Check`** (`/`)
    2. **`Website`** (`/website/`)
    3. **`Automation`** (`/automation/`)
  - Rechts: Pill-Button **`Kontakt`** (`.live-nav-cta`), der auf allen Seiten auf **`/kontakt/`** verlinkt.
  - Bewusst **ohne** wanderndes Puls-Pixel (`.nav-track` entfernt), da die Navigationsleiste mit den 3 Angebots-Links klar und aufgeräumt strukturiert ist.
  - Mobile (`≤ 720px`): Zweizeiliges Flex-Layout innerhalb der Sticky-Navbar ohne horizontales Wischen (`order: 3; width: 100%` für `.live-nav-links`).

---

### B. Startseite (`/`, `index.html` & synchron `preview-landingpage.html`)
Die Startseite führt den Besucher in einem durchgängigen Dark-Canvas (`#0a0c10` / `#0c1017`) durch 6 logisch aufeinander aufbauende Stufen:

1. **Sektion 1 — Hero & Der 7-Phasen-Prozess-Check (`#prozess`, 3D-Highway & Sanduhr-Kanal):**
   - **Die 7 Phasen der Wertschöpfungskette:**
     - *01 • Marktzugang (Marktseitig):* **Sichtbarkeit**
     - *02 • Erstkontakt (Marktseitig):* **Anfrage-Eingang**
     - *03 • Vorprüfung (Marktseitig):* **Anfrage-Bearbeitung**
     - *04 • Abschluss (Marktseitig):* **Vertrieb**
     - *05 • Kundenführung (Operativ):* **Kundenbetreuung**
     - *06 • Produktion / Dienstleistung (Operativ):* **Auftragsabwicklung**
     - *07 • Führung & KPIs (Operativ):* **Betriebssteuerung**
   - **Fazit unter dem Flow (`#flaschenhals`):** *„Das Prinzip der Begrenzung — Wo liegt der Flaschenhals in Ihrem Betrieb?“* mit Anker-CTA `Gespräch vereinbaren ↓`.
2. **Sektion 1B — Zwei konkrete Angebotsschwerpunkte entlang der 7 Phasen (`#angebote`):**
   - Verbindet die 7-Phasen-Diagnose direkt mit den zwei konkreten Leistungsbereichen:
     - **Angebot 01 • Website (Phase 01 & 02):** *Websites für Mensch & KI-Suche. Souverän im Betrieb.* $\rightarrow$ Link auf `/website/`
     - **Angebot 02 • Automation (Phase 03 bis 07):** *Büroprozesse automatisieren. Medienbrüche beenden.* $\rightarrow$ Link auf `/automation/`
3. **Sektion 2 — Das Lösungsprinzip nach der Analyse (Die betriebliche Informationsschicht):**
   - Headline: *„Bestehende Systeme verbinden statt neue Insellösungen aufzwingen.“*
   - Interaktiver 9-Knoten-Netzwerkgraph (Desktop) bzw. Zero-Layout-Shift Mobile-Bridge (Smartphone) mit 4 Szenarien rund um den Microsoft-365-Anker (Teams, Power BI, SharePoint).
4. **Sektion 3 — Bodenständig & Belastbar (Warum punktuelle Tools scheitern):**
   - 3 Karten im Dark-Glass-Design: *01 Keine neuen Insellösungen*, *02 Kontrollierte Autonomie*, *03 100 % Datenhoheit*.
5. **Sektion 4 — Kausalitätsbeweis aus der Praxis (`#case-studies`):**
   - 3 anonymisierte Vorher-Nachher-Cases (*Ausgangslage $\rightarrow$ Engpass $\rightarrow$ Lösung $\rightarrow$ Wirkung*) inkl. Direktverlinkung auf `/automation/` (Case 1 & 2) bzw. `/website/` (Case 3).
6. **Sektion 5 — 3-Schritte-Ablauf & Eingebettetes Kontaktformular (`#kontakt`):**
   - **3-Schritte-Dreiklang „Vom Prozess-Check zur gelösten Engstelle“:** *Schritt 01 Diagnose (7-Phasen-Prozess-Check & Potenzialbericht)*, *Schritt 02 Architektur (Integrationskonzept)*, *Schritt 03 Wirkung (Umsetzung & laufender Betrieb)*.
   - **2-spaltiges Kontaktformular darunter:** Angebunden an den n8n-Webhook `https://steewee.app.n8n.cloud/webhook/stefanwurzer-lead` mit `source: 'stefanwurzer.at/startseite'`.
   - Dropdown (`#f-leistung`) mit 4 kompakten, mobilfreundlichen Optionen (ohne Klammerzusätze):
     1. `7-Phasen-Prozess-Check`
     2. `Website`
     3. `Automation`
     4. `Allgemeines Kennenlerngespräch`

---

### C. Produkt-Unterseite 01: Website (`/website/`, `website/index.html`)
- **Hero (`#ph`):**
  - Eyebrow: `Leistungsschwerpunkt 01 • Marktzugang & Conversion (Phase 01 & 02)`
  - Headline: *„Websites für Mensch und KI-Suche. Souverän im eigenen Betrieb.“*
  - Rechts: Kompaktes Architektur-Panel (*Phase 01: Sichtbarkeit & Marktzugang*, *Phase 02: Erstkontakt & Conversion*, *Technik: Ablöse anfälliger Altbestände*, *Eigentum: 100 % Digitale Souveränität*).
- **Sektion 2 — Ausgangslage im KMU-Markt:**
  - *Warum gewachsene Websites aus den 00er- und 10er-Jahren heute doppelt bremsen:* 3 Diagnose-Karten (*Engpass 01: Web-1.0-Struktur / fehlende Conversion*, *Engpass 02: PHP & Plugin-Anfälligkeit / WordPress-Wartungsfalle*, *Engpass 03: KI-Blindflug*).
- **Sektion 3 — Die 2 Kernhebel (`#hebel`):**
  - **Hebel 01: Auffindbarkeit 2.0 — Sichtbarkeit für Mensch und KI-Systeme** (inkl. Tech-Chips `JSON-LD Schema`, `/ai & llms.txt`, `Agentic Resource Discovery (ARD)`, `/compare & Fakten-Struktur`, `WebMCP / MCP-ready`).
  - **Hebel 02: Digitale Souveränität — 100 % Eigentum, 0 % Agentur-Abhängigkeit** (volle Code-Kontrolle, direkte Handlungsfähigkeit im Haus in wenigen Minuten, keine monatlichen Wartungspauschalen).
  - Darunter das **Leitmotiv-Zitat** als Gold-Callout-Box.
- **Sektion 4 — Teil Ihrer Wertschöpfungskette:**
  - Zeigt den nahtlosen Übergang von Phase 01 (Gefunden werden) über Phase 02 (Strukturierte Conversion) bis zur Übergabe an Microsoft 365 & CRM (Phase 03–04).
- **Sektion 5 — Eingebettetes Kontaktformular (`#formular`):**
  - Vorausgewählte Option `Website`, Webhook `source: 'stefanwurzer.at/website'`.

---

### D. Produkt-Unterseite 02: Automation (`/automation/`, `automation/index.html`)
- **Hero (`#ph`):**
  - Eyebrow: `Leistungsschwerpunkt 02 • Prozesskette & Systemintegration (Phase 03 bis 07)`
  - Headline: *„Büroprozesse automatisieren. Medienbrüche dauerhaft beenden.“*
  - Rechts: Visuelles **4-Stufen-Kausalitäts-Panel**:
    - `01 • Problem im Alltag:` **Zu viel Administration**
    - `02 • Eigentliche Ursache:` **Medienbrüche und Informationsverluste**
    - `03 • Lösung:` **Büroprozesse automatisieren**
    - `04 • Verbundene Technologie:` **Microsoft 365 · CRM · ERP · KI**
- **Sektion 2 — Zwei Ausbaustufen der Automatisierung:**
  - **Stufe 01 (Vorhandene Ressourcen nutzen):** *Büroprozesse im Microsoft-365-Ökosystem automatisieren (Power Automate, SharePoint, Teams)* — vorhandene Lizenzen voll ausschöpfen.
  - **Stufe 02 (Integrative System-Intelligenz):** *Spezialisierte KI-Agenten & Assistenten zwischen CRM, ERP und Datenorten* — vorgelagerte Server-Architektur für unstrukturierte Eingaben (Sprache, Chat, Dokumente).
- **Sektion 3 — 4 Konkrete Praxis-Module (`#praxis`):**
  1. **Modul 01 (Phase 04 • Vertrieb & Außendienst):** *Autonomer CRM-Agent per Chat & Sprache*
  2. **Modul 02 (Phase 01–03 • Marktbearbeitung & Vorprüfung):** *B2B-Lead-Finder & Qualifizierungs-Agent*
  3. **Modul 03 (Phase 06 • Lager & Auftragsabwicklung):** *Dispo-Assistent zur Lagerkosten-Optimierung*
  4. **Modul 04 (Phase 05 & 07 • Kundenführung & Steuerung):** *Systemübergreifender Recherche-Assistent*
- **Sektion 4 — Technische Leitplanken:**
  - *Prinzip 01: Keine neuen Insellösungen*, *Prinzip 02: Kontrollierte Autonomie (Closed Loops)*, *Prinzip 03: 100 % Datenhoheit & DSGVO*.
- **Sektion 5 — Eingebettetes Kontaktformular (`#formular`):**
  - Vorausgewählte Option `Automation`, Webhook `source: 'stefanwurzer.at/automation'`.

---

### E. Über mich & Kontakt (`/kontakt/`, `kontakt/index.html`) sowie Rechtliche Seiten (`/agb/`, `/datenschutz/`, `/cookie-richtlinie/`)
- Alle Seiten teilen die identische globale Dark-Glass-Navigation (`Prozess-Check` · `Website` · `Automation` · `[Kontakt]`), das einheitliche Klaro-Cookie-Consent-Design (Gold-OK-Button `var(--gold)`) und den schlanken globalen Footer ohne Link-Duplikationen:
  - Claim: *„7-Phasen-Prozess-Check, Website & Automation für KMU. Engpässe in der marktseitigen und operativen Wertschöpfungskette aufdecken und beheben.“*
  - Links: `Impressum` · `Datenschutz` · `AGB` · `Kontakt`.

---

## 3. Mobile-First, Typografie & Technische Leitplanken

- **Horizontale Fixierung auf Mobilgeräten (Zero Horizontal Scroll):**
  - Auf allen Seiten ist `html, body, section, footer { overflow-x: clip; max-width: 100%; }` gesetzt; alle Grid-Kinder besitzen `min-width: 0` und Formularfelder nutzen auf Mobile `font-size: 16px`.
- **0 Render-Blocking CSS & Inline-SVGs:**
  - `index.html`, `website/index.html` und `automation/index.html` betten sämtliche Styles und Icons direkt inline ein (0 externe Render-Blocking-Requests).
- **SEO, GEO/AEO, Maschinenlesbarkeit & Agentic Browsing (4/4):**
  - **JSON-LD:** `ProfessionalService` + `OfferCatalog` auf `index.html` sowie dedizierte `Service`-Schemata auf `/website/` und `/automation/`.
  - **`llms.txt`, `ai.txt`, `.well-known/ard.json` & `.well-known/ai-catalog.json`:** Dokumentieren strukturiert den 7-Phasen-Prozess-Check sowie die beiden Produktbereiche **Website** (`/website/`) und **Automation** (`/automation/`).
  - **`sitemap.xml`:** Umfasst `/`, `/website/`, `/automation/` und `/kontakt/`.
