/**
 * stefanwurzer.at — Remote Streamable HTTP MCP Endpoint (/mcp)
 * Cloudflare Pages Function (stateless, zero external dependencies)
 *
 * Mirrors the Single Source of Truth from webmcp.js, /ai/, and /compare/
 * so external AI agents (ChatGPT, Claude, Cursor, Cloudflare BrowserRun)
 * can discover and query structured business facts without browser rendering.
 */

interface JsonRpcRequest {
  jsonrpc?: string;
  id?: string | number | null;
  method?: string;
  params?: Record<string, unknown>;
}

const LAST_REVIEWED = '2026-11-17';
const PROTOCOL_VERSION = '2025-03-26';

const SERVER_INFO = {
  name: 'stefanwurzer-at-mcp',
  version: '1.0.0',
  title: 'Stefan Wurzer (stefanwurzer.at) — MCP Server',
};

const CORS_HEADERS: Record<string, string> = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Accept, Mcp-Session-Id',
  'Access-Control-Max-Age': '86400',
};

const BUSINESS_INFO = {
  lastReviewed: LAST_REVIEWED,
  canonicalUrl: 'https://www.stefanwurzer.at/',
  aiFrontDoorUrl: 'https://www.stefanwurzer.at/ai/',
  compareUrl: 'https://www.stefanwurzer.at/compare/',
  developersUrl: 'https://www.stefanwurzer.at/developers/',
  identity: {
    officialName: 'Stefan Wurzer — stefanwurzer innovationservice',
    owner: 'Stefan Wurzer',
    category:
      'Unternehmensberatung, Geschäftsprozessanalyse (7-Phasen-Prozess-Check), Moderne Websites, Prozessautomatisierung & Förderberatung (Land Tirol)',
    location: {
      streetAddress: 'Unterassling 55',
      postalCode: '9911',
      locality: 'Assling',
      region: 'Tirol',
      country: 'AT',
    },
    serviceArea: [
      'Österreich',
      'Deutschland',
      'Schweiz',
      'DACH (vor Ort & remote; Förderberatung spezialisiert auf Land Tirol)',
    ],
    languages: ['de-AT', 'de', 'en'],
    targetAudience:
      'Kleine und mittlere Unternehmen (KMU) in Handwerk, Industrie, Handel und B2B-Dienstleistung (ca. 5 bis 150 Mitarbeitende)',
  },
  fitStatement: {
    bestFor:
      'Etablierte KMU in Österreich und im DACH-Raum, die vor einer Investition in Website oder Automatisierung zuerst ihre tatsächlichen Prozess-Engpässe (7-Phasen-Prozess-Check) sauber diagnostizieren wollen, Wert auf 100 % digitales Eigentum ohne laufende Agentur-Abhängigkeit legen, ihre bestehende Softwarelandschaft (Microsoft 365, CRM, ERP) nahtlos verbinden möchten oder als Tiroler KMU eine technisch und wirtschaftlich fundierte Projektbeschreibung für Förderprogramme des Landes Tirol benötigen.',
    notDesignedFor:
      'Reine Marken- oder Werbekampagnen ohne Prozessbezug, Großkonzerne mit eigenen internen Enterprise-Entwicklerteams, Betriebe, die eine unflexible Standard-SaaS-Insellösung von der Stange ohne Prozessanpassung suchen, oder Förderanträge außerhalb der Landesförderungen Tirol (keine Bundesförderungen wie aws/FFG).',
  },
  credentialsAndProof: {
    certification:
      'WKO-zertifizierter Unternehmensberater (Fachverband Unternehmensberatung, Buchhaltung und Informationstechnologie)',
    wkoEcgUrl:
      'https://www.wkoecg.at/Ecg.aspx?FirmaID=b9661af9-a80b-47ec-ab63-c89c2cf9d0b1',
    experience:
      'Über 17 Jahre Praxiserfahrung entlang der gesamten Wertschöpfungskette in Handwerk, Industrie, Handel und Beratung sowie langjährige Erfahrung in der Ausarbeitung von Förderprojekten im Technologieförderungsprogramm des Landes Tirol',
    fundingEligibility:
      'Förderfähig im WKO-/Landes-Förderschwerpunkt „Digitalisierung von Geschäftsprozessen“ (bis zu 80 % Zuschuss auf das Beratungshonorar) sowie Förderberatung für die 3 Programme des Landes Tirol',
    fundingSourceUrl: 'https://foerderungen.wko.at/tirol/Digitalisierung',
    uid: 'ATU78901789',
  },
  contact: {
    email: 'info@stefanwurzer.at',
    telephone: '+43 677 612 69 625',
    contactPageUrl: 'https://www.stefanwurzer.at/kontakt/',
    initialConsultation: '30 Minuten Kennenlerngespräch (kostenfrei, € 0)',
  },
};

