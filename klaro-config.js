// stefanwurzer.at — Klaro Cookie Consent Configuration
// Docs: https://heyklaro.com/docs/getting-started/annotating-your-code

var klaroConfig = {
    version: 1,

    // Storage key for consent decisions
    storageKey: 'klaro-stefanwurzer',

    // Show banner on first visit
    noticeAsModal: false,

    // Language
    lang: 'de',

    // Position of the banner
    elementID: 'klaro',

    // Styling
    styling: {
        theme: ['light', 'top', 'wide'],
    },

    // Hide "Decline all" button — user must make active choice
    hideDeclineAll: false,

    // Show learn more link
    acceptAll: true,

    // Cookie name for storing consent
    cookieName: 'klaro-stefanwurzer',

    // Cookie expiry in days
    cookieExpiresAfterDays: 365,

    // Custom translations
    translations: {
        de: {
            consentNotice: {
                title: 'Diese Website verwendet Cookies',
                description: 'Wir verwenden Google Analytics um zu verstehen, wie Besucher unsere Website nutzen. Ihre Daten werden anonymisiert verarbeitet.',
                learnMore: 'Mehr erfahren',
            },
            consentModal: {
                title: 'Cookie-Einstellungen',
                description: 'Hier können Sie einsehen und anpassen, welche Informationen wir über Sie sammeln. Einträge die als "Immer aktiv" gekennzeichnet sind, sind für den Betrieb der Website erforderlich.',
                privacyPolicy: {
                    name: 'Datenschutzerklärung',
                    text: 'Mehr erfahren Sie in unserer {privacyPolicy}.',
                },
            },
            acceptAll: 'Alle akzeptieren',
            acceptSelected: 'Auswahl speichern',
            decline: 'Ablehnen',
            close: 'Schließen',
            ok: 'OK',
            purposes: {
                analytics: 'Analyse',
            },
            service: {
                disableAll: {
                    title: 'Alle deaktivieren',
                    description: 'Alle Dienste deaktivieren.',
                },
                optOut: {
                    title: '(opt-out)',
                    description: 'Dieser Dienst ist standardmäßig aktiv. Sie können ihn deaktivieren.',
                },
                required: {
                    title: '(immer aktiv)',
                    description: 'Dieser Dienst ist für den Betrieb der Website erforderlich.',
                },
                purposes: 'Zwecke',
                purpose: 'Zweck',
            },
        },
    },

    // Services requiring consent
    services: [
        {
            name: 'google-analytics',
            title: 'Google Analytics',
            purposes: ['analytics'],
            default: false,
            required: false,
            optOut: false,

            // This callback fires when consent changes
            // When consent is given: GA loads. When withdrawn: GA is blocked.
            onAccept: `
                // Enable Google Analytics
                window['ga-disable-G-XL6E22PCJC'] = false;
                gtag('consent', 'update', {
                    'analytics_storage': 'granted'
                });
            `,
            onDecline: `
                // Disable Google Analytics
                window['ga-disable-G-XL6E22PCJC'] = true;
                gtag('consent', 'update', {
                    'analytics_storage': 'denied'
                });
            `,

            cookies: [
                [/^_ga/, '/'],
                [/^_gid/, '/'],
                [/^_gat/, '/'],
            ],
        },
    ],
};
