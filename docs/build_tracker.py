"""Build docs/tracker.html from docs/TICKETS.md.

Run:  python3 docs/build_tracker.py
Checkbox state is saved in the browser (localStorage), so rebuilding keeps your progress
as long as the order of checklist items inside a ticket doesn't change.
Client dates and needs come from mockup/progress/data.js, the same file the client page reads.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
md = (ROOT / "TICKETS.md").read_text()

# Day-by-day plan. A ticket that spans several days is listed on each of them.
SCHEDULE = [
    {"date": "2026-11-02", "focus": "Kickoff, kirim link progress, tunggu pilihan desain",
     "tickets": ["TDC-001", "TDC-002", "TDC-003", "TDC-027"],
     "tasks": ["Kirim pesan Kickoff (tab Template)", "Sore: catat pilihan desain klien, update data.js"]},
    {"date": "2026-11-03", "focus": "Terapkan arah desain ke Homepage",
     "tickets": ["TDC-005", "TDC-006"], "tasks": ["Pastikan klien sudah menunjuk 1 PIC"]},
    {"date": "2026-11-04", "focus": "Selesaikan Dog Daycare, kirim desain v1",
     "tickets": ["TDC-002", "TDC-003", "TDC-006"],
     "tasks": ["Hari ini batas bahan & jawaban klien. Kalau belum ada, kirim Reminder", "Cek desktop dan HP sebelum kirim"]},
    {"date": "2026-11-05", "focus": "Terima feedback, revisi putaran 1", "tickets": ["TDC-007"], "tasks": []},
    {"date": "2026-11-06", "focus": "Kirim revisi, minta approval desain",
     "tickets": ["TDC-007"],
     "tasks": ["Buat invoice termin 2 (INV-TDC-2026-002)", "Jumat: update data.js & kirim update ke klien"],
     "gate": "Build baru mulai setelah klien tulis \"Design approved\". Batas aman: Senin 9 Nov pagi."},
    {"date": "2026-11-09", "focus": "Repo baru, Netlify, komponen dasar",
     "tickets": ["TDC-004", "TDC-008"], "tasks": ["Cek akun GitHub klien sudah dibuat"]},
    {"date": "2026-11-10", "focus": "Homepage & lokasi", "tickets": ["TDC-009", "TDC-010"],
     "tasks": ["Isi title & meta description sekalian tiap halaman"]},
    {"date": "2026-11-11", "focus": "8 halaman layanan + Services", "tickets": ["TDC-011"], "tasks": []},
    {"date": "2026-11-12", "focus": "Pricing, Schedule, Join, About, FAQ, Franchise, Blog",
     "tickets": ["TDC-012", "TDC-013", "TDC-014"], "tasks": []},
    {"date": "2026-11-13", "focus": "Legal, 404, semua link booking & WhatsApp",
     "tickets": ["TDC-015", "TDC-016"],
     "tasks": ["Jumat: update data.js & kirim update ke klien", "Sabtu 14 Nov dipakai sebagai cadangan kalau build telat"]},
    {"date": "2026-11-16", "focus": "SEO, performa, redirect",
     "tickets": ["TDC-017", "TDC-018", "TDC-019", "TDC-020"], "tasks": []},
    {"date": "2026-11-17", "focus": "QA pagi, kirim preview ke klien sore",
     "tickets": ["TDC-021", "TDC-022"], "tasks": ["14 temuan audit harus tercentang sebelum kirim preview"]},
    {"date": "2026-11-18", "focus": "Klien review. Pakai untuk bug dari tab Bug & CR", "tickets": ["TDC-022"], "tasks": []},
    {"date": "2026-11-19", "focus": "Batas daftar koreksi klien", "tickets": ["TDC-022"],
     "tasks": ["Mulai kerjakan koreksi begitu daftar masuk"]},
    {"date": "2026-11-20", "focus": "Selesaikan koreksi, tagih pelunasan",
     "tickets": ["TDC-022", "TDC-023"],
     "tasks": ["Jumat: update data.js & kirim update ke klien", "Jangan ubah DNS hari ini"],
     "gate": "Website tidak live sebelum pelunasan masuk dan klien konfirmasi tertulis."},
    {"date": "2026-11-23", "focus": "Go live pagi hari", "tickets": ["TDC-024", "TDC-025"],
     "tasks": ["Video call DomaiNesia ± 15 menit", "Jangan sentuh MX dan TXT google-site-verification"]},
    {"date": "2026-11-30", "focus": "Cek +7 hari, kabari hosting lama boleh dihentikan", "tickets": ["TDC-026"], "tasks": []},
    {"date": "2026-12-23", "focus": "Laporan +30 hari, serahkan akses, tawarkan maintenance", "tickets": ["TDC-026"], "tasks": []},
]

PROGRESS_URL = "https://arnoldtherigan15.github.io/thedogclub/progress/"
GUIDE_URL = "https://arnoldtherigan15.github.io/thedogclub/onboarding/"

TEMPLATES = [
    ("Kickoff", f"""Halo Kak Erry, terima kasih, DP sudah saya terima dan proyek resmi mulai hari ini, Senin 2 Nov. Target website live Senin 23 Nov.

