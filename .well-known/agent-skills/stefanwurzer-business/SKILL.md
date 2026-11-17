---
name: stefanwurzer-business
description: Query verified business facts, 7-Phasen-Prozess-Check, website, automation, and Land Tirol funding services for stefanwurzer.at via MCP or semantic endpoints.
---

# stefanwurzer.at — Agent Skill

Use the remote Streamable HTTP MCP endpoint at `https://www.stefanwurzer.at/mcp` (JSON-RPC 2.0 `POST`) to retrieve structured, dated facts:

- `get_business_info`: Identity, WKO certification, fit statement, location, service area, contact.
- `get_offers_and_pricing`: 7-Phasen-Prozess-Check (€ 2,400 / € 480 net with 80% WKO funding), Website, Automation & Land Tirol grant services (€ 110/h, € 0 monthly agency retainer).
- `get_7_phases_framework`: Phases 01–07 value-chain framework.
- `get_comparison_summary`: Fact-only market comparison from `/compare/`.
- `get_contact_channels`: Verified contact channels (`/kontakt/#formular`, email, phone).

## Canonical Web Endpoints
- AI Front Door: `https://www.stefanwurzer.at/ai/`
- Comparison: `https://www.stefanwurzer.at/compare/`
- Developers & WebMCP: `https://www.stefanwurzer.at/developers/`
- Markdown Summary: `https://www.stefanwurzer.at/llms.txt`
