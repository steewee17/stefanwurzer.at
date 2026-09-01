import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
finder_file = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html")

with open(finder_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Subline & CTA Button
old_hero = """      <h1>Der B2B Lead Finder:<br><em>Fokussierte Vertriebszeit.</em></h1>
      <p class="hsub">Die Neukundengewinnung ist ein Problem, das nie verschwindet. Lösen Sie es mit einem System, das nie schläft. Von der automatisierten Recherche über die KI-Qualifizierung nach Ihrem Wunschkundenprofil (ICP) bis zur nahtlosen CRM-Übergabe.</p>
      <div class="hctag">
        <a href="#anfrage" class="btn">Systemcheck vereinbaren →</a>
      </div>"""

new_hero = """      <h1>Der B2B Lead Finder:<br><em>Fokussierte Vertriebszeit.</em></h1>
      <p class="hsub">Der Engpass im B2B-Vertrieb ist selten der Markt – sondern die Zeit für manuelle Lead-Recherche. Der B2B Lead Finder liefert jeden Morgen geprüfte, angereicherte Wunschkunden direkt in Ihr CRM. Ohne Kalt-Spam, 100 % DSGVO-konform.</p>
      <div class="hctag">
        <a href="#anfrage" class="btn">Pilotprojekt anfragen →</a>
      </div>"""

content = content.replace(old_hero, new_hero)

# 2. Step 2 Maschinenraum
old_step2 = """      <!-- Step 2 -->
      <div class="step-card glass-card fu d1">
        <div class="step-icon"><i data-lucide="database"></i></div>
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
            <div class="step-num">2</div>
            <h3 class="step-title" style="margin-bottom:0;">Daten-Upload & Strukturierung</h3>
          </div>
          <p class="step-desc">Die rohen Leads werden nicht mühsam in Excel gepflegt, sondern landen sicher, DSGVO-konform und strukturiert in einer eigenen, dedizierten Datenbank (einer sicheren Datenbank).</p>
        </div>
      </div>"""

new_step2 = """      <!-- Step 2 -->
      <div class="step-card glass-card fu d1">
        <div class="step-icon"><i data-lucide="database"></i></div>
        <div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
            <div class="step-num">2</div>
            <h3 class="step-title" style="margin-bottom:0;">Daten-Upload & CRM-Hygiene</h3>
          </div>
          <p class="step-desc">Keine Datenleichen, keine doppelten Kontakte: Automatische Dublettenprüfung und Datenbereinigung vor dem CRM-Import. Die Rohdaten landen sicher, DSGVO-konform und strukturiert in einer dedizierten Datenbank.</p>
        </div>
      </div>"""

content = content.replace(old_step2, new_step2)

# 3. Add Betriebsmodelle Block after Maschinenraum (before OUTCOME)
old_outcome_start = """<!-- OUTCOME -->"""

new_betriebsmodelle = """<!-- BETRIEBSMODELLE -->
<section class="sec" style="background:var(--bg); border-bottom:1px solid var(--border);">
  <div class="wrap">
    <div class="fu" style="text-align:center;margin-bottom:48px;max-width:650px;margin-left:auto;margin-right:auto;">
      <span class="ey">Betriebsmodelle</span>
      <div class="rule" style="margin:16px auto;"></div>
      <h2>Volle Flexibilität<br><em>für Ihr Team.</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin-top:16px;">Wählen Sie das Modell, das am besten zu Ihren internen Ressourcen und Ihrer IT-Strategie passt.</p>
    </div>

    <div class="fu d1" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(300px, 1fr));gap:32px;max-width:900px;margin:0 auto;">
      <div class="glass-card" style="padding:36px;border:1px solid var(--border);border-radius:12px;display:flex;flex-direction:column;gap:16px;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div class="step-icon" style="background:var(--bg-sec);color:var(--gold);"><i data-lucide="server"></i></div>
          <div>
            <div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;">Rundum-Sorglos</div>
            <h3 style="font-family:var(--display);font-size:22px;color:var(--dark);margin:0;">Managed Service</h3>
          </div>
        </div>
        <p style="font-size:15px;color:var(--text);line-height:1.65;margin:0;">Wir betreiben die gesamte Infrastruktur, pflegen die Schnittstellen und spülen kontinuierlich qualifizierte Wunschkunden verlässlich in Ihr CRM. Ihr Team konzentriert sich rein auf den Abschluss.</p>
      </div>

      <div class="glass-card" style="padding:36px;border:1px solid var(--gold-pale);border-radius:12px;display:flex;flex-direction:column;gap:16px;background:var(--bg-warm);">
        <div style="display:flex;align-items:center;gap:12px;">
          <div class="step-icon" style="background:var(--gold);color:#fff;"><i data-lucide="key-round"></i></div>
          <div>
            <div style="font-size:12px;font-weight:600;color:var(--gold);text-transform:uppercase;letter-spacing:0.1em;">Maximale Autonomie</div>
            <h3 style="font-family:var(--display);font-size:22px;color:var(--dark);margin:0;">Inhouse Setup</h3>
          </div>
        </div>
        <p style="font-size:15px;color:var(--text);line-height:1.65;margin:0;">Wir richten das gesamte System komplett in Ihren eigenen Tools & Accounts ein. Ihr Team behält 100 % Systemhoheit und steuert alle Prozesse eigenständig ohne laufende Betreiberkosten.</p>
      </div>
    </div>
  </div>
</section>

<!-- OUTCOME -->"""

content = content.replace(old_outcome_start, new_betriebsmodelle)

# 4. Formular / CTA Section update
old_form = """<!-- FORMULAR -->
<section class="sec" id="anfrage" style="background:var(--bg-warm);">
  <div class="wrap form-wrap">
    
    <div class="form-left fu">
      <span class="ey">Pipeline Automatisieren</span>
      <div class="rule"></div>
      <h2>Bereit für eine<br><em>volle Pipeline?</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin:24px 0 32px">Lassen Sie uns in 30 Minuten analysieren, wie wir diesen Lead-Prozess auf Ihre spezifische Branche und Ihr CRM anpassen können.</p>
      
      <div class="t-item">
        <div class="t-icon"><i data-lucide="shield-check"></i></div>
        <div class="t-text">Qualität vor Quantität. 100% Fokus auf präzise Recherche & Qualifizierung.</div>
      </div>
      <div class="t-item">
        <div class="t-icon"><i data-lucide="network"></i></div>
        <div class="t-text">Nahtlose Integration in Ihr bestehendes CRM.</div>
      </div>
      <div class="t-item">
        <div class="t-icon"><i data-lucide="infinity"></i></div>
        <div class="t-text">Ein System, das bleibt. Lösen Sie das Dauerproblem der Neukundengewinnung nachhaltig.</div>
      </div>
    </div>

    <div class="form-right fu d1">
      <div class="glass-card" style="padding:40px;">
        <h3 style="font-family:var(--display);font-size:22px;font-weight:600;color:var(--dark);margin-bottom:6px">Systemcheck anfragen</h3>
        <p style="font-size:14px;color:var(--muted);margin-bottom:24px;margin-top:6px">Ich melde mich in der Regel innerhalb von 24 Stunden.</p>"""

new_form = """<!-- FORMULAR -->
<section class="sec" id="anfrage" style="background:var(--bg-warm);">
  <div class="wrap form-wrap">
    
    <div class="form-left fu">
      <span class="ey">Pilotprojekt</span>
      <div class="rule"></div>
      <h2>Testen Sie die Qualität<br><em>mit realen Zielkunden.</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin:24px 0 32px">Starten Sie mit einem kompakten Pilot: Wir definieren gemeinsam Ihr ICP und testen die Datenqualität mit echten Wunschkunden direkt in Ihrem CRM – risikolos, bevor Sie skalieren.</p>
      
      <div class="t-item">
        <div class="t-icon"><i data-lucide="crosshair"></i></div>
        <div class="t-text">Präzise ICP-Definition für Ihre spezifische Zielgruppe.</div>
      </div>
      <div class="t-item">
        <div class="t-icon"><i data-lucide="shield-check"></i></div>
        <div class="t-text">Keine Datenleichen: 100 % Dublettenprüfung & DSGVO-Konformität.</div>
      </div>
      <div class="t-item">
        <div class="t-icon"><i data-lucide="database"></i></div>
        <div class="t-text">Reale Testdaten direkt in Ihrem bestehenden CRM.</div>
      </div>
    </div>

    <div class="form-right fu d1">
      <div class="glass-card" style="padding:40px;">
        <h3 style="font-family:var(--display);font-size:22px;font-weight:600;color:var(--dark);margin-bottom:6px">Pilotprojekt anfragen</h3>
        <p style="font-size:14px;color:var(--muted);margin-bottom:24px;margin-top:6px">Ich melde mich in der Regel innerhalb von 24 Stunden für die Abstimmung.</p>"""

content = content.replace(old_form, new_form)

# Form button
content = content.replace(
    '<button class="btn" style="width:100%" onclick="submitContactForm(\'stefanwurzer.at/akquise\')">Gespräch anfragen →</button>',
    '<button class="btn" style="width:100%" onclick="submitContactForm(\'stefanwurzer.at/akquise\')">Pilotierung anfragen →</button>'
)

with open(finder_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Applied all 4 tuning points to b2b-lead-finder!")