Timeline, progress, dan daftar yang perlu disiapkan ada di satu link ini:
{PROGRESS_URL}

Yang paling dekat:
1. Pilih arah desain
2. Tunjuk 1 orang sebagai contact person
3. Kirim logo, foto, konfirmasi harga, dan jawaban pertanyaan paling lambat Rabu 4 Nov

Panduan langkah per langkahnya ada di sini:
{GUIDE_URL}

Update berikutnya saya kirim Jumat ini."""),
    ("Reminder bahan", f"""Halo Kak Erry, sekadar mengingatkan, yang masih saya tunggu:
- [isi item yang belum]

Supaya target live 23 Nov tetap aman, mohon dikirim paling lambat [tanggal]. Daftarnya ada di sini: {PROGRESS_URL}
Terima kasih!"""),
    ("Desain siap review", """Halo Kak Erry, desain Homepage dan Dog Daycare sudah siap direview, versi desktop dan HP:
[link]

Mohon kirim semua masukan tim dalam satu daftar paling lambat [tanggal], supaya tidak ada yang terlewat. Harga sudah termasuk 2 putaran revisi besar.

Kalau sudah cocok, cukup balas "Design approved" dan saya lanjut ke tahap build."""),
    ("Design approved + termin 2", f"""Terima kasih Kak Erry, approval desain sudah saya catat. Mulai sekarang desain dikunci dan saya lanjut build.

Invoice termin 2 (IDR 2.250.000): [link invoice]

Satu lagi, mohon dibuatkan akun GitHub ya, ± 10 menit. Panduannya ada di sini: {GUIDE_URL}#github"""),
    ("Update Jumat", f"""Halo Kak Erry, update minggu ini:

Selesai:
- [isi]

Minggu depan:
- [isi]

Yang saya butuhkan:
- [isi, atau "belum ada"]

Status target live: [tetap 23 Nov / bergeser ke ...]
Detail lengkap: {PROGRESS_URL}"""),
    ("Timeline bergeser", """Halo Kak Erry, [bahan/feedback] yang dijadwalkan [tanggal] belum saya terima, sehingga target live bergeser dari [tanggal lama] ke [tanggal baru]. Kalau bisa diterima [tanggal], target awal masih saya usahakan.

Terima kasih atas pengertiannya."""),
    ("Permintaan di luar scope", """Siap Kak Erry, permintaan ini di luar scope paket Essential yang disepakati, jadi saya catat sebagai pekerjaan tambahan:
- [isi]: IDR [harga], estimasi [x hari]

Kalau setuju, saya kerjakan setelah item yang berjalan selesai. Kalau mau ditunda sampai setelah launch juga bisa."""),
    ("Preview siap", """Halo Kak Erry, semua halaman sudah bisa dicek di link ini, bisa dibuka di HP dan laptop:
[link preview]

Mohon cek isi dan harganya, lalu kirim satu daftar koreksi paling lambat Kamis 19 Nov."""),
    ("Pelunasan + go live", """Halo Kak Erry, semua koreksi sudah selesai. Mohon konfirmasi website siap live, lalu pelunasan IDR 1.500.000 bisa ditransfer sesuai invoice:
[link invoice]

Setelah masuk, kita jadwalkan video call ± 15 menit Senin 23 Nov pagi untuk pindah domain. Mohon siapkan login DomaiNesia. Email @thedogclub.id tidak akan terganggu."""),
]

