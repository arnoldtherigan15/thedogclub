"""Generate the design direction samples (a, b, c) and the chooser page.

Run:  python3 mockup/design/build_design.py
Each direction is one short sample page with the same real content, so the client
compares style only. Photos and prices come from the live thedogclub.id site.
"""
from pathlib import Path

ROOT = Path(__file__).parent
PAWSI = "https://book.pawsi.id/thedogclubbali"

SERVICES = [
    ("Dog Daycare", "Cage-free play in a 700 sqm park with two bone-shaped pools.", "From IDR 100.000", "golden-pool.jpg"),
    ("Luxury Dog Hotel", "Sleepovers at the Dog Villa, with staff on site day and night.", "From IDR 160.000 / night", "pack.jpg"),
    ("Dog Spa", "Baths, cuts and brushing with natural products only.", "From IDR 110.000", "spa.jpg"),
]
PRICES = [
    ("Half daycare", "4 hours", "100.000"),
    ("Full daycare", "All day", "120.000"),
    ("Deluxe boarding", "Weekday night", "160.000"),
    ("Essential bath & brush", "Small, short hair", "110.000"),
]
LOCATIONS = ["Umalas", "Berawa", "Ungasan"]

BASE = """
*{box-sizing:border-box;margin:0}html{scroll-behavior:smooth}img{display:block;max-width:100%}a{color:inherit;text-decoration:none}
.bar{background:#111;color:#fff;font:500 12px/1.4 system-ui,sans-serif;text-align:center;padding:8px 16px}.bar a{text-decoration:underline}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}
.nav{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:16px 20px;max-width:1200px;margin:0 auto}
.nav img{height:54px;width:auto}.links{display:flex;gap:28px;font-size:15px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.price-row{display:flex;justify-content:space-between;gap:16px;padding:16px 0}
@media(max-width:820px){.links{display:none}.grid3{grid-template-columns:1fr}}
"""

