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
- `ki-mitarbeiter/<case-name>/index.html` — einzelne Case-Study-Unterseiten
  (z. B. `case-premium-leads`, `b2b-lead-pipeline`), jede in eigenem Ordner.
- Diverse `*.py`-Hilfsskripte im Root (z. B. `update_bef.py`,
  `link_metek.py`, `remove_tools.py`) sind Bearbeitungswerkzeuge für die
  HTML-Dateien — **nicht ausführen**, David liest nur, ändert keinen Code.

## Nutzung durch David — Ablauf beim Einlesen

1. Verzeichnis auflisten, um aktuelle Seiten/Cases zu erfassen, bevor einzelne
   Dateien gelesen werden (Struktur kann sich zwischen Sessions ändern).
2. Kerninhalte lesen: Startseite, Leistungsseiten (`ki-befaehigung.html` u.
   ä.), Case-Studies unter `ki-mitarbeiter/`.
3. Daraus extrahieren: Value Proposition, Fachbegriffe, Leistungsportfolio-
   Struktur, Tone of Voice (Ansprache, Satzlänge, Fachlichkeit).
4. Tone-of-Voice-Profil im eigenen Memory verankern, nicht bei jeder Anfrage
   neu aus den Dateien rekonstruieren. Bei größeren Website-Änderungen erneut
   gegenlesen und aktualisieren.
5. Nichts erfinden, was nicht im Bestand steht oder von Stefan explizit
   angegeben wurde.

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
