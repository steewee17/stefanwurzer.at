import os

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"
finder_file = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html")

with open(finder_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_text = "Der B2B Lead Finder liefert jeden Morgen geprüfte, angereicherte Wunschkunden direkt in Ihr CRM. Ohne Kalt-Spam, 100 % DSGVO-konform."
new_text = "Der B2B Lead Finder liefert jeden Morgen geprüfte, angereicherte Wunschkunden direkt in Ihr CRM. Bereit für die persönliche Ansprache, 100 % DSGVO-konform."

content = content.replace(old_text, new_text)

with open(finder_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Replaced 'Kalt-Spam' with positive B2B framing.")
