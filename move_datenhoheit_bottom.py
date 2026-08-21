import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

datenhoheit_html = """
    <!-- DATENHOHEIT & KONTROLLE (Andrei) -->
    <div class="fu d2" style="background: var(--bg-warm); border: 1px solid var(--border); border-radius: 12px; padding: 40px; margin-bottom: 64px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
      <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:16px;">Kontrollierte Autonomie & Datenhoheit</h3>
      <p style="font-size:15px; color:var(--text); line-height:1.7; margin-bottom:24px;">
        Unsere digitalen Experten arbeiten nach dem strikten <strong>Least-Privilege-Prinzip</strong>: Jeder Agent hat nur Zugriff auf die Daten und Systeme, die er für seine spezifische Aufgabe zwingend benötigt. System-Prompts und Langzeitgedächtnisse liegen sicher auf europäischen Servern. Die eigentlichen KI-Modelle dienen lediglich als austauschbare Motoren – so garantieren wir 100% Datenkontrolle und absolute Unabhängigkeit von einzelnen Anbietern.
      </p>
      <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="display:inline-flex;">Genau dieses Prinzip setzen wir für Kunden um <i data-lucide="arrow-right" style="width:16px;height:16px;margin-left:4px;"></i></a>
    </div>
"""

# Find and remove existing block
if "<!-- DATENHOHEIT & KONTROLLE (Andrei) -->" in content:
    # We need to extract the exact block because spacing might vary.
    import re
    # Match from the start of the comment to the closing div of the block
    pattern = r"\s*<!-- DATENHOHEIT & KONTROLLE \(Andrei\) -->.*?</div>\s*"
    content = re.sub(pattern, "\n\n", content, flags=re.DOTALL)

# Insert after HR process
# HR process ends with:
#           </div>
#       </div>
#  
#  
#     </div>
#   </section>

target = """          </div>
      </div>"""

replacement = """          </div>
      </div>
      
      <div class="rule c" style="margin: 80px auto;"></div>
""" + datenhoheit_html

if target in content:
    content = content.replace(target, replacement)
else:
    print("Could not find HR process end!")

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
