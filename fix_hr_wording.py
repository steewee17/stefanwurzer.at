import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Personalakte -> Rollenprofil
content = content.replace(
    '1. Die Personalakte',
    '1. Das Rollenprofil'
)

# Fix Card 3
target_card_3 = """<h3 style="font-family:var(--display); font-size:20px; color:var(--dark); margin:0;">3. Probezeit & Harness</h3>
            <p style="font-size:14px; color:var(--text); line-height:1.6; margin:0;">Ein Sprachmodell allein ist nur ein Gehirn im Glas. Wir nutzen die moderne <strong>Hermes-Architektur (Agent = Harness + Modell)</strong>. Das verleiht dem Agenten Langzeitgedächtnis und Tool-Zugriff. Während der 1-monatigen Probezeit evaluiert sich das System selbst und lernt aus menschlichem Feedback.</p>"""

new_card_3 = """<h3 style="font-family:var(--display); font-size:20px; color:var(--dark); margin:0;">3. Probezeit & Feedback-Loop</h3>
            <p style="font-size:14px; color:var(--text); line-height:1.6; margin:0;">Ein Sprachmodell allein ist nur ein Gehirn im Glas. Erst ein maßgeschneidertes Framework verleiht dem Agenten Langzeitgedächtnis, sicheren System-Zugriff und die Fähigkeit zur Selbstreflexion. Während einer strikten Probezeit evaluiert sich der Agent stetig selbst und lernt aus menschlichem Feedback.</p>"""

content = content.replace(target_card_3, new_card_3)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
