import os
import shutil

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
old_dir = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-pipeline")
new_dir = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder")

# Rename folder
if os.path.exists(old_dir):
    os.rename(old_dir, new_dir)

# Update references in all relevant files
files_to_update = [
    "index.html",
    "ki-mitarbeiter/index.html",
    "ki-mitarbeiter/b2b-lead-finder/index.html",
    "llms.txt",
    "sitemap.xml",
    "_redirects"
]

for rel_path in files_to_update:
    abs_path = os.path.join(base_dir, rel_path.replace('/', '\\'))
    if os.path.exists(abs_path):
        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace URLs/Slugs
        content = content.replace('b2b-lead-pipeline', 'b2b-lead-finder')
        
        # Replace Display Names
        content = content.replace('B2B Lead Pipeline', 'B2B Lead Finder')
        content = content.replace('B2B Lead-Pipeline', 'B2B Lead Finder')
        
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Add Carsten to the Team page
team_page = os.path.join(base_dir, "team", "index.html")
with open(team_page, 'r', encoding='utf-8') as f:
    team_content = f.read()

carsten_html = """
      <!-- CARSTEN -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="carsten.jpg" alt="Carsten - Lead-Recherche" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">Carsten <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Vertriebsassistenz & Lead-Recherche</div>
          <div class="agent-pate">Namenspate: Carsten Niebuhr (Pionier der systematischen Datenerhebung)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Systematische Recherche und Identifikation passgenauer B2B-Zielkunden.</li>
            <li><i data-lucide="check-circle-2"></i> Automatische Anreicherung von Unternehmensprofilen (Branche, Kontaktpunkte).</li>
            <li><i data-lucide="check-circle-2"></i> Aufbereitung bereinigter Lead-Listen für die direkte Vertriebsansprache.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">lead-qualification</span>
            <span class="agent-tag">data-enrichment</span>
            <span class="agent-tag">company-research</span>
            <span class="agent-tag">market-mapping</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">Web Scraping</span>
            <span class="agent-tag">CRM-Integration</span>
            <span class="agent-tag">Data Formatting</span>
            <span class="agent-tag">Memory</span>
          </div>
        </div>
      </div>
"""

# Insert into team page before closing agent grid
if '<!-- CARSTEN -->' not in team_content:
    target = """        </div>
      </div>

    </div>"""

    replacement = """        </div>
      </div>
""" + carsten_html + """
    </div>"""

    team_content = team_content.replace(target, replacement)
    team_content = team_content.replace('Ein Mensch.<br><em>Fünf digitale Experten.</em>', 'Ein Mensch.<br><em>Sechs digitale Experten.</em>')

    with open(team_page, 'w', encoding='utf-8') as f:
        f.write(team_content)

print("Renaming and injection complete.")
