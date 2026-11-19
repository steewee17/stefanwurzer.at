# Agent Access & Authentication Policy — stefanwurzer.at

- **Authentication Required:** `none` (Public, Read-Only)
- **OAuth 2.0 / OIDC:** Not applicable (no protected user APIs or login-gated resources)
- **Content-Signal:** `ai-train=yes, search=yes, ai-input=yes`

## Public Endpoints (No Registration or Token Required)

| Endpoint | Format | Purpose |
| :--- | :--- | :--- |
| `https://www.stefanwurzer.at/mcp` | Streamable HTTP (JSON-RPC 2.0) | Remote MCP server (`get_business_info`, `get_offers_and_pricing`, `get_7_phases_framework`, `get_comparison_summary`, `get_contact_channels`) |
| `https://www.stefanwurzer.at/ai/` | HTML / Markdown via `Accept: text/markdown` | Canonical AI Front Door (verified business facts & pricing) |
| `https://www.stefanwurzer.at/compare/` | HTML / Markdown via `Accept: text/markdown` | Dated market comparison matrix |
| `https://www.stefanwurzer.at/developers/` | HTML / Markdown via `Accept: text/markdown` | WebMCP & remote MCP documentation |
| `https://www.stefanwurzer.at/llms.txt` | Markdown | Concise LLM overview |
| `https://www.stefanwurzer.at/.well-known/mcp/server-card.json` | JSON | MCP server discovery card |
| `https://www.stefanwurzer.at/.well-known/api-catalog` | `application/linkset+json` | RFC 9727 / Linkset API catalog |
| `https://www.stefanwurzer.at/.well-known/agent-skills/index.json` | JSON | Agent Skills discovery index |

## Browser-Assisted Consultation Requests

Consultation requests on `/`, `/website/`, `/automation/`, `/foerderung/`, and `/kontakt/` are submitted via standard browser forms or the client-side WebMCP tool `prepare_consultation_request` (which pre-fills the form for explicit human confirmation). Unauthenticated automated form submission is not exposed as a remote API.

## Contact

- **Owner:** Stefan Wurzer (`stefanwurzer innovationservice`)
- **Email:** `info@stefanwurzer.at`
- **Phone:** `+43 677 612 69 625`
