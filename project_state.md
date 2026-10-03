# Project State: stefanwurzer.at (KI-Agenten & KMU-Befähigung)

> [!NOTE]
> Dieses Dokument bildet den **aktuellen, verbindlichen Live-Stand der Website** ab (Stand: Oktober 2026). Es dient als Single Source of Truth für alle Agenten, Sessions und Weiterentwicklungen.

---

## 1. Strategische Kernpositionierung & Wording-Regeln

Die Website positioniert Stefan Wurzer als unabhängigen Experten für **autonome KI-Agenten, Closed-Loop-Systeme und technologische KMU-Befähigung**.

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
- **Hero-Bereich:** Dynamischer Word-Rotator („Vertrieb“, „Auftragsabwicklung“, „Analyse“, „Prozesse“) mit klarem Leistungsversprechen.
- **Showcase-Banner:** Prominenter Dark-Banner für **Der Website-Agent** (Souveräne Inhouse-Web-Infrastruktur für KMU: Änderungen per Dialog im Minutentakt, 100 % Firmeneigentum im Git-Tresor, globale Edge-Auslieferung unter 0,5 s bei 0 € CMS-Kosten).
- **Interaktiver ROI-Rechner:** Ermöglicht KMU die Berechnung von Zeitersparnis und ROI durch Agenten-Einsatz.
- **FAQ-Sektion:** Proaktive Klärung von Qualitätsfragen (Kein Spam, geschlossene IT-Systeme, DSGVO-Konformität).

### B. KI-Befähigung (`/ki-befaehigung/`)
- Interaktiver Kurs-/Befähigungs-Konfigurator mit Live-Preisen und Phasenübersicht.
- Praxisnahe B2B-Anwendungsbeispiele (Dokumentenanalyse, Sitzungsprotokolle, ERP-/Excel-Verarbeitung).

### C. KI-Agenten Hub (`/ki-agenten/`)
- **Hero:** Fokus auf kontrollierte Autonomie, API-Anbindung an bestehende ERP-/CRM-Landschaften.
- **Symmetrisches 6-Card-Grid (`Anwendungsfälle`):**
  1. *Propstack-Agent* (Deep-Dive verfügbar)
  2. *B2B Lead Finder* (Deep-Dive verfügbar – Case Study MICADO)
  3. *Multimodale Lead Engine* (Deep-Dive verfügbar – Case Study METEK)
  4. *Management- & Controlling-Agent*
  5. *Der Website-Agent* (Deep-Dive verfügbar – Souveräne Web-Infrastruktur)
  6. *Der Erstkontakt-Agent (Außenanbindung)* (Deep-Dive verfügbar – Dark/Yin-Yang-Design)

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
   - Bricht das klassische Agenturmodell auf: Änderungen per KI-Dialog im Minutentakt, 100 % Firmeneigentum (Git-Tresor), weltweite Edge-Auslieferung (< 0,5 s) und native AEO/GEO-Maschinenlesbarkeit bei 0 € laufenden CMS-Infrastrukturkosten.

### E. Innovation Lab: `/x402/` (`x402/index.html`)
- Dedizierte Forschungs- und Experimentalseite für **autonome Machine-to-Machine-Payments** über den HTTP-402-Standard.
- Pay-per-Inference, autonome Agenten-Ökonomie und Verlinkung zur Skool-Community (`https://www.skool.com/x402-8237/about`).

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
  - Schema.org-Typen `ProfessionalService`, `WebPage`, `FAQPage` mit semantischen `knowsAbout`-Tags für Agentic Systems, B2B-Automatisierung und API-Workflows.
