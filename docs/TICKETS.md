# Tiket Kerja — The Dog Club (Paket Essential)

Daftar tiket dari DP sampai garansi selesai. Kerjakan berurutan per fase. Satu tiket = satu branch `feature/TDC-xxx-nama` = satu Pull Request ke `develop`.

**Cara pakai**
- Centang `[x]` checklist saat selesai. Tiket dianggap **Done** hanya kalau semua poin "Done kalau" terpenuhi.
- Status: `TODO` → `DOING` → `REVIEW` (menunggu klien) → `DONE`.
- Kalau ada pekerjaan baru di luar daftar ini, buat tiket baru dengan label **CR (change request)** dan beri harga dulu ke klien sebelum dikerjakan.
- Panduan alur kerja dan environment: [WORKFLOW.md](WORKFLOW.md).

## Ringkasan

| ID | Tiket | Fase | Estimasi | Bergantung pada | Status |
| --- | --- | --- | --- | --- | --- |
| TDC-001 | DP & kickoff | 0 Kickoff | 0,5 hari | — | TODO |
| TDC-002 | Kumpulkan aset & data dari klien | 0 Kickoff | 1–2 hari | 001 | TODO |
| TDC-003 | Klarifikasi konten yang belum pasti | 0 Kickoff | 0,5 hari | 001 | TODO |
| TDC-004 | Setup repo, Next.js & Netlify | 0 Kickoff | 0,5 hari | 001 | TODO |
| TDC-005 | Brand alignment: warna, font, logo | 1 Desain | 1 hari | 002 | TODO |
| TDC-006 | Desain homepage + 1 halaman layanan | 1 Desain | 2 hari | 005 | TODO |
| TDC-007 | Revisi & approval desain | 1 Desain | 1–2 hari | 006 | TODO |
| TDC-008 | Komponen & layout dasar | 2 Build | 1 hari | 007, 004 | TODO |
| TDC-009 | Homepage | 2 Build | 1 hari | 008 | TODO |
| TDC-010 | Section & halaman lokasi | 2 Build | 0,5 hari | 008, 003 | TODO |
| TDC-011 | 8 halaman layanan + Services | 2 Build | 1,5 hari | 008 | TODO |
| TDC-012 | Pricing & Schedule (teks, bukan gambar) | 2 Build | 0,5 hari | 008, 002 | TODO |
| TDC-013 | Join the Club, About, FAQ, Franchise | 2 Build | 1 hari | 008 | TODO |
| TDC-014 | Blog + 4 artikel | 2 Build | 0,5 hari | 008 | TODO |
| TDC-015 | Halaman legal + 404 | 2 Build | 0,5 hari | 008, 003 | TODO |
| TDC-016 | Link booking & WhatsApp | 2 Build | 0,5 hari | 009–013 | TODO |
| TDC-017 | SEO on-page | 3 SEO | 1 hari | 009–015 | TODO |
| TDC-018 | Structured data & link preview | 3 SEO | 0,5 hari | 017 | TODO |
| TDC-019 | Optimasi gambar & performa | 3 SEO | 0,5 hari | 009–015 | TODO |
| TDC-020 | Redirect URL lama & sitemap | 3 SEO | 0,5 hari | 009–015 | TODO |
| TDC-021 | QA internal | 4 QA | 1 hari | 016–020 | TODO |
| TDC-022 | Review klien di staging | 4 QA | 2–3 hari | 021 | TODO |
| TDC-023 | Pelunasan | 4 QA | — | 022 | TODO |
| TDC-024 | Launch & pindah domain | 5 Launch | 0,5 hari | 023 | TODO |
| TDC-025 | Search Console & laporan launch | 5 Launch | 0,5 hari | 024 | TODO |
| TDC-026 | Garansi 30 hari & penutupan | 6 Garansi | 30 hari | 024 | TODO |

**Total kerja aktif:** ± 15 hari kerja, dalam timeline 3 minggu.

## Pemetaan temuan audit → tiket

Setiap temuan di [laporan audit](../mockup/seo-audit/index.html) harus tertutup oleh satu tiket. Cek tabel ini sebelum launch.

| # | Temuan audit | Diperbaiki di | Cek |
| --- | --- | --- | --- |
| 1 | Tombol Sign up ke Gingr, tidak ada link ke Pawsi | TDC-016 | [ ] |
| 2 | Lokasi (Ungasan, Seseh, dll.) tidak bisa diklik | TDC-010 | [ ] |
| 3 | Harga & jadwal berupa gambar | TDC-012 | [ ] |
| 4 | Homepage hampir tanpa teks | TDC-009 | [ ] |
| 5 | Tidak ada meta description | TDC-017 | [ ] |
| 6 | Judul halaman lemah | TDC-017 | [ ] |
| 7 | 2–4 H1 per halaman | TDC-008, TDC-017 | [ ] |
| 8 | Tidak ada structured data | TDC-018 | [ ] |
| 9 | Website berat & lambat | TDC-019 | [ ] |
| 10 | Gambar tanpa alt text & nama file | TDC-019 | [ ] |
| 11 | Tidak ada preview saat dibagikan | TDC-018 | [ ] |
| 12 | Konten usang: © 2024, typo, Terms Shopify, Hello world, FAQ ganda | TDC-013, TDC-015, TDC-020 | [ ] |
| 13 | Email pribadi penulis di blog | TDC-014 | [ ] |
| 14 | Slider kosong di homepage | TDC-009 | [ ] |

