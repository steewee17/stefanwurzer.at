import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_agent_html = """
      <!-- TIM -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="tim.jpg" alt="Tim - Head of Web & Development" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">Tim <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Head of Web & Development</div>
          <div class="agent-pate">Namenspate: Tim Berners-Lee (Erfinder des World Wide Web)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Konzeption, Design und technische Architektur der Webpräsenz.</li>
            <li><i data-lucide="check-circle-2"></i> Autonome Programmierung und Implementierung neuer Funktionen.</li>
            <li><i data-lucide="check-circle-2"></i> Qualitätssicherung, Pushing und unterbrechungsfreies Deployment.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">clean-code-architecture</span>
            <span class="agent-tag">ux-researcher</span>
            <span class="agent-tag">deployment-automation</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">A2A (Design-Abstimmung)</span>
            <span class="agent-tag">Terminal Access</span>
            <span class="agent-tag">Version Control</span>
            <span class="agent-tag">Code Review</span>
          </div>
        </div>
      </div>
"""

# Insert before "</div> <!-- PLATZHALTER ZUKUNFT -->" or rather, inside the agent-grid.
# We need to find the end of the agent-grid, which is after the David card.
# The David card ends with `</div>\n        </div>\n      </div>\n\n    </div>`
# Let's target the exact string to insert before the closing `</div>` of `.agent-grid`

target = "      </div>\n\n    </div>\n    \n    <!-- HR PROCESS / ONBOARDING -->"
replacement = "      </div>\n" + new_agent_html + "\n    </div>\n    \n    <!-- HR PROCESS / ONBOARDING -->"

content = content.replace(target, replacement)

# Update the headline from "Drei digitale Experten" to "Vier digitale Experten"
content = content.replace('Ein Mensch.<br><em>Drei digitale Experten.</em>', 'Ein Mensch.<br><em>Vier digitale Experten.</em>')

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
