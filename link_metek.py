import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\ki-mitarbeiter\case-premium-leads\index.html"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<span class="ey">Case Study: METEK GmbH</span>',
    '<span class="ey">Case Study: <a href="https://www.metek.com" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">METEK GmbH</a></span>'
)

# Fix the subtext that was missed previously
target_subtext = "Die Neukundengewinnung ist ein Problem, das nie verschwindet. Lösen Sie es mit einem System, das nie schläft. Von der automatisierten Recherche über die KI-Qualifizierung nach Ihrem Wunschkundenprofil (ICP) bis zur nahtlosen CRM-Übergabe."
# Oh wait, my previous regex failed because the text was `nahtlosen Nahtlose CRM-Übergabe`! Look at the output of the select string: `bis zur nahtlosen Nahtlose CRM-Übergabe.`!
import re
content = re.sub(
    r'Die Neukundengewinnung ist ein Problem.*CRM-Übergabe\.</p>',
    'Wie identifiziert man hochspezialisierte Architekten für den gehobenen Innenausbau (Luxus), die man nicht einfach "ergoogeln" kann? Diese Case Study zeigt, wie die METEK GmbH durch eine Kombination aus semantischer Textanalyse, Medien-Recherche und visueller Ästhetik-Bewertung ihren Vertrieb revolutioniert.</p>',
    content, flags=re.DOTALL
)

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
