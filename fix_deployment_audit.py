import os
import re

base_dir = r"c:\Users\Stefan\Antigravity-Workspace\stefanwurzer.at"

# 1. Clean and fix _redirects
redirects_path = os.path.join(base_dir, "_redirects")
clean_redirects = """/markt / 301
/markt/ / 301
/planung /ki-befaehigung/ 301
/planung/ /ki-befaehigung/ 301
/umsetzung /ki-mitarbeiter/ 301
/umsetzung/ /ki-mitarbeiter/ 301

/strategische-partnerschaft / 301
/strategische-partnerschaft/ / 301
/ki-mitarbeiter/digitale-akquise/* /ki-mitarbeiter/b2b-lead-finder/:splat 301!
/ki-mitarbeiter/digitale-akquise /ki-mitarbeiter/b2b-lead-finder/ 301!
/ki-mitarbeiter/b2b-lead-pipeline/* /ki-mitarbeiter/b2b-lead-finder/:splat 301!
/ki-mitarbeiter/b2b-lead-pipeline /ki-mitarbeiter/b2b-lead-finder/ 301!
"""
with open(redirects_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(clean_redirects)
print("Fixed _redirects")

# 2. Fix sitemap.xml
sitemap_path = os.path.join(base_dir, "sitemap.xml")
clean_sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.stefanwurzer.at/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/ki-befaehigung/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/ki-mitarbeiter/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/team/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/ki-mitarbeiter/b2b-lead-finder/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/ki-mitarbeiter/case-premium-leads/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/ki-mitarbeiter/propstack-agent/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/kontakt/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/datenschutz/</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/agb/</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://www.stefanwurzer.at/cookie-richtlinie/</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>
"""
with open(sitemap_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(clean_sitemap)
print("Fixed sitemap.xml")

# 3. Fix canonicals & meta in ki-mitarbeiter/b2b-lead-finder/index.html
finder_path = os.path.join(base_dir, "ki-mitarbeiter", "b2b-lead-finder", "index.html")
with open(finder_path, 'r', encoding='utf-8') as f:
    finder_content = f.read()

finder_content = finder_content.replace(
    'href="https://www.stefanwurzer.at/ki-mitarbeiter/digitale-akquise/"',
    'href="https://www.stefanwurzer.at/ki-mitarbeiter/b2b-lead-finder/"'
)
finder_content = finder_content.replace(
    'content="https://www.stefanwurzer.at/ki-mitarbeiter/digitale-akquise/"',
    'content="https://www.stefanwurzer.at/ki-mitarbeiter/b2b-lead-finder/"'
)
finder_content = finder_content.replace(
    '"url": "https://www.stefanwurzer.at/ki-mitarbeiter/digitale-akquise/"',
    '"url": "https://www.stefanwurzer.at/ki-mitarbeiter/b2b-lead-finder/"'
)
with open(finder_path, 'w', encoding='utf-8') as f:
    f.write(finder_content)
print("Fixed b2b-lead-finder canonicals")

# 4. Fix canonicals & JSON-LD in ki-mitarbeiter/case-premium-leads/index.html
metek_path = os.path.join(base_dir, "ki-mitarbeiter", "case-premium-leads", "index.html")
with open(metek_path, 'r', encoding='utf-8') as f:
    metek_content = f.read()

metek_content = metek_content.replace(
    'href="https://www.stefanwurzer.at/ki-mitarbeiter/digitale-akquise/"',
    'href="https://www.stefanwurzer.at/ki-mitarbeiter/case-premium-leads/"'
)
metek_content = metek_content.replace(
    'content="https://www.stefanwurzer.at/ki-mitarbeiter/digitale-akquise/"',
    'content="https://www.stefanwurzer.at/ki-mitarbeiter/case-premium-leads/"'
)
metek_content = metek_content.replace(
    '"url": "https://www.stefanwurzer.at/ki-mitarbeiter/digitale-akquise/"',
    '"url": "https://www.stefanwurzer.at/ki-mitarbeiter/case-premium-leads/"'
)
metek_content = metek_content.replace(
    '"description": "Ein Automatisierungs-Flow sucht Leads, eine KI qualifiziert diese strikt nach Wunschkundenprofil (ICP), reichert Kontaktdaten an und legt sie mundgerecht im CRM ab."',
    '"description": "Case Study: Wie die METEK GmbH durch multimodale KI-Analyse (Semantik & visuelle Ästhetik) exklusive Architektur-Leads für den Premium-Innenausbau identifiziert."'
)
with open(metek_path, 'w', encoding='utf-8') as f:
    f.write(metek_content)
print("Fixed case-premium-leads canonicals")

# 5. Add Klaro, GTM, Canonical and OpenGraph to team/index.html
team_path = os.path.join(base_dir, "team", "index.html")
with open(team_path, 'r', encoding='utf-8') as f:
    team_content = f.read()

team_header_insert = """<!-- Cookie Consent: Klaro -->
<script defer src="/klaro-config.js"></script>
<script defer src="https://cdn.kiprotect.com/klaro/v0.7/klaro.js"></script>

<!-- Google tag (gtag.js) — loads only after consent via Klaro -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'analytics_storage': 'denied'
  });
  gtag('js', new Date());
  gtag('config', 'G-XL6E22PCJC');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XL6E22PCJC"></script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Team & KI-Agenten | Stefan Wurzer</title>
<meta name="description" content="Lernen Sie unser hybrides Kernteam kennen. Wir verbinden Prozess-Architektur mit digitalen KI-Experten durch kontrollierte Autonomie und das Least-Privilege-Prinzip.">
<meta name="keywords" content="KI Agenten, Team, KI-Mitarbeiter, Stefan Wurzer, Automatisierung, KMU">
<meta name="author" content="Stefan Wurzer">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.stefanwurzer.at/team/">
<link rel="alternate" hreflang="de-AT" href="https://www.stefanwurzer.at/team/">
<link rel="alternate" hreflang="de" href="https://www.stefanwurzer.at/team/">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.stefanwurzer.at/team/">
<meta property="og:title" content="Team & KI-Agenten | Stefan Wurzer">
<meta property="og:description" content="Lernen Sie unser hybrides Kernteam kennen. Wir verbinden Prozess-Architektur mit digitalen KI-Experten durch kontrollierte Autonomie.">
<meta property="og:locale" content="de_AT">
<meta name="twitter:card" content="summary_large_image">"""

old_team_head = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Team & KI-Agenten | Stefan Wurzer</title>
<meta name="description" content="Lernen Sie unser hybrides Kernteam kennen. Wir verbinden Prozess-Architektur mit digitalen KI-Experten durch kontrollierte Autonomie und das Least-Privilege-Prinzip.">
<meta name="keywords" content="KI Agenten, Team, KI-Mitarbeiter, Stefan Wurzer, Automatisierung, KMU">"""

if old_team_head in team_content:
    team_content = team_content.replace(old_team_head, team_header_insert)
    with open(team_path, 'w', encoding='utf-8') as f:
        f.write(team_content)
    print("Fixed team/index.html head & tracking")
else:
    print("Could not match old team head directly, checking...")

print("All audit fixes applied.")
