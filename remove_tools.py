import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'Ein GPT-gestütztes Modul analysiert',
    'Ein intelligentes Sprachmodell analysiert'
)

content = content.replace(
    'Ein KI-Recherchemodul (Perplexity)',
    'Ein KI-Recherchemodul'
)

content = content.replace(
    'ins Pipedrive-CRM der METEK GmbH',
    'in das bestehende CRM-System der METEK GmbH'
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
