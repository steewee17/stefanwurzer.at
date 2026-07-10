# Project State: stefanwurzer.at (B2A & KI-Agent Integration)

> [!NOTE]
> Dieses Dokument fasst alle strategischen und technischen Implementierungen zusammen, die in der vergangenen Projektphase umgesetzt wurden. Es dient als Fundament für zukünftige Weiterentwicklungen.

## 1. Neue Dienstleistungsarchitektur: KI-Befähigung (Feature Branch)
Die bisherige dreigeteilte Struktur (`markt.html`, `planung.html`, `umsetzung.html`) wurde zugunsten einer klaren, einheitlichen Dienstleistung abgelöst: **KI-Befähigung für KMU**. 
- **Das 3-Ebenen-Modell**: Arbeitsplatz (Ebene 1), Automation (Ebene 2) und Entscheidung (Ebene 3).
- **Zustand**: Implementiert auf dem Branch `feature/ki-befaehigung`. Die Startseite (`index.html`) und die globale Navigation (`components.js`) verweisen nun zentral auf die neue Seite `ki-befaehigung.html`. Die alten Seiten sind vorerst de-indexiert/isoliert.
- **Verticals**: Das System ist darauf vorbereitet, künftig spezifische "Verticals" (z.B. Immo-KI via Propstack) neben der generischen KI-Befähigung aufzunehmen.

## 2. Strategische Neuausrichtung: Agent-First (B2A)
Die Website wurde inhaltlich auf den Paradigmenwechsel **Business-to-Agent (B2A)** und **Answer Engine Optimization (AEO)** ausgerichtet.
- **Eigene Landingpage (`/agent-first`)**: Erklärt das B2A-Konzept als Manifest.
- **Visuelle Abstraktion**: Code-basierte SVG-Grafik zur Darstellung von *HUMAN UI* vs. *AGENT DATA*.

## 3. Der autonome "KI-Agent" (Walk the Talk)
Um das B2A-Konzept live zu beweisen, wurde ein nativer, intelligenter Strategie-Assistent auf der gesamten Website implementiert.

### Technische Architektur:
- **Frontend Widget (`agent-widget.js`)**: 
  - Entwicklung als **Vanilla JS Web Component (Shadow DOM)**. Dadurch ist das Widget zu 100% vor CSS-Interferenzen (wie dem `dlm-root` Reset) geschützt.
  - **Design**: "Terminal-Ästhetik" im Dark Mode mit der Programmier-Schriftart *JetBrains Mono*, um sich als technische KI-Instanz vom Rest der Website (`Instrument Sans`) abzuheben.
  - **Positionierung**: Der Trigger-Button (`KI-AGENT`) wurde exakt so platziert (`bottom: 84px`), dass er nicht mit dem permanenten Klaro-Consent-Banner kollidiert.
  - **Deployment**: Das Widget ist global auf den Seiten `index.html`, `agent-first.html`, `markt.html`, `planung.html` und `umsetzung.html` eingebunden.
- **Backend (n8n & Supabase)**:
  - Anbindung an einen bestehenden **n8n Webhook**, der Anfragen an Anthropic (Claude) weiterleitet.
  - Integration von strukturierten **CTA-Buttons** im Chat-Flow, die direkt vom Backend an das Frontend durchgereicht werden.

## 3. Knowledge Base (Supabase)
Das "Gehirn" des Agenten wird dynamisch aus einer Supabase-Datenbank (`tenants` Table, ID: `stefanwurzer-at`) gespeist.
- **Website-Scrape**: Der gesamte Text-Inhalt der Website (ca. 35.000 Zeichen) wurde extrahiert, bereinigt und in die Spalte `kb_content` geladen. Der Agent kennt somit jedes Detail der angebotenen Leistungen (Markt, Planung, Umsetzung).
- **System Prompt Engineering**: Der `system_prompt` wurde hart konfiguriert:
  - **Rolle**: Tritt als "KI-Agent" (nicht "B2A Agent") auf.
  - **Tonalität**: Streng professionell, B2B-Fokus, absolutes Verbot von Emojis.
  - **Definitionen**: Harte Anweisung, die Abkürzung "AEO" immer als *Answer Engine Optimization* und niemals als die zollrechtliche Bedeutung (*Authorized Economic Operator*) zu definieren.

## 4. Offene Potenziale & Zukünftige Roadmap
Aus den ursprünglich vier strategischen Ideen für die Website sind drei erfolgreich umgesetzt. Für zukünftige Projektphasen stehen noch folgende Hebel zur Verfügung:

> [!TIP]
> **Idee 2: Interaktiver "Agent-Readiness Score" (Lead-Magnet)**
> Entwicklung eines interaktiven Quiz (3-5 Fragen) direkt auf der Website. Nutzer können ihren Reifegrad testen und erhalten einen automatisierten Score im Tausch gegen ihre E-Mail-Adresse (Lead-Generierung für den AEO-Report).

- **Automatisierung der Knowledge Base**: Zukünftiger Aufbau eines n8n-Flows, der die Website bei Änderungen automatisch neu ausliest und in Supabase überschreibt.
- **Realer Use Case (Idee 4)**: Ausarbeitung und Integration einer detaillierten Case Study, die den ROI von "Agent-Ready" Infrastrukturen an einem echten Kundenbeispiel demonstriert.

## 5. Troubleshooting & Bugfixes (Letzter Stand)
- **AEO-Report Webhook**: Das JavaScript-Frontend (`index.html`) für den AEO-Report wurde so angepasst, dass es die verschachtelten JSON-Pfade (`sc.categories...`) aus dem n8n-Webhook sauber liest und die Sub-Scores grafisch korrekt darstellt.
- **Supabase Quota & Tokens**: Das AEO-Formular nutzt nun den dedizierten Token `website-embed` (statt des fehlerhaften `stefanwurzer-embed`). Dieser hat ein hartes Limit von 999 Anfragen/Monat in der Supabase-Datenbank.
- **GitHub PAT**: Ein neuer Personal Access Token (classic) mit `repo` Scope wurde für automatisierte Deployments integriert.
