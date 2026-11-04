# Rencana Pengembangan — Website The Dog Club

Dasar: desain Canva dari klien (`design/WEBSITE MOCKUP.pdf`, 12 layar) dan aset di `design/assets/`. Mockup lama 27 halaman sudah tidak dipakai.

> Folder `design/` (3,1 GB) hanya disimpan di laptop dan sudah masuk `.gitignore`. Jangan pernah di-commit.

## 1. Daftar halaman

12 layar Canva = 9 menu. Ditambah FAQ (konten ada di aset), Privacy Policy, dan 404.

| # | Halaman | URL | Layar Canva | Isi |
| --- | --- | --- | --- | --- |
| 1 | Home | `/` | 1, 2 | Hero foto penuh "Happiness Center for Doggies" + tombol Join the Club + daftar layanan. Galeri 4 foto bertumpuk. |
| 2 | Services | section di Home `/#services` | 3 | **Bukan halaman sendiri** (keputusan 4 Nov): section di bawah galeri Home, menu Service scroll ke sini. Judul + 6 kartu (Boarding, Daycare, Walking, Pet Taxi, Grooming, Dog's Birthday). **Usulan:** tambah daftar harga dari pricelist sebagai teks. |
| 3 | Facility | section di Home `/#facility` | 4, 5 | **Section di Home** (4 Nov), di bawah Services. Foto penuh + judul & teks kanan, lalu Mansion, 700 sqm park, Bone-Shaped Pools dengan foto bertumpuk. |
| 4 | Locations | section di Home `/#locations` | 6, 7 | **Section di Home** (4 Nov), di bawah Facility. Video drone (12 detik, ±2 MB) + logo + 4 label cabang, lalu 4 kartu: foto, nama, Address (Google Maps), Contact Us (WhatsApp admin). |
| 5 | House Rules | section di Home `/#house-rules` | 8 | **Section di Home** (4 Nov). Kartu kertas di atas foto blur; 5 aturan + Booking & Refunds (draf dari FAQ, menunggu persetujuan klien) sebagai baris buka-tutup. |
| 6 | Book a Visit | section di Home `/#book-a-visit` | 9 + `Contact Admin.pdf` | **Section di Home** (4 Nov). Foto + Schedule your visit + tombol yang membuka pop-up 4 admin cabang (WhatsApp), meniru Contact Admin.pdf. |
| 7 | Partnership | `/partnership/` | 10 | Judul + 4 foto + teks + tombol kontak. |
| 8 | Loyalty Program | `/loyalty-program/` | 11 | Latar foto + kartu Top Up Balance + section **Friends of The Dog Club** (referral, tombol ke form). Teks, bukan gambar flyer. |
| 9 | About Us | `/about-us/` | 12 | Hero + 2 paragraf cerita Kevin. Video TDC Story (opsional). |
| 10 | FAQ | `/faq/` | — (aset `7. FAQ`) | 9 kategori dari FAQ.pdf, model accordion. Gaya mengikuti House Rules. Link di footer & Book a Visit. |
| 11 | Privacy Policy | `/privacy-policy/` | — | Dari website lama, dirapikan. Link di footer. |
| — | 404 | — | — | Halaman tidak ditemukan + tombol ke Home. |

**Jumlah:** 11 halaman (404 tidak dihitung). Quotation menyebut 27 halaman; desain klien lebih ringkas, harga tetap. Halaman tambahan di luar daftar ini tetap IDR 750.000 per halaman.

### Komponen global (tidak ada di Canva, harus disetujui klien bersama Home)
- **Header desktop:** 4 menu kiri, logo tengah, 4 menu kanan. Versi transparan (teks & logo putih) di atas foto hero: Home, Facility, Locations, House Rules, Loyalty, About. Versi putih (teks & logo hitam) di halaman lain.
- **Header mobile:** logo + tombol menu → menu layar penuh.
- **Footer:** belum ada di Canva. Usulan: logo, 4 cabang dengan tombol WhatsApp, jam buka, Instagram @thedogclub.bali, link FAQ & Privacy, © tahun otomatis.
- **Versi mobile semua halaman:** Canva hanya desktop. Kita yang menentukan; disetujui lewat preview Home.

### Brand
- Font: **Open Sans** 400 & 500 (dari klien). Judul kartu di Canva tampak tebal → pakai 600.
- Huruf renggang: menu & teks kecil ± `0.12em`, paragraf ± `0.06em`.
- Warna klien: `#f4f8f3`, `#ebe7e3`, `#37402f`, `#000000`, `#ffffff`. Tombol di Canva `#6b7065`. Logo hijau di layar 9–10 `#596a3a`; tanyakan apakah memang disengaja, kalau tidak pakai logo hitam.
- Latar halaman: putih, sesuai Canva.

### Perbaikan teks yang perlu diusulkan ke klien (jangan diubah tanpa izin)
- "Boned Shaped Pools" → "Bone-Shaped Pools"
- "a enjoyable and safety experience" → "an enjoyable and safe experience"
- "your dogs stay" → "your dog's stay"
- Paragraf Partnership tanpa titik di akhir

### Catatan SEO dari desain
- Home hampir tanpa teks (temuan audit #4 terulang). Usulkan 1 paragraf pembuka singkat di bawah galeri saat review Home.
- Tidak ada halaman per layanan, jadi pencarian seperti "dog daycare Umalas" bergantung pada halaman Services + FAQ + title/meta yang kuat.

## 2. Jawaban klien & pertanyaan yang masih terbuka

### Sudah dijawab (4 Nov)
| Topik | Jawaban |
| --- | --- |
| Tombol Book a Visit | Membuka pilihan 4 admin cabang (seperti `Contact Admin.pdf`), masing-masing ke WhatsApp. Bukan form kunjungan |
| WhatsApp admin | Umalas `628113940055`, Berawa `6281237816931`, Seseh `628133918425`, Ungasan `628133834459` |
| Pendaftaran / Join the Club | Customer portal Pawsi: https://book.pawsi.id/thedogclubbali |
| Ungasan | Jl. Toya Ning I No.313, Ungasan, Kec. Kuta Sel., Kabupaten Badung, Bali 80361. Jam 9 AM–6 PM. Layanan: Boarding, Daycare, Grooming, Pet Taxi, Retail, Training |
| Seseh | Sudah buka sejak Mei 2026 |
| Berawa | thedoghotel.id akan ditutup, jadi kartu Berawa tidak link ke sana |
| Refund & Terms | Masih perlu, disederhanakan di halaman House Rules |
| Referral | Section baru **Friends of The Dog Club** di Loyalty Program, tombolnya ke form pendaftaran referral |

Akibatnya:
- Nomor Ungasan di website = `+62 813-3834-459`. FAQ dan flyer referral menulis `+62 812-4645-3589`; tanyakan apakah itu nomor lain (misalnya contact person referral).
- House Rules dapat section tambahan "Booking & refunds" versi singkat.
- Loyalty Program dapat section "Friends of The Dog Club".

### Masih terbuka
1. **Jam buka Senin:** pricelist menulis Senin–Minggu 9am–6pm, tapi ada juga "Monday 10am–4pm". Berlaku di semua cabang?
2. **Alamat + Google Maps:** Umalas (website lama: Jl. Umalas 1 No. 1700, Kerobokan Kelod — masih benar?), Berawa, Seseh, dan link Maps keempat cabang.
3. **Friends of The Dog Club:** link form referral, dan nominalnya (IDR 100K, atau 50K teman / 200K pengajak).
4. **Teks refund & terms singkat:** klien kirim sendiri, atau kami susun dari FAQ (tidak ada refund untuk check-out lebih awal, sisa saldo jadi store credit) lalu klien setujui?
5. Hero menyebut Retail, Training, Homecare, tapi halaman Services cuma 6 kartu. Tambah kartu (foto + 1 kalimat), atau hapus dari daftar?
6. Partnership: kontak lewat WhatsApp atau email apa?
7. Harga ditampilkan di website (disarankan, sebagai teks)?
8. 4 artikel blog lama tidak ada di desain. Boleh dihapus (diarahkan ke Home)?
9. Video TDC Story (2,1 GB): diunggah ke YouTube/Vimeo mereka, atau cukup foto?
10. Perbaikan teks kecil di bagian 1 boleh diterapkan?

## 3. Teknologi

| Bagian | Pilihan |
| --- | --- |
| Framework | Next.js (versi stabil terbaru, `create-next-app@latest`), App Router, TypeScript |
| Styling | Tailwind CSS |
| Output | Static export: `output: 'export'`, `trailingSlash: true` (URL lama WordPress pakai garis miring di akhir), `images.unoptimized: true` |
| Font | `next/font/google` Open Sans |
| Gambar | Dioptimasi sebelum masuk repo dengan script `sharp` → WebP |
| Video | `ffmpeg`: drone → MP4 720p tanpa suara, < 5 MB, ada poster. Video About → YouTube/Vimeo, dimuat setelah diklik |
| Hosting | Netlify gratis. `main` = production, `develop` = staging, Pull Request = Deploy Preview |
| Repo | Repo baru private `thedogclub-website` di akun Arnold, dipindah ke GitHub klien setelah lunas |

### Struktur folder
```
thedogclub-website/
├── src/
│   ├── app/                 # satu folder per halaman: page.tsx
│   │   ├── layout.tsx       # font, header, footer, metadata dasar
│   │   ├── not-found.tsx    # 404
│   │   ├── sitemap.ts
│   │   └── robots.ts
│   ├── components/          # Header, Footer, PageHero, PhotoStack, PaperCard, Accordion, BranchPicker
│   └── content/             # SEMUA teks & data bisnis di sini, bukan di komponen
│       ├── site.ts          # cabang, alamat, nomor WA, jam buka, Instagram
│       ├── services.ts
│       ├── pricing.ts
│       ├── faq.ts
│       ├── house-rules.ts
│       └── loyalty.ts
├── public/
│   ├── images/              # hasil optimasi saja
│   ├── video/
│   └── _redirects           # URL lama → baru (Netlify)
├── scripts/optimize-images.mjs
└── README.md
```

Aturan: nomor telepon, alamat, harga ditulis **sekali** di `src/content/`. Kalau klien ganti nomor, cukup ubah satu baris.

### Aset → halaman
| Folder aset | Dipakai di |
| --- | --- |
| `Photo/. Cover` | Home hero |
| `Photo/1. Service` | Services, galeri Home |
| `Photo/2. Loc` | Locations (foto + drone) |
| `Photo/3. Facility` | Facility |
| `Photo/4. House Rules`, `Doc/2.png` | House Rules (teks diketik ulang) |
| `Photo/5. Book a Visit` | Book a Visit |
| `Photo/6. Partnership` | Partnership |
| `Photo/7. FAQ`, `Doc/1.png` | FAQ |
| `Photo/8. About Us`, `about us/TDC Story-001.mov` | About Us |
| `Doc/3–5.png` | Loyalty Program (teks diketik ulang) |
| `Pricelist/` | Services (harga) |
| `Contact/Contact Admin.pdf` | Book a Visit (pilihan cabang) |
| `Logo & Brand/` | Header, footer, favicon |

Target ukuran: foto hero < 300 KB, foto kartu < 150 KB.

## 4. Alur kerja per halaman

Setiap halaman lewat 7 langkah yang sama:

1. **Run-through:** buka layar Canva-nya, sepakati section, isi teks, dan versi mobile. Catat di tiketnya.
2. **Branch:** `git switch develop && git pull && git switch -c feature/TDC-0xx-nama-halaman`
3. **Build per section**, commit per section (lihat bagian 5).
4. **Cek sendiri** pakai Definition of Done di bawah.
5. **Pull Request** ke `develop`. Netlify membuat link Deploy Preview.
6. **Squash and merge.** Judul PR menjadi satu commit rapi di `develop`.
7. **Update tracker:** centang tiket, catat bug kalau ada.

### Definition of Done (setiap halaman)
- [ ] Desktop 1440px mirip Canva (layout, jarak, ukuran huruf)
- [ ] Mobile 375px dan tablet 768px rapi, tidak ada scroll ke samping
- [ ] Semua teks & data dari `src/content/`, bukan placeholder
- [ ] Tepat 1 `<h1>`, gambar punya alt text
- [ ] Title & meta description terisi
- [ ] Semua tombol & link sudah diklik dan benar
- [ ] Tidak ada error di console, `npm run build` sukses
- [ ] Sudah dicek di link Deploy Preview

## 5. Aturan Git & commit

### Branch
| Branch | Fungsi | Deploy |
| --- | --- | --- |
| `main` | Production. Hanya dari `develop` setelah klien approve | thedogclub.id |
| `develop` | Staging, untuk review klien | `develop--<site>.netlify.app` |
| `feature/TDC-0xx-nama` | Satu tiket / halaman | Deploy Preview per PR |
| `fix/TDC-0xx-nama` | Perbaikan bug | Deploy Preview per PR |

Jangan push langsung ke `main` atau `develop`. Saat launch, beri tag `v1.0.0`.

### Format commit ([Conventional Commits](https://www.conventionalcommits.org))
```
type(scope): ringkasan singkat

Penjelasan kenapa (opsional, kalau tidak jelas dari ringkasan).

Refs: TDC-0xx
```
- Bahasa Inggris, kalimat perintah, huruf kecil, maksimal 72 karakter, tanpa titik.
- Satu commit = satu perubahan yang utuh. Jangan campur "tambah hero" dengan "ganti font".

| Type | Kapan |
| --- | --- |
| `feat` | Tambah section, komponen, atau halaman |
| `fix` | Perbaiki bug |
| `content` | Ganti/isi teks, harga, foto tanpa ubah layout |
| `style` | Ubah tampilan tanpa ubah fungsi (jarak, warna) |
| `refactor` | Rapikan kode tanpa ubah tampilan |
| `perf` | Optimasi gambar, video, kecepatan |
| `build` | Konfigurasi Next.js, Netlify, dependency |
| `docs` | README, catatan |
| `chore` | Hal lain (setup awal, `.gitignore`) |

Scope = nama halaman (`home`, `services`, `facility`, `locations`, `house-rules`, `book-a-visit`, `partnership`, `loyalty`, `about`, `faq`, `privacy`) atau bagian umum (`layout`, `ui`, `content`, `seo`, `assets`, `config`).

Contoh urutan commit halaman Home:
```
feat(home): add full-bleed hero with headline and join cta
feat(home): add service list strip under hero
feat(home): add staggered four-photo gallery
style(home): stack gallery photos on mobile
content(home): use final hero photo and alt text
```

Contoh lain:
```
chore: scaffold next.js app with typescript and tailwind
build(config): enable static export with trailing slashes
feat(layout): add header with centered logo and split nav
feat(layout): add mobile menu
perf(assets): add sharp script to export webp images
feat(seo): add localbusiness json-ld for four branches
fix(header): keep nav on one line at 1280px
```

### Pull Request
Judul PR = pesan commit squash, misalnya `feat(home): build homepage (TDC-011)`. Isi PR:
```
Tiket: TDC-0xx
Apa yang berubah:
Screenshot desktop & mobile:
Definition of Done: [ ] ... (salin checklist di atas)
```

## 6. Jadwal internal

Target live ke klien tetap **Senin 23 Nov**. Jadwal di bawah sengaja lebih cepat supaya ada cadangan.

| Tanggal | Kerja | Tiket |
| --- | --- | --- |
| Rab 4 Nov | Rencana ini, kirim pertanyaan, run-through semua layar | 003, 004 |
| Kam 5 Nov | Repo + Netlify, layout dasar, data cabang, pipeline aset | 007–010 |
| Jum 6 Nov | Home + header/footer desktop & mobile → kirim preview untuk approval | 005, 006, 011 |
| Sen 9 Nov | Services, Facility | 012, 013 |
| Sel 10 Nov | Locations, House Rules, Book a Visit | 014–016 |
| Rab 11 Nov | Partnership, Loyalty, About Us | 017–019 |
| Kam 12 Nov | FAQ, Privacy, 404, cek semua tombol → tagih termin 2 | 020–022 |
| Jum 13 Nov | SEO, structured data, redirect (setelah termin 2 masuk) | 023–026 |
| Sen 16 Nov | Performa + QA internal | 025, 027 |
| Sel 17 Nov | Kirim preview ke klien, review 17–19 Nov | 028 |
| Jum 20 Nov | Koreksi selesai, pelunasan | 028, 029 |
| Sen 23 Nov | Live | 030, 031 |

## 7. Redirect URL lama → baru

| URL lama | URL baru |
| --- | --- |
| `/services/`, `/dog-daycare/`, `/luxury-dog-hotel/`, `/dog-spa-massage-grooming/`, `/dog-training/`, `/dog-walking/`, `/dog-birthday-party/`, `/pet-taxi/`, `/in-house-vet/`, `/our-schedule/` | `/#services` |
| `/pricing/` | `/#services` (atau section harga kalau disetujui) |
| `/join-the-club/` | `/book-a-visit/` |
| `/umalas/` | `/locations/` |
| `/own-a-franchise/` | `/partnership/` |
| `/faqs/` | `/faq/` |
| `/about-us/`, `/privacy-policy/` | sama |
| `/terms-of-service/`, `/refund_returns/`, `/shipping-policy/` | `/` |
| Artikel blog `/2024/11/29/...` (ambil slug lengkap dari website live) dan `/2023/11/01/hello-world/` | `/` |
