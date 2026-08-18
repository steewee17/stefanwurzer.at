import os

f_path = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at\sitemap.xml"

with open(f_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add <url><loc>https://www.stefanwurzer.at/team/</loc></url> before </urlset>
content = content.replace('</urlset>', '  <url>\n    <loc>https://www.stefanwurzer.at/team/</loc>\n  </url>\n</urlset>')

with open(f_path, 'w', encoding='utf-8') as f:
    f.write(content)
