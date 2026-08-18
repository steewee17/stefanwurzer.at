import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-befaehigung.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """
<!-- DIE PHILOSOPHIE -->
<section class="sec" style="background:var(--bg); border-bottom:1px solid var(--border);">
  <div class="wrap">
    <div class="fu" style="max-width:800px;margin:0 auto;text-align:center;">
      <span class="ey">Die Realität des KI-Hypes</span>
      <div class="rule c"></div>
      <h2>Das Spiel wird entschieden in<br><em>Prozessen und Kultur.</em></h2>
      <p style="font-size:18px;color:var(--dark);line-height:1.6;font-weight:500;margin-top:24px;">Die Technologie – ob das neueste Flaggschiff-Modell oder Open-Source – ist mittlerweile austauschbare Commodity.</p>
      
      <p style="font-size:15px;color:var(--text);line-height:1.75;margin-top:16px;">Jeder kann sich heute für wenige Cent die gleichen APIs buchen. Ein reiner Fokus auf Tools greift zu kurz. Der wahre Wettbewerbsvorteil, der sprichwörtliche <strong>Burggraben</strong>, entsteht an zwei Stellen, die man nicht einfach abonnieren kann:</p>
    </div>

    <div class="uc-grid" style="max-width:900px;margin:40px auto 0;">
      <div class="glass-card" style="padding:32px;border:1px solid var(--border);border-radius:8px;">
        <h3 style="font-size:18px;color:var(--dark);margin-bottom:12px;display:flex;align-items:center;gap:8px;"><i data-lucide="git-merge" style="color:var(--gold);width:20px;height:20px;"></i> Prozesse (Die Struktur)</h3>
        <p style="font-size:14px;color:var(--text);line-height:1.6;">Eine KI kann nur so präzise agieren, wie der zugrunde liegende Prozess definiert ist. Wenn die Übergabepunkte, Qualitätskriterien und Datenflüsse im Unternehmen chaotisch sind, skaliert ein KI-Agent lediglich das Chaos in Rekordzeit.</p>
      </div>
      <div class="glass-card" style="padding:32px;border:1px solid var(--border);border-radius:8px;">
        <h3 style="font-size:18px;color:var(--dark);margin-bottom:12px;display:flex;align-items:center;gap:8px;"><i data-lucide="users" style="color:var(--gold);width:20px;height:20px;"></i> Kultur (Die Haltung)</h3>
        <p style="font-size:14px;color:var(--text);line-height:1.6;">Wie reagiert das Team? Wird die Technologie boykottiert oder als Hebel begriffen? Eine Organisation braucht die Neugier, um Routineaufgaben abzugeben, sowie den "Risikoappetit", Fehler im System offen zu korrigieren und kontinuierlich zu iterieren.</p>
      </div>
    </div>

    <div class="fu" style="max-width:800px;margin:40px auto 0;text-align:center;">
      <p style="font-size:15px;color:var(--dark);line-height:1.75;padding:24px;border-left:2px solid var(--gold);background:var(--bg-sec);text-align:left;"><strong>Deshalb scheitern reine Software-Einführungen so oft im Mittelstand:</strong> Man kauft Tools, ignoriert aber die Prozessreife und die Befähigung der Mitarbeiter. Wer stattdessen vom konkreten <strong>Use Case</strong> ausgeht – <em>"Welche Aufgaben gehen den Leuten im Alltag eigentlich total auf den Keks?"</em> – und diese gezielt automatisiert, liefert keinen bloßen "Tech-Stack", sondern operative Transformation mit messbarem ROI.</p>
    </div>
  </div>
</section>
"""

content = content.replace('<!-- THE PROBLEM (Status Quo) -->', new_section + '\n<!-- THE PROBLEM (Status Quo) -->')

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
