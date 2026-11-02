"""Generate the design direction samples (a, b, c) and the chooser page.

Run:  python3 mockup/design/build_design.py
d.html is written by hand, so this script does not touch it. All are clean and minimalist, inspired by the client's references (Blank Street,
dogppl.co, lilluvdog.com). Same real content in each, so the client compares style only.
Photos and prices come from the live thedogclub.id site.
"""
from pathlib import Path

ROOT = Path(__file__).parent
PAWSI = "https://book.pawsi.id/thedogclubbali"

SERVICES = [
    ("Dog Daycare", "Cage-free play in a 700 sqm park with two bone-shaped pools.", "From IDR 100.000", "golden-pool.jpg"),
    ("Luxury Dog Hotel", "Sleepovers at the Dog Villa, supervised by our team 24/7.", "From IDR 160.000 a night", "pack.jpg"),
    ("Dog Spa", "Baths, cuts and brushing with natural products only.", "From IDR 110.000", "spa.jpg"),
]
PRICES = [
    ("Half daycare", "4 hours play in park & pool", "100.000"),
    ("Full daycare", "All day play & care", "120.000"),
    ("Deluxe boarding", "Weekday night at the Dog Villa", "160.000"),
    ("Prestige boarding", "+1 hour beach walk included", "200.000"),
    ("Essential bath & brush", "Small dog, short hair", "110.000"),
]
LOCATIONS = [
    ("Umalas", "The Dog Club", "+62 811-3940-055"),
    ("Ungasan", "The Dog Club", "+62 812-4645-3589"),
    ("Berawa", "The Dog Hotel", "+62 813-1155-109"),
]
DAY = [
    ("01", "morning walk", "On the beach with the gang, on leash."),
    ("02", "playtime", "All day in the park, with trained staff."),
    ("03", "dinner", "A well-deserved meal at 5pm."),
    ("04", "rest", "Back to the Dog Villa for a good night's sleep."),
]

BASE = """
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}img{display:block;max-width:100%}a{color:inherit;text-decoration:none}
.bar{background:#0F120E;color:#fff;font:500 12px/1.4 system-ui,sans-serif;text-align:center;padding:8px 16px}.bar a{text-decoration:underline}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.nav{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 24px;max-width:1240px;margin:0 auto}
.nav img{height:50px;width:auto}.links{display:flex;gap:32px;font-size:15px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.price-row{display:flex;justify-content:space-between;gap:16px;padding:18px 0}.price-row small{display:inline-block;margin-left:10px;opacity:.6}
@media(max-width:820px){.links{display:none}.grid3,.grid4,.split{grid-template-columns:1fr}.split{gap:32px}}
/* Motion: subtle reveal on scroll, hover states, slow hero zoom */
.reveal{opacity:0;transform:translateY(20px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}
.reveal.in{opacity:1;transform:none}
.ph{overflow:hidden;border-radius:inherit}.ph img{transition:transform .7s cubic-bezier(.2,.7,.2,1)}
.card:hover .ph img,.rowc:hover .ph img{transform:scale(1.04)}
.btn{transition:opacity .25s ease,transform .25s ease}.btn:hover{opacity:.85;transform:translateY(-1px)}
.links a{transition:opacity .25s ease}.links a:hover{opacity:.55}
.hero{overflow:hidden}.hero>img,.hero .zoom{animation:heroZoom 1.8s cubic-bezier(.2,.7,.2,1) both}
@keyframes heroZoom{from{transform:scale(1.05)}to{transform:none}}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}.hero>img,.hero .zoom{animation:none}.ph img,.btn{transition:none}}
"""

# Hidden state is added by JS, so the page stays fully visible if scripts don't run.
MOTION = """<script>
(function () {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  var els = document.querySelectorAll('.hero h1,.hero p,.hero .btn,.hero .btn-ghost,.sec h2,.sec-title,.story p,.story-box p,.story img,.card,.rowc,.price-row,.loc,.loc-card,.step,.step-card');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) {
    var i = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.transitionDelay = (i % 4) * 80 + 'ms';
    el.classList.add('reveal');
    io.observe(el);
  });
})();
</script>"""

