import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/externe-ki-agenten/index.html (Fix Bing error: was 198 chars -> now 155 chars)
deep_file = os.path.join(base_dir, "ki-mitarbeiter", "externe-ki-agenten", "index.html")
with open(deep_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_desc = 'content="Entscheider recherchieren im B2B-Umfeld immer seltener manuell durch Unterseiten. Sie beauftragen spezialisierte Agenten, um den Markt zu scannen, Zertifizierungen zu prüfen und konkrete Termine vorzubereiten."'
new_desc = 'content="B2B-Schnittstellen für externe KI-Agenten: Machen Sie Ihr Unternehmen direkt für autonome Einkaufs-KIs erreichbar. Schneller Intake & Termine ohne Umwege."'

content = content.replace(old_desc, new_desc)

# Also update in JSON-LD description
old_json_desc = '"description": "Entscheider recherchieren im B2B-Umfeld immer seltener manuell durch Unterseiten. Sie beauftragen spezialisierte Agenten, um den Markt zu scannen, Zertifizierungen zu prüfen und konkrete Termine vorzubereiten.",'
new_json_desc = '"description": "B2B-Schnittstellen für externe KI-Agenten: Machen Sie Ihr Unternehmen direkt für autonome Einkaufs-KIs erreichbar. Schneller Intake & Termine ohne Umwege.",'
content = content.replace(old_json_desc, new_json_desc)

with open(deep_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("Updated ki-mitarbeiter/externe-ki-agenten/index.html meta description (155 chars)")

# 2. Update team/index.html (was 166 chars -> now 153 chars)
team_file = os.path.join(base_dir, "team", "index.html")
with open(team_file, 'r', encoding='utf-8') as f:
    t_content = f.read()

old_team_desc = 'content="Lernen Sie unser hybrides Kernteam kennen. Wir verbinden Prozess-Architektur mit digitalen KI-Experten durch kontrollierte Autonomie und das Least-Privilege-Prinzip."'
new_team_desc = 'content="Lernen Sie unser hybrides Kernteam kennen: Wir verbinden Prozess-Architektur mit digitalen KI-Experten durch kontrollierte Autonomie im KMU-Tagesgeschäft."'
t_content = t_content.replace(old_team_desc, new_team_desc)

with open(team_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(t_content)
print("Updated team/index.html meta description (153 chars)")

# 3. Update case-premium-leads/index.html (was 162 chars -> now 147 chars)
metek_file = os.path.join(base_dir, "ki-mitarbeiter", "case-premium-leads", "index.html")
with open(metek_file, 'r', encoding='utf-8') as f:
    m_content = f.read()

old_metek_desc = 'content="Case Study: Wie die METEK GmbH durch multimodale KI-Analyse (Semantik & visuelle Ästhetik) exklusive Architektur-Leads für den Premium-Innenausbau identifiziert."'
new_metek_desc = 'content="Case Study: Wie die METEK GmbH durch multimodale KI-Analyse (Semantik & Ästhetik) exklusive Architektur-Leads für den Premium-Innenausbau gewinnt."'
m_content = m_content.replace(old_metek_desc, new_metek_desc)

with open(metek_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(m_content)
print("Updated case-premium-leads/index.html meta description (147 chars)")
