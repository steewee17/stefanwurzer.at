import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Revert /team/index.html H1 to original
team_file = os.path.join(base_dir, "team", "index.html")
with open(team_file, 'r', encoding='utf-8') as f:
    team_content = f.read()

old_team_h1 = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein hybrides Kernteam.<br>Maximale Schlagkraft durch <span class="rotator-wrap" data-words=\'["kontrollierte Autonomie.", "spezialisierte Fachagenten.", "stabile Feedback-Loops.", "maßgeschneiderte Workflows."]\'><em class="rotator-word in">kontrollierte Autonomie.</em></span></h1>'
new_team_h1 = '<h1 style="font-family:var(--display);font-size:clamp(42px,5vw,64px);color:var(--dark);line-height:1.1;margin-bottom:24px;">Ein Mensch.<br><em>Sechs digitale Experten.</em></h1>'

if old_team_h1 in team_content:
    team_content = team_content.replace(old_team_h1, new_team_h1)
else:
    # fallback
    import re
    team_content = re.sub(r'<h1 style="font-family:var\(--display\)[^>]+>.*?</h1>', new_team_h1, team_content, flags=re.DOTALL)

with open(team_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(team_content)
print("Reverted team/index.html H1 to static version")

# 2. Fix mobile nav breakpoint and styling in components.js
comp_file = os.path.join(base_dir, "components.js")
with open(comp_file, 'r', encoding='utf-8') as f:
    comp_content = f.read()

old_comp_style = """      <style>
        @media(max-width:640px) {
          #nav .nl { display: none; }
          #nav .nl.open { 
            display: flex !important; 
            flex-direction: column; 
            position: fixed; 
            top: 64px; 
            left: 0; 
            right: 0; 
            background: #fff; 
            padding: 20px 40px 28px; 
            border-bottom: 1px solid var(--border); 
            box-shadow: 0 8px 24px rgba(0,0,0,.08); 
            gap: 4px; 
            z-index: 199; 
          }
          #nav .ham { display: flex !important; }
        }
      </style>"""

new_comp_style = """      <style>
        @media(max-width:800px) {
          .nl { display: none !important; }
          .nl.open { 
            display: flex !important; 
            flex-direction: column !important; 
            position: fixed !important; 
            top: 64px !important; 
            left: 0 !important; 
            right: 0 !important; 
            background: #fff !important; 
            padding: 20px 40px 28px !important; 
            border-bottom: 1px solid var(--border) !important; 
            box-shadow: 0 8px 24px rgba(0,0,0,.08) !important; 
            gap: 8px !important; 
            z-index: 999 !important; 
          }
          .ham { display: flex !important; }
        }
      </style>"""

comp_content = comp_content.replace(old_comp_style, new_comp_style)

with open(comp_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(comp_content)
print("Updated components.js mobile nav styles")

# 3. Update style.css mobile nav rules
style_file = os.path.join(base_dir, "style.css")
with open(style_file, 'r', encoding='utf-8') as f:
    style_content = f.read()

old_style_mq = """@media(max-width:640px){
  .wrap{padding:0 20px}
  .ni{padding:0 20px}
  .nl{display:none}
  .ham{display:flex}
  section{padding:64px 0}
  .phi{padding:60px 20px}
  .bc{padding:88px 20px 0}
  .fg2{grid-template-columns:1fr}
}"""

new_style_mq = """@media(max-width:800px){
  .wrap{padding:0 20px}
  .ni{padding:0 20px}
  .nl{display:none}
  .ham{display:flex !important}
  section{padding:64px 0}
  .phi{padding:60px 20px}
  .bc{padding:88px 20px 0}
  .fg2{grid-template-columns:1fr}
}"""

style_content = style_content.replace(old_style_mq, new_style_mq)

with open(style_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(style_content)
print("Updated style.css mobile nav rules")
