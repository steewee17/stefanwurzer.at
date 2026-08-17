# Nous Research & Hermes Agent (vs. Claude)

Zusammenfassung aus der Vortrags-Dokumentation des Tutors (Screenshots + Notizen).

## 1. Wer steht dahinter: Nous Research

- Nous Research ist die Firma hinter **Hermes** (dem Agenten/Modell, um den es im Vortrag geht).
- Die ersten Screenshots zeigen eine Recherche zu "Nous Research" (Suchergebnisse, Firmen-/Projektseite) sowie die Landingpage, auf der Hermes vorgestellt wird.
- Kernaussage aus den Notizen: **"Hermes here to stay. Like virtual person to talk to."** – Hermes wird explizit als langfristig angelegter, persönlicher/virtueller Gesprächspartner positioniert (Framing näher an einer "virtuellen Person" als an einem klassischen Chat-Tool).

## 2. Setup & Infrastruktur

- **Für Kunden wird Hermes in einer virtuellen Maschine installiert** – ähnlich wie beim Ansatz von Claude ("Virtual machine with windows. Wie bei claude").
- D.h. Hermes läuft nicht "nackt" auf einem Server, sondern in einer isolierten VM-Umgebung mit Windows – vergleichbar mit dem Computer-Use/Sandbox-Ansatz, den auch Claude verfolgt.
- Ein eigener Abschnitt der Doku zeigt das **Hosting** (Screenshot zur Hosting-Umgebung/-Konfiguration).

## 3. Kosten-Vergleich

- Notiz: **"open ai cheaper than claude"** – im Vortrag wurde herausgestellt, dass OpenAI-Modelle im Preis günstiger sind als Claude-Modelle.
- Notiz: **"Hermes is free"** – Hermes selbst wird als kostenlos nutzbar dargestellt (im Gegensatz zu den kostenpflichtigen Modell-APIs von OpenAI/Anthropic).

## 4. Features von Hermes Agent

- **Web-Scraping mit kostenlosem Account** möglich ("Scrape web (free account)") – ein Screenshot zeigt die entsprechende Funktion/Oberfläche.
- Mehrere weitere Screenshots (Interface-Ansichten von hermes-agent.nousresearch.com) dokumentieren die Bedienoberfläche und Fähigkeiten des Agenten – u. a. Chat-/Agenten-Interaktion, Tool-Nutzung und Konfigurationsoptionen.
- Die zentrale Plattform-URL: **hermes-agent.nousresearch.com**

## 5. Integration in bestehende Workflows

- **Hermes ↔ n8n via API-Key**: Hermes lässt sich per API-Key direkt an n8n anbinden – relevant für die Einbindung in bestehende Automatisierungs-Workflows (analog zur Claude-API-Anbindung in n8n).

## 6. Kurzfazit (Hermes vs. Claude)

| Aspekt | Hermes (Nous Research) | Claude |
|---|---|---|
| Kosten | kostenlos nutzbar | kostenpflichtig (API) |
| Betrieb | in virtueller Windows-Maschine | ebenfalls VM-/Sandbox-Ansatz |
| Modellkosten dahinter | OpenAI-Modelle (günstiger) | Anthropic-Modelle |
| Web-Scraping | ja, mit Free-Account | – (im Doc nicht verglichen) |
| Automatisierung | Anbindung an n8n via API-Key | Anbindung an n8n via API-Key |

---

**Hinweis:** Diese Datei basiert auf den im Word-Dokument enthaltenen Screenshots und handschriftlichen Notizen des Tutors. Die Screenshots selbst (Suchergebnisse, Website-Ansichten, Hosting- und Interface-Screens) liegen als Bilddateien im Originaldokument vor; die Kernaussagen und Fakten daraus sind oben strukturiert zusammengefasst. Für Detail-Screenshots (z. B. exakte UI-Elemente) empfiehlt es sich, bei Bedarf gezielt einzelne Bilder nochmal anzusehen.