THEMES = {
"a": {"name": "A — Paper", "fonts": "family=Instrument+Sans:wght@400;500;600", "css": """
body{background:#FFFDFC;color:#0F120E;font-family:'Instrument Sans',sans-serif}
h1,h2,h3{font-weight:500;letter-spacing:-.025em}
.btn{display:inline-block;background:#0F120E;color:#FFFDFC;padding:13px 26px;border-radius:999px;font-weight:500;font-size:15px}
.hero{padding:56px 0 24px}.hero h1{font-size:clamp(44px,8vw,104px);line-height:1;max-width:14ch}
.hero .row{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin:28px 0 40px}.hero p{font-size:18px;color:#73736E;max-width:40ch}
.hero img{width:100%;aspect-ratio:2/1;object-fit:cover;border-radius:4px}
.sec{padding:88px 0}.sec>.wrap>h2{font-size:clamp(28px,3.4vw,40px);padding-bottom:20px;border-bottom:1px solid #E2E2E2;margin-bottom:32px}
.card img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:4px}.card h3{font-size:22px;margin-top:16px}.card p{color:#73736E;margin-top:4px}.card small{display:block;margin-top:10px;font-size:14px}
.price-row{border-bottom:1px solid #E2E2E2;font-size:18px}
.loc{border-top:1px solid #0F120E;padding-top:14px}.loc p{color:#73736E;font-size:14px}.loc h3{font-size:30px;margin:2px 0 10px}
"""},
"b": {"name": "B — Olive", "fonts": "family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&family=DM+Sans:wght@400;500", "css": """
body{background:#F3F1EF;color:#49503D;font-family:'DM Sans',sans-serif}
h1,h2,h3{font-family:'Fraunces',serif;font-weight:300;letter-spacing:-.02em}h1 em,h2 em{font-style:italic;color:#A47E5C}
.btn{display:inline-block;background:#49503D;color:#F3F1EF;padding:14px 28px;border-radius:999px;font-size:15px}.hero .btn{background:#F3F1EF;color:#49503D}
.hero{position:relative;height:min(84vh,740px);min-height:500px;color:#fff}.hero>img{width:100%;height:100%;object-fit:cover}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(30,34,24,.7),rgba(30,34,24,.1) 60%)}
.hero .txt{position:absolute;z-index:1;left:0;right:0;bottom:48px}.hero h1{font-size:clamp(44px,7.6vw,100px);line-height:1;max-width:13ch;margin-bottom:24px}.hero h1 em{color:#fff}
.sec{padding:96px 0}.sec h2{font-size:clamp(32px,4.4vw,56px);line-height:1.08;margin-bottom:20px}.sec p{line-height:1.65}
.story img{width:100%;aspect-ratio:4/5;object-fit:cover}
.rowc{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;padding:32px 0}.rowc img{width:100%;aspect-ratio:3/2;object-fit:cover}.rowc:nth-child(even) .ph{order:2}.rowc h3{font-size:34px;margin-bottom:8px}.rowc small{display:block;margin-top:12px;color:#A47E5C;font-size:15px}
.price-row{border-top:1px solid #cfccc4;font-size:18px}
.loc h3{font-size:30px}.loc p{font-size:14px;opacity:.75}
@media(max-width:820px){.rowc{grid-template-columns:1fr;gap:16px}.rowc:nth-child(even) .ph{order:0}}
"""},
"c": {"name": "C — Soft", "fonts": "family=Figtree:wght@400;500;600", "css": """
body{background:#fff;color:#3F443F;font-family:'Figtree',sans-serif}
h1,h2,h3{font-weight:500;text-transform:lowercase;letter-spacing:-.02em}h1 em,h2 em{font-style:italic;font-weight:400;color:#766E5F}
.btn{display:inline-block;background:#3F443F;color:#fff;padding:14px 28px;border-radius:8px;font-weight:500;font-size:15px;text-transform:lowercase}
.links{text-transform:lowercase}
.hero{text-align:center;padding:56px 0 40px}.hero h1{font-size:clamp(42px,7vw,88px);line-height:1.04;margin-bottom:16px}.hero p{font-size:18px;color:#766E5F;margin:0 auto 28px;max-width:44ch}
.hero img{width:100%;aspect-ratio:2/1;object-fit:cover;border-radius:16px;margin-top:48px}
.sec{padding:80px 0}.sec.tint{background:#F4F3EE}.sec h2{font-size:clamp(28px,3.6vw,44px);text-align:center;margin-bottom:40px}
.step b{display:block;font-size:13px;font-weight:600;color:#766E5F;margin-bottom:8px}.step h3{font-size:22px;margin-bottom:4px}.step p{font-size:15px;color:#766E5F}
.card img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:12px}.card h3{font-size:22px;margin-top:14px}.card p{color:#766E5F;margin-top:2px}.card small{display:block;margin-top:8px;font-size:14px;font-weight:500}
.price-row{border-bottom:1px solid #DCDAD3;font-size:17px}.narrow{max-width:760px;margin:0 auto}
.loc{text-align:center}.loc h3{font-size:26px}.loc p{font-size:14px;color:#766E5F}
"""},
}


