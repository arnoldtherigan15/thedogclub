# Tiket Kerja — The Dog Club (Paket Essential)

Daftar tiket dari DP sampai garansi selesai, berdasarkan desain Canva dari klien. Rencana lengkap (halaman, teknologi, aturan commit): [PLAN.md](PLAN.md).

**Cara pakai**
- Satu tiket = satu branch `feature/TDC-0xx-nama` = satu Pull Request ke `develop`.
- Centang `[x]` saat selesai. Tiket **Done** hanya kalau "Done kalau" terpenuhi.
- Setiap halaman juga harus lolos Definition of Done di PLAN.md bagian 4.
- Pekerjaan baru di luar daftar ini = tiket **CR (change request)**, kasih harga dulu.

## Ringkasan

| ID | Tiket | Fase | Estimasi | Bergantung pada | Status |
| --- | --- | --- | --- | --- | --- |
| TDC-001 | DP & kickoff | 0 Kickoff | 0,5 hari | — | DOING |
| TDC-002 | Terima desain & aset dari klien | 0 Kickoff | — | 001 | DOING |
| TDC-003 | Klarifikasi konten | 0 Kickoff | 0,5 hari | 002 | TODO |
| TDC-004 | Run-through desain per halaman | 1 Desain | 0,5 hari | 002 | TODO |
| TDC-005 | Versi mobile & komponen global | 1 Desain | 0,5 hari | 004 | TODO |
| TDC-006 | Approval desain | 1 Desain | 1–2 hari | 011 | TODO |
| TDC-007 | Setup repo, Next.js & Netlify | 2 Build | 0,5 hari | 004 | TODO |
| TDC-008 | Design tokens & layout | 2 Build | 0,5 hari | 007 | TODO |
| TDC-009 | Pipeline gambar & video | 2 Build | 0,5 hari | 007 | TODO |
| TDC-010 | Data bisnis di satu tempat | 2 Build | 0,5 jam | 007, 003 | TODO |
| TDC-011 | Home | 2 Build | 0,5 hari | 008, 009 | TODO |
| TDC-012 | Services + harga | 2 Build | 0,5 hari | 008, 010 | TODO |
| TDC-013 | Facility | 2 Build | 0,5 hari | 008 | TODO |
| TDC-014 | Locations | 2 Build | 0,5 hari | 008, 010 | TODO |
| TDC-015 | House Rules | 2 Build | 0,25 hari | 008 | TODO |
| TDC-016 | Book a Visit | 2 Build | 0,25 hari | 008, 010 | TODO |
| TDC-017 | Partnership | 2 Build | 0,25 hari | 008 | TODO |
| TDC-018 | Loyalty Program | 2 Build | 0,25 hari | 008, 003 | TODO |
| TDC-019 | About Us | 2 Build | 0,25 hari | 008, 009 | TODO |
| TDC-020 | FAQ | 2 Build | 0,5 hari | 008 | TODO |
| TDC-021 | Privacy Policy & 404 | 2 Build | 0,25 hari | 008 | TODO |
| TDC-022 | Semua halaman selesai + termin 2 | 2 Build | 0,25 hari | 011–021 | TODO |
| TDC-023 | SEO on-page | 3 SEO | 0,5 hari | 022 | TODO |
| TDC-024 | Structured data & link preview | 3 SEO | 0,5 hari | 023 | TODO |
| TDC-025 | Performa & gambar | 3 SEO | 0,5 hari | 022 | TODO |
| TDC-026 | Redirect URL lama & sitemap | 3 SEO | 0,5 hari | 022 | TODO |
| TDC-027 | QA internal | 4 QA | 0,5 hari | 023–026 | TODO |
| TDC-028 | Review klien di staging | 4 QA | 3 hari | 027 | TODO |
| TDC-029 | Pelunasan | 4 QA | — | 028 | TODO |
| TDC-030 | Launch & pindah domain | 5 Launch | 0,5 hari | 029 | TODO |
| TDC-031 | Search Console & laporan launch | 5 Launch | 0,5 hari | 030 | TODO |
| TDC-032 | Garansi 30 hari & penutupan | 6 Garansi | 30 hari | 030 | TODO |

