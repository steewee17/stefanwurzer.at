import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Target section definition
target = """<section class="section" style="padding-top: 0; padding-bottom: 80px;">
  <div class="c">
    <!-- DATENHOHEIT & KONTROLLE (Andrei) -->
    <div class="fu d2" style="background: var(--bg-warm); border: 1px solid var(--border); border-radius: 12px; padding: 40px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">"""

# If exactly found, replace. Otherwise regex.
replacement = """<section class="section" style="padding-top: 80px; padding-bottom: 80px;">
  <div class="c">
    <!-- DATENHOHEIT & KONTROLLE (Andrei) -->
    <div class="fu d2" style="text-align: center; max-width: 800px; margin: 0 auto;">"""

if target in content:
    content = content.replace(target, replacement)
else:
    # Use regex for flexibility if spaces differ
    pattern = r'<section class="section" style="padding-top:\s*0;\s*padding-bottom:\s*80px;">\s*<div class="c">\s*<!-- DATENHOHEIT & KONTROLLE \(Andrei\) -->\s*<div class="fu d2" style="background:[^>]+>'
    content = re.sub(pattern, replacement, content)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
