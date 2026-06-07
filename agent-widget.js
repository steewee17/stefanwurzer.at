/**
 * Stefan Wurzer - Agent-First Terminal Widget (Shadow DOM)
 */

class B2AAgentWidget extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.tenantId = 'stefanwurzer-at';
    this.webhookUrl = 'https://steewee.app.n8n.cloud/webhook/leanAgent';
    this.sessionId = this.generateUUID();
    this.isOpen = false;
    this.isThinking = false;
  }

  connectedCallback() {
    this.render();
    this.setupListeners();
    // Load Lucide Icons dynamically inside Shadow DOM
    const script = document.createElement('script');
    script.src = 'https://unpkg.com/lucide@latest';
    script.onload = () => {
      if (window.lucide) {
        window.lucide.createIcons({ root: this.shadowRoot });
      }
    };
    document.head.appendChild(script);
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          --bg-dark: #111111;
          --bg-panel: #1A1A1A;
          --border: #333333;
          --gold: #D4B86A;
          --gold-hover: #B8962E;
          --text-main: #F7F5F0;
          --text-muted: #8A8A8A;
          --font-sans: 'Instrument Sans', system-ui, sans-serif;
          --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        }
        
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        /* Trigger Button */
        #trigger {
          position: fixed;
          bottom: 24px;
          right: 24px;
          background: var(--bg-dark);
          color: var(--gold);
          border: 1px solid var(--border);
          border-radius: 30px;
          padding: 12px 20px;
          font-family: var(--font-sans);
          font-size: 14px;
          font-weight: 500;
          letter-spacing: 0.05em;
          cursor: pointer;
          display: flex;
          align-items: center;
          gap: 10px;
          box-shadow: 0 8px 24px rgba(0,0,0,0.2);
          transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), border-color 0.2s;
          z-index: 2147483647;
          text-transform: uppercase;
        }
        #trigger:hover {
          transform: translateY(-3px) scale(1.02);
          border-color: var(--gold);
        }
        #trigger.hidden {
          display: none;
        }

        /* Terminal Window */
        #window {
          position: fixed;
          bottom: 24px;
          right: 24px;
          width: 400px;
          height: 600px;
          max-height: calc(100vh - 48px);
          max-width: calc(100vw - 48px);
          background: var(--bg-dark);
          border-radius: 12px;
          box-shadow: 0 12px 48px rgba(0,0,0,0.4);
          display: flex;
          flex-direction: column;
          overflow: hidden;
          opacity: 0;
          pointer-events: none;
          transform: translateY(20px) scale(0.95);
          transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1);
          border: 1px solid var(--border);
          z-index: 2147483647;
          font-family: var(--font-sans);
        }
        #window.open {
          opacity: 1;
          pointer-events: all;
          transform: translateY(0) scale(1);
        }

        /* Header */
        #header {
          background: var(--bg-panel);
          padding: 16px 20px;
          display: flex;
          justify-content: space-between;
          align-items: center;
          border-bottom: 1px solid var(--border);
        }
        .header-info {
          display: flex;
          align-items: center;
          gap: 12px;
        }
        .header-title {
          font-family: var(--font-mono);
          font-size: 13px;
          color: var(--gold);
          letter-spacing: 0.1em;
          text-transform: uppercase;
        }
        .status-dot {
          width: 6px;
          height: 6px;
          background: #4ade80;
          border-radius: 50%;
          box-shadow: 0 0 8px #4ade80;
        }
        #close {
          background: none;
          border: none;
          color: var(--text-muted);
          cursor: pointer;
          transition: color 0.2s;
          display: flex;
        }
        #close:hover { color: var(--text-main); }

        /* Message Stream */
        #messages {
          flex: 1;
          padding: 24px 20px;
          overflow-y: auto;
          display: flex;
          flex-direction: column;
          gap: 24px;
          background: var(--bg-dark);
        }
        
        .msg {
          display: flex;
          flex-direction: column;
          gap: 6px;
          animation: fade-in 0.3s ease;
          width: 100%;
        }
        @keyframes fade-in {
          from { opacity: 0; transform: translateY(6px); }
          to { opacity: 1; transform: translateY(0); }
        }
        
        .msg-label {
          font-family: var(--font-mono);
          font-size: 11px;
          letter-spacing: 0.05em;
          text-transform: uppercase;
        }
        .msg.user .msg-label { color: var(--text-muted); }
        .msg.assistant .msg-label { color: var(--gold); }
        
        .msg-content {
          color: var(--text-main);
          font-size: 14.5px;
          line-height: 1.6;
        }
        .msg.user .msg-content { color: rgba(247, 245, 240, 0.8); }
        
        .msg-content a {
          color: var(--gold);
          text-decoration: none;
          border-bottom: 1px solid rgba(212, 184, 106, 0.3);
          transition: border-color 0.2s;
        }
        .msg-content a:hover {
          border-bottom-color: var(--gold);
        }
        
        .cta-btn {
          display: inline-block;
          margin-top: 12px;
          background: transparent;
          color: var(--gold);
          border: 1px solid var(--gold);
          padding: 8px 16px;
          border-radius: 4px;
          font-size: 13px;
          text-decoration: none !important;
          transition: all 0.2s;
          font-family: var(--font-mono);
          text-transform: uppercase;
          letter-spacing: 0.05em;
        }
        .cta-btn:hover {
          background: rgba(212, 184, 106, 0.1);
        }

        /* Input Area */
        #input-area {
          padding: 16px 20px;
          background: var(--bg-panel);
          border-top: 1px solid var(--border);
          display: flex;
          gap: 12px;
          align-items: center;
        }
        #input-prefix {
          color: var(--gold);
          font-family: var(--font-mono);
          font-size: 14px;
        }
        #input {
          flex: 1;
          background: transparent;
          border: none;
          color: var(--text-main);
          font-family: var(--font-sans);
          font-size: 14px;
          outline: none;
        }
        #input::placeholder {
          color: var(--text-muted);
        }
        #send {
          background: none;
          color: var(--gold);
          border: none;
          cursor: pointer;
          transition: color 0.2s, transform 0.2s;
          display: flex;
          opacity: 0.7;
        }
        #send:hover { opacity: 1; transform: translateX(2px); }
        #send:disabled { opacity: 0.3; cursor: not-allowed; }

        /* Thinking Indicator */
        .thinking {
          display: flex;
          gap: 4px;
          padding: 4px 0;
        }
        .dot {
          width: 4px;
          height: 4px;
          background: var(--gold);
          border-radius: 50%;
          animation: blink 1.4s infinite;
        }
        .dot:nth-child(2) { animation-delay: 0.2s; }
        .dot:nth-child(3) { animation-delay: 0.4s; }
        @keyframes blink {
          0%, 100% { opacity: 0.2; }
          50% { opacity: 1; }
        }

        @media (max-width: 480px) {
          #window {
            width: 100vw;
            height: 100vh;
            max-width: none;
            max-height: none;
            bottom: 0;
            right: 0;
            border-radius: 0;
          }
        }
      </style>

      <button id="trigger">
        <i data-lucide="terminal" style="width:18px;height:18px;"></i>
        AGENT-FIRST
      </button>

      <div id="window">
        <div id="header">
          <div class="header-info">
            <div class="status-dot"></div>
            <div class="header-title">SYSTEM_READY</div>
          </div>
          <button id="close"><i data-lucide="x" style="width:18px;height:18px;"></i></button>
        </div>

        <div id="messages">
          <div class="msg assistant">
            <div class="msg-label">B2A Agent</div>
            <div class="msg-content">
              System initialisiert. Ich bin der autonome KI-Agent von stefanwurzer.at. 
              <br><br>
              Wie kann ich weiterhelfen?
            </div>
          </div>
        </div>

        <div id="input-area">
          <div id="input-prefix">_></div>
          <input type="text" id="input" placeholder="Query eingeben..." autocomplete="off">
          <button id="send"><i data-lucide="corner-down-left" style="width:18px;height:18px;"></i></button>
        </div>
      </div>
    `;
  }

  setupListeners() {
    this.trigger = this.shadowRoot.getElementById('trigger');
    this.win = this.shadowRoot.getElementById('window');
    this.closeBtn = this.shadowRoot.getElementById('close');
    this.msgs = this.shadowRoot.getElementById('messages');
    this.input = this.shadowRoot.getElementById('input');
    this.sendBtn = this.shadowRoot.getElementById('send');

    this.trigger.addEventListener('click', () => {
      this.isOpen = true;
      this.win.classList.add('open');
      this.trigger.classList.add('hidden');
      this.input.focus();
    });

    this.closeBtn.addEventListener('click', () => {
      this.isOpen = false;
      this.win.classList.remove('open');
      this.trigger.classList.remove('hidden');
    });

    this.input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && !this.isThinking) this.sendMessage();
    });

    this.sendBtn.addEventListener('click', () => {
      if (!this.isThinking) this.sendMessage();
    });
  }

  async sendMessage() {
    const text = this.input.value.trim();
    if (!text) return;

    this.appendMessage('user', text);
    this.input.value = '';
    
    this.isThinking = true;
    this.input.disabled = true;
    this.sendBtn.disabled = true;
    
    const typingId = 'typing-' + Date.now();
    this.appendTyping(typingId);

    try {
      const response = await fetch(this.webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: this.sessionId,
          tenant_id: this.tenantId,
          user_message: text
        })
      });
      
      if (!response.ok) throw new Error('Network response failed');
      const data = await response.json();
      
      this.removeTyping(typingId);
      
      if (data.assistant_message) {
        this.appendMessage('assistant', data.assistant_message, data.cta);
      }
    } catch (error) {
      console.error('Agent Error:', error);
      this.removeTyping(typingId);
      this.appendMessage('assistant', 'System Error: Verbindung zum Server unterbrochen.');
    } finally {
      this.isThinking = false;
      this.input.disabled = false;
      this.sendBtn.disabled = false;
      setTimeout(() => this.input.focus(), 100);
    }
  }

  appendMessage(role, text, cta) {
    const wrapper = document.createElement('div');
    wrapper.className = `msg ${role}`;
    
    const label = role === 'assistant' ? 'KI-Agent' : 'User';
    let contentHtml = text.replace(/\n/g, '<br>');
    contentHtml = contentHtml.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
    
    let ctaHtml = '';
    if (cta && cta.label && cta.url) {
      ctaHtml = `<br><a href="${cta.url}" class="cta-btn" target="${cta.url.startsWith('http') ? '_blank' : '_self'}">${cta.label}</a>`;
    }
    
    wrapper.innerHTML = `
      <div class="msg-label">${label}</div>
      <div class="msg-content">${contentHtml}${ctaHtml}</div>
    `;
    
    this.msgs.appendChild(wrapper);
    this.msgs.scrollTop = this.msgs.scrollHeight;
    
    if (window.lucide) {
      window.lucide.createIcons({ root: this.shadowRoot });
    }
  }

  appendTyping(id) {
    const wrapper = document.createElement('div');
    wrapper.className = 'msg assistant';
    wrapper.id = id;
    wrapper.innerHTML = `
      <div class="msg-label">KI-Agent</div>
      <div class="msg-content thinking">
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
      </div>
    `;
    this.msgs.appendChild(wrapper);
    this.msgs.scrollTop = this.msgs.scrollHeight;
  }

  removeTyping(id) {
    const el = this.shadowRoot.getElementById(id);
    if (el) el.remove();
  }

  generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }
}

customElements.define('b2a-agent-widget', B2AAgentWidget);

// Inject into body if not already there
if (!document.querySelector('b2a-agent-widget')) {
  document.body.appendChild(document.createElement('b2a-agent-widget'));
}
