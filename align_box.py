import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-befaehigung.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<div class="fu" style="max-width:800px;margin:40px auto 0;text-align:center;">\n      <p style="font-size:15px;color:var(--dark);line-height:1.75;padding:24px;border-left:2px solid var(--gold);background:var(--bg-sec);text-align:left;"><strong>Deshalb scheitern'

replacement = '<div class="fu" style="max-width:900px;margin:40px auto 0;text-align:center;">\n      <p style="font-size:15px;color:var(--dark);line-height:1.75;padding:24px;border-left:2px solid var(--gold);background:var(--bg-sec);text-align:left;"><strong>Deshalb scheitern'

if target in content:
    content = content.replace(target, replacement)
else:
    # fallback
    import re
    pattern = r'<div class="fu" style="max-width:800px;margin:40px auto 0;text-align:center;">\s*<p style="font-size:15px;color:var\(--dark\);line-height:1.75;padding:24px;border-left:2px solid var\(--gold\);background:var\(--bg-sec\);text-align:left;"><strong>Deshalb scheitern'
    
    replacement_regex = r'<div class="fu" style="max-width:900px;margin:40px auto 0;text-align:center;">\n      <p style="font-size:15px;color:var(--dark);line-height:1.75;padding:24px;border-left:2px solid var(--gold);background:var(--bg-sec);text-align:left;"><strong>Deshalb scheitern'
    content = re.sub(pattern, replacement_regex, content)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