**Total kerja aktif:** ± 9 hari kerja. Mulai 2 Nov 2026, target live 23 Nov 2026. Jadwal per tanggal ada di tab Jadwal pada `tracker.html`.

## Pemetaan temuan audit → tiket

Setiap temuan di [laporan audit](../client/seo-audit/index.html) harus tertutup oleh satu tiket. Cek tabel ini sebelum kirim preview ke klien.

| # | Temuan audit | Diperbaiki di | Cek |
| --- | --- | --- | --- |
| 1 | Tombol Sign up ke Gingr, tidak ada link ke Pawsi | TDC-016, TDC-022 | [ ] |
| 2 | Lokasi (Ungasan, Seseh, dll.) tidak bisa diklik | TDC-014 | [ ] |
| 3 | Harga & jadwal berupa gambar | TDC-012 | [ ] |
| 4 | Homepage hampir tanpa teks | TDC-011, TDC-023 | [ ] |
| 5 | Tidak ada meta description | TDC-023 | [ ] |
| 6 | Judul halaman lemah | TDC-023 | [ ] |
| 7 | 2–4 H1 per halaman | TDC-008, TDC-023 | [ ] |
| 8 | Tidak ada structured data | TDC-024 | [ ] |
| 9 | Website berat & lambat | TDC-025 | [ ] |
| 10 | Gambar tanpa alt text & nama file | TDC-025 | [ ] |
| 11 | Tidak ada preview saat dibagikan | TDC-024 | [ ] |
| 12 | Konten usang: © 2024, typo, Terms Shopify, Hello world, FAQ ganda | TDC-020, TDC-021, TDC-026 | [ ] |
| 13 | Email pribadi penulis di blog | TDC-026 | [ ] |
| 14 | Slider kosong di homepage | TDC-011 | [ ] |

---

## Fase 0 — Kickoff

### TDC-001 · DP & kickoff
- [x] Kirim link invoice (`/invoice/`) + quotation `#essential`
- [x] DP IDR 3.750.000 masuk ke BCA, bukti transfer disimpan
- [ ] Kirim link progress (`/progress/`) ke klien
- [x] Catat tanggal mulai dan target launch (mulai 2 Nov, target 23 Nov 2026)

**Done kalau:** DP masuk, klien sudah pegang link progress.

### TDC-002 · Terima desain & aset dari klien
- [x] Desain Canva 12 layar (`design/WEBSITE MOCKUP.pdf`)
- [x] Logo hitam & putih, font & kode warna
- [x] Foto per halaman (`design/assets/Photo/`)
- [x] Price list, FAQ, House Rules, Loyalty, Contact Admin
- [x] Video drone & TDC Story
- [ ] Alamat + link Google Maps 4 lokasi
- [ ] Logo dalam format SVG (yang ada PNG; kalau tidak ada, buat SVG dari PNG)

**Done kalau:** semua bahan untuk 11 halaman sudah ada, tidak ada placeholder "Address".

### TDC-003 · Klarifikasi konten
Pertanyaan lengkap ada di PLAN.md bagian 2. Kirim lewat template "Pertanyaan desain", catat jawaban tertulis.
- [ ] Jam buka Senin
- [ ] Nomor WhatsApp Berawa & Ungasan yang benar
- [ ] Nominal referral (100K, atau 50K/200K)
- [ ] Tujuan tombol Join the Club & Book a Visit (WhatsApp, Pawsi, Gingr)
- [ ] Retail, Training, Homecare: tambah kartu atau hapus dari daftar
- [ ] Kontak Partnership
- [ ] Harga tampil di website atau tidak
- [ ] Blog lama boleh dihapus
- [ ] Video TDC Story: YouTube/Vimeo atau foto saja
- [ ] Perbaikan teks kecil disetujui (Bone-Shaped Pools, dll.)

**Done kalau:** semua terjawab tertulis dan `src/content/` bisa diisi tanpa tebakan.

## Fase 1 — Desain