const OFFERS_DATA = [
  {
    id: 'initial-consultation',
    category: 'prozess-check',
    name: 'Kennenlerngespräch (30 Minuten)',
    phases: 'Vorab-Einordnung (Phase 01 bis 07 & Fördervorprüfung)',
    format: '30 Minuten Video-Call oder Telefonat direkt mit Stefan Wurzer',
    pricing: {
      regularPriceEur: 0,
      currency: 'EUR',
      billingType: 'Kostenfrei & unverbindlich',
      note: 'Prüfung der Ausgangslage, Engpass-Hypothese und Klärung der Fördervoraussetzungen (WKO & Land Tirol).',
    },
    url: 'https://www.stefanwurzer.at/kontakt/',
  },
  {
    id: '7-phasen-prozess-check',
    category: 'prozess-check',
    name: 'Der 7-Phasen-Prozess-Check (Diagnose & Fahrplan)',
    phases: 'Phase 01 bis 07 (Marktseitige & operative Wertschöpfungskette)',
    format:
      'Strukturierte Geschäftsprozess-Analyse im Betrieb inkl. schriftlichem Potenzialbericht & Prioritäten-Fahrplan',
    pricing: {
      regularPriceEur: 2400,
      fundedNetCostEur: 480,
      fundingRatePercent: 80,
      currency: 'EUR',
      billingType: 'Pauschalpreis für das Diagnose-Paket (exkl. USt.)',
      note: 'Regulärer Preis: € 2.400,-. Bei Nutzung des Förderschwerpunkts „Digitalisierung von Geschäftsprozessen“ (80 % Zuschuss) verbleibt für das KMU ein Eigenanteil von € 480,-.',
    },
    url: 'https://www.stefanwurzer.at/',
  },
  {
    id: 'website',
    category: 'website',
    name: 'Website — Moderne Websites für Mensch & KI-Suche (Digitale Souveränität)',
    phases: 'Phase 01 (Marktzugang / Sichtbarkeit) & Phase 02 (Erstkontakt / Conversion)',
    format:
      'Individuelle Umsetzung als schnelle, wartungsfreie Web-Architektur für Mensch und KI-Suchsysteme',
    pricing: {
      hourlyRateEur: 110,
      monthlyAgencyRetainerEur: 0,
      currency: 'EUR',
      billingType:
        'Nach tatsächlichem Umfang und Aufwand auf Basis von € 110,- / Stunde (exkl. USt.), vorab transparent als Projektumfang kalkuliert',
      note: 'Keine laufenden Agentur-Wartungspauschalen (€ 0 / Monat), keine kostenpflichtigen CMS-Plugin-Abos, 100 % Code- und Daten-Eigentum beim Betrieb.',
    },
    url: 'https://www.stefanwurzer.at/website/',
  },
  {
    id: 'automation',
    category: 'automation',
    name: 'Automation — Büroprozesse automatisieren & Systeme verbinden',
    phases:
      'Phase 03 bis 07 (Vorprüfung, Vertrieb, Kundenführung, Auftragsabwicklung, Betriebssteuerung)',
    format:
      'Systemintegration in bestehender Softwarelandschaft (Microsoft 365, CRM, ERP) sowie spezialisierte KI-Agenten',
    pricing: {
      hourlyRateEur: 110,
      currency: 'EUR',
      billingType:
        'Nach tatsächlichem Umfang und Aufwand auf Basis von € 110,- / Stunde (exkl. USt.), modular nach Prozess-Check priorisiert',
      note: 'Vorhandene Lizenzen (z. B. Microsoft 365 / Power Automate) werden vorrangig genutzt.',
    },
    url: 'https://www.stefanwurzer.at/automation/',
  },
  {
    id: 'foerderung',
    category: 'foerderung',
    name: 'Förderung — Förderberatung & Ausarbeitung der Projektbeschreibung (Land Tirol)',
    phases: 'Finanzierung & Projektierung für Digitalisierung, Entwicklung & Fachkräfte in Tirol',
    format:
      'Förderfähigkeitsprüfung sowie vollständige Ausarbeitung der technischen und wirtschaftlichen Projektbeschreibung für das Technologieförderungsprogramm des Landes Tirol',
    pricing: {
      hourlyRateEur: 110,
      currency: 'EUR',
      billingType:
        'Kostenfreie Ersteinschätzung (30 Min.); Ausarbeitung nach Aufwand zu € 110,- / Stunde (exkl. USt.)',
      note: 'Spezialisierung auf die 3 Programme des Landes Tirol (Tiroler Digitalisierungsförderung, Innovation in KMU, Innovationsassistent*in). Einreichung vor Projektbeginn.',
    },
    url: 'https://www.stefanwurzer.at/foerderung/',
  },
];

