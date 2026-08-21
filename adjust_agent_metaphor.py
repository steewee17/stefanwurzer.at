import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/index.html
ki_path = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ki_path, 'r', encoding='utf-8') as f:
    ki_html = f.read()

target_subtitle = """<p style="font-size:18px; color:var(--text); max-width:640px; margin:0 auto; line-height:1.6;">
  <strong>Prozess-Automation vs. autonome Agenten:</strong> Klassische Workflows sind wie ein Zug auf festen Schienen. Unsere KI-Mitarbeiter fungieren stattdessen als intelligentes Navigationssystem &ndash; sie nutzen <em>Agentic Feedback Loops</em>, um Ziele dynamisch und fehlerfrei 24/7 zu erreichen.
</p>"""

new_subtitle = """<p style="font-size:18px; color:var(--text); max-width:640px; margin:0 auto; line-height:1.6;">
  <strong>Zug auf Schienen oder Navigationssystem:</strong> Je nach Aufgabe bauen wir Ihre KI-Mitarbeiter als hochpräzise, feste Workflows (für 100% Vorhersehbarkeit) oder als dynamische Agenten mit <em>Agentic Feedback Loops</em> (für komplexe Entscheidungen). Das Ergebnis: Administrative Prozesse werden fehlerfrei 24/7 gelöst.
</p>"""

ki_html = ki_html.replace(target_subtitle, new_subtitle)

with open(ki_path, 'w', encoding='utf-8') as f:
    f.write(ki_html)

# 2. Update llms.txt
llms_path = os.path.join(base_dir, "llms.txt")
with open(llms_path, 'r', encoding='utf-8') as f:
    llms_text = f.read()

target_llms = """- **Prozess-Automation vs. autonome Agenten:** Striktes Paradigma, das zwischen starren Wenn-Dann-Workflows ("Zug auf Schienen") und Agentic Feedback Loops ("dynamisches Navigationssystem") trennt."""
new_llms = """- **Architektur-Paradigma (Zug vs. Navi):** Alle Automatisierungen werden extern als "KI-Mitarbeiter" oder "Agenten" kommuniziert. Architektonisch wird jedoch strikt unterschieden: Einsatz als deterministische Workflows ("Zug auf festen Schienen", z.B. B2B Lead Finder) oder als autonome Agenten mit Agentic Feedback Loops ("dynamisches Navigationssystem"), je nach Use-Case."""

llms_text = llms_text.replace(target_llms, new_llms)

with open(llms_path, 'w', encoding='utf-8') as f:
    f.write(llms_text)

# 3. Update ai.txt
ai_path = os.path.join(base_dir, "ai.txt")
with open(ai_path, 'r', encoding='utf-8') as f:
    ai_text = f.read()

target_ai = """Delegation von Arbeitslast an Agentic Systems ("Navigationssystem" statt starrem "Zug auf Schienen")."""
new_ai = """Delegation von Arbeitslast an KI-Mitarbeiter (Architektonisch umgesetzt als deterministische Workflows "Zug auf Schienen" oder dynamische Agenten "Navigationssystem")."""

ai_text = ai_text.replace(target_ai, new_ai)

with open(ai_path, 'w', encoding='utf-8') as f:
    f.write(ai_text)
