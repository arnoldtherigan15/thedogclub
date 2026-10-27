# The Dog Club Bali — Mockup

Mockup statis (HTML + Tailwind CDN) untuk redesign thedogclub.id. Desain mengikuti mockup awal (cream / forest / sunshine, Playfair Display + Inter), tapi semua konten diganti dengan data asli dari website lama.

## Cara lihat

Buka `mockup/index.html` langsung di browser, atau:

```bash
cd mockup && python3 -m http.server 8000
# buka http://localhost:8000
```

## Cara edit

Semua halaman di-generate dari `build.py`. Harga, jam buka, kontak, FAQ, layanan → ubah data di bagian atas `build.py`, lalu:

```bash
python3 mockup/build.py
```

Teks blog dan halaman legal ada di `content/blog/` dan `content/legal/`. Jangan edit file `.html` secara langsung, karena akan tertimpa saat build ulang.

## Pemetaan halaman (web lama → mockup)

| Web lama (WordPress) | Mockup |
| --- | --- |
| `/` | `index.html` |
| `/services/` | `services.html` |
| `/dog-daycare/` | `dog-daycare.html` |
| `/luxury-dog-hotel/` | `luxury-dog-hotel.html` |
| `/dog-spa-massage-grooming/` | `dog-spa-massage-grooming.html` |
| `/dog-training/` | `dog-training.html` |
| `/dog-walking/` | `dog-walking.html` |
| `/dog-birthday-party/` | `dog-birthday-party.html` |
| `/pet-taxi/` | `pet-taxi.html` |
| `/in-house-vet/` | `in-house-vet.html` |
| `/pricing/` | `pricing.html` |
| `/our-schedule/` | `our-schedule.html` |
| `/join-the-club/` | `join-the-club.html` |
| `/about-us/` | `about-us.html` |
| `/faqs/` | `faqs.html` |
| `/umalas/` | `umalas.html` |
| `/own-a-franchise/` | `own-a-franchise.html` |
| Blog (4 artikel) | `blog.html` + `blog-*.html` |
| `/privacy-policy/` | `privacy-policy.html` |
| `/terms-of-service/` | `terms-of-service.html` |
| `/refund_returns/` | `refund-policy.html` |
| `/shipping-policy/` | `shipping-policy.html` |
| — (baru) | `404.html` |

Tidak dibawa: `/my-account/` dan `/product-category/*` (sisa WooCommerce yang tidak dipakai), serta "Hello world!" (post default WordPress).

## Yang diperbaiki

**Dari web lama**
- Harga dan jadwal sebelumnya berupa **gambar** (tidak bisa dibaca Google, tidak bisa di-zoom di HP). Sekarang jadi teks/tabel, dan halaman Pricing baru menggabungkan semua harga.
- Homepage hampir tanpa teks (hanya gambar). Sekarang ada copy, layanan, harga populer, langkah daftar, peta, dan FAQ.
- Email pribadi penulis tampil di setiap artikel blog → diganti "The Dog Club team".
- Terms of Service masih template Shopify (kontak `nrshopify347@gmail.com`, menyebut "hosted on Shopify") → email diganti `woof@thedogclub.id` dan kalimat Shopify dihapus.
- Refund policy memakai `thedogclubid@gmail.com` → diganti `woof@thedogclub.id`.
- Typo: "Kapubaten", "unsure", "rabbies", "you dog holiday", dan lainnya.
- Copyright terkunci "© 2024" → otomatis tahun berjalan.
- FAQ di `/faqs/` dan `/umalas/` berbeda-beda → digabung jadi satu daftar lengkap tanpa duplikat.
- Tombol CTA tidak konsisten → booking selalu ke Pawsi; layanan by-request (taxi, vet, training, birthday) ke WhatsApp dengan pesan otomatis.

**Dari mockup awal**
- Konten karangan diganti data asli: lokasi (Canggu → **Umalas**), alamat, jam buka, harga, layanan. Day Pass / membership IDR 1.2M / 11M, cafe, co-working, dan Yappy Hour dihapus karena tidak ada di bisnis aslinya.
- Testimoni dan rating 4.9/5 palsu → diganti placeholder yang jelas, untuk diisi review Google asli.
- Peta berupa foto stok → Google Maps embed asli.
- Ikon `fa-calendar-heart` (Font Awesome Pro, tidak tampil) dan typo "VIP VIP" dihapus.
- Satu gambar Unsplash 404 diganti.
- FAQ & menu mobile pakai elemen yang aksesibel (`<details>`, `aria-expanded`), form tanpa `alert()`.

## Perlu dikonfirmasi ke klien

- [ ] **Harga terbaru.** Harga diambil dari teks halaman layanan. Gambar pricelist Feb 2026 tidak bisa diakses (server lama sedang down), jadi mungkin ada harga yang sudah berubah.
- [ ] **Jadwal.** Halaman "Our Schedule" lama berupa gambar yang tidak bisa diakses. Isi sementara: jam buka + rutinitas harian dari FAQ.
- [ ] **3 paket birthday party**: nama, isi, dan harga.
- [ ] Langkah daftar via **Pawsi** (sebelumnya "customer portal"/Gingr). Apakah registrasi member sekarang juga di Pawsi?
- [ ] Refund & shipping policy masih untuk toko online. Apakah toko online masih ada? Kalau tidak, dua halaman ini bisa dihapus.
- [ ] Foto asli (semua gambar di mockup masih foto stok Unsplash).
- [ ] Review Google asli untuk bagian testimoni.