---

## Fase 0 — Kickoff

### TDC-001 · DP & kickoff
- [ ] Kirim link invoice (`/invoice/`) + quotation `#essential`
- [ ] DP IDR 3.750.000 masuk ke BCA, bukti transfer disimpan
- [ ] Kirim pesan kickoff: timeline 3 minggu dimulai hari ini, daftar yang perlu disiapkan, siapa PIC
- [ ] Catat tanggal mulai, hitung tanggal target launch

**Done kalau:** DP masuk, klien menunjuk 1 PIC, tanggal mulai dan target launch tercatat.

### TDC-002 · Kumpulkan aset & data dari klien
- [ ] Logo file asli (SVG/AI/PDF/PNG transparan)
- [ ] Brand guideline: kode warna, font, contoh desain yang mereka suka
- [ ] Foto asli: park, villa, pool, spa, tim, anjing (bukan screenshot)
- [ ] Price list terbaru (versi teks, bukan hanya gambar)
- [ ] Jadwal / jam buka terbaru
- [ ] 3 paket birthday party (nama, isi, harga)
- [ ] Akses DomaiNesia
- [ ] Akses Google Search Console (opsional)
- [ ] Akses admin WordPress lama (opsional, untuk ambil foto asli)

**Done kalau:** semua item wajib (5 pertama) diterima. Kalau lewat 2 hari kerja, kabari klien secara tertulis bahwa timeline bergeser.

### TDC-003 · Klarifikasi konten yang belum pasti
Tanyakan ke klien, catat jawabannya tertulis:
- [ ] Ungasan: alamat, jam buka, layanan apa saja, perlu halaman sendiri? (kalau ya = +1 halaman tambahan)
- [ ] Seseh: kapan buka, tampil sebagai "Coming soon"?
- [ ] The Dog Hotel Berawa: tetap link ke thedoghotel.id?
- [ ] Gingr: masih dipakai untuk daftar member, atau semua sudah lewat Pawsi?
- [ ] Refund & Shipping Policy: masih perlu? (toko online sudah tidak ada)
- [ ] Terms of Service: punya versi baru, atau kita rapikan dari template lama?
- [ ] Nama di invoice: The Dog Club Bali atau PT PMA The Dog Paradise?

**Done kalau:** semua pertanyaan terjawab tertulis. Perubahan jumlah halaman dicatat sebagai CR.

### TDC-004 · Setup repo, Next.js & Netlify
- [ ] Buat branch `develop` dari `main`
- [ ] Inisialisasi Next.js dengan `output: 'export'` (static) + Tailwind
- [ ] Hubungkan repo ke Netlify: production = `main`, branch deploy = `develop`, Deploy Preview untuk PR
- [ ] Staging diberi `noindex`
- [ ] Cek halaman pricing Netlify: paket gratis boleh untuk website bisnis
- [ ] Simpan link staging di WORKFLOW.md

**Done kalau:** push ke `develop` otomatis tampil di link staging, dan staging tidak terindeks Google.

## Fase 1 — Desain

### TDC-005 · Brand alignment
- [ ] Ganti warna mockup dengan warna brand klien
- [ ] Ganti font sesuai brand guideline (atau usulkan pasangan font)
- [ ] Pasang logo asli (header, footer, favicon)
- [ ] Pilih foto asli untuk hero dan setiap layanan

**Done kalau:** tampilan memakai identitas brand klien, tidak ada lagi logo/ikon pengganti.

### TDC-006 · Desain homepage + 1 halaman layanan
- [ ] Homepage versi desktop & mobile
- [ ] Halaman Dog Daycare versi desktop & mobile (contoh pola untuk semua layanan)
- [ ] Kirim link ke klien + minta **satu daftar feedback gabungan** dalam 3 hari kerja

**Done kalau:** link desain terkirim ke klien.

### TDC-007 · Revisi & approval desain
- [ ] Revisi putaran 1
- [ ] Revisi putaran 2 (maksimal; lebih dari ini = CR)
- [ ] Klien menulis "Design approved" (WA/email), screenshot disimpan
- [ ] Tagih termin 2: IDR 2.250.000

**Done kalau:** approval tertulis diterima dan termin 2 ditagih. Desain dikunci mulai titik ini.

