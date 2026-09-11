import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update Headline in b2b-lead-finder/index.html
finder_file = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html")
with open(finder_file, 'r', encoding='utf-8') as f:
    finder_content = f.read()

finder_content = finder_content.replace(
    '<h1>Der B2B Lead Finder:<br><em>Wunschkunden im Smart Engineering.</em></h1>',
    '<h1>Der B2B Lead Finder:<br><em>Wunschkunden im High-Tech-Segment.</em></h1>'
)

with open(finder_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(finder_content)
print("Updated headline in b2b-lead-finder/index.html to High-Tech-Segment")

# 2. Add Cross-Link Box in case-premium-leads/index.html
metek_file = os.path.join(base_dir, "ki-mitarbeiter", "case-premium-leads", "index.html")
with open(metek_file, 'r', encoding='utf-8') as f:
    metek_content = f.read()

cross_link_section = """<!-- B2B LEAD FINDER CROSS LINK -->
<section class="sec" style="padding-top:0;">
  <div class="wrap">
    <div class="fu d1 glass-card" style="text-align:center; padding:40px; max-width:800px; margin:0 auto; border:1px solid var(--gold);">
      <span class="ey" style="justify-content:center;margin-bottom:12px;">Standardisierte Lead Engine</span>
      <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:12px;">Suchen Sie nach skalierbarem B2B-Wachstum?</h3>
      <p style="font-size:15px; color:var(--dark); max-width:650px; margin:0 auto 24px;">Während wir für METEK ein hochspezialisiertes Custom-Modell für Nischenarchitektur entwickelt haben, deckt unser <strong>B2B Lead Finder</strong> die automatisierte Lead-Recherche für Industrie-Zulieferer und den Mittelstand ab. Erfahren Sie, wie die <strong>MICADO SMART ENGINEERING GmbH</strong> damit technische Entscheider vollautomatisiert identifiziert und ins CRM übergibt.</p>
      <a href="/ki-mitarbeiter/b2b-lead-finder/" class="btn" style="display:inline-flex;">Zum B2B Lead Finder (Case Study: MICADO) →</a>
    </div>
  </div>
</section>

<!-- FORMULAR -->"""

metek_content = metek_content.replace('<!-- FORMULAR -->', cross_link_section)

with open(metek_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(metek_content)
print("Added cross-link section in case-premium-leads/index.html")