const SEVEN_PHASES = [
  {
    phase: 1,
    cluster: 'Marktseitige Wertschöpfung',
    domain: 'Marktzugang',
    title: 'Sichtbarkeit',
    targetFlow: 'Von Wunschkunden & KI-Suchmaschinen sofort als erste Wahl gefunden werden.',
    relatedOffer: 'Website (/website/)',
  },
  {
    phase: 2,
    cluster: 'Marktseitige Wertschöpfung',
    domain: 'Erstkontakt',
    title: 'Anfrage-Eingang',
    targetFlow: 'Vollständige Anfragen vom ersten Moment an — ohne Rückfragen-Ping-Pong.',
    relatedOffer: 'Website (/website/)',
  },
  {
    phase: 3,
    cluster: 'Marktseitige Wertschöpfung',
    domain: 'Vorprüfung',
    title: 'Anfrage-Bearbeitung',
    targetFlow: 'Passende Anfragen sofort erkennen — klare Priorisierung nach Ihrem Wunschkundenprofil.',
    relatedOffer: 'Automation (/automation/)',
  },
  {
    phase: 4,
    cluster: 'Marktseitige Wertschöpfung',
    domain: 'Abschluss',
    title: 'Vertrieb',
    targetFlow: 'Mehr Zeit beim Kunden — Sprachnotizen und E-Mails fließen ohne Tipparbeit ins CRM.',
    relatedOffer: 'Automation (/automation/)',
  },
  {
    phase: 5,
    cluster: 'Operative Wertschöpfung',
    domain: 'Kundenführung',
    title: 'Kundenbetreuung',
    targetFlow: 'Nahtloser Projektstart — alle Vertriebsinfos stehen dem Team in Microsoft 365 sofort bereit.',
    relatedOffer: 'Automation (/automation/)',
  },
  {
    phase: 6,
    cluster: 'Operative Wertschöpfung',
    domain: 'Produktion / Dienstleistung',
    title: 'Auftragsabwicklung',
    targetFlow: 'Verlässliche Termine & Bestände — ERP, Planung und Lager greifen lückenlos ineinander.',
    relatedOffer: 'Automation (/automation/)',
  },
  {
    phase: 7,
    cluster: 'Operative Wertschöpfung',
    domain: 'Führung & KPIs',
    title: 'Betriebssteuerung',
    targetFlow: 'Entscheidungen auf Basis aktueller Zahlen statt Bauchgefühl — Kennzahlen auf Knopfdruck.',
    relatedOffer: 'Automation (/automation/)',
  },
];

