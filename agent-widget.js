/**
 * Stefan Wurzer - Agent Widget
 * Injects a chat interface and connects to n8n webhook.
 */

(function() {
  const TENANT_ID = 'stefanwurzer-at';
  const WEBHOOK_URL = 'https://steewee.app.n8n.cloud/webhook/leanAgent';
  const WIDGET_CSS_URL = '/agent-widget.css';

  // State
  let sessionId = generateUUID();
  let isOpen = false;
  let isThinking = false;
  
  // Load CSS
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = WIDGET_CSS_URL;
  document.head.appendChild(link);

  // Load Lucide Icons if not present
  if (typeof lucide === 'undefined') {
    const script = document.createElement('script');
    script.src = 'https://unpkg.com/lucide@latest';
    document.head.appendChild(script);
  }

  // Inject HTML
  const root = document.createElement('div');
  root.id = 'sw-agent-root';
  root.innerHTML = `
    <button id="sw-agent-trigger">
      <i data-lucide="message-circle"></i> Strategie-Chat
    </button>
    
    <div id="sw-agent-window">
      <div id="sw-agent-header">
        <div class="sw-header-info">
          <div class="sw-header-title">Stefan Wurzer</div>
          <div class="sw-header-subtitle">Digitale Strategie · KI Assistent</div>
        </div>
        <button id="sw-agent-close"><i data-lucide="x"></i></button>
      </div>
      
      <div id="sw-agent-messages">
        <!-- Initial Message -->
        <div class="sw-msg sw-msg-assistant">
          <div class="sw-avatar">S</div>
          <div class="sw-msg-content">
            Hallo! Ich bin der digitale Assistent von Stefan Wurzer. Haben Sie Fragen zur KI-Sichtbarkeit, AEO oder digitalen Systemen für den Mittelstand?
          </div>
        </div>
      </div>
      
      <div id="sw-agent-input-area">
        <input type="text" id="sw-agent-input" placeholder="Frage stellen..." autocomplete="off">
        <button id="sw-agent-send"><i data-lucide="send" style="width:18px;height:18px"></i></button>
      </div>
      <div id="sw-agent-footer">
        Powered by Agent-First Architecture
      </div>
    </div>
  `;
  document.body.appendChild(root);

  // Elements
  const trigger = document.getElementById('sw-agent-trigger');
  const win = document.getElementById('sw-agent-window');
  const closeBtn = document.getElementById('sw-agent-close');
  const msgs = document.getElementById('sw-agent-messages');
  const input = document.getElementById('sw-agent-input');
  const sendBtn = document.getElementById('sw-agent-send');

  // Initialize Icons
  setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 500);

  // Event Listeners
  trigger.addEventListener('click', () => {
    isOpen = true;
    win.classList.add('sw-open');
    trigger.classList.add('sw-hidden');
    input.focus();
  });

  closeBtn.addEventListener('click', () => {
    isOpen = false;
    win.classList.remove('sw-open');
    trigger.classList.remove('sw-hidden');
  });

  input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !isThinking) sendMessage();
  });

  sendBtn.addEventListener('click', () => {
    if (!isThinking) sendMessage();
  });

  async function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    // Add User Message
    appendMessage('user', text);
    input.value = '';
    
    // UI State
    isThinking = true;
    input.disabled = true;
    sendBtn.disabled = true;
    
    // Add Typing Indicator
    const typingId = 'typing-' + Date.now();
    appendTyping(typingId);

    try {
      const response = await fetch(WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          tenant_id: TENANT_ID,
          user_message: text
        })
      });
      
      if (!response.ok) throw new Error('Network response was not ok');
      const data = await response.json();
      
      // Remove typing
      removeTyping(typingId);
      
      // Add Assistant Message
      if (data.assistant_message) {
        appendMessage('assistant', data.assistant_message, data.cta);
      }
    } catch (error) {
      console.error('Chat Error:', error);
      removeTyping(typingId);
      appendMessage('assistant', 'Entschuldigung, es gab einen Verbindungsfehler. Bitte versuchen Sie es später noch einmal.');
    } finally {
      isThinking = false;
      input.disabled = false;
      sendBtn.disabled = false;
      setTimeout(() => input.focus(), 100);
    }
  }

  function appendMessage(role, text, cta) {
    const wrapper = document.createElement('div');
    wrapper.className = `sw-msg sw-msg-${role}`;
    
    if (role === 'assistant') {
      let contentHtml = text.replace(/\n/g, '<br>');
      // Render URLs as links (simple regex)
      contentHtml = contentHtml.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
      
      let ctaHtml = '';
      if (cta && cta.label && cta.url) {
        ctaHtml = `<br><a href="${cta.url}" class="sw-cta-btn" target="${cta.url.startsWith('http') ? '_blank' : '_self'}">${cta.label}</a>`;
      }
      
      wrapper.innerHTML = `
        <div class="sw-avatar">S</div>
        <div class="sw-msg-content">${contentHtml}${ctaHtml}</div>
      `;
    } else {
      wrapper.innerText = text;
    }
    
    msgs.appendChild(wrapper);
    msgs.scrollTop = msgs.scrollHeight;
    if (window.lucide) lucide.createIcons();
  }

  function appendTyping(id) {
    const wrapper = document.createElement('div');
    wrapper.className = 'sw-msg sw-msg-assistant';
    wrapper.id = id;
    wrapper.innerHTML = `
      <div class="sw-avatar">S</div>
      <div class="sw-msg-content sw-typing">
        <div class="sw-dot"></div><div class="sw-dot"></div><div class="sw-dot"></div>
      </div>
    `;
    msgs.appendChild(wrapper);
    msgs.scrollTop = msgs.scrollHeight;
  }

  function generateUUID() { // Simple UUID fallback
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }
})();
