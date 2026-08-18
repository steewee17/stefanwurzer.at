import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\b2b-lead-pipeline\index.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix mojibake in the file first just in case
replacements = {
    'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¼': 'ü', 'ÃŸ': 'ß',
    'Ã„': 'Ä', 'Ã–': 'Ö', 'Ãœ': 'Ü', 'â€“': '–',
    'â€ž': '„', 'â€œ': '“', 'â€': '”', 'â€™': '’'
}
for k, v in replacements.items():
    content = content.replace(k, v)

# The target block to replace
target_pattern = r'<div class="fu d1 glass-card" style="text-align:center; padding:40px; max-width:800px; margin:0 auto; border:1px solid var\(--gold\);">.*?Zur Case Study\s*→?</a>\s*</div>'

new_block = """<div class="fu d1 glass-card" style="text-align:center; padding:40px; max-width:800px; margin:0 auto; border:1px solid var(--gold);">
        <span class="ey" style="justify-content:center;margin-bottom:12px;">Custom Engineering / Advanced Use Case</span>
        <h3 style="font-family:var(--display); font-size:24px; color:var(--dark); margin-bottom:12px;">Reicht ein Standard-Filter nicht aus?</h3>
        <p style="font-size:15px; color:var(--dark); max-width:650px; margin:0 auto 24px;">Unsere standardisierte B2B-Pipeline filtert schnell und zuverlässig nach harten Fakten (Branche, Größe, Rolle). Doch was, wenn Ihre Nische vielschichtiger ist? Erfahren Sie, wie wir für die METEK GmbH (Premium-Innenausbau) eine hochspezialisierte <strong>Custom-KI</strong> entwickelt haben, die sogar Branchenmagazine liest und die <strong>visuelle Ästhetik</strong> von Architektur-Websites bewertet, um exklusive Wunschkunden zu identifizieren.</p>
        <a href="/ki-mitarbeiter/case-premium-leads/" class="btn" style="display:inline-flex;">Zur Premium Case Study →</a>
      </div>"""

content = re.sub(target_pattern, new_block, content, flags=re.DOTALL)

# Fix some known broken chars that might exist
content = content.replace('Ästhetik', 'Ästhetik')

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
