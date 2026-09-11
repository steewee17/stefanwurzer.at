import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
index_file = os.path.join(base_dir, "index.html")

with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_showcase = """      <div class="aeol fu">
        <span class="ey" style="color:var(--gold-light)">Fokus-System</span>
        <div class="rule" style="background:rgba(255,255,255,0.2)"></div>
        <h2>B2B Vertrieb auf Autopilot:<br><em>Der B2B Lead Finder.</em></h2>
        <p>Machen Sie die Lead-Recherche zum System, nicht zum Zufall. Entdecken Sie unsere produktisierte Lead-Engine, die potenzielle Kunden identifiziert, streng nach Ihrem Wunschkundenprofil (ICP) qualifiziert und mundgerecht in Ihr CRM (HubSpot, Pipedrive etc.) übergibt.</p>
        <div style="margin-top:32px;">
          <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btngold" style="display:inline-flex;width:auto;">System-Architektur ansehen →</a>
        </div>
      </div>"""

new_showcase = """      <div class="aeol fu">
        <span class="ey" style="color:var(--gold-light)">Fokus-System (Praxiserprobt bei MICADO)</span>
        <div class="rule" style="background:rgba(255,255,255,0.2)"></div>
        <h2>B2B Vertrieb auf Autopilot:<br><em>Der B2B Lead Finder.</em></h2>
        <p>Machen Sie die Lead-Recherche zum System, nicht zum Zufall. Entdecken Sie unsere produktisierte Lead-Engine (im Praxiseinsatz bei der <strong>MICADO SMART ENGINEERING GmbH</strong>), die relevante Industrie-Entscheider identifiziert, streng nach Ihrem Wunschkundenprofil (ICP) qualifiziert und ansprechbereit in Ihr CRM übergibt.</p>
        <div style="margin-top:32px;">
          <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btngold" style="display:inline-flex;width:auto;">Case Study & System-Architektur ansehen →</a>
        </div>
      </div>"""

content = content.replace(old_showcase, new_showcase)

with open(index_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Updated Lead Finder showcase on index.html with MICADO reference")
