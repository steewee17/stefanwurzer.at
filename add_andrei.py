import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

andrei_html = """
      <!-- ANDREI -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="andrei.jpg" alt="Andrei - Agenten-Architektur" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">Andrei <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Agenten-Architektur & Methodik</div>
          <div class="agent-pate">Namenspate: Andrei Markov (Begründer der Markov-Ketten für dynamische Prozesse)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Kontinuierliches Monitoring und Auswertung aktueller Praxis zu Agenten-Architekturen.</li>
            <li><i data-lucide="check-circle-2"></i> Pflege einer internen Wissensbasis zu Methodik, Use Cases und technischer Umsetzung.</li>
            <li><i data-lucide="check-circle-2"></i> Strategischer Sparringspartner für die Architektur-Entscheidung: statischer Workflow vs. autonomer Agent.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">arxiv-research</span>
            <span class="agent-tag">competitor-monitor</span>
            <span class="agent-tag">llm-wiki</span>
            <span class="agent-tag">grounded-citations</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">Web Search & arXiv</span>
            <span class="agent-tag">File Operations</span>
            <span class="agent-tag">Clarifying Questions</span>
            <span class="agent-tag">Memory</span>
          </div>
        </div>
      </div>
"""

target = """        </div>
      </div>

    </div>"""

replacement = """        </div>
      </div>
""" + andrei_html + """
    </div>"""

content = content.replace(target, replacement)
content = content.replace('Ein Mensch.<br><em>Vier digitale Experten.</em>', 'Ein Mensch.<br><em>Fünf digitale Experten.</em>')

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