RULES = [
    ("Rutin harian", [
        "Pagi: buka tab Hari ini. Kerjakan yang ada di situ saja.",
        "Sore: centang tiket, catat bug baru, cek daftar Nunggu klien.",
        "Jumat: tulis update di data.js, push, lalu kirim template Update Jumat.",
    ]),
    ("Gerbang: jangan dilewati", [
        "Tidak mulai build sebelum ada tulisan \"Design approved\".",
        "Tidak kirim preview sebelum 14 temuan audit tercentang.",
        "Tidak ubah DNS sebelum pelunasan masuk dan klien konfirmasi tertulis.",
        "Kode pindah ke GitHub klien setelah lunas.",
    ]),
    ("Scope", [
        "Revisi mayor maksimal 2 putaran. Selebihnya jadi CR.",
        "Permintaan baru dicatat sebagai CR di tab Bug & CR, kasih harga dulu, kerjakan setelah setuju.",
        "Halaman tambahan IDR 750.000. Update konten IDR 150.000 per permintaan.",
    ]),
    ("Komunikasi", [
        "Semua keputusan dan approval harus tertulis. Screenshot dan simpan.",
        "Telat bahan dari klien: kabari hari itu juga, tanggal live bergeser sama banyak.",
        "Telat dari sisi sendiri: kabari sebelum tanggalnya lewat, sertakan tanggal baru.",
        "Jangan minta password lewat WhatsApp.",
    ]),
]


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
        items, seeded, done, notes = [], [], "", []
        for line in lines[1:]:
            if line.startswith(("- [ ] ", "- [x] ")):
                if line.startswith("- [x] "):
                    seeded.append(len(items))
                items.append(inline(line[6:]))
            elif line.startswith("**Done kalau:**"):
                done = inline(line.replace("**Done kalau:**", "").strip())
            elif line.strip() and not line.startswith(("---", "## ")):
                notes.append(inline(line.strip()))
        tickets.append({"id": tid, "name": inline(name), "items": items, "seeded": seeded, "done": done,
                        "notes": notes, **meta.get(tid, {"estimate": "", "depends": ""})})
    phases.append({"title": title, "tickets": tickets})