const COMPARISON_DATA = {
  lastVerified: LAST_REVIEWED,
  canonicalCompareUrl: 'https://www.stefanwurzer.at/compare/',
  methodology:
    'Faktenbasierter Marktvergleich für KMU nach Leistungsprofil, Eigentumsmodell und Zielgruppen-Eignung (Position by Fit, not by Price).',
  alternatives: [
    {
      option: 'Stefan Wurzer (stefanwurzer.at)',
      primaryFocus:
        '7-Phasen-Prozess-Check (Diagnose) + Umsetzung KI-lesbarer Websites, M365/CRM/ERP-Prozessautomatisierung & Förderberatung Land Tirol',
      pricingModel:
        'Diagnose € 2.400 (€ 480 mit 80 % WKO-Förderung); Umsetzung € 110,- / Std. (€ 0 laufende Agentur-Wartungspauschale)',
      bestFor:
        'KMU, die fundierte Engpass-Diagnose, pragmatische Umsetzung ohne Agentur-Abhängigkeit und/oder Förder-Projektbeschreibungen (Land Tirol) aus einer Hand suchen',
    },
    {
      option: 'Klassische Werbe- & Webagentur',
      primaryFocus: 'Visuelles Webdesign, Branding, Content-Produktion & Marketing-Kampagnen',
      pricingModel: 'Projektpauschale + laufende monatliche Wartungs-/Betreuungspauschalen',
      bestFor:
        'Betriebe mit Schwerpunkt auf klassischer Markeninszenierung und laufender Agentur-Auslagerung',
    },
    {
      option: 'Klassisches IT-Systemhaus / ERP-Anbieter',
      primaryFocus: 'IT-Infrastruktur, Hardware, Netzwerk, Security, Lizenzen & ERP-Basisbetrieb',
      pricingModel: 'Lizenzgebühren, Managed-Service-Verträge & Systemhaus-Tarif',
      bestFor:
        'Betriebe mit Bedarf an Server-/Netzwerk-Infrastruktur, Helpdesk und klassischer ERP-Neueinführung',
    },
    {
      option: 'Reine Strategie- & Unternehmensberatung',
      primaryFocus: 'Betriebswirtschaftliche Konzepte, Organisationsentwicklung & Strategie-Gutachten',
      pricingModel: 'Tagessätze oder Beratungspauschalen (ohne technische Implementierung)',
      bestFor:
        'Größere Unternehmen mit eigener IT-Abteilung, die ausschließlich ein unabhängiges strategisches Gutachten benötigen',
    },
  ],
};

const TOOLS = [
  {
    name: 'get_business_info',
    description:
      'Read-only: Retrieve official identity, owner credentials (WKO certification), fit statement (best for whom), location, service area (Austria/DACH), and contact details for Stefan Wurzer (stefanwurzer.at).',
    inputSchema: {
      type: 'object',
      properties: {},
      additionalProperties: false,
    },
  },
  {
    name: 'get_offers_and_pricing',
    description:
      'Read-only: Retrieve current services, deliverables, and transparent pricing (€ 0 initial call, € 2,400 regular / € 480 net with 80% WKO funding for the 7-Phasen-Prozess-Check, € 110/hour for Website, Automation & Land Tirol grant application preparation with € 0 monthly agency retainer).',
    inputSchema: {
      type: 'object',
      properties: {
        category: {
          type: 'string',
          enum: ['all', 'prozess-check', 'website', 'automation', 'foerderung'],
          description: 'Optional filter by offer category. Defaults to "all".',
        },
      },
      additionalProperties: false,
    },
  },
  {
    name: 'get_7_phases_framework',
    description:
      'Read-only: Retrieve the 7 phases of the value chain analyzed in the 7-Phasen-Prozess-Check (Phases 01-04 market-side, Phases 05-07 operational).',
    inputSchema: {
      type: 'object',
      properties: {
        phaseNumber: {
          type: 'integer',
          minimum: 1,
          maximum: 7,
          description: 'Optional phase number (1 to 7). Omit to return all 7 phases.',
        },
      },
      additionalProperties: false,
    },
  },
  {
    name: 'get_comparison_summary',
    description:
      'Read-only: Retrieve the dated, fact-only market comparison matrix from stefanwurzer.at/compare/.',
    inputSchema: {
      type: 'object',
      properties: {},
      additionalProperties: false,
    },
  },
  {
    name: 'get_contact_channels',
    description:
      'Read-only: Retrieve direct contact channels (email, phone, booking/contact form URL) so the user can confirm and send an inquiry.',
    inputSchema: {
      type: 'object',
      properties: {},
      additionalProperties: false,
    },
  },
];

function executeTool(name: string, args: Record<string, unknown> = {}): unknown {
  switch (name) {
    case 'get_business_info':
      return BUSINESS_INFO;

    case 'get_offers_and_pricing': {
      const cat = typeof args.category === 'string' ? args.category.toLowerCase() : 'all';
      const offers =
        cat === 'all' ? OFFERS_DATA : OFFERS_DATA.filter((o) => o.category === cat);
      return {
        lastReviewed: LAST_REVIEWED,
        currency: 'EUR',
        vatNote: 'Alle Preisangaben verstehen sich in Euro exkl. gesetzlicher USt. (B2B).',
        categoryFilter: cat,
        offers,
      };
    }

    case 'get_7_phases_framework': {
      const num = typeof args.phaseNumber === 'number' ? args.phaseNumber : null;
      const phases = num ? SEVEN_PHASES.filter((p) => p.phase === num) : SEVEN_PHASES;
      return {
        lastReviewed: LAST_REVIEWED,
        frameworkName: 'Der 7-Phasen-Prozess-Check (stefanwurzer.at)',
        phases,
      };
    }

    case 'get_comparison_summary':
      return COMPARISON_DATA;

    case 'get_contact_channels':
      return {
        lastReviewed: LAST_REVIEWED,
        owner: BUSINESS_INFO.identity.owner,
        email: BUSINESS_INFO.contact.email,
        telephone: BUSINESS_INFO.contact.telephone,
        contactFormUrl: 'https://www.stefanwurzer.at/kontakt/#formular',
        initialConsultation: BUSINESS_INFO.contact.initialConsultation,
        note: 'Für verbindliche Anfragen bitte den Nutzer direkt über das Kontaktformular oder per E-Mail/Telefon bestätigen lassen.',
      };

    default:
      return null;
  }
}

