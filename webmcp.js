/**
 * stefanwurzer.at — Native Browser WebMCP Tool Registration (Layer E)
 * Specification: Web Model Context Protocol (document.modelContext.registerTool)
 * Last reviewed: 2026-11-03
 * Principle: Read-only deterministic evidence tools + user-confirmed form helper. Single Source of Truth.
 */
(function () {
  'use strict';

  const LAST_REVIEWED = '2026-11-03';

  const BUSINESS_INFO = {
    lastReviewed: LAST_REVIEWED,
    canonicalUrl: 'https://www.stefanwurzer.at/',
    aiFrontDoorUrl: 'https://www.stefanwurzer.at/ai/',
    compareUrl: 'https://www.stefanwurzer.at/compare/',
    developersUrl: 'https://www.stefanwurzer.at/developers/',
    identity: {
      officialName: 'Stefan Wurzer — stefanwurzer innovationservice',
      owner: 'Stefan Wurzer',
      category: 'Unternehmensberatung, Geschäftsprozessanalyse (7-Phasen-Prozess-Check), Moderne Websites & Prozessautomatisierung',
      location: {
        streetAddress: 'Unterassling 55',
        postalCode: '9911',
        locality: 'Assling',
        region: 'Tirol',
        country: 'AT'
      },
      serviceArea: ['Österreich', 'Deutschland', 'Schweiz', 'DACH (vor Ort & remote)'],
      languages: ['de-AT', 'de', 'en'],
      targetAudience: 'Kleine und mittlere Unternehmen (KMU) in Handwerk, Industrie, Handel und B2B-Dienstleistung (ca. 5 bis 150 Mitarbeitende)'
    },
    fitStatement: {
      bestFor: 'Etablierte KMU in Österreich und im DACH-Raum, die vor einer Investition in Website oder Automatisierung zuerst ihre tatsächlichen Prozess-Engpässe (7-Phasen-Prozess-Check) sauber diagnostizieren wollen, Wert auf 100 % digitales Eigentum ohne laufende Agentur-Abhängigkeit legen und ihre bestehende Softwarelandschaft (Microsoft 365, CRM, ERP) nahtlos verbinden möchten, statt neue Insellösungen einzuführen.',
      notDesignedFor: 'Reine Marken- oder Werbekampagnen ohne Prozessbezug, Großkonzerne mit eigenen internen Enterprise-Entwicklerteams oder Betriebe, die eine unflexible Standard-SaaS-Insellösung von der Stange ohne Prozessanpassung suchen.'
    },
    credentialsAndProof: {
      certification: 'WKO-zertifizierter Unternehmensberater (Fachverband Unternehmensberatung, Buchhaltung und Informationstechnologie)',
      wkoEcgUrl: 'https://www.wkoecg.at/Ecg.aspx?FirmaID=b9661af9-a80b-47ec-ab63-c89c2cf9d0b1',
      experience: 'Über 17 Jahre Praxiserfahrung entlang der gesamten Wertschöpfungskette in Handwerk, Industrie, Handel und Beratung (Marketing, Vertrieb, Planung und Produktion)',
      fundingEligibility: 'Förderfähig im WKO-/Landes-Förderschwerpunkt „Digitalisierung von Geschäftsprozessen“ (bis zu 80 % Zuschuss auf das Beratungshonorar für Mitgliedsbetriebe, z. B. WK Tirol)',
      fundingSourceUrl: 'https://foerderungen.wko.at/tirol/Digitalisierung',
      uid: 'ATU78901789'
    },
    contact: {
      email: 'info@stefanwurzer.at',
      telephone: '+43 677 612 69 625',
      contactPageUrl: 'https://www.stefanwurzer.at/kontakt/',
      initialConsultation: '30 Minuten Kennenlerngespräch (kostenfrei, € 0)'
    }
  };

  const OFFERS_DATA = [
    {
      id: 'initial-consultation',
      category: 'prozess-check',
      name: 'Kennenlerngespräch (30 Minuten)',
      phases: 'Vorab-Einordnung (Phase 01 bis 07)',
      format: '30 Minuten Video-Call oder Telefonat direkt mit Stefan Wurzer',
      pricing: {
        regularPriceEur: 0,
        currency: 'EUR',
        billingType: 'Kostenfrei & unverbindlich',
        note: 'Prüfung der Ausgangslage, Engpass-Hypothese und Klärung der Fördervoraussetzungen (bis zu 80 % WKO-Zuschuss).'
      },
      url: 'https://www.stefanwurzer.at/kontakt/'
    },
    {
      id: '7-phasen-prozess-check',
      category: 'prozess-check',
      name: 'Der 7-Phasen-Prozess-Check (Diagnose & Fahrplan)',
      phases: 'Phase 01 bis 07 (Marktseitige & operative Wertschöpfungskette)',
      format: 'Strukturierte Geschäftsprozess-Analyse im Betrieb inkl. schriftlichem Potenzialbericht & Prioritäten-Fahrplan',
      pricing: {
        regularPriceEur: 2400,
        fundedNetCostEur: 480,
        fundingRatePercent: 80,
        currency: 'EUR',
        billingType: 'Pauschalpreis für das Diagnose-Paket (exkl. USt.)',
        note: 'Regulärer Preis: € 2.400,-. Bei Nutzung des Förderschwerpunkts „Digitalisierung von Geschäftsprozessen“ (80 % Zuschuss) verbleibt für das KMU ein Eigenanteil von € 480,-.'
      },
      deliverables: [
        'Analyse aller 7 Phasen (01 Sichtbarkeit, 02 Anfrage-Eingang, 03 Anfrage-Bearbeitung, 04 Vertrieb, 05 Kundenbetreuung, 06 Auftragsabwicklung, 07 Betriebssteuerung)',
        'Lokalisierung der 1–2 geschäftskritischen Flaschenhälse',
        'Konkreter Potenzialbericht & umsetzbarer Systemintegrations-Fahrplan'
      ],
      url: 'https://www.stefanwurzer.at/'
    },
    {
      id: 'website',
      category: 'website',
      name: 'Website — Moderne Websites für Mensch & KI-Suche (Digitale Souveränität)',
      phases: 'Phase 01 (Marktzugang / Sichtbarkeit) & Phase 02 (Erstkontakt / Conversion)',
      format: 'Individuelle Umsetzung als schnelle, wartungsfreie Web-Architektur für Mensch und KI-Suchsysteme',
      pricing: {
        hourlyRateEur: 110,
        monthlyAgencyRetainerEur: 0,
        currency: 'EUR',
        billingType: 'Nach tatsächlichem Umfang und Aufwand auf Basis von € 110,- / Stunde (exkl. USt.), vorab transparent als Projektumfang kalkuliert',
        note: 'Keine laufenden Agentur-Wartungspauschalen (€ 0 / Monat), keine kostenpflichtigen CMS-Plugin-Abos, 100 % Code- und Daten-Eigentum beim Betrieb.'
      },
      keyCapabilities: [
        'Auffindbarkeit 2.0: Sichtbarkeit für Menschen und KI-Suchsysteme (ChatGPT, Gemini, Perplexity, Copilot)',
        'Strukturierte Unternehmens- und Angebotsfakten zur verlässlichen Erfassung durch Such- und Antwort-Engines',
        'Ablöse veralteter Web-1.0-Seiten sowie wartungs- und sicherheitsanfälliger PHP-/WordPress-Systeme',
        'Digitale Souveränität: 100 % Eigentum im Betrieb, Änderungen in wenigen Minuten selbst durchführbar'
      ],
      url: 'https://www.stefanwurzer.at/website/'
    },
    {
      id: 'automation',
      category: 'automation',
      name: 'Automation — Büroprozesse automatisieren & Systeme verbinden',
      phases: 'Phase 03 bis 07 (Vorprüfung, Vertrieb, Kundenführung, Auftragsabwicklung, Betriebssteuerung)',
      format: 'Systemintegration in bestehender Softwarelandschaft (Microsoft 365, CRM, ERP) sowie spezialisierte KI-Agenten',
      pricing: {
        hourlyRateEur: 110,
        currency: 'EUR',
        billingType: 'Nach tatsächlichem Umfang und Aufwand auf Basis von € 110,- / Stunde (exkl. USt.), modular nach Prozess-Check priorisiert',
        note: 'Vorhandene Lizenzen (z. B. Microsoft 365 / Power Automate) werden vorrangig genutzt, um zusätzliche Software-Lizenzkosten zu vermeiden.'
      },
      causalityFormula: {
        problem: 'Zu viel Administration',
        cause: 'Medienbrüche und Informationsverluste',
        solution: 'Büroprozesse automatisieren',
        technology: ['Microsoft 365 (Power Automate, SharePoint, Teams)', 'CRM', 'ERP', 'KI-Agenten & Assistenten']
      },
      modules: [
        'Stufe 1: Büroprozesse im Microsoft-365-Ökosystem automatisieren (Power Automate, SharePoint, Teams, Outlook)',
        'Modul 01 (Phase 04): Autonomer CRM-Agent per Chat & Sprache (vorgelagerter Server-Agent für Kontakt-/Suchprofil-Anlage, Objektabfrage & PDF-Generierung)',
        'Modul 02 (Phase 01–03): B2B-Lead-Finder & Qualifizierungs-Agent (ICP-Analyse, Vorqualifizierung & Erstansprache)',
        'Modul 03 (Phase 06): Dispo-Assistent zur Lagerkosten-Optimierung (Bestandsanalyse vs. Lieferversprechen)',
        'Modul 04 (Phase 05 & 07): Systemübergreifender Recherche-Assistent (Status quo über ERP, CRM, E-Mail & Laufwerke auf Knopfdruck)'
      ],
      url: 'https://www.stefanwurzer.at/automation/'
    }
  ];

  const SEVEN_PHASES = [
    {
      phase: 1,
      cluster: 'Marktseitige Wertschöpfung',
      domain: 'Marktzugang',
      title: 'Sichtbarkeit',
      bottleneckQuestion: 'Werden unser Fachangebot und unsere Kernkompetenzen im Markt und von modernen KI-Suchmaschinen (Perplexity, ChatGPT, Copilot) verlässlich erfasst?',
      targetFlow: 'Von Wunschkunden & KI-Suchmaschinen sofort als erste Wahl gefunden werden.',
      relatedOffer: 'Website (/website/)'
    },
    {
      phase: 2,
      cluster: 'Marktseitige Wertschöpfung',
      domain: 'Erstkontakt',
      title: 'Anfrage-Eingang',
      bottleneckQuestion: 'Springen Interessenten nach wenigen Sekunden ab oder machen wir es Einkäufern und Partnern leicht, sofort strukturiert anzufragen?',
      targetFlow: 'Vollständige Anfragen vom ersten Moment an — ohne Rückfragen-Ping-Pong.',
      relatedOffer: 'Website (/website/)'
    },
    {
      phase: 3,
      cluster: 'Marktseitige Wertschöpfung',
      domain: 'Vorprüfung',
      title: 'Anfrage-Bearbeitung',
      bottleneckQuestion: 'Bleiben Anfragen tagelang liegen oder vergeudet das Team Zeit mit der manuellen Vorprüfung unpassender Anfragen?',
      targetFlow: 'Passende Anfragen sofort erkennen — klare Priorisierung nach Ihrem Wunschkundenprofil.',
      relatedOffer: 'Automation (/automation/)'
    },
    {
      phase: 4,
      cluster: 'Marktseitige Wertschöpfung',
      domain: 'Abschluss',
      title: 'Vertrieb',
      bottleneckQuestion: 'Fressen Medienbrüche, zeitraubende Notizerfassung und manuelle CRM-Pflege die eigentliche Verkaufszeit, die beim Kunden fehlt?',
      targetFlow: 'Mehr Zeit beim Kunden — Sprachnotizen und E-Mails fließen ohne Tipparbeit ins CRM.',
      relatedOffer: 'Automation (/automation/)'
    },
    {
      phase: 5,
      cluster: 'Operative Wertschöpfung',
      domain: 'Kundenführung',
      title: 'Kundenbetreuung',
      bottleneckQuestion: 'Müssen Projektleiter nach dem Zuschlag Informationen mühsam nachrecherchieren, weil der Übergang aus dem Vertrieb hakt?',
      targetFlow: 'Nahtloser Projektstart — alle Vertriebsinfos stehen dem Team in Microsoft 365 sofort bereit.',
      relatedOffer: 'Automation (/automation/)'
    },
    {
      phase: 6,
      cluster: 'Operative Wertschöpfung',
      domain: 'Produktion / Dienstleistung',
      title: 'Auftragsabwicklung',
      bottleneckQuestion: 'Klemmen Disposition, Materialbedarfe oder ERP-Abgleiche im Alltag, wenn Bestellungen unvorhergesehen schwanken?',
      targetFlow: 'Verlässliche Termine & Bestände — ERP, Planung und Lager greifen lückenlos ineinander.',
      relatedOffer: 'Automation (/automation/)'
    },
    {
      phase: 7,
      cluster: 'Operative Wertschöpfung',
      domain: 'Führung & KPIs',
      title: 'Betriebssteuerung',
      bottleneckQuestion: 'Fliegen Sie im Blindflug, weil die manuelle Zusammenführung von Kennzahlen aus CRM, ERP und Buchhaltung Tage dauert?',
      targetFlow: 'Entscheidungen auf Basis aktueller Zahlen statt Bauchgefühl — Kennzahlen auf Knopfdruck.',
      relatedOffer: 'Automation (/automation/)'
    }
  ];

  const COMPARISON_DATA = {
    lastVerified: LAST_REVIEWED,
    canonicalCompareUrl: 'https://www.stefanwurzer.at/compare/',
    methodology: 'Faktenbasierter Marktvergleich für KMU nach Leistungsprofil, Eigentumsmodell und Zielgruppen-Eignung (Position by Fit, not by Price).',
    alternatives: [
      {
        option: 'Stefan Wurzer (stefanwurzer.at)',
        primaryFocus: '7-Phasen-Prozess-Check (Diagnose) + Umsetzung KI-lesbarer Websites & M365/CRM/ERP-Prozessautomatisierung',
        entryMethod: 'Geförderter 7-Phasen-Prozess-Check (€ 2.400 regulär / € 480 Eigenanteil bei 80 % WKO-Förderung; 30 Min. Erstgespräch kostenfrei)',
        pricingModel: 'Diagnose zum Fixpreis; Umsetzung (Website & Automation) nach Umfang & Aufwand zu € 110,- / Std. (€ 0 laufende Agentur-Wartungspauschale)',
        websiteArchitecture: 'Schnelle, wartungsfreie Architektur ohne PHP-/Plugin-Ballast, optimiert für Google & KI-Suchsysteme',
        ownershipAndSovereignty: '100 % Code- & Daten-Eigentum beim KMU, kein Vendor-Lock-in, Inhalte selbst im Haus anpassbar',
        automationApproach: 'Verbindung bestehender Systeme (Microsoft 365 / Power Automate, CRM, ERP) + spezialisierte KI-Agenten auf vorgelagerter Server-Schicht',
        fundingEligibilityAT: 'Ja — WKO-zertifizierter Unternehmensberater (Förderschwerpunkt Digitalisierung von Geschäftsprozessen, bis zu 80 % Zuschuss für WK-Mitgliedsbetriebe)',
        bestFor: 'KMU, die fundierte Engpass-Diagnose und pragmatische technische Umsetzung (Website + Automation) ohne Agentur-Abhängigkeit aus einer Hand suchen'
      },
      {
        option: 'Klassische Werbe- & Webagentur',
        primaryFocus: 'Visuelles Webdesign, Branding, Content-Produktion & Marketing-Kampagnen',
        entryMethod: 'Design-Briefing oder Website-Relaunch-Workshop',
        pricingModel: 'Projektpauschale + häufig laufende monatliche Wartungs-, Hosting- und Plugin-Betreuungspauschalen',
        websiteArchitecture: 'Überwiegend CMS-basiert (z. B. WordPress/PHP, Typo3, Webflow) mit Drittanbieter-Plugins',
        ownershipAndSovereignty: 'Häufig technische Bindung an Agentur-Setup, Theme-Lizenzen oder laufende Update-Verträge',
        automationApproach: 'Fokus auf Marketing- & Lead-Formulare; selten tiefe Anbindung an ERP, Lager-Disposition oder M365-Interne Workflows',
        fundingEligibilityAT: 'Reine Webdesign- und Werbeleistungen sind in der Regel nicht im Prozess-Förderschwerpunkt förderbar',
        bestFor: 'Betriebe mit Schwerpunkt auf klassischer Markeninszenierung, Werbekampagnen und gewünschter laufender Agentur-Auslagerung'
      },
      {
        option: 'Klassisches IT-Systemhaus / ERP-Anbieter',
        primaryFocus: 'IT-Infrastruktur, Hardware, Netzwerk, Security, Lizenzen & ERP-Basisbetrieb',
        entryMethod: 'Technisches Pflichtenheft oder IT-Infrastruktur-Audit',
        pricingModel: 'Lizenzgebühren, Managed-Service-Verträge & Stundensätze nach IT-Kollektiv/Systemhaus-Tarif',
        websiteArchitecture: 'Meist nicht Teil des Kernportfolios (Fokus auf interner IT)',
        ownershipAndSovereignty: 'Lizenz- und Systemwartungsverträge über das jeweilige Systemhaus bzw. den Softwarehersteller',
        automationApproach: 'Schwerpunkt auf tiefer ERP-Programmierung; oft weniger spezialisiert auf leichtgewichtige KI-Agenten oder marktseitige Phasen (01–04)',
        fundingEligibilityAT: 'Beratungsanteil teilweise förderbar (sofern zertifiziert); reine Hardware- und Lizenzkäufe sind nicht förderbar',
        bestFor: 'Betriebe mit Bedarf an Server-/Netzwerk-Infrastruktur, laufendem IT-Helpdesk und klassischer ERP-Neueinführung'
      },
      {
        option: 'Reine Strategie- & Unternehmensberatung',
        primaryFocus: 'Betriebswirtschaftliche Konzepte, Organisationsentwicklung & Strategie-Gutachten',
        entryMethod: 'Betriebswirtschaftliche Ist-Analyse & Management-Workshops',
        pricingModel: 'Tagessätze oder Beratungspauschalen (ohne technische Implementierung)',
        websiteArchitecture: 'Keine eigene technische Umsetzung',
        ownershipAndSovereignty: 'Übergabe von Strategie-Dokumenten und Konzepten (PDF / Präsentationen)',
        automationApproach: 'Konzeptionelle Soll-Prozesse; für die technische Realisierung in M365, CRM, ERP oder KI-Agenten wird ein weiterer Umsetzungspartner benötigt',
        fundingEligibilityAT: 'Grundsätzlich gegeben, sofern das beratene Unternehmen Mitglied der Wirtschaftskammer (z. B. WK Tirol) ist und die Berater-Zertifizierung vorliegt',
        bestFor: 'Größere Unternehmen mit eigener IT-Abteilung, die ausschließlich ein unabhängiges strategisches Gutachten benötigen'
      }
    ]
  };

  const TOOLS = [
    {
      name: 'get_business_info',
      description: 'Read-only: Retrieve official identity, owner credentials (WKO certification), fit statement (best for whom), location, service area (Austria/DACH), and contact details for Stefan Wurzer (stefanwurzer.at).',
      inputSchema: {
        type: 'object',
        properties: {},
        additionalProperties: false
      },
      execute: async function () {
        return BUSINESS_INFO;
      }
    },
    {
      name: 'get_offers_and_pricing',
      description: 'Read-only: Retrieve current services, deliverables, and transparent pricing (€ 0 initial call, € 2,400 regular / € 480 net with 80% WKO funding for the 7-Phasen-Prozess-Check, € 110/hour for Website & Automation implementation with € 0 monthly agency retainer).',
      inputSchema: {
        type: 'object',
        properties: {
          category: {
            type: 'string',
            enum: ['all', 'prozess-check', 'website', 'automation'],
            description: 'Optional filter by offer category. Defaults to "all".'
          }
        },
        additionalProperties: false
      },
      execute: async function (args) {
        const cat = (args && args.category) ? String(args.category).toLowerCase() : 'all';
        const filtered = cat === 'all'
          ? OFFERS_DATA
          : OFFERS_DATA.filter(function (o) { return o.category === cat; });
        return {
          lastReviewed: LAST_REVIEWED,
          currency: 'EUR',
          vatNote: 'Alle Preisangaben verstehen sich in Euro exkl. gesetzlicher USt. (B2B).',
          categoryFilter: cat,
          offers: filtered
        };
      }
    },
    {
      name: 'get_7_phases_framework',
      description: 'Read-only: Retrieve the 7 phases of the value chain analyzed in the 7-Phasen-Prozess-Check (Phases 01-04 market-side, Phases 05-07 operational), including bottleneck questions and mapped implementation offers.',
      inputSchema: {
        type: 'object',
        properties: {
          phaseNumber: {
            type: 'integer',
            minimum: 1,
            maximum: 7,
            description: 'Optional phase number (1 to 7) to retrieve a specific phase. Omit to return all 7 phases.'
          }
        },
        additionalProperties: false
      },
      execute: async function (args) {
        const num = args && typeof args.phaseNumber === 'number' ? args.phaseNumber : null;
        const phases = num
          ? SEVEN_PHASES.filter(function (p) { return p.phase === num; })
          : SEVEN_PHASES;
        return {
          lastReviewed: LAST_REVIEWED,
          frameworkName: 'Der 7-Phasen-Prozess-Check (stefanwurzer.at)',
          phases: phases
        };
      }
    },
    {
      name: 'get_comparison_summary',
      description: 'Read-only: Retrieve the dated, fact-only market comparison matrix from stefanwurzer.at/compare/ comparing Stefan Wurzer against traditional web agencies, IT system houses, and pure strategy consultants.',
      inputSchema: {
        type: 'object',
        properties: {},
        additionalProperties: false
      },
      execute: async function () {
        return COMPARISON_DATA;
      }
    },
    {
      name: 'prepare_consultation_request',
      description: 'Agent-ready inquiry form helper: Pre-fills the consultation inquiry form (#f-name, #f-email, #f-leistung, #f-firma, #f-nachricht) on the page and scrolls it into view for human confirmation. If userConfirmedSubmission is true, submits the inquiry after explicit user consent.',
      inputSchema: {
        type: 'object',
        properties: {
          name: {
            type: 'string',
            description: 'Full name of the person requesting the consultation.'
          },
          email: {
            type: 'string',
            description: 'Business email address of the requester.'
          },
          topic: {
            type: 'string',
            enum: ['7-Phasen-Prozess-Check', 'Website', 'Automation', 'Allgemeines Kennenlerngespräch'],
            description: 'Selected focus topic for the inquiry.'
          },
          company: {
            type: 'string',
            description: 'Company name or domain (optional).'
          },
          message: {
            type: 'string',
            description: 'Short description of current process bottleneck or project goal (optional).'
          },
          userConfirmedSubmission: {
            type: 'boolean',
            description: 'Set to true ONLY if the user has explicitly confirmed sending the inquiry now. Defaults to false (pre-fills form for visual review).'
          }
        },
        required: ['name', 'email']
      },
      execute: async function (args) {
        const payload = {
          name: (args && args.name) ? String(args.name).trim() : '',
          email: (args && args.email) ? String(args.email).trim() : '',
          topic: (args && args.topic) ? String(args.topic).trim() : '7-Phasen-Prozess-Check',
          company: (args && args.company) ? String(args.company).trim() : '',
          message: (args && args.message) ? String(args.message).trim() : '',
          userConfirmedSubmission: Boolean(args && args.userConfirmedSubmission)
        };

        const nameEl = document.getElementById('f-name');
        const emailEl = document.getElementById('f-email');
        const topicEl = document.getElementById('f-leistung');
        const companyEl = document.getElementById('f-firma');
        const msgEl = document.getElementById('f-nachricht');

        if (nameEl && emailEl) {
          nameEl.value = payload.name;
          emailEl.value = payload.email;
          if (topicEl && payload.topic) {
            for (var i = 0; i < topicEl.options.length; i++) {
              if (topicEl.options[i].value === payload.topic) {
                topicEl.selectedIndex = i;
                break;
              }
            }
          }
          if (companyEl) companyEl.value = payload.company;
          if (msgEl) msgEl.value = payload.message;
          nameEl.scrollIntoView({ behavior: 'smooth', block: 'center' });

          if (payload.userConfirmedSubmission && typeof window.submitContactForm === 'function') {
            await window.submitContactForm('stefanwurzer.at/webmcp-agent');
            return {
              status: 'submitted_with_user_confirmation',
              submittedData: payload,
              note: 'Anfrage wurde erfolgreich über das Formular abgesendet. Stefan Wurzer meldet sich innerhalb von 24 Stunden.'
            };
          }

          return {
            status: 'prefilled_awaiting_user_click',
            prefilledData: payload,
            note: 'Das Kontaktformular auf der Seite wurde vorausgefüllt und in den sichtbaren Bereich gescrollt. Bitte klicken Sie auf den Senden-Button zur finalen Bestätigung.'
          };
        }

        return {
          status: 'redirect_required',
          contactFormUrl: 'https://www.stefanwurzer.at/kontakt/#formular',
          preparedData: payload,
          note: 'Auf dieser Unterseite befindet sich kein eingebettetes Formular. Öffnen Sie https://www.stefanwurzer.at/kontakt/#formular oder die Startseite, um das Formular auszufüllen.'
        };
      }
    }
  ];

  // Expose deterministic tool registry on window for the interactive tester on /developers/
  window.SW_WEBMCP = {
    version: '1.1.0',
    lastReviewed: LAST_REVIEWED,
    nativeSupport: false,
    registeredTarget: 'none',
    tools: TOOLS,
    invoke: async function (toolName, args) {
      const found = TOOLS.find(function (t) { return t.name === toolName; });
      if (!found) {
        throw new Error('Unknown WebMCP tool: ' + toolName);
      }
      return await found.execute(args || {});
    }
  };

  // Register via standard document.modelContext.registerTool (with safe fallback check for navigator.modelContext)
  try {
    var ctx = null;
    var targetName = 'none';
    if (typeof document !== 'undefined' && 'modelContext' in document && document.modelContext && typeof document.modelContext.registerTool === 'function') {
      ctx = document.modelContext;
      targetName = 'document.modelContext';
    } else if (typeof navigator !== 'undefined' && 'modelContext' in navigator && navigator.modelContext && typeof navigator.modelContext.registerTool === 'function') {
      ctx = navigator.modelContext;
      targetName = 'navigator.modelContext';
    }

    if (ctx) {
      TOOLS.forEach(function (tool) {
        ctx.registerTool({
          name: tool.name,
          description: tool.description,
          inputSchema: tool.inputSchema,
          execute: tool.execute
        });
      });
      window.SW_WEBMCP.nativeSupport = true;
      window.SW_WEBMCP.registeredTarget = targetName;
    }
  } catch (err) {
    console.warn('[stefanwurzer.at WebMCP] Tool registration skipped:', err);
  }
})();
