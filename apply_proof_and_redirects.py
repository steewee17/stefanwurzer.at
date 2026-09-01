import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update ki-mitarbeiter/externe-ki-agenten/index.html with the new 2-card Market Proof
deep_file = os.path.join(base_dir, "ki-mitarbeiter", "externe-ki-agenten", "index.html")
with open(deep_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_trend_section = """<!-- REALER BELEG & TREND -->
<section class="sec">
  <div class="wrap">
    <div class="fu" style="text-align:center;max-width:700px;margin:0 auto;">
      <span class="ey">Markt-Entwicklung</span>
      <div class="rule c"></div>
      <h2 style="margin-bottom:20px;">Der Trend ist <em>messbar.</em></h2>
      <p style="font-size:15px;color:var(--text);line-height:1.75;">
        Branchenanalysen (u. a. von Cloudflare und Gartner) dokumentieren eine rapide Verschiebung: Der Anteil an automatisiertem Datenverkehr durch KI-Systeme und autonome Recherche-Bots wächst kontinuierlich. Unternehmen, die ihre digitale Infrastruktur frühzeitig auf strukturierte Maschinenlesbarkeit und Webhook-Gateways ausrichten, sichern sich den schnellsten Zugang zu Neugeschäft.
      </p>
    </div>
  </div>
</section>"""

new_trend_section = """<!-- REALER BELEG & TREND -->
<section class="sec">
  <div class="wrap">
    <div class="fu" style="text-align:center;max-width:700px;margin:0 auto 48px;">
      <span class="ey">Markt-Entwicklung</span>
      <div class="rule c"></div>
      <h2>Der Trend ist <em>messbar.</em></h2>
      <p style="font-size:16px;color:var(--text);line-height:1.75;margin-top:16px;">
        Zwei unabhängig verifizierbare Belege verdeutlichen die fundamentale Verschiebung von menschlichem Klick-Traffic hin zu autonomer Machine-to-Machine-Interaktion:
      </p>
    </div>

    <div class="fg2 fu d1" style="gap:24px;max-width:960px;margin:0 auto;">
      <!-- Card 1: Global (Cloudflare) -->
      <div class="glass-card" style="padding:32px;border:1px solid var(--border);display:flex;flex-direction:column;">
        <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">Globaler Datenverkehr</div>
        <h3 style="font-size:18px;color:var(--dark);margin-bottom:12px;font-family:var(--display);font-weight:600;">Mehr Bots als Menschen im Netz</h3>
        <p style="font-size:14px;color:var(--text);line-height:1.65;margin-bottom:16px;">
          Laut Auswertungen von <strong>Cloudflare</strong> hat automatisierter Bot-Traffic im Juni 2026 erstmals den menschlichen Internetverkehr überholt (<strong>57,5 % aller weltweiten HTTP-Anfragen</strong>). Der Anteil der Crawler-Anfragen speziell für KI-Systeme stieg von 22 % (Frühjahr 2025) auf 52 % im Juni 2026 &ndash; Haupttreiber sind autonome KI-Agenten.
        </p>
        <div style="margin-top:auto;font-size:12px;color:var(--muted);">
          Quelle: <a href="https://radar.cloudflare.com/" target="_blank" rel="noopener" style="color:var(--gold);text-decoration:underline;">Cloudflare Radar</a> / <a href="https://www.it-daily.net/shortnews/bot-traffic-internet-datenverkehr" target="_blank" rel="noopener" style="color:var(--muted);text-decoration:underline;">it-daily Bericht</a>
        </div>
      </div>

      <!-- Card 2: Regional (RIS Österreich) -->
      <div class="glass-card" style="padding:32px;border:1px solid var(--border-gold);background:#FAF8F3;display:flex;flex-direction:column;">
        <div style="font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">DACH-Praxisfall (Österreich)</div>
        <h3 style="font-size:18px;color:var(--dark);margin-bottom:12px;font-family:var(--display);font-weight:600;">KI-Bots überlasten Bundes-Server</h3>
        <p style="font-size:14px;color:var(--text);line-height:1.65;margin-bottom:16px;">
          Das österreichische <strong>Rechtsinformationssystem des Bundes (RIS)</strong> hatte im August 2026 akute Kapazitätsprobleme bis hin zu zeitweisen Ausfällen: Die sprunghaft gestiegene Zahl automatisierter KI-Bot-Zugriffe überlastete die Infrastruktur &ndash; offiziell vom Bundeskanzleramt bestätigt.
        </p>
        <div style="margin-top:auto;font-size:12px;color:var(--muted);">
          Quelle: <a href="https://orf.at/stories/3439709/" target="_blank" rel="noopener" style="color:var(--gold);text-decoration:underline;">ORF.at Bericht (August 2026)</a>
        </div>
      </div>
    </div>
  </div>
</section>"""

content = content.replace(old_trend_section, new_trend_section)

with open(deep_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("Updated trend section with Cloudflare & ORF/RIS proof cards")

# 2. Update _redirects for 301 apex-to-www redirection
redirects_file = os.path.join(base_dir, "_redirects")
with open(redirects_file, 'r', encoding='utf-8') as f:
    red_content = f.read()

apex_redirect_rule = """http://stefanwurzer.at/* https://www.stefanwurzer.at/:splat 301!
https://stefanwurzer.at/* https://www.stefanwurzer.at/:splat 301!

"""

if "http://stefanwurzer.at/*" not in red_content:
    red_content = apex_redirect_rule + red_content
    with open(redirects_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(red_content)
    print("Added apex-to-www 301 rules in _redirects")
