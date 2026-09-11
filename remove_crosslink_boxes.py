import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Remove from ki-mitarbeiter/b2b-lead-finder/index.html
finder_file = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html")
with open(finder_file, 'r', encoding='utf-8') as f:
    finder_content = f.read()

box_finder = """<!-- CASE STUDY CROSS LINK -->
<section class="sec" style="padding-top:0;">
  <div class="wrap">
    <div class="fu d1 glass-card" style="text-align:center; padding:40px; max-width:800px; margin:0 auto; border:1px solid var(--gold);">
        <span class="ey" style="justify-content:center;margin-bottom:12px;">Custom Engineering / Advanced Use Case</span>
        <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:12px;">Reicht ein Standard-Filter nicht aus?</h3>
        <p style="font-size:15px; color:var(--dark); max-width:650px; margin:0 auto 24px;">Unser standardisierter B2B Lead Finder filtert schnell und zuverlässig nach harten Fakten (Branche, Größe, Rolle). Doch was, wenn Ihre Nische vielschichtiger ist? Erfahren Sie, wie wir für die METEK GmbH (Premium-Innenausbau) eine hochspezialisierte <strong>Custom-KI</strong> entwickelt haben, die sogar Branchenmagazine liest und die <strong>visuelle Ästhetik</strong> von Architektur-Websites bewertet, um exklusive Wunschkunden zu identifizieren.</p>
        <a href="/ki-mitarbeiter/case-premium-leads/" class="btn" style="display:inline-flex;">Zur Premium Case Study →</a>
      </div>
  </div>
</section>

"""

finder_content = finder_content.replace(box_finder, "")

with open(finder_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(finder_content)
print("Removed cross-link box from b2b-lead-finder/index.html")

# 2. Remove from ki-mitarbeiter/case-premium-leads/index.html
metek_file = os.path.join(base_dir, "ki-mitarbeiter", "case-premium-leads", "index.html")
with open(metek_file, 'r', encoding='utf-8') as f:
    metek_content = f.read()

box_metek = """<!-- B2B LEAD FINDER CROSS LINK -->
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

"""

metek_content = metek_content.replace(box_metek, "")

with open(metek_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(metek_content)
print("Removed cross-link box from case-premium-leads/index.html")