### TDC-004 · Run-through desain per halaman
Buka layar Canva-nya satu per satu, sepakati section, teks, dan versi mobile. Catat keputusannya di tiket halaman tersebut.
- [ ] Home (layar 1–2)
- [ ] Services (3)
- [ ] Facility (4–5)
- [ ] Locations (6–7)
- [ ] House Rules (8)
- [ ] Book a Visit (9)
- [ ] Partnership (10)
- [ ] Loyalty Program (11)
- [ ] About Us (12)
- [ ] FAQ, Privacy, 404 (tanpa layar Canva)

**Done kalau:** setiap halaman punya daftar section yang disepakati.

### TDC-005 · Versi mobile & komponen global
- [ ] Header desktop: versi transparan & versi putih
- [ ] Header mobile + menu layar penuh
- [ ] Footer (belum ada di Canva)
- [ ] Aturan umum mobile: kolom jadi 1, foto bertumpuk jadi berurutan, ukuran judul

**Done kalau:** semua keputusan tercatat dan terlihat di preview Home.

### TDC-006 · Approval desain
Yang direview: Home + header + footer, desktop & mobile, di link preview.
- [ ] Kirim link preview + template "Desain siap review"
- [ ] Revisi putaran 1
- [ ] Revisi putaran 2 (maksimal; lebih dari ini = CR)
- [ ] Klien menulis "Design approved", screenshot disimpan

**Done kalau:** approval tertulis diterima. Gaya halaman lain mengikuti Home dan Canva.

## Fase 2 — Build

### TDC-007 · Setup repo, Next.js & Netlify
- [ ] Repo baru private `thedogclub-website`, branch `main` & `develop`
- [ ] `npx create-next-app@latest` dengan TypeScript, Tailwind, App Router, folder `src/`
- [ ] `next.config`: `output: 'export'`, `trailingSlash: true`, `images.unoptimized: true`
- [ ] README: cara jalan lokal, aturan branch & commit (salin dari PLAN.md bagian 5)
- [ ] Template Pull Request `.github/pull_request_template.md`
- [ ] Netlify: production = `main`, branch deploy = `develop`, Deploy Preview untuk PR
- [ ] Staging & preview diberi `noindex`

**Done kalau:** PR pertama menghasilkan Deploy Preview, push ke `develop` tampil di link staging.

### TDC-008 · Design tokens & layout
- [ ] Open Sans 400/500/600 lewat `next/font`
- [ ] Warna brand & huruf renggang sebagai token Tailwind
- [ ] `Header` desktop (transparan & putih) dan mobile
- [ ] `Footer` dengan © tahun otomatis
- [ ] Layout dasar: `Container`, jarak antar section konsisten
- [ ] Hanya 1 H1 per halaman di template

**Done kalau:** halaman kosong dengan header & footer tampil benar di desktop dan HP.

### TDC-009 · Pipeline gambar & video
- [ ] `scripts/optimize-images.mjs` (sharp): WebP, lebar 2400/1200/800, nama file deskriptif
- [ ] Ekspor foto yang dipakai dari `design/assets/Photo/` ke `public/images/`
- [ ] Drone: ffmpeg → MP4 720p tanpa suara, < 5 MB + poster
- [ ] Video About: ikuti jawaban TDC-003
- [ ] Logo SVG/PNG putih & hitam + favicon

**Done kalau:** tidak ada file mentah > 1 MB di repo.

### TDC-010 · Data bisnis di satu tempat
- [ ] `src/content/site.ts`: 4 cabang (nama, alamat, Maps, WhatsApp), jam buka, Instagram
- [ ] Helper link WhatsApp dengan pesan otomatis per cabang

**Done kalau:** tidak ada nomor telepon atau alamat yang diketik langsung di komponen.

### TDC-011 · Home
- [ ] Hero foto penuh + "Happiness Center for Doggies" (H1) + tombol Join the Club
- [ ] Daftar layanan di bawah hero
- [ ] Galeri 4 foto bertumpuk
- [ ] Usulan paragraf pembuka singkat (kalau disetujui)
- [ ] Versi mobile

**Done kalau:** lolos Definition of Done, tidak ada section kosong atau slider kosong.

### TDC-012 · Services + harga
- [ ] Judul + 6 kartu layanan (foto, nama, 1 kalimat)
- [ ] Kartu tambahan Retail/Training/Homecare kalau disetujui di TDC-003
- [ ] Daftar harga sebagai teks dari pricelist (`#prices`), dicek 1 per 1
- [ ] Catatan "11% tax and service not included"

