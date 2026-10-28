"""Build docs/tracker.html from docs/TICKETS.md.

Run:  python3 docs/build_tracker.py
Checkbox state is saved in the browser (localStorage), so rebuilding keeps your progress
as long as the checklist text doesn't change.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
md = (ROOT / "TICKETS.md").read_text()


def inline(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


# Summary table: id -> (estimate, depends)
meta = {}
for row in re.findall(r"^\| (TDC-\d+) \| [^|]+\| [^|]+\| ([^|]+)\| ([^|]+)\|", md, re.M):
    meta[row[0]] = {"estimate": row[1].strip(), "depends": row[2].strip()}

# Audit mapping table
audit = []
for num, finding, tickets in re.findall(r"^\| (\d+) \| ([^|]+)\| ([^|]+)\| \[ \] \|", md, re.M):
    audit.append({"num": int(num), "finding": inline(finding.strip()), "tickets": tickets.strip()})

# Phases and tickets
phases = []
for block in re.split(r"^## (?=Fase)", md, flags=re.M)[1:]:
    block = block.split("\n## ")[0]  # stop at the next non-phase section (e.g. the CR template)
    title = block.splitlines()[0].strip()
    tickets = []
    for t in re.split(r"^### ", block, flags=re.M)[1:]:
        lines = t.splitlines()
        tid, name = [x.strip() for x in lines[0].split("·", 1)]
        items, done, notes = [], "", []
        for line in lines[1:]:
            if line.startswith("- [ ] "):
                items.append(inline(line[6:]))
            elif line.startswith("**Done kalau:**"):
                done = inline(line.replace("**Done kalau:**", "").strip())
            elif line.strip() and not line.startswith(("---", "## ")):
                notes.append(inline(line.strip()))
        tickets.append({"id": tid, "name": inline(name), "items": items, "done": done,
                        "notes": notes, **meta.get(tid, {"estimate": "", "depends": ""})})
    phases.append({"title": title, "tickets": tickets})

data = json.dumps({"phases": phases, "audit": audit}, ensure_ascii=False)

html = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tracker — The Dog Club</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Inter', sans-serif; background: #F9F6F0; color: #1A2E26; }
  .serif { font-family: 'Playfair Display', serif; }
  code { background: #EFEAE1; padding: 1px 5px; border-radius: 4px; font-size: .85em; }
  input[type=checkbox] { accent-color: #1A2E26; width: 1rem; height: 1rem; margin-top: .2rem; flex-shrink: 0; cursor: pointer; }
  .item-done span { text-decoration: line-through; color: #9a9a9a; }
  details > summary { list-style: none; cursor: pointer; }
  details > summary::-webkit-details-marker { display: none; }
  details[open] .chev { transform: rotate(90deg); }
</style>
</head>
<body>
<main class="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
  <header class="mb-8">
    <p class="text-xs font-bold uppercase tracking-widest text-[#E4B047]">Tracker proyek</p>
    <h1 class="serif text-4xl font-bold mt-1">The Dog Club — Essential</h1>
    <p class="text-sm text-[#707070] mt-2">Centang tersimpan otomatis di browser ini. Sumber: <code>docs/TICKETS.md</code></p>
  </header>

  <section class="bg-white/60 border border-[#E4DDD0] rounded-2xl p-5 mb-6">
    <div class="flex items-baseline justify-between mb-2">
      <p class="font-semibold">Progres keseluruhan</p>
      <p id="overall-text" class="text-sm text-[#707070]"></p>
    </div>
    <div class="h-3 bg-[#EFEAE1] rounded-full overflow-hidden"><div id="overall-bar" class="h-full bg-[#1A2E26] transition-all"></div></div>
    <div id="phase-stats" class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5 text-sm"></div>
  </section>

  <div class="flex flex-wrap gap-2 mb-6 text-sm">
    <button data-filter="all" class="filter px-4 py-2 rounded-full border border-[#1A2E26]">Semua</button>
    <button data-filter="open" class="filter px-4 py-2 rounded-full border border-[#1A2E26]">Belum selesai</button>
    <button data-filter="done" class="filter px-4 py-2 rounded-full border border-[#1A2E26]">Selesai</button>
    <button id="expand" class="px-4 py-2 rounded-full border border-[#E4DDD0] ml-auto">Buka semua</button>
    <button id="reset" class="px-4 py-2 rounded-full border border-[#E4DDD0] text-red-700">Reset</button>
  </div>

  <div id="phases" class="space-y-8"></div>

  <section class="mt-10">
    <h2 class="serif text-2xl font-bold mb-1">Temuan audit</h2>
    <p class="text-sm text-[#707070] mb-4">Otomatis tercentang kalau semua tiket yang memperbaikinya selesai.</p>
    <div id="audit" class="bg-white/60 border border-[#E4DDD0] rounded-2xl divide-y divide-[#E4DDD0]"></div>
  </section>
</main>

<script>
const DATA = __DATA__;
const KEY = 'tdc-tracker-v1';
let state = {};
try { state = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) {}
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} };
const itemKey = (t, i) => t.id + '::' + i;
let filter = 'all';

const ticketProgress = t => {
  const n = t.items.length, d = t.items.filter((_, i) => state[itemKey(t, i)]).length;
  return { n, d, complete: n > 0 && d === n };
};
const statusOf = p => p.complete ? ['DONE', 'bg-[#1A2E26] text-white'] : p.d > 0 ? ['DOING', 'bg-[#E4B047] text-[#1A2E26]'] : ['TODO', 'bg-[#EFEAE1] text-[#707070]'];
const byId = {};
DATA.phases.forEach(ph => ph.tickets.forEach(t => byId[t.id] = t));

function render() {
  const root = document.getElementById('phases');
  const open = new Set([...root.querySelectorAll('details[open]')].map(d => d.dataset.id));
  root.innerHTML = '';
  let all = 0, allDone = 0;
  const stats = [];

  DATA.phases.forEach(ph => {
    let pn = 0, pd = 0;
    const wrap = document.createElement('section');
    const list = ph.tickets.map(t => {
      const p = ticketProgress(t); pn += p.n; pd += p.d;
      if (filter === 'open' && p.complete) return '';
      if (filter === 'done' && !p.complete) return '';
      const [label, cls] = statusOf(p);
      const items = t.items.map((it, i) => `
        <label class="flex gap-3 py-1.5 ${state[itemKey(t, i)] ? 'item-done' : ''}">
          <input type="checkbox" data-key="${itemKey(t, i)}" ${state[itemKey(t, i)] ? 'checked' : ''}>
          <span class="text-sm leading-relaxed">${it}</span>
        </label>`).join('');
      const notes = t.notes.map(n => `<p class="text-sm text-[#707070] mb-2">${n}</p>`).join('');
      return `
        <details data-id="${t.id}" class="bg-white/60 border border-[#E4DDD0] rounded-2xl" ${open.has(t.id) ? 'open' : ''}>
          <summary class="p-4 sm:p-5 flex items-center gap-3">
            <span class="chev text-[#707070] transition-transform">&#9656;</span>
            <span class="font-mono text-xs text-[#707070] w-16 shrink-0">${t.id}</span>
            <span class="font-semibold flex-1">${t.name}</span>
            <span class="hidden sm:inline text-xs text-[#707070]">${t.estimate}</span>
            <span class="text-xs text-[#707070] w-10 text-right">${p.d}/${p.n}</span>
            <span class="text-[11px] font-bold px-2.5 py-1 rounded-full ${cls}">${label}</span>
          </summary>
          <div class="px-5 pb-5 sm:pl-14">
            ${t.depends && t.depends !== '—' ? `<p class="text-xs text-[#707070] mb-3">Bergantung pada: ${t.depends}</p>` : ''}
            ${notes}
            ${items}
            ${t.done ? `<p class="mt-3 text-sm bg-[#E4B047]/15 rounded-lg px-3 py-2"><strong>Done kalau:</strong> ${t.done}</p>` : ''}
          </div>
        </details>`;
    }).join('');
    all += pn; allDone += pd;
    stats.push([ph.title, pd, pn]);
    if (!list.trim()) return;
    wrap.innerHTML = `<h2 class="serif text-2xl font-bold mb-3">${ph.title}</h2><div class="space-y-3">${list}</div>`;
    root.appendChild(wrap);
  });

  const pct = all ? Math.round(allDone / all * 100) : 0;
  document.getElementById('overall-bar').style.width = pct + '%';
  document.getElementById('overall-text').textContent = `${allDone}/${all} tugas · ${pct}%`;
  document.getElementById('phase-stats').innerHTML = stats.map(([t, d, n]) => `
    <div><p class="text-xs text-[#707070] truncate">${t}</p>
    <div class="h-1.5 bg-[#EFEAE1] rounded-full mt-1 overflow-hidden"><div class="h-full bg-[#E4B047]" style="width:${n ? d / n * 100 : 0}%"></div></div>
    <p class="text-xs mt-1">${d}/${n}</p></div>`).join('');

  document.getElementById('audit').innerHTML = DATA.audit.map(a => {
    const ids = a.tickets.match(/TDC-\\d+/g) || [];
    const ok = ids.length && ids.every(id => byId[id] && ticketProgress(byId[id]).complete);
    return `<div class="flex items-start gap-3 p-4 text-sm">
      <span class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold shrink-0 ${ok ? 'bg-[#1A2E26] text-white' : 'bg-[#EFEAE1] text-[#707070]'}">${ok ? '&#10003;' : a.num}</span>
      <span class="flex-1 ${ok ? 'line-through text-[#9a9a9a]' : ''}">${a.finding}</span>
      <span class="font-mono text-xs text-[#707070]">${a.tickets}</span></div>`;
  }).join('');

  document.querySelectorAll('.filter').forEach(b => {
    const on = b.dataset.filter === filter;
    b.classList.toggle('bg-[#1A2E26]', on); b.classList.toggle('text-white', on);
  });
}

document.addEventListener('change', e => {
  if (!e.target.matches('input[data-key]')) return;
  state[e.target.dataset.key] = e.target.checked; save(); render();
});
document.querySelectorAll('.filter').forEach(b => b.addEventListener('click', () => { filter = b.dataset.filter; render(); }));
document.getElementById('expand').addEventListener('click', e => {
  const ds = document.querySelectorAll('#phases details');
  const openAll = [...ds].some(d => !d.open);
  ds.forEach(d => d.open = openAll);
  e.target.textContent = openAll ? 'Tutup semua' : 'Buka semua';
});
document.getElementById('reset').addEventListener('click', () => {
  if (confirm('Hapus semua centang?')) { state = {}; save(); render(); }
});
render();
</script>
</body>
</html>
"""

(ROOT / "tracker.html").write_text(html.replace("__DATA__", data))
print(f"Built docs/tracker.html: {sum(len(p['tickets']) for p in phases)} tickets, {len(audit)} audit findings")
