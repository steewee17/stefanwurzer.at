import os
import re

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Replacements
css_old_card = ".agent-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; transition: transform 0.3s ease, border-color 0.3s ease; display: flex; flex-direction: column; }"
css_new_card = ".agent-card { background: var(--bg); border: 1px solid var(--border); border-radius: 12px; transition: transform 0.3s ease, border-color 0.3s ease; display: flex; flex-direction: column; padding: 32px 24px; }"
content = content.replace(css_old_card, css_new_card)

css_old_img_wrap = ".agent-img-wrap { width: 100%; aspect-ratio: 3/4; overflow: hidden; border-bottom: 1px solid var(--border); background: var(--bg-sec); }"
css_new_img_wrap = ".agent-img-wrap { width: 100px; height: 100px; border-radius: 50%; overflow: hidden; margin-bottom: 24px; border: 2px dashed var(--gold-pale); background: var(--bg-sec); flex-shrink: 0; }"
content = content.replace(css_old_img_wrap, css_new_img_wrap)

css_old_img = ".agent-img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(20%) contrast(1.1); transition: filter 0.3s ease; }"
css_new_img = ".agent-img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(60%) contrast(1.1); transition: filter 0.3s ease; }"
content = content.replace(css_old_img, css_new_img)

css_old_content = ".agent-content { padding: 32px 24px; flex-grow: 1; display: flex; flex-direction: column; }"
css_new_content = ".agent-content { flex-grow: 1; display: flex; flex-direction: column; }"
content = content.replace(css_old_content, css_new_content)

# Additionally, the agent-name flex layout. Let's make the avatar flex aligned if needed, but it's currently a block margin-bottom:24px.
# We have `<div class="agent-name">Kurt <span class="agent-badge">KI-Agent</span></div>`
# To align the avatar and name side by side would be cool, but stacking them is also fine (avatar, then name below).
# Stacking them is exactly what happens since we just set width/height on the wrap.

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