## Fase 2 — Build

### TDC-008 · Komponen & layout dasar
- [ ] Header + menu (desktop & mobile), footer, tombol, kartu, tabel harga, FAQ accordion
- [ ] Data bisnis (alamat, WA, email, harga) di satu file data, bukan diketik ulang per halaman
- [ ] **Hanya 1 H1 per halaman** di template (temuan #7)
- [ ] Copyright tahun otomatis (temuan #12)

**Done kalau:** semua komponen dipakai ulang, tidak ada data bisnis yang ditulis ganda.

### TDC-009 · Homepage
- [ ] Hero, filosofi, layanan, inside the club, harga populer, cara daftar, lokasi & peta, testimoni, FAQ
- [ ] Teks lengkap, bukan hanya gambar (temuan #4)
- [ ] Tidak ada section kosong / slider kosong (temuan #14)

**Done kalau:** semua section berisi konten asli, sesuai desain yang di-approve.

### TDC-010 · Section & halaman lokasi
- [ ] Section "Our locations": Umalas, Ungasan, Berawa, Seseh (temuan #2)
- [ ] Setiap kartu bisa diklik ke tujuan yang benar
- [ ] Halaman Umalas: alamat, jam buka, peta, kontak
- [ ] Halaman Ungasan (hanya kalau disetujui di TDC-003)
- [ ] Menu "Home" dan logo mengarah ke halaman yang sama

**Done kalau:** semua lokasi bisa dibuka dalam 1 klik dari homepage.

### TDC-011 · 8 halaman layanan + Services
- [ ] Services (overview)
- [ ] Dog Daycare
- [ ] Luxury Dog Hotel
- [ ] Dog Spa, Massage & Grooming
- [ ] Dog Training
- [ ] Dog Walking
- [ ] Dog Birthday Party (3 paket dari TDC-002)
- [ ] Pet Taxi
- [ ] In-house Vet

**Done kalau:** setiap halaman punya deskripsi, harga (teks), jam/syarat, CTA, sesuai data terbaru klien.

### TDC-012 · Pricing & Schedule
- [ ] Semua harga sebagai teks/tabel, bukan gambar (temuan #3)
- [ ] Harga dicocokkan 1 per 1 dengan price list terbaru klien
- [ ] Jadwal / jam buka & rutinitas harian sebagai teks

**Done kalau:** tidak ada satu pun harga/jadwal yang berupa gambar, dan semua angka sudah dicek dengan klien.

### TDC-013 · Join the Club, About, FAQ, Franchise
- [ ] Join the Club: langkah daftar sesuai jawaban Gingr/Pawsi di TDC-003
- [ ] About Us
- [ ] FAQ: **satu versi gabungan**, tanpa duplikat (temuan #12)
- [ ] Own a Franchise + form (kirim ke email franchise@thedogclub.id, misalnya via Netlify Forms)
- [ ] Perbaiki typo "Kapubaten" dan typo lain (temuan #12)

**Done kalau:** form franchise benar-benar terkirim ke email (sudah dites).

### TDC-014 · Blog + 4 artikel
- [ ] Halaman daftar blog
- [ ] 4 artikel dipindahkan
- [ ] Penulis = "The Dog Club team", tanpa email pribadi (temuan #13)
- [ ] Post "Hello world!" **tidak** dibawa (temuan #12)

**Done kalau:** 4 artikel tampil rapi, tidak ada email pribadi di mana pun.

### TDC-015 · Halaman legal + 404
- [ ] Privacy Policy
- [ ] Terms of Service: hapus teks Shopify, email kontak = woof@thedogclub.id (temuan #12)
- [ ] Refund & Shipping Policy (hanya kalau masih perlu, lihat TDC-003)
- [ ] Halaman 404

**Done kalau:** tidak ada lagi kata "Shopify" atau email `nrshopify347@gmail.com`.

### TDC-016 · Link booking & WhatsApp
- [ ] Semua tombol "Book" / "Sign up" ke Pawsi (temuan #1)
- [ ] Layanan by-request (taxi, vet, training, birthday) ke WhatsApp dengan pesan otomatis
- [ ] Tombol "Join the Club" sesuai keputusan Gingr/Pawsi di TDC-003
- [ ] Cari ulang di kode: tidak ada lagi `gingrapp` kecuali memang disetujui

**Done kalau:** setiap tombol booking sudah diklik manual dan sampai ke tujuan yang benar.

## Fase 3 — SEO & performa

### TDC-017 · SEO on-page
- [ ] Meta description unik di setiap halaman (temuan #5)
- [ ] Title berisi kata kunci, misalnya "Dog Hotel Bali", "Dog Daycare Umalas" (temuan #6)
- [ ] Cek ulang: tepat 1 H1 per halaman (temuan #7)
- [ ] Heading H2/H3 berurutan
- [ ] Canonical URL & `lang` benar

**Done kalau:** Lighthouse SEO ≥ 90 di homepage dan 1 halaman layanan.

### TDC-018 · Structured data & link preview
- [ ] JSON-LD LocalBusiness: nama, alamat, jam buka, telepon (temuan #8)
- [ ] JSON-LD FAQPage di halaman FAQ (temuan #8)
- [ ] Open Graph + gambar share untuk setiap halaman (temuan #11)
- [ ] Tes: Google Rich Results Test tanpa error
- [ ] Tes: kirim link ke WhatsApp sendiri, preview muncul

**Done kalau:** kedua tes di atas lolos.

### TDC-019 · Optimasi gambar & performa
- [ ] Semua gambar dikompres (WebP/AVIF) dan diberi ukuran yang pas (temuan #9)
- [ ] Nama file deskriptif, misalnya `dog-daycare-umalas-pool.webp` (temuan #10)
- [ ] Alt text di setiap gambar (temuan #10)
- [ ] Font dimuat seperlunya saja (maksimal 2 keluarga font, hanya ketebalan yang dipakai)
- [ ] Tanpa plugin / script yang tidak dipakai

**Done kalau:** Lighthouse Performance mobile ≥ 90.

### TDC-020 · Redirect URL lama & sitemap
- [ ] File `_redirects` Netlify: semua URL lama → URL baru (lihat tabel di `mockup/README.md`)
- [ ] Termasuk 4 URL artikel blog `/2024/11/29/...`
- [ ] `/2023/11/01/hello-world/` → `/blog` (temuan #12)
- [ ] `sitemap.xml` dan `robots.txt`

**Done kalau:** setiap URL lama dibuka satu per satu dan sampai ke halaman yang benar (bukan 404).

## Fase 4 — QA & review

### TDC-021 · QA internal
- [ ] Semua halaman terbuka, tidak ada link mati
- [ ] Tampilan benar di iPhone, Android, laptop
- [ ] Harga, jam buka, alamat sama persis dengan data klien
- [ ] Form franchise & newsletter berfungsi
- [ ] Tabel "Pemetaan temuan audit" di atas: 14 dari 14 sudah dicentang
- [ ] Rekam skor PageSpeed/Lighthouse staging (untuk laporan)

**Done kalau:** semua poin dicentang.

### TDC-022 · Review klien di staging
- [ ] Kirim link staging + minta **satu daftar koreksi** dalam 3 hari kerja
- [ ] Perbaiki semua koreksi
- [ ] Klien konfirmasi tertulis "siap launch"

**Done kalau:** konfirmasi tertulis diterima. Koreksi di luar desain yang di-approve = CR.

### TDC-023 · Pelunasan
- [ ] Tagih pelunasan IDR 1.500.000
- [ ] Pembayaran masuk

**Done kalau:** lunas. **Jangan launch sebelum tiket ini Done.**

## Fase 5 — Launch

### TDC-024 · Launch & pindah domain
Kerjakan di hari kerja, pagi hari, jangan Jumat sore.
- [ ] Merge `develop` → `main`, cek URL production Netlify
- [ ] Tambah domain `thedogclub.id` & `www.thedogclub.id` di Netlify
- [ ] DomaiNesia: ganti **hanya** A record & CNAME `www`
- [ ] ⚠️ **Jangan sentuh** MX (email Google) dan TXT google-site-verification
- [ ] SSL aktif di kedua alamat
- [ ] Kirim email test ke woof@thedogclub.id, pastikan masuk
- [ ] Kabari klien: website live

**Done kalau:** website baru terbuka di thedogclub.id dengan HTTPS, dan email klien tetap berfungsi.

### TDC-025 · Search Console & laporan launch
- [ ] Submit `sitemap.xml` di Search Console
- [ ] Cek tidak ada error crawl
- [ ] Kirim laporan launch ke klien: skor PageSpeed/Lighthouse sebelum vs sesudah, 14 temuan audit sudah diperbaiki
- [ ] Ingatkan klien: jangan matikan hosting WordPress lama sebelum 1 minggu stabil

**Done kalau:** laporan terkirim ke klien.

## Fase 6 — Garansi

### TDC-026 · Garansi 30 hari & penutupan
- [ ] Hari +7: cek website & Search Console, kabari klien hosting lama boleh dihentikan
- [ ] Perbaiki bug dari pekerjaan sendiri (gratis)
- [ ] Permintaan baru di luar bug → tawarkan update konten (IDR 150.000/permintaan), maintenance (IDR 1.000.000/bulan), atau upgrade ke Recommended
- [ ] Hari +30: laporan singkat (halaman terindeks, impressions & klik pertama)
- [ ] Serahkan semua akses (Netlify, GitHub, Search Console) atas nama klien
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
