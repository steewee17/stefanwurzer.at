import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

hr_section = """
    <!-- HR PROCESS / ONBOARDING -->
    <div class="rule c" style="margin: 80px auto;"></div>
    
    <div class="fu" style="text-align:center; margin-bottom:48px;">
      <h2 style="font-family:var(--display); font-size:32px; color:var(--dark);">Wie wir digitale Kollegen "einstellen"</h2>
      <p style="font-size:15px; color:var(--text); max-width:600px; margin:0 auto;">Die Integration autonomer Agenten ist kein klassisches IT-Projekt, sondern ein moderner HR-Prozess. Sicherheit, Zuverlässigkeit und Firmenkultur stehen an oberster Stelle.</p>
    </div>
    
    <div class="agent-grid fu" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); margin-bottom: 32px;">
        <!-- Card 1 -->
        <div class="glass-card" style="padding: 32px; border: 1px solid var(--border); border-radius: 12px; display:flex; flex-direction:column; gap:16px; background:var(--bg);">
            <i data-lucide="folder-open" style="color:var(--gold); width:32px; height:32px;"></i>
            <h3 style="font-family:var(--display); font-size:20px; color:var(--dark); margin:0;">1. Die Personalakte</h3>
            <p style="font-size:14px; color:var(--text); line-height:1.6; margin:0;">Der System-Prompt ist die DNA des Agenten. Hier definieren wir Befugnisse und das <strong>Big-Five-Persönlichkeitsprofil</strong>. Das verhindert generisches "KI-Sprech" und sorgt dafür, dass sich der Agent nahtlos in die Tonalität einfügt. Harte No-Go-Listen definieren absolute rote Linien.</p>
        </div>
        <!-- Card 2 -->
        <div class="glass-card" style="padding: 32px; border: 1px solid var(--border); border-radius: 12px; display:flex; flex-direction:column; gap:16px; background:var(--bg);">
            <i data-lucide="shield-alert" style="color:var(--gold); width:32px; height:32px;"></i>
            <h3 style="font-family:var(--display); font-size:20px; color:var(--dark); margin:0;">2. Das Assessment Center</h3>
            <p style="font-size:14px; color:var(--text); line-height:1.6; margin:0;">Bevor ein Agent produktiv auf echte Daten zugreift, muss er sich beweisen. In einer isolierten Umgebung testen Hacker-KIs den Neuzugang: Sie versuchen, Sicherheitslücken zu finden, Halluzinationen zu provozieren oder ein PR-Desaster auszulösen. Nur wer standhält, wird übernommen.</p>
        </div>
        <!-- Card 3 -->
        <div class="glass-card" style="padding: 32px; border: 1px solid var(--border); border-radius: 12px; display:flex; flex-direction:column; gap:16px; background:var(--bg);">
            <i data-lucide="cpu" style="color:var(--gold); width:32px; height:32px;"></i>
            <h3 style="font-family:var(--display); font-size:20px; color:var(--dark); margin:0;">3. Probezeit & Harness</h3>
            <p style="font-size:14px; color:var(--text); line-height:1.6; margin:0;">Ein Sprachmodell allein ist nur ein Gehirn im Glas. Wir nutzen die moderne <strong>Hermes-Architektur (Agent = Harness + Modell)</strong>. Das verleiht dem Agenten Langzeitgedächtnis und Tool-Zugriff. Während der 1-monatigen Probezeit evaluiert sich das System selbst und lernt aus menschlichem Feedback.</p>
        </div>
    </div>
"""

# Find the end of the agent-grid div
# Wait, let's just insert it before "<!-- PLATZHALTER ZUKUNFT -->"
content = content.replace('<!-- PLATZHALTER ZUKUNFT -->', hr_section + '\n    <!-- PLATZHALTER ZUKUNFT -->')

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
