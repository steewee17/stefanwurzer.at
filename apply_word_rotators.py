import os
import json

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update style.css with rotator CSS
style_file = os.path.join(base_dir, "style.css")
with open(style_file, 'r', encoding='utf-8') as f:
    style_content = f.read()

rotator_css = """
/* WORD ROTATOR */
.rotator-wrap {
  display: inline-block;
  position: relative;
  vertical-align: baseline;
  text-align: left;
}
.rotator-word {
  display: inline-block;
  font-style: italic;
  color: var(--gold);
  transition: opacity 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
  white-space: nowrap;
}
.rotator-word.out {
  opacity: 0;
  transform: translateY(-8px);
}
.rotator-word.in {
  opacity: 1;
  transform: translateY(0);
}
.rotator-word.init {
  opacity: 0;
  transform: translateY(8px);
  transition: none !important;
}
"""

if "/* WORD ROTATOR */" not in style_content:
    style_content += rotator_css
    with open(style_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(style_content)
    print("Added rotator CSS to style.css")

# 2. Update components.js with rotator JS
comp_file = os.path.join(base_dir, "components.js")
with open(comp_file, 'r', encoding='utf-8') as f:
    comp_content = f.read()

rotator_js = """
// Word Rotator Component
function initWordRotators() {
  const rotators = document.querySelectorAll('[data-words]');
  rotators.forEach(el => {
    try {
      const raw = el.getAttribute('data-words');
      if (!raw) return;
      const words = JSON.parse(raw);
      if (!Array.isArray(words) || words.length <= 1) return;

      let currentIndex = 0;
      let wordEl = el.querySelector('.rotator-word');
      if (!wordEl) {
        wordEl = el.querySelector('em') || el;
      }
      wordEl.classList.add('rotator-word', 'in');

      setInterval(() => {
        wordEl.classList.remove('in');
        wordEl.classList.add('out');

        setTimeout(() => {
          currentIndex = (currentIndex + 1) % words.length;
          wordEl.textContent = words[currentIndex];
          wordEl.classList.remove('out');
          wordEl.classList.add('init');

          // Trigger reflow
          void wordEl.offsetWidth;

          wordEl.classList.remove('init');
          wordEl.classList.add('in');
        }, 350);
      }, 3000);
    } catch (e) {
      console.warn('WordRotator error:', e);
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initWordRotators);
} else {
  initWordRotators();
}
"""

if "// Word Rotator Component" not in comp_content:
    comp_content += rotator_js
    with open(comp_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(comp_content)
    print("Added rotator JS to components.js")

# 3. Update index.html (Startseite — Konzept A)
# Words: vereinen., befähigen., verbinden., skalieren.
index_file = os.path.join(base_dir, "index.html")
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

old_index_h1 = "<h1>Den Engpass im Büro auflösen.<br>Mensch und KI <em>vereinen.</em></h1>"
new_index_h1 = '<h1>Den Engpass im Büro auflösen.<br>Mensch und KI <span class="rotator-wrap" data-words=\'["vereinen.", "befähigen.", "verbinden.", "skalieren."]\'><em class="rotator-word in">vereinen.</em></span></h1>'

if old_index_h1 in index_content:
    index_content = index_content.replace(old_index_h1, new_index_h1)
    with open(index_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(index_content)
    print("Updated index.html H1")
else:
    print("Could not match old index.html H1")

# 4. Update ki-befaehigung.html (/ki-befaehigung/ — Konzept B)
# Words: Ihren Vertrieb., Ihre Projektteams., Ihre Verwaltung., Ihr gesamtes Team.
bef_file = os.path.join(base_dir, "ki-befaehigung.html")
with open(bef_file, 'r', encoding='utf-8') as f:
    bef_content = f.read()

old_bef_h1 = "<h1>KI, die passt.<br>Abläufe stärkt.<br>Teams entlastet.<br><em>Nicht umgekehrt.</em></h1>"
new_bef_h1 = '<h1>KI, die passt.<br>Echtes Praxis-Know-how für <span class="rotator-wrap" data-words=\'["Ihren Vertrieb.", "Ihre Projektteams.", "Ihre Verwaltung.", "Ihr gesamtes Team."]\'><em class="rotator-word in">Ihren Vertrieb.</em></span></h1>'

if old_bef_h1 in bef_content:
    bef_content = bef_content.replace(old_bef_h1, new_bef_h1)
    with open(bef_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(bef_content)
    print("Updated ki-befaehigung.html H1")
else:
    print("Could not match old ki-befaehigung.html H1")

# 5. Update ki-mitarbeiter/index.html (/ki-mitarbeiter/ — Konzept B)
# Words: den Vertrieb., das Marketing., die Angebotserstellung., Verwaltungsaufgaben., Recht & Steuern.
ma_file = os.path.join(base_dir, "ki-mitarbeiter", "index.html")
with open(ma_file, 'r', encoding='utf-8') as f:
    ma_content = f.read()

old_ma_h1 = "<h1>Delegieren statt klicken.<br>Ihr CRM wird <em>autonom.</em></h1>"
new_ma_h1 = '<h1>Delegieren statt klicken.<br>Autonome Unterstützung für <span class="rotator-wrap" data-words=\'["den Vertrieb.", "das Marketing.", "die Angebotserstellung.", "Verwaltungsaufgaben.", "Recht & Steuern."]\'><em class="rotator-word in">den Vertrieb.</em></span></h1>'

if old_ma_h1 in ma_content:
    ma_content = ma_content.replace(old_ma_h1, new_ma_h1)
    with open(ma_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(ma_content)
    print("Updated ki-mitarbeiter/index.html H1")
else:
    print("Could not match old ki-mitarbeiter/index.html H1")

# 6. Update kontakt/index.html (/kontakt/ — Konzept A)
# Words: zum Punkt., zu mehr Klarheit., zu neuen Ideen., zur passenden Lösung.
kontakt_file = os.path.join(base_dir, "kontakt", "index.html")
with open(kontakt_file, 'r', encoding='utf-8') as f:
    kontakt_content = f.read()

old_kontakt_h1 = "<h1>30 Minuten.<br><em>Direkt zum Punkt.</em></h1>"
new_kontakt_h1 = '<h1>30 Minuten.<br>Direkt <span class="rotator-wrap" data-words=\'["zum Punkt.", "zu mehr Klarheit.", "zu neuen Ideen.", "zur passenden Lösung."]\'><em class="rotator-word in">zum Punkt.</em></span></h1>'

if old_kontakt_h1 in kontakt_content:
    kontakt_content = kontakt_content.replace(old_kontakt_h1, new_kontakt_h1)
    with open(kontakt_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(kontakt_content)
    print("Updated kontakt/index.html H1")
else:
    print("Could not match old kontakt/index.html H1")

print("All updates successfully executed.")
