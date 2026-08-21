import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the rule div just before the Datenhoheit block
pattern = r'<div class="rule c" style="margin: 0 auto 80px auto;"></div>\s*<!-- DATENHOHEIT'
replacement = '<!-- DATENHOHEIT'

content = re.sub(pattern, replacement, content)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
