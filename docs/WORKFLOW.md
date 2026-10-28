# Workflow Proyek — The Dog Club Bali (Paket Essential)

Panduan kerja dari DP sampai website live. Setiap fase punya **gerbang**: fase berikutnya baru mulai kalau syarat gerbangnya terpenuhi.

## Ringkasan

| Fase | Durasi | Gerbang untuk lanjut | Pembayaran |
| --- | --- | --- | --- |
| 0. Kickoff | 1–2 hari | DP masuk + brand kit diterima | DP 50% — IDR 3.750.000 |
| 1. Desain | Minggu 1 | Klien tulis "Design approved" | Termin 2 30% — IDR 2.250.000 |
| 2. Build | Minggu 2 | Semua halaman ada di staging | — |
| 3. Review & QA | Minggu 3 | Daftar revisi selesai + termin 3 masuk | Pelunasan 20% — IDR 1.500.000 |
| 4. Launch | 1 hari | Website live di thedogclub.id | — |
| 5. Garansi | 30 hari | — | — |

## Environment: development, staging, production

```
feature/xxx  ──PR──▶  develop  ──merge (setelah klien approve)──▶  main
     │                   │                                          │
 Deploy Preview      STAGING                                   PRODUCTION
 (link per PR)   develop--thedogclub.netlify.app             thedogclub.id
 untuk kamu       untuk review klien                          untuk publik
```

| Environment | Branch | URL | Siapa yang lihat |
| --- | --- | --- | --- |
| Local | branch apa saja | `localhost:3000` | Kamu |
| Preview | `feature/*` (via Pull Request) | Link otomatis dari Netlify per PR | Kamu |
| Staging | `develop` | `develop--<nama-site>.netlify.app` | Klien (untuk review) |
| Production | `main` | `thedogclub.id` | Publik |
| Mockup | `main`, folder `mockup/` | GitHub Pages | Klien (sebelum proyek) |

**Aturan:**
- Jangan pernah push langsung ke `main`. Semua lewat `develop` dulu.
- `develop` → `main` hanya setelah klien approve di staging.
- Staging diberi `noindex` supaya tidak muncul di Google.

### Setup awal (sekali saja)

1. Buat branch `develop` dari `main`.
2. Buat project Next.js dengan `output: 'export'` (static), supaya nanti bisa di-upgrade ke paket Recommended (tambah Payload) tanpa bangun ulang.
3. Hubungkan repo ke Netlify:
   - Production branch: `main`
   - Branch deploys: aktifkan untuk `develop`
   - Deploy Previews: aktifkan untuk Pull Request
4. Pasang `noindex` untuk semua deploy selain production (cek `process.env.CONTEXT !== 'production'` di Netlify).
5. Cek dulu halaman pricing Netlify. Pastikan paket gratisnya masih boleh untuk website bisnis.

## Fase 0 — Kickoff

Mulai setelah DP masuk. Kirim invoice: `mockup/invoice/`.

Minta dari klien (sudah tercantum di invoice):
- [ ] Logo file asli (AI/SVG/PDF/PNG transparan besar)
- [ ] Brand guideline: kode warna, font, contoh desain yang mereka suka
- [ ] Foto asli: park, villa, pool, spa, tim, anjing
- [ ] Price list & jadwal terbaru, 3 paket birthday party
- [ ] Akses DomaiNesia, Google Search Console, WordPress lama
- [ ] **Satu PIC** (contact person) untuk feedback & approval

Kalau brand kit belum lengkap dalam 2 hari kerja, timeline mundur. Bilang ke klien secara tertulis.

## Fase 1 — Desain (finalisasi desain)

Tujuan: menyesuaikan mockup dengan brand mereka, lalu **mengunci desain** sebelum build.

**Yang direview klien:** homepage + 1 halaman layanan (misal Dog Daycare), versi desktop dan mobile. Halaman lain mengikuti pola yang sama, jadi cukup dua ini yang di-approve.

**Alur revisi:**
1. Kirim desain v1 (link staging atau mockup).
2. Klien kirim **satu daftar feedback gabungan** dalam 3 hari kerja.
3. Revisi → v2. Ulangi maksimal **2 putaran revisi mayor**.
4. Klien tulis approval secara tertulis (WA/email), misalnya: *"Design approved."*