def book(cls="btn"):
    return f'<a class="{cls}" href="{PAWSI}" target="_blank" rel="noopener noreferrer">Book a visit</a>'


def cards():
    return "".join(f'<article class="card"><div class="ph"><img src="img/{i}" alt="{n}" loading="lazy"></div><h3>{n}</h3><p>{d}</p><small>{p}</small></article>' for n, d, p, i in SERVICES)


def rows():
    return "".join(f'<div class="price-row"><span>{a}<small>{b}</small></span><span>IDR {c}</span></div>' for a, b, c in PRICES)


def locs():
    return "".join(f'<div class="loc"><p>{b}</p><h3>{a}</h3><p>{c}</p></div>' for a, b, c in LOCATIONS)


def body_a():
    return f"""<section class="hero"><div class="wrap"><h1>Your dog's new favorite place.</h1>
<div class="row"><p>Cage-free daycare, a luxury dog hotel, spa and training across Bali.</p>{book()}</div>
<div class="ph" style="border-radius:4px"><img class="zoom" src="img/pool-dogs.jpg" alt="Two dogs in the pool at The Dog Club"></div></div></section>
<section class="sec"><div class="wrap"><h2>What we do</h2><div class="grid3">{cards()}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Popular services</h2>{rows()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Visit us</h2><div class="grid3">{locs()}</div></div></section>"""


def body_b():
    items = "".join(f'<div class="rowc"><div class="ph"><img src="img/{"husky-water.jpg" if i == "golden-pool.jpg" else i}" alt="{n}" loading="lazy"></div><div><h3>{n}</h3><p>{d}</p><small>{p}</small></div></div>' for n, d, p, i in SERVICES)
    return f"""<section class="hero"><img src="img/golden-pool.jpg" alt="Dogs in the pool at The Dog Club"><div class="txt"><div class="wrap"><h1>Your dog's <em>new favorite</em> place.</h1>{book()}</div></div></section>
<section class="sec"><div class="wrap split story"><div><h2>Dogs should enjoy their holiday as much <em>as you do.</em></h2><p>Our dog-loving team combines home-like attention with supervised fun, whether your pup stays for a day, a week or several months.</p></div><img src="img/park-pool.jpg" alt="The park at The Dog Club" loading="lazy"></div></section>
<section class="sec" style="padding-top:0"><div class="wrap">{items}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2>Popular services</h2>{rows()}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap grid3">{locs()}</div></section>"""


def body_c():
    steps = "".join(f'<div class="step"><b>{n}</b><h3>{t}</h3><p>{d}</p></div>' for n, t, d in DAY)
    return f"""<section class="hero"><div class="wrap"><h1>happy dog. <em>happy you.</em></h1><p>Cage-free daycare, a luxury dog hotel, spa and training across Bali.</p>{book()}
<div class="ph" style="border-radius:16px;margin-top:48px"><img class="zoom" style="margin-top:0" src="img/beach.jpg" alt="Morning beach walk with The Dog Club"></div></div></section>
<section class="sec tint"><div class="wrap"><h2>a day at the club</h2><div class="grid4">{steps}</div></div></section>
<section class="sec"><div class="wrap"><h2>what we do</h2><div class="grid3">{cards()}</div></div></section>
<section class="sec tint"><div class="wrap narrow"><h2>popular services</h2>{rows()}</div></section>
<section class="sec"><div class="wrap"><h2>visit us</h2><div class="grid3">{locs()}</div></div></section>"""


BODIES = {"a": body_a, "b": body_b, "c": body_c}