THEMES = {
"a": {
 "name": "A — Editorial",
 "fonts": "family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=DM+Sans:wght@400;500;700",
 "css": """
body{background:#FBF8F2;color:#161513;font-family:'DM Sans',sans-serif}
h1,h2,h3{font-family:'Fraunces',serif;font-weight:400;letter-spacing:-.02em}
h1 em,h2 em{font-style:italic}
.btn{display:inline-block;background:#161513;color:#FBF8F2;padding:14px 28px;border-radius:999px;font-weight:500}
.btn.light{background:#FBF8F2;color:#161513}
.hero{position:relative;height:min(86vh,760px);min-height:520px;color:#fff}
.hero img{width:100%;height:100%;object-fit:cover}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.72),rgba(0,0,0,.25) 45%,rgba(0,0,0,0) 75%)}
.hero .txt{position:absolute;z-index:1;left:0;right:0;bottom:48px}
.hero h1{font-size:clamp(46px,8.5vw,112px);line-height:.98;max-width:13ch;margin-bottom:24px}
.intro{padding:96px 0;text-align:center}.intro h2{font-size:clamp(30px,4.6vw,56px);line-height:1.1;max-width:20ch;margin:0 auto}
.card img{width:100%;aspect-ratio:4/5;object-fit:cover}.card h3{font-size:30px;margin-top:16px}.card p{margin-top:6px;color:#57534c}.card small{display:block;margin-top:10px;font-size:14px;font-weight:700}
.prices{padding:96px 0}.prices h2{font-size:clamp(30px,4vw,48px);margin-bottom:24px}.price-row{border-top:1px solid #d9d3c7;font-size:18px}.price-row span:last-child{font-family:'Fraunces',serif;font-size:22px}.price-row small{color:#6c675f;margin-left:10px}
.foot{background:#161513;color:#FBF8F2;padding:56px 0}.foot h2{font-size:clamp(30px,5vw,60px);margin-bottom:20px}
"""},
"b": {
 "name": "B — Playful",
 "fonts": "family=Archivo+Black&family=Outfit:wght@400;500;700",
 "css": """
body{background:#FFD23F;color:#111;font-family:'Outfit',sans-serif}
h1,h2,h3{font-family:'Archivo Black',sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:-.01em}
.btn{display:inline-block;background:#111;color:#FFD23F;padding:16px 30px;border-radius:14px;font-weight:700;box-shadow:5px 5px 0 #fff}
.btn.light{background:#fff;color:#111;box-shadow:5px 5px 0 #FFD23F}
.hero{padding:24px 0 72px}.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}
.hero h1{font-size:clamp(44px,7.4vw,96px);line-height:.95;margin-bottom:20px}.hero p{font-size:20px;max-width:34ch;margin-bottom:28px}
.hero img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:50% 50% 24px 24px;border:6px solid #111}
.intro{background:#111;color:#fff;padding:22px 0;text-align:center}.intro h2{font-size:clamp(18px,2.6vw,28px)}.intro em{font-style:normal;color:#FFD23F}
.svc{background:#fff;padding:80px 0}.card{border:4px solid #111;border-radius:22px;overflow:hidden;background:#fff;box-shadow:8px 8px 0 #111}
.card img{width:100%;aspect-ratio:1;object-fit:cover;border-bottom:4px solid #111}.card h3{font-size:24px;padding:18px 18px 0}.card p{padding:6px 18px 0}.card small{display:inline-block;margin:12px 18px 18px;background:#FFD23F;padding:6px 12px;border-radius:999px;font-size:14px;font-weight:700}
.prices{padding:80px 0}.prices h2{font-size:clamp(30px,4.6vw,56px);margin-bottom:24px}.price-row{background:#fff;border:4px solid #111;border-radius:14px;padding:16px 20px;margin-bottom:12px;font-weight:700}.price-row small{font-weight:400;margin-left:10px}
.foot{background:#111;color:#fff;padding:56px 0}.foot h2{font-size:clamp(30px,5vw,60px);color:#FFD23F;margin-bottom:20px}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr}}
"""},
"c": {
 "name": "C — Warm",
 "fonts": "family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Inter:wght@400;500;600",
 "css": """
body{background:#F9F6F0;color:#1A2E26;font-family:'Inter',sans-serif}
h1,h2,h3{font-family:'Playfair Display',serif;font-weight:700}
h1 em,h2 em{font-weight:500;color:#B98A2B}
.btn{display:inline-block;background:#1A2E26;color:#F9F6F0;padding:14px 28px;border-radius:999px;font-weight:600}
.btn.light{background:#E4B047;color:#1A2E26}
.hero{padding:32px 0 80px}.hero .wrap{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.hero h1{font-size:clamp(40px,5.6vw,72px);line-height:1.1;margin-bottom:20px}.hero p{font-size:18px;line-height:1.6;max-width:42ch;margin-bottom:28px;opacity:.8}
.hero img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:28px;box-shadow:0 24px 48px rgba(26,46,38,.2)}
.intro{background:#EFEAE1;padding:72px 0;text-align:center}.intro h2{font-size:clamp(28px,3.8vw,44px);max-width:24ch;margin:0 auto}
.svc{padding:80px 0}.card{background:#fff;border:1px solid #E4DDD0;border-radius:24px;overflow:hidden}
.card img{width:100%;aspect-ratio:4/3;object-fit:cover}.card h3{font-size:24px;padding:20px 20px 0}.card p{padding:6px 20px 0;opacity:.75}.card small{display:block;padding:12px 20px 20px;font-size:14px;font-weight:600;color:#B98A2B}
.prices{background:#1A2E26;color:#F9F6F0;padding:80px 0}.prices h2{font-size:clamp(30px,4vw,48px);margin-bottom:24px}.price-row{border-top:1px solid #2A453A}.price-row span:last-child{color:#E4B047;font-weight:600}.price-row small{opacity:.65;margin-left:10px}
.foot{background:#F9F6F0;padding:56px 0;text-align:center}.foot h2{font-size:clamp(30px,5vw,56px);margin-bottom:20px}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr}}
"""},
}

HEADLINE = {
    "a": "Your dog's <em>new favorite</em> place.",
    "b": "Your dog's new favorite place.",
    "c": "Your furry friend's new <em>favorite</em> place.",
}
INTRO = {
    "a": "A home for dogs <em>who love a good time</em>, and the humans who love them.",
    "b": "Daycare <em>•</em> Hotel <em>•</em> Spa <em>•</em> Training <em>•</em> Beach walks",
    "c": "Dogs should enjoy their holiday as much as <em>you do</em>.",
}
HERO_IMG = {"a": "pool-dogs.jpg", "b": "husky.jpg", "c": "park-pool.jpg"}
SUB = "Cage-free daycare, a luxury dog hotel, spa and training across Bali."


