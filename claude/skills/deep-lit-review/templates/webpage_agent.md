# Webpage Generation Agent

You are a webpage generation agent. Your job is to create an interactive HTML viewer for a completed literature review.

## Inputs

- `OUTPUT_DIR`: the literature review output directory (contains reports/, workbench/agents/, etc.)
- `TOPIC`: the review topic (from the review's README.md title)
- `MODEL_ARG`: the `--model` value passed to the skill (haiku / sonnet / opus)

## Model ID mapping

| Arg | Model ID |
|-----|----------|
| haiku | claude-haiku-4-5-20251001 |
| sonnet | claude-sonnet-4-6 |
| opus | claude-opus-4-6 |

Default (if unspecified): `claude-haiku-4-5-20251001`

## Your Steps

1. Read `{OUTPUT_DIR}/README.md` to get the topic title.
2. Use Glob to list all `.md` files under:
   - `{OUTPUT_DIR}/reports/per_stream/`
   - `{OUTPUT_DIR}/reports/` (synthesis.md, open_questions.md)
   - `{OUTPUT_DIR}/workbench/agents/`
3. Build the navigation structure (see HTML template below).
4. Fill in all `PLACEHOLDER` values in the HTML template.
5. Fill in all `PLACEHOLDER` values in the server.py template.
6. Write `{OUTPUT_DIR}/index.html` and `{OUTPUT_DIR}/server.py`.
7. Make server.py executable: `chmod +x {OUTPUT_DIR}/server.py`

## Navigation structure to generate

Build `NAV_DOCS` as a JS array of `{label, path}` objects, in this order:
1. `reports/synthesis.md` → label "Synthesis"
2. `reports/open_questions.md` → label "Open Questions"
3. Each file in `reports/per_stream/` → label = filename without .md, replace _ with space, title-case
4. Each file in `workbench/agents/` → label = filename without .md, prefix "Agent: "

Build `NAV_HTML` as sidebar HTML using this pattern per item:
```html
<a class="nav-item" onclick="loadDoc('RELATIVE_PATH', this)">LABEL</a>
```
Group into sections with:
```html
<div class="nav-section">
  <div class="nav-section-title">SECTION NAME</div>
  ... items ...
</div>
```
Sections: "Reports", "Per Stream", "Workbench"

---

## index.html template

Write this file verbatim, substituting every `___PLACEHOLDER___`:
- `___TOPIC___` → the review topic string
- `___MODEL_DISPLAY___` → e.g. "claude-haiku-4-5-20251001"
- `___MODEL_ID___` → the full model ID string
- `___NAV_HTML___` → the sidebar HTML you built
- `___NAV_DOCS_JS___` → the JS array literal, e.g. `[{label:"Synthesis",path:"reports/synthesis.md"},...]`
- `___FIRST_DOC___` → path of the first document (reports/synthesis.md)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lit Review: ___TOPIC___</title>
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;display:flex;height:100vh;overflow:hidden;background:#f8f9fa;color:#1e1e2e}
/* Sidebar */
#sidebar{width:260px;background:#1e1e2e;color:#cdd6f4;overflow-y:auto;flex-shrink:0;display:flex;flex-direction:column}
#sidebar-header{padding:16px;border-bottom:1px solid #313244}
#sidebar-header .logo{font-size:11px;font-weight:700;color:#89b4fa;text-transform:uppercase;letter-spacing:.1em}
#sidebar-header .topic{font-size:13px;color:#cdd6f4;margin-top:6px;line-height:1.4}
#sidebar-nav{flex:1;padding:8px 0}
.nav-section{margin:8px 0}
.nav-section-title{font-size:10px;padding:6px 16px;color:#6c7086;text-transform:uppercase;letter-spacing:.12em;font-weight:600}
.nav-item{display:block;padding:7px 20px;font-size:13px;color:#bac2de;cursor:pointer;border-left:3px solid transparent;text-decoration:none;transition:all .15s}
.nav-item:hover{background:#313244;color:#cdd6f4;border-left-color:#585b70}
.nav-item.active{background:#313244;color:#cdd6f4;border-left-color:#89b4fa}
/* Main */
#main{flex:1;overflow-y:auto;padding:0;display:flex;flex-direction:column}
#topbar{background:white;border-bottom:1px solid #e5e5e5;padding:12px 48px;font-size:13px;color:#6c7086;flex-shrink:0;display:flex;align-items:center;gap:8px}
#topbar #doc-title{color:#1e1e2e;font-weight:600}
#content-wrap{flex:1;padding:40px 48px;max-width:860px;width:100%}
/* Markdown */
#content h1{font-size:26px;font-weight:700;margin:0 0 24px;color:#1e1e2e;line-height:1.3}
#content h2{font-size:18px;font-weight:600;margin:36px 0 12px;color:#313244;border-bottom:1px solid #e5e7eb;padding-bottom:8px}
#content h3{font-size:15px;font-weight:600;margin:24px 0 8px;color:#45475a}
#content p{line-height:1.75;margin:0 0 16px;color:#3d3d52}
#content ul,#content ol{margin:0 0 16px 24px;line-height:1.75;color:#3d3d52}
#content li{margin:4px 0}
#content li p{margin:0}
#content strong{color:#1e1e2e}
#content em{color:#45475a}
#content table{width:100%;border-collapse:collapse;margin:20px 0;font-size:13px}
#content th{background:#f0f2f5;padding:9px 14px;text-align:left;font-weight:600;color:#1e1e2e;border-bottom:2px solid #ddd}
#content td{padding:9px 14px;border-bottom:1px solid #eee;vertical-align:top}
#content tr:last-child td{border-bottom:none}
#content tr:nth-child(even) td{background:#fafafa}
#content code{background:#f0f2f5;padding:2px 6px;border-radius:4px;font-size:12.5px;font-family:'SF Mono','Fira Code',monospace;color:#e64553}
#content pre{background:#1e1e2e;color:#cdd6f4;padding:20px;border-radius:8px;overflow-x:auto;margin:20px 0}
#content pre code{background:none;padding:0;color:inherit;font-size:13px}
#content blockquote{border-left:4px solid #89b4fa;margin:20px 0;padding:12px 20px;background:#eff6ff;color:#1e1e2e;border-radius:0 6px 6px 0}
#content a{color:#1d4ed8;text-decoration:none;border-bottom:1px dotted #93c5fd}
#content a:hover{border-bottom-color:#1d4ed8}
#content hr{border:none;border-top:1px solid #e5e7eb;margin:32px 0}
/* Chat */
#chat-btn{position:fixed;bottom:28px;right:28px;width:52px;height:52px;background:#89b4fa;border:none;border-radius:50%;cursor:pointer;font-size:20px;box-shadow:0 4px 16px rgba(0,0,0,.18);z-index:200;display:flex;align-items:center;justify-content:center;transition:transform .15s,background .15s}
#chat-btn:hover{background:#74c7ec;transform:scale(1.05)}
#chat-panel{position:fixed;bottom:92px;right:28px;width:400px;background:white;border-radius:14px;box-shadow:0 8px 40px rgba(0,0,0,.18);display:none;flex-direction:column;z-index:199;max-height:560px;border:1px solid #e5e7eb}
#chat-panel.open{display:flex}
#chat-header{background:#1e1e2e;color:#cdd6f4;padding:14px 16px;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:space-between}
#chat-header .title{font-size:14px;font-weight:600}
#chat-header .model-badge{font-size:10px;background:#313244;color:#89b4fa;padding:2px 8px;border-radius:99px;font-family:monospace}
#chat-header .close-btn{background:none;border:none;color:#6c7086;cursor:pointer;font-size:18px;line-height:1;padding:0}
#chat-header .close-btn:hover{color:#cdd6f4}
#chat-messages{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px;min-height:180px;max-height:320px}
.msg{padding:10px 13px;border-radius:10px;font-size:13px;line-height:1.6;max-width:92%;word-break:break-word}
.msg.user{background:#1d4ed8;color:white;align-self:flex-end;border-radius:10px 10px 2px 10px}
.msg.assistant{background:#f3f4f6;color:#1e1e2e;align-self:flex-start;border-radius:10px 10px 10px 2px}
.msg.assistant a{color:#1d4ed8}
.msg.error{background:#fee2e2;color:#991b1b;align-self:flex-start}
.msg.thinking{background:#f3f4f6;color:#9ca3af;align-self:flex-start;font-style:italic;font-size:12px}
#apikey-row{padding:8px 14px;border-top:1px solid #f0f0f0;display:flex;gap:6px;align-items:center}
#apikey-row label{font-size:11px;color:#9ca3af;white-space:nowrap}
#apikey-input{flex:1;padding:5px 8px;border:1px solid #e5e7eb;border-radius:6px;font-size:12px;font-family:monospace;color:#374151}
#chat-input-row{padding:10px 14px;border-top:1px solid #f0f0f0;display:flex;gap:8px;align-items:flex-end}
#chat-input{flex:1;padding:8px 10px;border:1px solid #e5e7eb;border-radius:8px;font-size:13px;resize:none;height:56px;font-family:inherit;color:#1e1e2e;outline:none;transition:border-color .15s}
#chat-input:focus{border-color:#89b4fa}
#chat-send{background:#1d4ed8;color:white;border:none;border-radius:8px;padding:8px 14px;cursor:pointer;font-weight:600;font-size:13px;white-space:nowrap;height:38px;transition:background .15s}
#chat-send:hover{background:#1e40af}
#chat-send:disabled{opacity:.45;cursor:not-allowed}
/* Context indicator */
#context-bar{padding:6px 14px;border-top:1px solid #f0f0f0;font-size:11px;color:#9ca3af;background:#fafafa;border-radius:0}
</style>
</head>
<body>

<div id="sidebar">
  <div id="sidebar-header">
    <div class="logo">Deep Lit Review</div>
    <div class="topic">___TOPIC___</div>
  </div>
  <div id="sidebar-nav">
    ___NAV_HTML___
  </div>
</div>

<div id="main">
  <div id="topbar">
    <span>📄</span>
    <span id="doc-title">Loading…</span>
  </div>
  <div id="content-wrap">
    <div id="content"></div>
  </div>
</div>

<button id="chat-btn" onclick="toggleChat()" title="Ask AI Assistant">💬</button>

<div id="chat-panel">
  <div id="chat-header">
    <div>
      <div class="title">AI Assistant</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span class="model-badge">___MODEL_DISPLAY___</span>
      <button class="close-btn" onclick="toggleChat()">✕</button>
    </div>
  </div>
  <div id="chat-messages">
    <div class="msg assistant">Hi! I've read this literature review. Ask me anything — I'll explain concepts, summarise findings, or help you understand any paper mentioned.</div>
  </div>
  <div id="context-bar">Context: <span id="context-label">none loaded</span></div>
  <div id="apikey-row">
    <label>API key</label>
    <input id="apikey-input" type="password" placeholder="sk-ant-… (or set ANTHROPIC_API_KEY in server)" />
  </div>
  <div id="chat-input-row">
    <textarea id="chat-input" placeholder="Ask about this section… (Enter to send, Shift+Enter for newline)" onkeydown="handleKey(event)"></textarea>
    <button id="chat-send" onclick="sendMessage()">Send</button>
  </div>
</div>

<script>
const MODEL_ID = "___MODEL_ID___";
const NAV_DOCS = ___NAV_DOCS_JS___;

let currentDocPath = null;
let currentDocContent = "";
let chatHistory = [];
let contextSentForDoc = null; // tracks which doc's context is already in chatHistory

// ── Navigation ──────────────────────────────────────────────────────────────

function loadDoc(path, el) {
  document.querySelectorAll('.nav-item').forEach(e => e.classList.remove('active'));
  if (el) el.classList.add('active');
  currentDocPath = path;
  const label = el ? el.textContent : path;
  document.getElementById('doc-title').textContent = label;
  document.getElementById('context-label').textContent = label;

  chatHistory = [];        // isolate context per document
  contextSentForDoc = null;

  fetch('/docs/' + path)
    .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); })
    .then(md => {
      currentDocContent = md;
      const html = marked.parse(md);
      document.getElementById('content').innerHTML = linkifyCitations(html);
      document.getElementById('content-wrap').scrollTop = 0;
    })
    .catch(err => {
      document.getElementById('content').innerHTML = '<p style="color:#991b1b">Failed to load: ' + err.message + '</p>';
    });
}

// ── Citation auto-linking ────────────────────────────────────────────────────

function linkifyCitations(html) {
  // DOIs — match 10.NNNN/... not already inside an href
  html = html.replace(/(?<![="\/])\b(10\.\d{4,9}\/[^\s<"')\]]+[a-zA-Z0-9])/g,
    '<a href="https://doi.org/$1" target="_blank" title="Open via DOI">$1</a>');
  // OpenAlex IDs (W + 8+ digits)
  html = html.replace(/(?<![="\/])\b(W\d{8,})\b/g,
    '<a href="https://openalex.org/works/$1" target="_blank" title="Open in OpenAlex">$1</a>');
  // arXiv IDs
  html = html.replace(/arXiv[:\s]+(\d{4}\.\d{4,5}(?:v\d)?)/gi,
    'arXiv:<a href="https://arxiv.org/abs/$1" target="_blank">$1</a>');
  return html;
}

// ── Chat ─────────────────────────────────────────────────────────────────────

function toggleChat() {
  document.getElementById('chat-panel').classList.toggle('open');
}

function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
}

async function sendMessage() {
  const input = document.getElementById('chat-input');
  const text = input.value.trim();
  if (!text) return;

  const apiKey = document.getElementById('apikey-input').value.trim();

  // Inject document context once as a user/assistant turn (observation masking:
  // only on first message per document, not re-sent on every turn)
  if (contextSentForDoc !== currentDocPath && currentDocContent) {
    chatHistory.push({
      role: 'user',
      content: `[Document: ${currentDocPath}]\n\n${currentDocContent.slice(0, 12000)}`
    });
    chatHistory.push({
      role: 'assistant',
      content: "I've read this document and I'm ready to help you understand it."
    });
    contextSentForDoc = currentDocPath;
  }

  appendMsg('user', text);
  chatHistory.push({ role: 'user', content: text });
  input.value = '';

  const sendBtn = document.getElementById('chat-send');
  sendBtn.disabled = true;
  const thinking = appendMsg('thinking', 'Thinking…');

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: MODEL_ID,
        messages: chatHistory,
        api_key: apiKey
      })
    });
    const data = await res.json();
    thinking.remove();
    if (data.error) throw new Error(data.error);
    const reply = data.content[0].text;
    chatHistory.push({ role: 'assistant', content: reply });
    appendMsg('assistant', reply);
  } catch (err) {
    thinking.remove();
    appendMsg('error', '⚠ ' + err.message);
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

function appendMsg(role, text) {
  const div = document.createElement('div');
  div.className = 'msg ' + role;
  // render simple markdown in assistant replies
  if (role === 'assistant') {
    div.innerHTML = marked.parse(text);
  } else {
    div.textContent = text;
  }
  const msgs = document.getElementById('chat-messages');
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
  return div;
}

// ── Init ──────────────────────────────────────────────────────────────────────

(function init() {
  const firstNav = document.querySelector('.nav-item');
  if (firstNav) loadDoc(NAV_DOCS[0].path, firstNav);
})();
</script>
</body>
</html>
```

---

## server.py template

Write this file verbatim, substituting:
- `___MODEL_ID___` → full model ID
- `___OUTPUT_DIR___` → absolute path to the output directory

```python
#!/usr/bin/env python3
"""
Lit Review Interactive Viewer
Usage:  python server.py
Then open:  http://localhost:8765
Set ANTHROPIC_API_KEY in your environment, or enter it in the chat box.
"""
import http.server, json, os, urllib.request, urllib.error
from pathlib import Path

PORT = 8765
OUTPUT_DIR = Path("___OUTPUT_DIR___")
DEFAULT_MODEL = "___MODEL_ID___"
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # suppress per-request logs

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._file(OUTPUT_DIR / "index.html", "text/html; charset=utf-8")
        elif self.path.startswith("/docs/"):
            rel = self.path[6:]  # strip /docs/
            target = (OUTPUT_DIR / rel).resolve()
            # safety: must stay inside OUTPUT_DIR and be a .md file
            if target.suffix == ".md" and str(target).startswith(str(OUTPUT_DIR)):
                self._file(target, "text/plain; charset=utf-8")
            else:
                self._respond(404, b"Not found")
        else:
            self._respond(404, b"Not found")

    def do_POST(self):
        if self.path == "/api/chat":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))

            key = body.get("api_key") or API_KEY
            if not key:
                self._json({"error": "No API key. Set ANTHROPIC_API_KEY or enter it in the chat box."}, 400)
                return

            # Stable system prompt — never changes, so the API can cache it (KV-cache optimization).
            # Document context is injected client-side as the first user/assistant turn in messages,
            # keeping this prompt identical across all requests for the same session.
            system = [{
                "type": "text",
                "text": (
                    "You are an expert research assistant helping a user understand a deep literature review. "
                    "You are embedded in an interactive viewer — the user is reading the review right now. "
                    "Be clear and accessible: define technical terms, explain concepts from first principles "
                    "when needed, and connect ideas across the review. "
                    "Do not fabricate papers or citations not present in the review."
                ),
                "cache_control": {"type": "ephemeral"}
            }]

            payload = json.dumps({
                "model": body.get("model", DEFAULT_MODEL),
                "max_tokens": 1024,
                "system": system,
                "messages": body.get("messages", [])
            }).encode()

            req = urllib.request.Request(
                "https://api.anthropic.com/v1/messages",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": key,
                    "anthropic-version": "2023-06-01",
                    "anthropic-beta": "prompt-caching-2024-07-31",
                },
            )
            try:
                with urllib.request.urlopen(req) as r:
                    self._json(json.loads(r.read()))
            except urllib.error.HTTPError as e:
                try:
                    err = json.loads(e.read()).get("error", {}).get("message", str(e))
                except Exception:
                    err = str(e)
                self._json({"error": err}, e.code)
        else:
            self._respond(404, b"Not found")

    def _file(self, path, ctype):
        try:
            data = Path(path).read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self._cors()
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self._respond(404, b"File not found")

    def _json(self, obj, status=200):
        data = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self._cors()
        self.end_headers()
        self.wfile.write(data)

    def _respond(self, status, body):
        self.send_response(status)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    httpd = http.server.HTTPServer(("localhost", PORT), Handler)
    print(f"✓  Lit Review Viewer → http://localhost:{PORT}")
    print(f"   Model : {DEFAULT_MODEL}")
    print(f"   Key   : {'set ✓' if API_KEY else 'not set — enter in chat box'}")
    print("   Ctrl-C to stop\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")
```