data = json.dumps({"phases": phases, "audit": audit, "schedule": SCHEDULE,
                   "templates": TEMPLATES, "rules": RULES}, ensure_ascii=False).replace("</", "<\\/")

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
  details[open] > summary .chev { transform: rotate(90deg); }
  .tab[aria-selected=true] { background: #1A2E26; color: #fff; }
  .field { background: #fff; border: 1px solid #E4DDD0; border-radius: .75rem; padding: .55rem .75rem; font-size: .875rem; }
</style>
</head>
<body>
<main class="max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
  <header class="mb-6">
    <p class="text-xs font-bold uppercase tracking-widest text-[#B98A25]">Tracker proyek · internal</p>
    <h1 class="serif text-4xl font-bold mt-1">The Dog Club — Essential</h1>
    <p id="head-note" class="text-sm text-[#707070] mt-2"></p>
  </header>

  <section class="bg-white/60 border border-[#E4DDD0] rounded-2xl p-5 mb-6">
    <div class="flex items-baseline justify-between mb-2">
      <p class="font-semibold">Progres keseluruhan</p>
      <p id="overall-text" class="text-sm text-[#707070]"></p>
    </div>
    <div class="h-3 bg-[#EFEAE1] rounded-full overflow-hidden"><div id="overall-bar" class="h-full bg-[#1A2E26] transition-all"></div></div>
    <div id="phase-stats" class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-5 text-sm"></div>
  </section>

  <nav class="flex flex-wrap gap-2 mb-6 text-sm" role="tablist">
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="today">Hari ini</button>
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="schedule">Jadwal</button>
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="tickets">Tiket</button>
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="bugs">Bug &amp; CR</button>
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="client">Nunggu klien</button>
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="templates">Template</button>
    <button class="tab px-4 py-2 rounded-full border border-[#1A2E26]" data-tab="rules">Aturan</button>
  </nav>

  <div data-panel="today" id="today"></div>
  <div data-panel="schedule" id="schedule" class="space-y-2"></div>

  <div data-panel="tickets">
    <div class="flex flex-wrap gap-2 mb-6 text-sm">
      <button data-filter="all" class="filter px-4 py-2 rounded-full border border-[#1A2E26]">Semua</button>
      <button data-filter="open" class="filter px-4 py-2 rounded-full border border-[#1A2E26]">Belum selesai</button>
      <button data-filter="done" class="filter px-4 py-2 rounded-full border border-[#1A2E26]">Selesai</button>
      <button id="expand" class="px-4 py-2 rounded-full border border-[#E4DDD0] ml-auto">Buka semua</button>
    </div>
    <div id="phases" class="space-y-8"></div>
  </div>

  <div data-panel="bugs">
    <h2 class="serif text-2xl font-bold mb-1">Catat bug atau change request</h2>
    <p class="text-sm text-[#707070] mb-4">Bug dari pekerjaan sendiri gratis. Permintaan baru dari klien = CR, kasih harga dulu.</p>
    <form id="log-form" class="grid sm:grid-cols-[1fr_8rem_8rem] gap-2 mb-3">
      <input name="title" required class="field" placeholder="Contoh: Tombol Book di pet taxi salah link">
      <select name="type" class="field"><option>Bug</option><option>CR</option></select>
      <select name="priority" class="field"><option>Tinggi</option><option selected>Sedang</option><option>Rendah</option></select>
      <input name="note" class="field sm:col-span-2" placeholder="Halaman, dari siapa, harga CR">
      <button class="bg-[#1A2E26] text-white rounded-xl px-4 py-2 text-sm font-semibold">Tambah</button>
    </form>
    <div id="log" class="bg-white/60 border border-[#E4DDD0] rounded-2xl divide-y divide-[#E4DDD0] mb-10"></div>

    <h2 class="serif text-2xl font-bold mb-1">Temuan audit</h2>
    <p class="text-sm text-[#707070] mb-4">Otomatis tercentang kalau semua tiket yang memperbaikinya selesai.</p>
    <div id="audit" class="bg-white/60 border border-[#E4DDD0] rounded-2xl divide-y divide-[#E4DDD0]"></div>
  </div>

  <div data-panel="client">
    <p class="text-sm text-[#707070] mb-4">Status diambil dari <code>mockup/progress/data.js</code>. Ganti <code>status: 'done'</code> di file itu supaya halaman client ikut berubah.</p>
    <div id="client" class="bg-white/60 border border-[#E4DDD0] rounded-2xl divide-y divide-[#E4DDD0]"></div>
    <h2 class="serif text-2xl font-bold mt-10 mb-3">Angka untuk data.js</h2>
    <div id="numbers" class="text-sm bg-white/60 border border-[#E4DDD0] rounded-2xl p-5"></div>
  </div>

  <div data-panel="templates" id="templates" class="space-y-3"></div>

  <div data-panel="rules">
    <div id="rules" class="grid sm:grid-cols-2 gap-4"></div>
    <div class="mt-10 flex flex-wrap gap-2 text-sm">
      <button id="backup" class="px-4 py-2 rounded-full border border-[#1A2E26]">Backup progres</button>
      <label class="px-4 py-2 rounded-full border border-[#1A2E26] cursor-pointer">Restore<input id="restore" type="file" accept=".json" class="hidden"></label>
      <button id="reset" class="px-4 py-2 rounded-full border border-[#E4DDD0] text-red-700 ml-auto">Reset centang</button>
    </div>
    <p class="text-xs text-[#707070] mt-3">Centang tersimpan di browser ini saja. Backup tiap Jumat, jangan clear site data.</p>
  </div>
</main>

<script src="../mockup/progress/data.js"></script>
<script>
const DATA = __DATA__;
const P = window.PROJECT;
const KEY = 'tdc-tracker-v1';
const LOG_KEY = 'tdc-log-v1';
const load = (k, d) => { try { return JSON.parse(localStorage.getItem(k)) || d; } catch (e) { return d; } };
const store = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
let state = load(KEY, {});
let log = load(LOG_KEY, []);
const save = () => { store(KEY, state); store(LOG_KEY, log); };
const itemKey = (t, i) => t.id + '::' + i;
let filter = 'all';
let tab = 'today';

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const toDate = s => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d); };
const day = s => toDate(s).toLocaleDateString('id-ID', { weekday: 'short', day: 'numeric', month: 'short' });
const now = new Date();
const today = [now.getFullYear(), String(now.getMonth() + 1).padStart(2, '0'), String(now.getDate()).padStart(2, '0')].join('-');