**Revisi mayor vs minor:**

| Mayor (dihitung sebagai putaran) | Minor (bebas, kapan saja sebelum launch) |
| --- | --- |
| Ganti layout atau urutan section | Typo, ganti teks |
| Ganti warna, font, gaya visual | Ganti foto satu per satu |
| Ganti gaya foto/ilustrasi | Geser sedikit spacing |

**Syarat desain dianggap final (checklist sebelum minta approval):**
- [ ] Logo, warna, dan font sesuai brand kit klien
- [ ] Homepage + 1 halaman layanan sudah dicek di desktop **dan** HP
- [ ] Semua foto stok sudah diganti foto asli (atau disepakati placeholder mana yang tetap)
- [ ] Teks utama (judul, tagline, tombol) sudah disetujui
- [ ] Klien sudah kirim approval tertulis
- [ ] Termin 2 sudah ditagih

**Setelah approve:** desain terkunci. Perubahan desain setelah ini = *change request*: kasih penawaran harga dulu, kerjakan setelah klien setuju.

## Fase 2 — Build

- Kerjakan per halaman di branch `feature/*`, merge ke `develop`.
- Kirim update ke klien **tiap Jumat**: link staging + apa saja yang sudah jadi + apa yang dikerjakan minggu depan.
- Input konten asli (harga, jadwal, FAQ) dari data yang klien kirim.
- Setup redirect URL lama → baru (lihat tabel di `mockup/README.md`).

## Fase 3 — Review & QA

1. Cek sendiri dulu (checklist di bawah).
2. Kirim link staging ke klien. Minta **satu daftar koreksi** dalam 3 hari kerja.
3. Perbaiki semua, kirim ulang.
4. Tagih pelunasan **sebelum** launch.

**Checklist QA:**
- [ ] Semua 27 halaman terbuka, tidak ada link mati
- [ ] Tampilan benar di iPhone, Android, laptop
- [ ] Semua tombol booking menuju Pawsi, tombol WA ke nomor yang benar
- [ ] Harga, jam buka, alamat sama persis dengan data klien
- [ ] Judul tab & meta description terisi di setiap halaman
- [ ] Gambar punya teks alt, ukuran sudah dikompres
- [ ] Skor Lighthouse ≥ 90 (performance & SEO)
- [ ] Redirect URL lama berfungsi
- [ ] Halaman 404 tampil

## Fase 4 — Launch

Lakukan di hari kerja pagi, jangan Jumat sore.

1. Merge `develop` → `main`. Cek production URL Netlify.
2. Di Netlify: tambahkan custom domain `thedogclub.id` dan `www.thedogclub.id`. Catat record DNS yang diminta.
3. Di DomaiNesia, ganti **hanya** record website:
   - `A` untuk `thedogclub.id` → nilai dari Netlify
   - `CNAME` untuk `www` → nilai dari Netlify
4. ⚠️ **Jangan sentuh:** `MX` (email Google Workspace) dan `TXT google-site-verification`.
5. Tunggu SSL aktif (otomatis), cek `https://thedogclub.id` dan `https://www.thedogclub.id`.
6. Kirim email test ke `woof@thedogclub.id` untuk memastikan email tetap jalan.
7. Search Console: submit `sitemap.xml`.
8. Kabari klien: website live + link.

**Jangan minta klien mematikan hosting WordPress lama** sampai website baru jalan stabil minimal 1 minggu.

## Fase 5 — Garansi 30 hari

- Bug dari pekerjaanmu: perbaiki gratis.
- Permintaan baru (ganti konten, halaman baru): bukan garansi. Tawarkan:
  - Update konten: IDR 150.000 / permintaan (1 perubahan di 1 halaman)
  - Maintenance: IDR 1.000.000 / bulan
  - Upgrade ke Recommended (admin dashboard): bayar selisih paket
- Di hari ke-30, kirim pesan penutup + tawarkan maintenance.

## Komunikasi

- Semua approval dan keputusan **tertulis** (WA/email). Screenshot dan simpan.
- Update rutin tiap Jumat.
- Jam respon: hari kerja. Sampaikan di awal.
- Keterlambatan konten/feedback dari klien = timeline mundur sebanyak hari yang sama. Ingatkan secara sopan saat terjadi.
