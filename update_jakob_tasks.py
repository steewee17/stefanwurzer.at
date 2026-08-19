import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Kontinuierliche Optimierung steuer- und SVS-relevanter Kennzahlen.</li>
            <li><i data-lucide="check-circle-2"></i> Laufende Vorbereitung der Buchhaltung für den Steuerberater.</li>
          </ul>"""

replacement = """          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> <strong>Steuerstrategie:</strong> Saubere Trennung und Optimierung von betrieblichen und privaten Finanzen.</li>
            <li><i data-lucide="check-circle-2"></i> <strong>Liquiditätsmanagement:</strong> Steuerung des Cashflows und Bewertung von Anlagestrategien.</li>
            <li><i data-lucide="check-circle-2"></i> <strong>Compliance & Fristen:</strong> Überwachung von Abgaben und fundierte Vorbereitung für den Steuerberater.</li>
          </ul>"""

content = content.replace(target, replacement)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