**Done kalau:** tidak ada harga berupa gambar, semua angka sama dengan pricelist.

### TDC-013 · Facility
- [ ] Hero foto + "Our Facility" + teks pembuka
- [ ] 3 kolom: Mansion, 700 sqm park, Bone-Shaped Pools, masing-masing 2 foto bertumpuk

**Done kalau:** lolos Definition of Done.

### TDC-014 · Locations
- [ ] Hero drone (video atau foto) dengan 4 label lokasi
- [ ] 4 kartu: foto, nama, alamat, tombol WhatsApp, link Google Maps
- [ ] The Dog Hotel Berawa: tandai "Boarding only"

**Done kalau:** setiap lokasi bisa dihubungi dan dibuka di Maps dalam 1 klik.

### TDC-015 · House Rules
- [ ] Latar foto + kartu kertas
- [ ] 5 aturan sebagai teks dari `House Rules.pdf`

**Done kalau:** semua teks bisa diseleksi (bukan gambar).

### TDC-016 · Book a Visit
- [ ] Foto + "Schedule your visit" + teks
- [ ] Tombol Book a Visit → pilihan 4 cabang (sesuai Contact Admin.pdf)
- [ ] Tujuan tombol sesuai jawaban TDC-003 (WhatsApp/Pawsi/Gingr)
- [ ] Link ke FAQ

**Done kalau:** keempat tombol cabang sudah diklik dan sampai ke admin yang benar.

### TDC-017 · Partnership
- [ ] Judul + 4 foto + teks
- [ ] Tombol kontak kolaborasi (sesuai TDC-003)

**Done kalau:** lolos Definition of Done.

### TDC-018 · Loyalty Program
- [ ] Latar foto + kartu Top Up Balance (teks)
- [ ] Kartu Referral (teks, nominal sesuai TDC-003)
- [ ] Syarat & ketentuan

**Done kalau:** tidak ada flyer berupa gambar, nominal sudah dikonfirmasi klien.

### TDC-019 · About Us
- [ ] Hero + "About Us"
- [ ] 2 paragraf cerita
- [ ] Video TDC Story (kalau jadi), dimuat setelah diklik

**Done kalau:** lolos Definition of Done, halaman tetap ringan.

### TDC-020 · FAQ
- [ ] 9 kategori dari FAQ.pdf: Registration/Booking, General, Facilities, Health & Safety, Boarding, Daycare, Grooming, Dog Walking, Training
- [ ] Accordion yang bisa dipakai keyboard
- [ ] Nomor kontak di jawaban terakhir diambil dari `site.ts`

**Done kalau:** satu versi FAQ saja, tanpa pertanyaan ganda.

### TDC-021 · Privacy Policy & 404
- [ ] Privacy Policy dari website lama, email kontak = woof@thedogclub.id
- [ ] Halaman 404 + tombol ke Home
- [ ] Tidak ada Terms Shopify atau email `nrshopify347@gmail.com`

**Done kalau:** tidak ada teks Shopify di mana pun.

### TDC-022 · Semua halaman selesai + termin 2
- [ ] Semua link menu, footer, dan tombol diklik satu per satu
- [ ] Cari di kode: tidak ada `gingrapp` kecuali memang disetujui
- [ ] Update `client/progress/data.js`: `pagesBuilt: 11`
- [ ] Kirim invoice termin 2 IDR 2.250.000 + template "Semua halaman selesai"

**Done kalau:** termin 2 ditagih. SEO & testing mulai setelah termin 2 masuk.

## Fase 3 — SEO & performa

### TDC-023 · SEO on-page
- [ ] Title & meta description unik per halaman, berisi kata kunci ("Dog Daycare Bali", "Dog Hotel Umalas")
- [ ] Cek ulang: tepat 1 H1 per halaman
- [ ] Heading H2/H3 berurutan
- [ ] Canonical URL & `lang="en"`

**Done kalau:** Lighthouse SEO ≥ 90 di Home dan Services.

### TDC-024 · Structured data & link preview
- [ ] JSON-LD LocalBusiness untuk 4 cabang
- [ ] JSON-LD FAQPage di halaman FAQ
- [ ] Open Graph + gambar share per halaman
- [ ] Tes Google Rich Results tanpa error
- [ ] Tes kirim link ke WhatsApp sendiri, preview muncul

