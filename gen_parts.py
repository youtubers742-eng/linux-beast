#!/usr/bin/env python3
"""nexora.yml -> copy-nexora.html (6 chhote parts + download + poora guide)"""
import base64, sys, os, json

SRC = "/home/user/nexora/nexora.yml"
OUT = "/home/user/nexora/copy-nexora.html"
NPARTS = 6

raw = open(SRC, "rb").read()
b64 = base64.b64encode(raw).decode()

# split on line boundaries, BALANCED BY BYTES
lines = open(SRC, encoding="utf-8").read().split("\n")
target = len(raw) / NPARTS
parts, cur, cur_n = [], [], 0
for ln in lines:
    cur.append(ln); cur_n += len(ln.encode("utf-8")) + 1
    if cur_n >= target and len(parts) < NPARTS - 1:
        parts.append("\n".join(cur)); cur, cur_n = [], 0
if cur:
    parts.append("\n".join(cur))
while len(parts) < NPARTS:
    parts.append("")

join = "\n".join(parts)
assert join == open(SRC, encoding="utf-8").read(), "JOIN MISMATCH!"
print("JOIN EXACT: True |", len(raw), "bytes |", len(lines), "lines")
pj = json.dumps(parts)

HTML = """<!DOCTYPE html>
<html lang="hi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NEXORA — Download + Copy + Guide</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#07070a;color:#f2f2f6;font:15px/1.68 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
 padding:14px;max-width:840px;margin:0 auto;padding-bottom:80px}
h1{font-size:27px;letter-spacing:.03em;margin:6px 0 3px;
 background:linear-gradient(100deg,#fff,#e8b96a 45%,#a08fd4);-webkit-background-clip:text;background-clip:text;
 -webkit-text-fill-color:transparent}
.sub{color:#8a8a97;font-size:12.5px;margin-bottom:16px}
.card{background:#0e0e12;border:1px solid #1e1e26;border-radius:16px;padding:16px;margin-bottom:13px}
.card.hi{border-color:#e8b96a;background:linear-gradient(170deg,rgba(232,185,106,.09),transparent)}
.card.gn{border-color:#6fc47f;background:linear-gradient(170deg,rgba(111,196,127,.07),transparent)}
h2{font-size:15.5px;margin-bottom:10px;display:flex;align-items:center;gap:9px}
h2 .n{background:#e8b96a;color:#17120a;width:25px;height:25px;border-radius:8px;display:grid;
 place-items:center;font-size:12px;font-weight:900;flex:0 0 auto}
h2 .g{background:#6fc47f}
h3{font-size:13.5px;margin:14px 0 6px;color:#e8b96a}
ol,ul{margin:8px 0 0 20px;font-size:13.8px;color:#c8c8d4}ol li,ul li{margin:7px 0}
code{font-family:ui-monospace,Menlo,Consolas,monospace;background:#1a1a22;padding:2px 7px;border-radius:6px;
 font-size:12.5px;color:#e8b96a}
.box{background:#0a0a0e;border:1px solid #22222c;border-radius:13px;padding:11px;margin-bottom:10px}
.box .hd{display:flex;align-items:center;gap:9px;margin-bottom:8px;flex-wrap:wrap}
.box .t{font-weight:800;font-size:13.5px;flex:1}
.box .sz{font-size:10.5px;color:#66666f;font-family:ui-monospace}
textarea{width:100%;height:190px;background:#050508;color:#9fb8a8;border:1px solid #1c1c24;
 border-radius:9px;padding:10px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:10.5px;
 line-height:1.5;resize:vertical;white-space:pre;overflow-wrap:normal;overflow-x:scroll}
textarea:focus{outline:none;border-color:#e8b96a}
.btn{padding:10px 17px;border-radius:12px;background:#e8b96a;color:#17120a;font-weight:800;font-size:13.5px;
 border:0;cursor:pointer;transition:transform .12s,filter .12s;display:inline-block}
.btn:hover{filter:brightness(1.1)}.btn:active{transform:scale(.96)}
.btn.big{width:100%;padding:16px;font-size:16px;border-radius:15px;margin-top:12px}
.btn.g{background:#23232c;color:#f2f2f6;border:1px solid #33333f}
.btn:disabled{opacity:.5}
.foot{color:#66666f;font-size:11.5px;text-align:center;margin-top:22px;line-height:1.8}
hr{border:0;border-top:1px solid #1e1e26;margin:18px 0}
.warn{color:#e8b96a}
.ok{color:#6fc47f}
.step{display:flex;gap:11px;margin-bottom:13px;align-items:flex-start}
.step .sn{width:27px;height:27px;border-radius:9px;background:#23232c;color:#e8b96a;display:grid;
 place-items:center;font-weight:900;font-size:12.5px;flex:0 0 auto;margin-top:1px}
.step .sc{flex:1;font-size:13.8px;color:#c8c8d4;line-height:1.6}
.step .sc b{color:#f2f2f6}
.tip{background:#12121a;border-left:3px solid #e8b96a;border-radius:0 10px 10px 0;padding:11px 13px;
 margin:11px 0;font-size:13px;color:#c8c8d4;line-height:1.6}
.q{background:#12121a;border-left:3px solid #6fc47f;border-radius:0 10px 10px 0;padding:11px 13px;
 margin:11px 0;font-size:13px;color:#c8c8d4;line-height:1.65}
</style></head><body>

<h1>◈ NEXORA</h1>
<div class="sub">__KB__ KB · <b>__NP__ chhote parts</b> · download ya paste — dono ka poora tareeka neeche hai</div>

<!-- ══════════ 1. DOWNLOAD ══════════ -->
<div class="card gn">
<h2><span class="n g">1</span>Pehle file download karo</h2>
<div style="font-size:13.8px;color:#c8c8d4;margin-bottom:6px">
Neeche wala button dabao — <code>nexora.yml</code> file tumhare phone/PC mein save ho jayegi.
<b>Yahi wo "upload file" hai.</b></div>
<button class="btn big" onclick="dl()">⬇️ &nbsp; nexora.yml DOWNLOAD KARO</button>
<div class="tip" style="margin-top:12px">
<b>📱 Phone pe:</b> Download folder mein jayegi (Files app → Downloads).<br>
<b>💻 PC pe:</b> neeche left corner mein dikhega, ya Downloads folder.
</div>
<div class="q">
<b>Q: "Upload file kidar se download karu?"</b><br>
Yahin se — upar wala button. Koi aur jagah nahi. Ye page hi wo file banata hai
(poora code is page ke andar hi hai, internet se kuch nahi aata).
</div>
</div>

<!-- ══════════ 2. UPLOAD GUIDE ══════════ -->
<div class="card hi">
<h2><span class="n">2</span>GitHub mein upload ka poora tareeka</h2>

<h3>▸ Phone (Chrome) — 2 minute</h3>
<div class="step"><div class="sn">1</div><div class="sc">Browser mein <code>github.com</code> kholo aur login karo.<br>
Apna repo <b>nexora</b> kholo.</div></div>
<div class="step"><div class="sn">2</div><div class="sc">Upar <b>"&lt;&gt; Code"</b> tab hai — wahan tap karo.</div></div>
<div class="step"><div class="sn">3</div><div class="sc">Neeche file list mein <code>.github</code> folder dikhega — <b>uspe tap karo</b>.<br>
Phir <code>workflows</code> folder pe tap karo.</div></div>
<div class="step"><div class="sn">4</div><div class="sc">Upar right mein <b>"Add file ▾"</b> button hai — tap karo.<br>
Dropdown mein <b>"Upload files"</b> chuno.</div></div>
<div class="step"><div class="sn">5</div><div class="sc">Ab do tareeka hai:<br>
&nbsp;&nbsp;• <b>"choose your files"</b> pe tap → <code>nexora.yml</code> chuno (Downloads se)<br>
&nbsp;&nbsp;• ya file ko <b>ghaseet kar</b> is page pe chhod do (drag &amp; drop)</div></div>
<div class="step"><div class="sn">6</div><div class="sc">File upload hone ke baad neeche <b>"Commit changes"</b> likha hoga — <b>hara button dabao</b>.<br>
(Bas dabao, kuch nahi likhna)</div></div>
<div class="step"><div class="sn">7</div><div class="sc"><b>Ho gaya!</b> Ab <b>Actions</b> tab kholo.</div></div>

<h3>▸ PC (Chrome) — 1 minute</h3>
<div class="step"><div class="sn">1</div><div class="sc">Repo <code>nexora</code> kholo → <code>.github</code> → <code>workflows</code></div></div>
<div class="step"><div class="sn">2</div><div class="sc"><b>Add file → Upload files</b></div></div>
<div class="step"><div class="sn">3</div><div class="sc"><code>nexora.yml</code> drag &amp; drop karo ya choose karo</div></div>
<div class="step"><div class="sn">4</div><div class="sc"><b>Commit changes</b> dabao</div></div>

<h3>▸ Ab run kaise karein</h3>
<div class="step"><div class="sn">1</div><div class="sc">Repo ke upar <b>Actions</b> tab kholo</div></div>
<div class="step"><div class="sn">2</div><div class="sc">Left side mein <b>NEXORA</b> likha hoga — uspe click</div></div>
<div class="step"><div class="sn">3</div><div class="sc">Right side <b>"Run workflow ▾"</b> → <b>Run workflow</b></div></div>
<div class="step"><div class="sn">4</div><div class="sc">Ye value bharo:<pre style="background:#0a0a0e;border:1px solid #22222c;border-radius:9px;padding:10px;margin-top:7px;font-family:ui-monospace;font-size:12px;color:#9fb8a8;overflow-x:auto">hours:  5
gpu:    true
model:  qwen2.5-coder:32b
ollama: none</pre></div></div>
<div class="step"><div class="sn">5</div><div class="sc">Job khulega → <b>[9/9]</b> step mein jakar dekho.</div></div>

<div class="tip">
<b>⏳ 3–5 minute ruko.</b> Phir log mein aayega:<br>
<code>LINK &gt;&gt; https://xxxx.trycloudflare.com</code><br>
<code>PASSWORD &gt;&gt; aB3xK9mQp2</code><br>
Bas link kholo, password daalo — <b>NEXORA chal gaya</b>.
</div>
</div>

<!-- ══════════ 3. PASTE BACKUP ══════════ -->
<div class="card">
<h2><span class="n">3</span>Agar upload na ho — paste (backup tareeka)</h2>
<ol>
<li>Repo → <code>.github/workflows/</code> → <b>Add file → Create new file</b></li>
<li>Upar name mein likho: <code>nexora.yml</code></li>
<li>Neeche <b>Part 1</b> ka <b>📋 Copy</b> dabao → textarea select-all → paste</li>
<li>Phir <b>Part 2, 3, 4, 5, 6</b> — <b>ek ke beech koi extra line nahi</b></li>
<li><b>Commit changes</b></li>
</ol>
<div class="tip" style="border-left-color:#e8695f">
<b>⚠️ Dhyan:</b> Part 1 ke end mein cursor rakh ke Part 2 paste karo. Beech mein kuch mat likhna.
</div>
</div>

<hr>
<div style="font-size:13px;color:#8a8a97;margin-bottom:11px">
Neeche <b>__NP__ boxes</b> — har ek ~__PK__ KB (chhota hai, copy aaram se hoga)</div>
<div id="boxes"></div>

<!-- ══════════ 4. FILE (niche alag se) ══════════ -->
<div class="card gn" style="margin-top:22px">
<h2><span class="n g">📦</span>File — niche alag se</h2>
<div style="font-size:13.8px;color:#c8c8d4;margin-bottom:4px">
Upar <b>parts</b> the (agar paste karna ho). <b>Yahan poori file ek hi click mein.</b><br>
Isse <code>nexora.yml</code> milti hai — wahi jo GitHub mein upload karni hai.
</div>
<button class="btn big" onclick="dl()">⬇️ &nbsp; nexora.yml FILE DOWNLOAD KARO</button>
<div class="tip" style="margin-top:12px">
<b>📱 Phone:</b> Downloads folder mein jayegi &nbsp;·&nbsp;
<b>💻 PC:</b> neeche left ya Downloads<br>
Phir: <b>repo → .github/workflows → Add file → Upload files</b>
</div>
</div>

<div class="foot">
NEXORA 3.0 · ek file · koi dependency nahi · koi account nahi<br>
<b>Download karna sabse aasan hai</b> — upar wale parts sirf backup hain
</div>

<script>
var PARTS = __PJ__;
var boxes = document.getElementById('boxes');
PARTS.forEach(function(p, i){
  var d = document.createElement('div');
  d.className = 'box';
  d.innerHTML = '<div class="hd"><span class="t">Part ' + (i+1) + ' / __NP__</span>' +
    '<span class="sz" id="sz' + i + '"></span>' +
    '<button class="btn" id="b' + i + '" onclick="cp(' + i + ')">📋 Copy</button></div>' +
    '<textarea id="t' + i + '" readonly spellcheck="false"></textarea>';
  boxes.appendChild(d);
  document.getElementById('t' + i).value = p;
  var kb = (new Blob([p]).size / 1024).toFixed(1);
  document.getElementById('sz' + i).textContent = kb + ' KB · ' + p.split('\\n').length + ' lines';
});
function cp(i){
  var t = document.getElementById('t' + i), b = document.getElementById('b' + i);
  var done = function(){
    b.textContent = '✓ Copied!'; b.classList.add('g');
    setTimeout(function(){ b.textContent = '📋 Copy'; b.classList.remove('g'); }, 2200);
  };
  // mobile-friendly: select the text so user can long-press -> copy
  t.removeAttribute('readonly');
  t.focus(); t.select(); t.setSelectionRange(0, 999999);
  var ok = false;
  try { ok = document.execCommand('copy'); } catch(e){}
  t.setAttribute('readonly', true);
  if (ok) { done(); }
  else if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(t.value).then(done, function(){ b.textContent='Select → Copy'; });
  } else { b.textContent = 'Select all → Copy'; }
}
function dl(){
  var txt = PARTS.join('\\n');
  var a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([txt], {type:'text/plain;charset=utf-8'}));
  a.download = 'nexora.yml';
  document.body.appendChild(a); a.click();
  setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 4000);
}
</script>
</body></html>"""

HTML = HTML.replace("__PJ__", pj)
HTML = HTML.replace("__NP__", str(NPARTS))
HTML = HTML.replace("__KB__", str(round(len(raw) / 1024)))
HTML = HTML.replace("__PK__", str(round(len(raw) / NPARTS / 1024)))
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
print("parts KB:", [round(len(p) / 1024, 1) for p in parts])