const byId = {};
DATA.phases.forEach(ph => ph.tickets.forEach(t => byId[t.id] = t));
const lastDate = {};
DATA.schedule.forEach(s => s.tickets.forEach(id => lastDate[id] = s.date));

const isChecked = (t, i) => { const v = state[itemKey(t, i)]; return v === undefined ? t.seeded.includes(i) : v; };
const ticketProgress = t => {
  const n = t.items.length, d = t.items.filter((_, i) => isChecked(t, i)).length;
  return { n, d, complete: n > 0 && d === n };
};
const statusOf = p => p.complete ? ['DONE', 'bg-[#1A2E26] text-white'] : p.d > 0 ? ['DOING', 'bg-[#E4B047] text-[#1A2E26]'] : ['TODO', 'bg-[#EFEAE1] text-[#707070]'];
const lateTickets = () => Object.keys(lastDate).filter(id => lastDate[id] < today && byId[id] && !ticketProgress(byId[id]).complete);
const auditDone = a => { const ids = a.tickets.match(/TDC-\\d+/g) || []; return ids.length && ids.every(id => byId[id] && ticketProgress(byId[id]).complete); };

function ticketCard(t, open) {
  const p = ticketProgress(t);
  const [label, cls] = statusOf(p);
  const items = t.items.map((it, i) => `
    <label class="flex gap-3 py-1.5 ${isChecked(t, i) ? 'item-done' : ''}">
      <input type="checkbox" data-key="${itemKey(t, i)}" ${isChecked(t, i) ? 'checked' : ''}>
      <span class="text-sm leading-relaxed">${it}</span>
    </label>`).join('');
  const notes = t.notes.map(n => `<p class="text-sm text-[#707070] mb-2">${n}</p>`).join('');
  return `
    <details data-id="${t.id}" class="bg-white/60 border border-[#E4DDD0] rounded-2xl" ${open ? 'open' : ''}>
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
}

function renderToday(open) {
  const entry = DATA.schedule.find(s => s.date >= today);
  const late = lateTickets();
  const waiting = P.needs.filter(n => n.status !== 'done' && n.due <= (entry ? entry.date : today));
  const openBugs = log.filter(l => !l.done);
  let html = '';
  if (late.length) html += `<section class="bg-red-50 border border-red-200 rounded-2xl p-5 mb-6">
    <p class="font-semibold text-red-800 mb-2">Telat dari jadwal</p>
    <div class="space-y-3">${late.map(id => ticketCard(byId[id], open.has(id))).join('')}</div>
    <p class="text-sm text-red-800 mt-3">Selesaikan ini dulu. Kalau mengubah tanggal live, kabari klien hari ini.</p></section>`;
  if (entry) {
    const isToday = entry.date === today;
    html += `<section class="mb-6"><p class="text-xs font-bold uppercase tracking-widest text-[#B98A25]">${isToday ? 'Hari ini' : 'Jadwal berikutnya'} · ${day(entry.date)}</p>
      <h2 class="serif text-3xl font-bold mt-1 mb-4">${entry.focus}</h2>
      ${entry.gate ? `<p class="text-sm bg-[#E4B047]/15 rounded-lg px-3 py-2 mb-4"><strong>Gerbang:</strong> ${esc(entry.gate)}</p>` : ''}
      ${entry.tasks.length ? `<ul class="list-disc ml-5 text-sm space-y-1 mb-4">${entry.tasks.map(t => `<li>${esc(t)}</li>`).join('')}</ul>` : ''}
      <div class="space-y-3">${entry.tickets.filter(id => !late.includes(id)).map(id => ticketCard(byId[id], open.has(id) || !ticketProgress(byId[id]).complete)).join('')}</div></section>`;
  } else {
    html += '<p class="serif text-3xl font-bold mb-6">Semua jadwal sudah lewat.</p>';
  }
  html += `<div class="grid sm:grid-cols-2 gap-4">
    <section class="bg-white/60 border border-[#E4DDD0] rounded-2xl p-5"><p class="font-semibold mb-2">Nunggu klien (${waiting.length})</p>
      ${waiting.length ? `<ul class="text-sm space-y-1">${waiting.map(n => `<li class="${n.due < today ? 'text-red-700 font-medium' : ''}">${esc(n.title)} <span class="text-xs">· ${day(n.due)}</span></li>`).join('')}</ul>` : '<p class="text-sm text-[#707070]">Tidak ada.</p>'}</section>
    <section class="bg-white/60 border border-[#E4DDD0] rounded-2xl p-5"><p class="font-semibold mb-2">Bug &amp; CR terbuka (${openBugs.length})</p>
      ${openBugs.length ? `<ul class="text-sm space-y-1">${openBugs.slice(0, 6).map(l => `<li>${esc(l.title)} <span class="text-xs text-[#707070]">· ${l.type}, ${l.priority}</span></li>`).join('')}</ul>` : '<p class="text-sm text-[#707070]">Tidak ada.</p>'}</section>
  </div>`;
  document.getElementById('today').innerHTML = html;
}

function renderSchedule() {
  document.getElementById('schedule').innerHTML = DATA.schedule.map(s => {
    const done = s.tickets.every(id => byId[id] && ticketProgress(byId[id]).complete);
    const late = !done && s.date < today;
    const cls = done ? 'opacity-50' : s.date === today ? 'border-[#1A2E26] border-2' : late ? 'border-red-300 bg-red-50' : '';
    return `<div class="bg-white/60 border border-[#E4DDD0] rounded-2xl p-4 grid sm:grid-cols-[7rem_1fr_auto] gap-x-4 gap-y-1 ${cls}">
      <span class="text-sm font-semibold">${day(s.date)}</span>
      <span class="text-sm">${s.focus}</span>
      <span class="font-mono text-xs text-[#707070] sm:text-right">${s.tickets.map(id => id.replace('TDC-', '')).join(' ')}</span>
    </div>`;
  }).join('');
}

function renderTickets(open) {
  const root = document.getElementById('phases');
  root.innerHTML = '';
  DATA.phases.forEach(ph => {
    const list = ph.tickets.map(t => {
      const p = ticketProgress(t);
      if (filter === 'open' && p.complete) return '';
      if (filter === 'done' && !p.complete) return '';
      return ticketCard(t, open.has(t.id));
    }).join('');
    if (!list.trim()) return;
    const wrap = document.createElement('section');
    wrap.innerHTML = `<h2 class="serif text-2xl font-bold mb-3">${ph.title}</h2><div class="space-y-3">${list}</div>`;
    root.appendChild(wrap);
  });
  document.querySelectorAll('.filter').forEach(b => {
    const on = b.dataset.filter === filter;
    b.classList.toggle('bg-[#1A2E26]', on); b.classList.toggle('text-white', on);
  });
}

function renderLog() {
  document.getElementById('log').innerHTML = log.length ? log.map((l, i) => `
    <div class="flex items-start gap-3 p-4 text-sm ${l.done ? 'item-done' : ''}">
      <input type="checkbox" data-log="${i}" ${l.done ? 'checked' : ''}>
      <span class="flex-1"><strong class="font-semibold">${esc(l.title)}</strong>${l.note ? `<br><small class="text-[#707070]">${esc(l.note)}</small>` : ''}</span>
      <span class="text-xs text-[#707070] whitespace-nowrap">${l.type} · ${l.priority}</span>
      <button data-del="${i}" class="text-xs text-red-700" aria-label="Hapus">&times;</button>
    </div>`).join('') : '<p class="p-4 text-sm text-[#707070]">Belum ada catatan.</p>';
  document.getElementById('audit').innerHTML = DATA.audit.map(a => {
    const ok = auditDone(a);
    return `<div class="flex items-start gap-3 p-4 text-sm">
      <span class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold shrink-0 ${ok ? 'bg-[#1A2E26] text-white' : 'bg-[#EFEAE1] text-[#707070]'}">${ok ? '&#10003;' : a.num}</span>
      <span class="flex-1 ${ok ? 'line-through text-[#9a9a9a]' : ''}">${a.finding}</span>
      <span class="font-mono text-xs text-[#707070]">${a.tickets}</span></div>`;
  }).join('');
}

function renderClient() {
  document.getElementById('client').innerHTML = P.needs.map(n => {
    const overdue = n.status !== 'done' && n.due < today;
    return `<div class="flex items-center gap-3 p-4 text-sm">
      <span class="w-5 text-center">${n.status === 'done' ? '&#10003;' : '&#9675;'}</span>
      <span class="flex-1 ${n.status === 'done' ? 'line-through text-[#9a9a9a]' : ''}">${esc(n.title)}${n.optional ? ' <small class="text-[#707070]">opsional</small>' : ''}</span>
      <span class="text-xs whitespace-nowrap ${overdue ? 'text-red-700 font-bold' : 'text-[#707070]'}">${overdue ? 'Lewat · ' : ''}${day(n.due)}</span></div>`;
  }).join('');
  const fixed = DATA.audit.filter(auditDone).length;
  document.getElementById('numbers').innerHTML = `<p><code>auditFixed: ${fixed}</code> ${fixed === P.auditFixed ? '(sudah sama)' : `(data.js masih ${P.auditFixed})`}</p>
    <p class="mt-2"><code>updated</code> terakhir: ${day(P.updated)}. Ganti tiap kirim update.</p>`;
}

function render() {
  const open = new Set([...document.querySelectorAll('details[open]')].map(d => d.dataset.id));
  let all = 0, allDone = 0;
  const stats = DATA.phases.map(ph => {
    let pn = 0, pd = 0;
    ph.tickets.forEach(t => { const p = ticketProgress(t); pn += p.n; pd += p.d; });
    all += pn; allDone += pd;
    return [ph.title, pd, pn];
  });
  const pct = all ? Math.round(allDone / all * 100) : 0;
  document.getElementById('overall-bar').style.width = pct + '%';
  document.getElementById('overall-text').textContent = `${allDone}/${all} tugas · ${pct}%`;
  document.getElementById('phase-stats').innerHTML = stats.map(([t, d, n]) => `
    <div><p class="text-xs text-[#707070] truncate">${t}</p>
    <div class="h-1.5 bg-[#EFEAE1] rounded-full mt-1 overflow-hidden"><div class="h-full bg-[#E4B047]" style="width:${n ? d / n * 100 : 0}%"></div></div>
    <p class="text-xs mt-1">${d}/${n}</p></div>`).join('');
  document.getElementById('head-note').textContent = `Mulai ${day(P.start)} · target live ${day(P.target)}`;

  renderToday(open); renderSchedule(); renderTickets(open); renderLog(); renderClient();
  document.querySelectorAll('[data-panel]').forEach(p => p.hidden = p.dataset.panel !== tab);
  document.querySelectorAll('.tab').forEach(b => b.setAttribute('aria-selected', b.dataset.tab === tab));
}

document.getElementById('templates').innerHTML = DATA.templates.map(([name, text], i) => `
  <details class="bg-white/60 border border-[#E4DDD0] rounded-2xl">
    <summary class="p-4 flex items-center gap-3"><span class="chev text-[#707070] transition-transform">&#9656;</span><span class="font-semibold flex-1">${name}</span></summary>
    <div class="px-5 pb-5"><pre class="whitespace-pre-wrap text-sm font-sans leading-relaxed">${esc(text)}</pre>
    <button data-copy="${i}" class="mt-3 text-sm underline">Salin</button></div>
  </details>`).join('');
document.getElementById('rules').innerHTML = DATA.rules.map(([title, items]) => `
  <section class="bg-white/60 border border-[#E4DDD0] rounded-2xl p-5"><h2 class="font-semibold mb-2">${title}</h2>
  <ul class="list-disc ml-5 text-sm space-y-1.5">${items.map(x => `<li>${esc(x)}</li>`).join('')}</ul></section>`).join('');

document.addEventListener('change', e => {
  if (e.target.matches('input[data-key]')) { state[e.target.dataset.key] = e.target.checked; save(); render(); }
  if (e.target.matches('input[data-log]')) { log[e.target.dataset.log].done = e.target.checked; save(); render(); }
});
document.addEventListener('click', e => {
  const t = e.target;
  if (t.matches('.tab')) { tab = t.dataset.tab; render(); }
  if (t.matches('.filter')) { filter = t.dataset.filter; render(); }
  if (t.dataset.del !== undefined && confirm('Hapus catatan ini?')) { log.splice(+t.dataset.del, 1); save(); render(); }
  if (t.dataset.copy !== undefined) {
    navigator.clipboard.writeText(DATA.templates[t.dataset.copy][1]).then(() => { t.textContent = 'Tersalin'; }).catch(() => {});
  }
});
document.getElementById('log-form').addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  log.unshift({ title: f.get('title'), type: f.get('type'), priority: f.get('priority'), note: f.get('note'), done: false, created: today });
  e.target.reset(); save(); render();
});
document.getElementById('expand').addEventListener('click', e => {
  const ds = document.querySelectorAll('#phases details');
  const openAll = [...ds].some(d => !d.open);
  ds.forEach(d => d.open = openAll);
  e.target.textContent = openAll ? 'Tutup semua' : 'Buka semua';
});
document.getElementById('reset').addEventListener('click', () => {
  if (confirm('Hapus semua centang tiket?')) { state = {}; save(); render(); }
});
document.getElementById('backup').addEventListener('click', () => {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify({ state, log }, null, 2)], { type: 'application/json' }));
  a.download = `tdc-tracker-${today}.json`;
  a.click();
});
document.getElementById('restore').addEventListener('change', e => {
  const file = e.target.files[0];
  if (!file) return;
  file.text().then(text => {
    const saved = JSON.parse(text);
    state = saved.state || {}; log = saved.log || [];
    save(); render();
  }).catch(() => alert('File backup tidak bisa dibaca.'));
});
render();
</script>
</body>
</html>
"""

(ROOT / "tracker.html").write_text(html.replace("__DATA__", data))
print(f"Built docs/tracker.html: {sum(len(p['tickets']) for p in phases)} tickets, {len(audit)} audit findings")