**Done kalau:** kedua tes lolos.

### TDC-025 · Performa & gambar
- [ ] Semua gambar WebP dengan ukuran pas dan alt text
- [ ] Gambar di bawah layar dimuat belakangan (lazy)
- [ ] Video tidak menghambat tampilan pertama

**Done kalau:** Lighthouse Performance mobile ≥ 90.

### TDC-026 · Redirect URL lama & sitemap
- [ ] `public/_redirects` sesuai tabel PLAN.md bagian 7
- [ ] Ambil slug lengkap 4 artikel blog dari website live
- [ ] `sitemap.xml` dan `robots.txt`

**Done kalau:** setiap URL lama dibuka satu per satu dan tidak ada yang 404.

## Fase 4 — QA & review

### TDC-027 · QA internal
- [ ] 11 halaman terbuka, tidak ada link mati
- [ ] Tampilan benar di iPhone, Android, laptop
- [ ] Harga, jam buka, alamat, nomor WhatsApp sama dengan jawaban klien
- [ ] Tabel "Pemetaan temuan audit": 14 dari 14 tercentang
- [ ] Rekam skor PageSpeed untuk laporan

**Done kalau:** semua poin dicentang.

### TDC-028 · Review klien di staging
- [ ] Kirim link staging + template "Preview siap"
- [ ] Perbaiki semua koreksi
- [ ] Klien konfirmasi tertulis "siap launch"

**Done kalau:** konfirmasi tertulis diterima. Koreksi di luar desain = CR.

### TDC-029 · Pelunasan
- [ ] Tagih pelunasan IDR 1.500.000
- [ ] Pembayaran masuk

**Done kalau:** lunas. **Jangan launch sebelum tiket ini Done.**

## Fase 5 — Launch

### TDC-030 · Launch & pindah domain
Kerjakan di hari kerja, pagi hari, jangan Jumat sore.
- [ ] Merge `develop` → `main`, tag `v1.0.0`, cek URL production Netlify
- [ ] Tambah domain `thedogclub.id` & `www.thedogclub.id` di Netlify
- [ ] DomaiNesia: ganti **hanya** A record & CNAME `www`
- [ ] ⚠️ **Jangan sentuh** MX (email Google) dan TXT google-site-verification
- [ ] SSL aktif di kedua alamat
- [ ] Kirim email test ke woof@thedogclub.id, pastikan masuk
- [ ] Kabari klien: website live

**Done kalau:** website baru terbuka di thedogclub.id dengan HTTPS, dan email klien tetap berfungsi.

### TDC-031 · Search Console & laporan launch
- [ ] Submit `sitemap.xml` di Search Console
- [ ] Cek tidak ada error crawl
- [ ] Laporan ke klien: skor sebelum vs sesudah, 14 temuan audit sudah diperbaiki
- [ ] Ingatkan klien: jangan matikan hosting WordPress lama sebelum 1 minggu stabil

**Done kalau:** laporan terkirim ke klien.

## Fase 6 — Garansi

### TDC-032 · Garansi 30 hari & penutupan
- [ ] Hari +7: cek website & Search Console, kabari klien hosting lama boleh dihentikan
- [ ] Perbaiki bug dari pekerjaan sendiri (gratis)
- [ ] Permintaan baru → tawarkan update konten (IDR 150.000/permintaan), maintenance (IDR 1.000.000/bulan), atau upgrade ke Recommended
- [ ] Hari +30: laporan singkat (halaman terindeks, impressions & klik pertama)
- [ ] Transfer repo `thedogclub-website` ke GitHub klien, serahkan akses Netlify & Search Console
- [ ] Pesan penutup + tawaran maintenance

**Done kalau:** semua akses sudah diserahkan dan laporan +30 hari terkirim.

---

## Template tiket baru (change request)

```
### TDC-0xx · [CR] Judul singkat
Diminta oleh: ... (tanggal, via WA/email)
Deskripsi: ...
Harga: IDR ... — disetujui klien tanggal ...
- [ ] ...
Done kalau: ...
```
