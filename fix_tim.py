import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """        </div>
      </div>

    </div>"""

replacement = """        </div>
      </div>

      <!-- TIM -->
      <div class="agent-card">
        <div class="agent-img-wrap"><img src="tim.jpg" alt="Tim - Head of Web Engineering" class="agent-img"></div>
        <div class="agent-content">
          <div class="agent-name">Tim <span class="agent-badge">KI-Agent</span></div>
          <div class="agent-role">Head of Web Engineering & Deployment</div>
          <div class="agent-pate">Namenspate: Tim Berners-Lee (Erfinder des WWW)</div>
          
          <div class="agent-section-title">Hauptaufgaben</div>
          <ul class="agent-list">
            <li><i data-lucide="check-circle-2"></i> Webkonzeption und detaillierte Implementierungsplanung.</li>
            <li><i data-lucide="check-circle-2"></i> Autonome Programmierung der Website-Struktur und -Logik.</li>
            <li><i data-lucide="check-circle-2"></i> Qualitätssicherung, Code-Pushing und Live-Deployment.</li>
          </ul>

          <div class="agent-section-title">Aktive Fach-Skills</div>
          <div class="agent-tags">
            <span class="agent-tag">web-architecture</span>
            <span class="agent-tag">version-control</span>
            <span class="agent-tag">implementation-planning</span>
          </div>

          <div class="agent-section-title">Core-Tools</div>
          <div class="agent-tags">
            <span class="agent-tag">Codebase Operations</span>
            <span class="agent-tag">Terminal Execution</span>
            <span class="agent-tag">Task Tracking</span>
          </div>
        </div>
      </div>

    </div>"""

content = content.replace(target, replacement)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