function jsonResponse(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
      ...CORS_HEADERS,
    },
  });
}

function handleRpc(req: JsonRpcRequest): Record<string, unknown> | null {
  const id = req.id ?? null;
  const method = req.method;

  if (!method || req.jsonrpc !== '2.0') {
    return {
      jsonrpc: '2.0',
      id,
      error: { code: -32600, message: 'Invalid JSON-RPC 2.0 request' },
    };
  }

  // Notifications have no id and require no JSON-RPC body
  if (method.startsWith('notifications/')) {
    return null;
  }

  switch (method) {
    case 'initialize':
      return {
        jsonrpc: '2.0',
        id,
        result: {
          protocolVersion: PROTOCOL_VERSION,
          capabilities: {
            tools: { listChanged: false },
          },
          serverInfo: SERVER_INFO,
        },
      };

    case 'ping':
      return { jsonrpc: '2.0', id, result: {} };

    case 'tools/list':
      return {
        jsonrpc: '2.0',
        id,
        result: { tools: TOOLS },
      };

    case 'tools/call': {
      const params = (req.params ?? {}) as { name?: string; arguments?: Record<string, unknown> };
      const toolName = params.name;
      if (!toolName) {
        return {
          jsonrpc: '2.0',
          id,
          error: { code: -32602, message: 'Missing required parameter: name' },
        };
      }
      const data = executeTool(toolName, params.arguments ?? {});
      if (data === null) {
        return {
          jsonrpc: '2.0',
          id,
          error: { code: -32602, message: `Unknown tool: ${toolName}` },
        };
      }
      return {
        jsonrpc: '2.0',
        id,
        result: {
          content: [{ type: 'text', text: JSON.stringify(data, null, 2) }],
          structuredContent: data,
          isError: false,
        },
      };
    }

    default:
      return {
        jsonrpc: '2.0',
        id,
        error: { code: -32601, message: `Method not found: ${method}` },
      };
  }
}

export const onRequestOptions = async (): Promise<Response> => {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
};

export const onRequestGet = async (): Promise<Response> => {
  return jsonResponse({
    name: SERVER_INFO.name,
    title: SERVER_INFO.title,
    version: SERVER_INFO.version,
    protocol: 'MCP Streamable HTTP (JSON-RPC 2.0 via POST /mcp)',
    protocolVersion: PROTOCOL_VERSION,
    lastReviewed: LAST_REVIEWED,
    tools: TOOLS.map((t) => ({ name: t.name, description: t.description })),
    documentation: 'https://www.stefanwurzer.at/developers/',
    aiFrontDoor: 'https://www.stefanwurzer.at/ai/',
  });
};

export const onRequestPost = async (context: { request: Request }): Promise<Response> => {
  let payload: unknown;
  try {
    payload = await context.request.json();
  } catch {
    return jsonResponse(
      {
        jsonrpc: '2.0',
        id: null,
        error: { code: -32700, message: 'Parse error: invalid JSON' },
      },
      400
    );
  }

  if (Array.isArray(payload)) {
    const responses = payload
      .map((item) => handleRpc(item as JsonRpcRequest))
      .filter((r): r is Record<string, unknown> => r !== null);
    if (responses.length === 0) {
      return new Response(null, { status: 202, headers: CORS_HEADERS });
    }
    return jsonResponse(responses);
  }

  const response = handleRpc(payload as JsonRpcRequest);
  if (response === null) {
    return new Response(null, { status: 202, headers: CORS_HEADERS });
  }
  return jsonResponse(response);
};
