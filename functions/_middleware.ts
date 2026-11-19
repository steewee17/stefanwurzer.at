/**
 * stefanwurzer.at — Cloudflare Pages Middleware for Content Negotiation
 * Implements "Markdown for Agents" (Accept: text/markdown) on the Free Plan.
 *
 * When an AI agent requests an HTML page with `Accept: text/markdown`,
 * the middleware converts the HTML response into clean Markdown and returns
 * `Content-Type: text/markdown; charset=utf-8` + `x-markdown-tokens` + `Vary: Accept`.
 * Normal browser requests (`Accept: text/html`) pass through untouched.
 */

interface PagesContext {
  request: Request;
  next: () => Promise<Response>;
}

const SKIP_EXTENSIONS = /\.(js|css|svg|png|jpe?g|webp|gif|ico|woff2?|json|xml|txt|md|pdf|webmanifest)$/i;

function decodeHtmlEntities(input: string): string {
  const named: Record<string, string> = {
    amp: '&',
    lt: '<',
    gt: '>',
    quot: '"',
    apos: "'",
    nbsp: ' ',
    mdash: '—',
    ndash: '–',
    bull: '•',
    rarr: '→',
    larr: '←',
    darr: '↓',
    uarr: '↑',
    euro: '€',
    copy: '©',
    reg: '®',
    auml: 'ä',
    ouml: 'ö',
    uuml: 'ü',
    Auml: 'Ä',
    Ouml: 'Ö',
    Uuml: 'Ü',
    szlig: 'ß',
  };

  return input
    .replace(/&#(\d+);/g, (_, dec) => String.fromCharCode(Number(dec)))
    .replace(/&#x([0-9a-fA-F]+);/g, (_, hex) => String.fromCharCode(parseInt(hex, 16)))
    .replace(/&([a-zA-Z]+);/g, (full, name) => named[name] ?? full);
}

function stripTags(html: string): string {
  return decodeHtmlEntities(html.replace(/<[^>]+>/g, '')).replace(/[ \t]+/g, ' ').trim();
}

function htmlToMarkdown(html: string, canonicalUrl: string): string {
  const titleMatch = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  const descMatch = html.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)["']/i)
    || html.match(/<meta[^>]+content=["']([^"']*)["'][^>]+name=["']description["']/i);

  const title = titleMatch ? stripTags(titleMatch[1]) : 'stefanwurzer.at';
  const description = descMatch ? decodeHtmlEntities(descMatch[1]).trim() : '';

  // Isolate body if present
  const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  let body = bodyMatch ? bodyMatch[1] : html;

  // Remove non-content elements
  body = body
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '')
    .replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, '')
    .replace(/<noscript\b[^>]*>[\s\S]*?<\/noscript>/gi, '')
    .replace(/<svg\b[^>]*>[\s\S]*?<\/svg>/gi, '')
    .replace(/<nav\b[^>]*>[\s\S]*?<\/nav>/gi, '')
    .replace(/<footer\b[^>]*>[\s\S]*?<\/footer>/gi, '')
    .replace(/<form\b[^>]*>[\s\S]*?<\/form>/gi, '\n\n*[Kontaktformular im Browser unter ' + canonicalUrl + ']*\n\n');

  // Headings
  body = body
    .replace(/<h1\b[^>]*>([\s\S]*?)<\/h1>/gi, (_, t) => `\n\n# ${stripTags(t)}\n\n`)
    .replace(/<h2\b[^>]*>([\s\S]*?)<\/h2>/gi, (_, t) => `\n\n## ${stripTags(t)}\n\n`)
    .replace(/<h3\b[^>]*>([\s\S]*?)<\/h3>/gi, (_, t) => `\n\n### ${stripTags(t)}\n\n`)
    .replace(/<h4\b[^>]*>([\s\S]*?)<\/h4>/gi, (_, t) => `\n\n#### ${stripTags(t)}\n\n`);

  // Links, emphasis, code
  body = body
    .replace(/<a\b[^>]*href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi, (_, href, text) => {
      const label = stripTags(text);
      return label ? `[${label}](${href})` : href;
    })
    .replace(/<(strong|b)\b[^>]*>([\s\S]*?)<\/\1>/gi, (_, _tag, t) => `**${stripTags(t)}**`)
    .replace(/<(em|i)\b[^>]*>([\s\S]*?)<\/\1>/gi, (_, _tag, t) => `*${stripTags(t)}*`)
    .replace(/<code\b[^>]*>([\s\S]*?)<\/code>/gi, (_, t) => `\`${stripTags(t)}\``);

  // Blockquotes & lists
  body = body
    .replace(/<blockquote\b[^>]*>([\s\S]*?)<\/blockquote>/gi, (_, t) => `\n\n> ${stripTags(t)}\n\n`)
    .replace(/<li\b[^>]*>([\s\S]*?)<\/li>/gi, (_, t) => `\n- ${stripTags(t)}`);

  // Tables (simple row formatting)
  body = body.replace(/<tr\b[^>]*>([\s\S]*?)<\/tr>/gi, (_, row) => {
    const cells = [...row.matchAll(/<t[hd]\b[^>]*>([\s\S]*?)<\/t[hd]>/gi)].map((m) => stripTags(m[1]));
    return cells.length ? `\n| ${cells.join(' | ')} |` : '';
  });

  // Line breaks and block endings
  body = body
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/(p|div|section|article|header|ul|ol|table|dl|dt|dd)>/gi, '\n\n')
    .replace(/<[^>]+>/g, '');

  const cleanedBody = decodeHtmlEntities(body)
    .replace(/[ \t]+\n/g, '\n')
    .replace(/\n[ \t]+/g, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  const headerLines = [
    '---',
    `title: "${title.replace(/"/g, '\\"')}"`,
    `url: "${canonicalUrl}"`,
    ...(description ? [`description: "${description.replace(/"/g, '\\"')}"`] : []),
    'source_format: "text/html"',
    '---',
    '',
  ];

  return `${headerLines.join('\n')}${cleanedBody}\n`;
}

export const onRequest = async (context: PagesContext): Promise<Response> => {
  const { request } = context;

  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return context.next();
  }

  const accept = (request.headers.get('accept') || '').toLowerCase();
  if (!accept.includes('text/markdown')) {
    return context.next();
  }

  const url = new URL(request.url);
  if (
    url.pathname === '/mcp'
    || url.pathname.startsWith('/.well-known/')
    || SKIP_EXTENSIONS.test(url.pathname)
  ) {
    return context.next();
  }

  const response = await context.next();
  const contentType = (response.headers.get('content-type') || '').toLowerCase();
  if (!response.ok || !contentType.includes('text/html')) {
    return response;
  }

  const html = await response.text();
  const markdown = htmlToMarkdown(html, url.toString());
  const estimatedTokens = Math.max(1, Math.ceil(markdown.length / 4));

  const headers = new Headers(response.headers);
  headers.set('Content-Type', 'text/markdown; charset=utf-8');
  headers.set('Vary', 'Accept');
  headers.set('x-markdown-tokens', String(estimatedTokens));
  headers.set('Access-Control-Allow-Origin', '*');
  headers.delete('Content-Length');

  return new Response(request.method === 'HEAD' ? null : markdown, {
    status: response.status,
    headers,
  });
};
