import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\team\index.html"
with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update .human-img to have object-position
old_human = ".human-img { width: 140px; height: 140px; border-radius: 50%; object-fit: cover; margin-bottom: 24px; border: 2px solid var(--gold); }"
new_human = ".human-img { width: 140px; height: 140px; border-radius: 50%; object-fit: cover; object-position: center 15%; margin-bottom: 24px; border: 2px solid var(--gold); }"
content = content.replace(old_human, new_human)

# Update .agent-img to have object-position
old_agent = ".agent-img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(60%) contrast(1.1); transition: filter 0.3s ease; }"
new_agent = ".agent-img { width: 100%; height: 100%; object-fit: cover; object-position: center 15%; filter: grayscale(60%) contrast(1.1); transition: filter 0.3s ease; }"
content = content.replace(old_agent, new_agent)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