def page(key, t):
    logo = '<img src="img/logo.svg" alt="The Dog Club">'
    nav = f'<nav class="nav"><a href="#">{logo}</a><div class="links"><a href="#">Services</a><a href="#">Pricing</a><a href="#">Locations</a><a href="#">Join the Club</a></div><a class="btn" href="{PAWSI}" target="_blank" rel="noopener noreferrer">Book now</a></nav>'
    img = f'<img src="img/{HERO_IMG[key]}" alt="Dogs at The Dog Club">'
    book = f'<a class="btn{" light" if key == "a" else ""}" href="{PAWSI}" target="_blank" rel="noopener noreferrer">Book a visit</a>'
    if key == "a":
        hero = f'<section class="hero">{img}<div class="txt"><div class="wrap"><h1>{HEADLINE[key]}</h1>{book}</div></div></section>'
    else:
        hero = f'<section class="hero"><div class="wrap"><div><h1>{HEADLINE[key]}</h1><p>{SUB}</p>{book}</div>{img}</div></section>'
    intro = f'<section class="intro"><div class="wrap"><h2>{INTRO[key]}</h2></div></section>'
    cards = "".join(f'<article class="card"><img src="img/{i}" alt="{n}" loading="lazy"><h3>{n}</h3><p>{d}</p><small>{p}</small></article>' for n, d, p, i in SERVICES)
    svc = f'<section class="svc"><div class="wrap grid3">{cards}</div></section>'
    rows = "".join(f'<div class="price-row"><span>{a}<small>{b}</small></span><span>IDR {c}</span></div>' for a, b, c in PRICES)
    prices = f'<section class="prices"><div class="wrap"><h2>Popular services</h2>{rows}</div></section>'
    foot = f'<section class="foot"><div class="wrap"><h2>{" · ".join(LOCATIONS)}</h2><a class="btn{" light" if key != "c" else ""}" href="{PAWSI}" target="_blank" rel="noopener noreferrer">Book a visit</a></div></section>'
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow"><title>{t['name']} — The Dog Club design sample</title>
<link href="https://fonts.googleapis.com/css2?{t['fonts']}&display=swap" rel="stylesheet">
<style>{BASE}{t['css']}</style></head><body>
<div class="bar">Design sample {t['name']} · <a href="index.html">Back to all options</a></div>
{nav}{hero}{intro}{svc}{prices}{foot}
</body></html>
"""
    (ROOT / f"{key}.html").write_text(html)


def chooser():
    desc = {
        "a": ("Editorial", "Foto besar, judul besar, banyak ruang kosong. Paling dekat dengan referensi dogppl.co.", "pool-dogs.jpg"),
        "b": ("Playful", "Warna berani dan huruf tebal, mengikuti karakter logo The Dog Club.", "husky.jpg"),
        "c": ("Warm", "Cream dan hijau tua. Hangat, klasik, dan tenang.", "park-pool.jpg"),
    }
    cards = "".join(f"""
      <a href="{k}.html" class="o"><img src="img/{i}" alt=""><div><p class="k">Opsi {k.upper()}</p><h2>{n}</h2><p>{d}</p><span>Lihat sample &rarr;</span></div></a>""" for k, (n, d, i) in desc.items())
    html = f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow"><title>Pilihan Desain — The Dog Club</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{BASE}
body{{background:#fff;color:#161513;font-family:'Inter',sans-serif;line-height:1.5}}
main{{max-width:1100px;margin:0 auto;padding:48px 20px}}header img{{height:72px;margin-bottom:24px}}h1{{font-size:clamp(30px,5vw,44px);line-height:1.1;margin-bottom:12px}}
header p{{color:#57534c;max-width:60ch}}.opts{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin:36px 0}}
.o{{border:1px solid #e5e2db;border-radius:18px;overflow:hidden;display:flex;flex-direction:column}}.o:hover{{border-color:#161513}}.o img{{width:100%;aspect-ratio:4/3;object-fit:cover}}.o div{{padding:18px}}
.o .k{{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8a857b}}.o h2{{font-size:24px;margin:2px 0 6px}}.o p{{font-size:14px;color:#57534c}}.o span{{display:block;margin-top:12px;font-weight:600;font-size:14px}}
.note{{background:#f6f4ef;border-radius:18px;padding:22px}}.note h3{{margin-bottom:8px}}.note li{{margin:4px 0 4px 18px;font-size:14px}}
@media(max-width:820px){{.opts{{grid-template-columns:1fr}}}}
</style></head><body><main>
<header><img src="img/logo.svg" alt="The Dog Club"><h1>Pilih arah desain website</h1><p>Ini contoh gaya, bukan website final. Isinya sama di ketiga opsi supaya mudah dibandingkan. Silakan dibuka di HP juga.</p></header>
<div class="opts">{cards}</div>
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