def page(key, t):
    nav = f'<nav class="nav"><a href="#"><img src="img/logo.svg" alt="The Dog Club"></a><div class="links"><a href="#">Services</a><a href="#">Pricing</a><a href="#">Locations</a><a href="#">Join the Club</a></div><a class="btn" href="{PAWSI}" target="_blank" rel="noopener noreferrer">Book now</a></nav>'
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow"><title>{t['name']} — The Dog Club design sample</title>
<link href="https://fonts.googleapis.com/css2?{t['fonts']}&display=swap" rel="stylesheet">
<style>{BASE}{t['css']}</style></head><body>
<div class="bar">Design sample {t['name']} · <a href="index.html">Back to all options</a></div>
{nav}{BODIES[key]()}
{MOTION}
</body></html>
"""
    (ROOT / f"{key}.html").write_text(html)


def chooser():
    desc = {
        "a": ("Paper", "Putih bersih, hitam, huruf sederhana, garis tipis. Terinspirasi Blank Street.", "pool-dogs.jpg"),
        "b": ("Olive", "Hijau olive dan warna batu, judul serif dengan huruf miring, foto besar. Terinspirasi dogppl.", "golden-pool.jpg"),
        "c": ("Soft", "Huruf kecil, nuansa sage yang lembut, langkah bernomor. Terinspirasi lilluvdog.", "beach.jpg"),
        "d": ("Sanctuary", "Judul serif editorial, kartu rapi, dan rutinitas harian. Gabungan dari ketiga referensi.", "pack.jpg"),
    }
    items = "".join(f"""
      <a href="{k}.html" class="o"><img src="img/{i}" alt=""><div><p class="k">Opsi {k.upper()}</p><h2>{n}</h2><p>{d}</p><span>Lihat sample &rarr;</span></div></a>""" for k, (n, d, i) in desc.items())
    html = f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow"><title>Pilihan Desain — The Dog Club</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>{BASE}
body{{background:#FFFDFC;color:#0F120E;font-family:'Instrument Sans',sans-serif;line-height:1.5}}
main{{max-width:1100px;margin:0 auto;padding:48px 24px}}header img{{height:72px;margin-bottom:24px}}h1{{font-size:clamp(30px,5vw,44px);font-weight:500;letter-spacing:-.02em;line-height:1.1;margin-bottom:12px}}
header p{{color:#73736E;max-width:60ch}}.opts{{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin:36px 0}}
.o{{border:1px solid #E2E2E2;border-radius:6px;overflow:hidden;display:flex;flex-direction:column}}.o:hover{{border-color:#0F120E}}.o img{{width:100%;aspect-ratio:4/3;object-fit:cover}}.o div{{padding:18px}}
.o .k{{font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#73736E}}.o h2{{font-size:24px;font-weight:500;margin:2px 0 6px}}.o p{{font-size:14px;color:#73736E}}.o span{{display:block;margin-top:12px;font-weight:500;font-size:14px}}
.note{{background:#F5F4F1;border-radius:6px;padding:22px}}.note h3{{font-weight:600;margin-bottom:8px}}.note li{{margin:4px 0 4px 18px;font-size:14px}}
@media(max-width:820px){{.opts{{grid-template-columns:1fr}}}}
</style></head><body><main>
<header><img src="img/logo.svg" alt="The Dog Club"><h1>Pilih arah desain website</h1><p>Keempatnya bergaya clean dan minimalis, sesuai referensi. Ini contoh gaya, bukan website final. Isinya sama supaya mudah dibandingkan. Silakan dibuka di HP juga.</p></header>
<div class="opts">{items}</div>
<div class="note"><h3>Yang kami butuhkan dari tim The Dog Club</h3><ul>
<li>Pilih 1 opsi. Boleh juga gabungan, misalnya "warna B dengan layout A".</li>
<li>Foto di sini diambil dari website yang sekarang. Foto yang lebih baru dan beresolusi tinggi akan membuat hasilnya jauh lebih bagus.</li>
<li>Setelah dipilih, kami kembangkan menjadi 2 halaman contoh (Homepage + Dog Daycare) untuk disetujui, baru diterapkan ke semua halaman.</li>
</ul></div></main></body></html>
"""
    (ROOT / "index.html").write_text(html)


if __name__ == "__main__":
    for key, theme in THEMES.items():
        page(key, theme)
    chooser()
    print("Built design samples")
