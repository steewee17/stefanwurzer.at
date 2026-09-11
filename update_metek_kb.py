import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Update llms.txt to sharpen METEK positioning
llms_file = os.path.join(base_dir, "llms.txt")
with open(llms_file, 'r', encoding='utf-8') as f:
    llms_content = f.read()

llms_content = llms_content.replace(
    '  - *Premium Custom-KI:* Multimodale KI-Analyse für exklusive Nischen (z.B. Bewertung visueller Ästhetik, semantische Textanalyse, Branchenmagazine) - demonstrated by the METEK Case Study.',
    '  - *Premium Custom-KI (METEK Case Study):* "KI-Qualifizierung im Premium-Segment" für die METEK GmbH (High-End Glas- & Metallbau, Luxus-Innenausbau). Multimodale KI-Analyse zur Bewertung der visuellen Ästhetik von Architektur-Websites, semantische Analyse von Fachmagazinen und automatisierte CRM-Übergabe.'
)

with open(llms_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(llms_content)
print("Updated llms.txt with sharpened METEK Case Study positioning")

# 2. Update ai.txt to sharpen METEK positioning
ai_file = os.path.join(base_dir, "ai.txt")
with open(ai_file, 'r', encoding='utf-8') as f:
    ai_content = f.read()

ai_content = ai_content.replace(
    '- "Premium Lead-Engine (Custom)": Hochspezialisierte KI-Analyse (inkl. semantische Analyse und Bewertung der visuellen Ästhetik) für komplexe Nischen.',
    '- "Premium Lead-Engine (Case Study: METEK GmbH)": Multimodale KI-Analyse (Bewertung visueller Ästhetik von Architektur-Websites & Fachmagazinen) für exklusiven Glas- & Metallbau / Luxus-Innenausbau (METEK GmbH).'
)

with open(ai_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(ai_content)
print("Updated ai.txt with sharpened METEK Case Study positioning")
