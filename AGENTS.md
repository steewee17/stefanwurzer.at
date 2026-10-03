# AGENTS.md — stefanwurzer.at (Website-Repo)

Projektlokale Konventionen für David (Marketing, Brand Positioning & Content
Strategy). Gilt nur für dieses Repo — Davids Rolle/Scope/Persönlichkeit steht
in seiner eigenen `SOUL.md`, nicht hier.

## Zweck dieses Repos

Lokale, git-versionierte Kopie der Website stefanwurzer innovationservice
(GitHub-verbunden, Bearbeitung über Antigravity). Primäre Quelle für
bestehendes Wording, Leistungsportfolio und Tone of Voice.

## Struktur

- Statische HTML-Seiten im Root (z. B. `ki-befaehigung.html`) — jede Seite
  bringt ihr eigenes `<style>` mit, teils "von alten Leistungsseiten
  recycelt" (siehe Kommentare im Quelltext) — bei Tonalitäts-/Wording-Analyse
  reicht der sichtbare Textinhalt, das CSS ist für David nicht relevant.
- `ki-agenten/<case-name>/index.html` — einzelne Case-Study-Unterseiten
  (z. B. `case-premium-leads`, `b2b-lead-finder`), jede in eigenem Ordner.
- `x402/index.html` — Laborseite für M2M-Payments.
- Diverse `*.py`-Hilfsskripte im Root sind Bearbeitungswerkzeuge für die
  HTML-Dateien — **nicht ausführen**, David liest nur, ändert keinen Code.

## Nutzung durch David / AI-Assistenten — Ablauf beim Einlesen

1. `project_state.md` als Single Source of Truth für den aktuellen Stand,
   die Architektur und das Wording konsultieren.
2. Verzeichnis auflisten, um aktuelle Seiten/Cases zu erfassen, bevor einzelne
   Dateien gelesen werden (Struktur kann sich zwischen Sessions ändern).
3. Kerninhalte lesen: Startseite, Leistungsseiten (`ki-befaehigung.html` u.
   ä.), Case-Studies unter `ki-agenten/`, `x402/`.
4. Daraus extrahieren: Value Proposition, Fachbegriffe, Leistungsportfolio-
   Struktur, Tone of Voice (Ansprache, Satzlänge, Fachlichkeit).
5. Tone-of-Voice-Profil im eigenen Memory verankern, nicht bei jeder Anfrage
   neu aus den Dateien rekonstruieren. Bei größeren Website-Änderungen erneut
   gegenlesen und aktualisieren.
6. Nichts erfinden, was nicht im Bestand steht oder von Stefan explizit
   angegeben wurde.

## Dokumentation & Session-Abschluss (project_state.md)

- **Proaktive Aktualisierungs-Erinnerung:** Nach größeren inhaltlichen, architektonischen oder strategischen Änderungen bzw. zum Abschluss einer Session/Arbeitsphase proaktiv nachfragen, ob die Änderungen in der `project_state.md` dokumentiert und festgeschrieben werden sollen.

## Wording & Tonalitäts-Regeln (Österreich / DACH)

- **KI-Agenten statt KI-Mitarbeiter:** Durchgängig **KI-Agenten** verwenden (kein „KI-Mitarbeiter“ mehr in URLs, Texten oder Metadaten).
- **KMU statt Mittelstand:** Der Begriff „Mittelstand“ ist bundesdeutsches Vokabular (BRD). In Österreich und für Stefans Positionierung gilt: Immer **KMU** (Kleine und mittlere Unternehmen) oder **Betriebe / Unternehmen** verwenden.
- **Ansprache:** Immer das professionelle, wertschätzende „Sie / Ihr“ (kein unaufgefordertes Duzen auf der Website).
- **Stil:** Prägnant, rhythmisch, bodenständig und ingenieursnah (kein Agentur-Hype-Slang).

## SEO/Tracking-Hinweis

Seiten enthalten Google-Tag-Manager- und Klaro-Cookie-Consent-Einbindungen
sowie ausführliche `<meta>`-Tags (Description, Keywords, hreflang). Bei
Content-Vorschlägen für neue Seiten diese Struktur als Vorbild für
SEO-Metadaten mitliefern, aber die technische Einbindung selbst nicht ändern
(kein Coding-Auftrag für David).

## Out of scope für dieses Repo

- Kein Schreibzugriff auf Code/Deploy — David liefert Content-Entwürfe
  (Text), keine HTML-/CSS-Änderungen.
- Kein eigenständiges Live-Schalten von Inhalten.
