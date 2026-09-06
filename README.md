

Nama : Iqbal Virdiansyah

NPM : 2506656816

Kelas : PBP C

### Tugas 1

1. **Saat merancang struktur HTML, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Bagaimana elemen tersebut membantu Anda?**
   Ya, saya menggunakan elemen semantik HTML5 secara ekstensif seperti `<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, dan `<footer>`. Penggunaan elemen semantik ini sangat membantu saya dalam mengelompokkan blok-blok konten agar lebih logis dan bermakna dibandingkan menggunakan tag `<div>` secara berlebihan. Selain mempermudah proses modifikasi kode dan styling CSS, elemen semantik tersebut juga meningkatkan keterbacaan webpage saya, dan mematuhi kaidah SEO (Search Engine Optimization).

2. **Tantangan tata letak apa yang Anda temukan saat mengatur CSS responsive, dan bagaimana Anda mengevaluasi elemen yang diprioritaskan posisinya?**
   Tantangan utamanya adalah ketika mengatur elemen Grid kompleks pada bagian "Hero" (kolom ganda teks profil dan foto) serta pembagian kotak-kotak Cards pada bagian "Projects" agar tidak terhimpit di layar kecil. Saya mengevaluasi prioritas berdasarkan user experience dan alur baca di layar, komponen bisa diletakkan berdampingan, namun ketika berpindah ke layar hp (menggunakan media query `max-width: 600px`), tata letak dipaksa bertumpuk menjadi kolom tunggal (vertikal). Teks utama (Nama dan Bio) diposisikan paling atas dulu untuk dibaca, lalu diikuti oleh foto dan tautan sosial media.

3. **Batasan apa yang Anda rasakan pada static web murni ini, dan fungsionalitas dinamis apa yang ingin ditambahkan selanjutnya?**
   Batasan terbesar yang sangat terasa adalah sifatnya yang statis atau hardcoded. kalo saya mau memperbarui portofolio (misalnya menambah proyek baru, pengalaman organisasi, atau menambah keahlian), saya harus buka source code HTML dan memodifikasinya secara manual satu demi satu. Hal ini tidak efisien. Berdasarkan batasan ini, fungsionalitas dinamis yang paling ingin saya persiapkan ke depan adalah pengintegrasian basis data (menggunakan model bawaan Django/MVT) untuk menyimpan data Proyek, Pengalaman, dan *Skills*. Dengan begitu, konten portofolio dapat diisi dan dikelola secara dinamis melalui halaman *Django Admin* jadi seperti CMS (Content Management System).

---

## Deskripsi Proyek & Cara Menjalankan (*Setup Instructions*)
Proyek ini adalah *website* portofolio pribadi yang dibangun menggunakan *framework* Django (Python). Tampilan antarmuka (*frontend*) dikerjakan secara *native* menggunakan **HTML5 Semantik murni** dan **CSS3 murni** tanpa bergantung pada *framework* eksternal seperti Bootstrap atau Tailwind, guna melatih pemahaman dasar terkait elemen web dan *styling* responsif.

**Cara Menjalankan Server Lokal:**
1. Buka terminal (CMD/PowerShell).
2. Aktifkan *virtual environment*: `.\env\Scripts\activate` (Windows)
3. Instal semua dependensi: `pip install -r requirements.txt`
4. Jalankan *server* Django: `python manage.py runserver`
5. Buka peramban (*browser*) dan akses: `http://localhost:8000/`

---

## AI Disclosure
- **Alat AI yang Digunakan:** Google AI Agent (terintegrasi pada IDE).
- **Bagian yang Dibantu AI:** 
  1. Melakukan konversi teks mentah dari berkas PDF CV *Applicant Tracking System* (ATS) milik saya menjadi susunan HTML (*Experience, Projects, Skills*).
  2. Membantu memberikan fondasi awal untuk pembuatan *layout* responsif berbasis *CSS Grid* dan *Flexbox* (khususnya untuk penyusunan *timeline layout* yang elegan).
- **Strategi Prompting:** 
  Saya menyertakan seluruh teks profil CV saya langsung di dalam *prompt*, lalu memberikan instruksi dengan batasan yang sangat ketat ("murni dengan HTML5 dan CSS3, tanpa Tailwind/framework lain") untuk memastikan asisten AI tidak memberikan *code snippet* yang melanggar ketentuan tugas. Saya juga menginstruksikan spesifikasi desain ("jangan buat kotak-kotak, susun ke bawah") agar hasil kode sesuai ekspektasi.
- **Analisis Kritis & Perbaikan Manual:** 
  Keterbatasan AI sering kali terletak pada asumsinya dalam desain (*over-engineering*). Sebagai contoh, AI sempat menyarankan *styling* dalam bentuk *card-grid*, namun tampilan tersebut tidak cocok untuk pengalaman kerja. Oleh karena itu, saya secara manual mengevaluasi dan memberikan instruksi perbaikan (memerintahkan AI mengubah *grid* menjadi daftar menurun/vertikal dengan gaya *timeline*). Saya juga menyadari AI tidak paham mengenai konteks penamaan *class* yang ideal jika tidak diawasi, sehingga saya memastikan setiap *class* CSS tetap mudah dipelihara (*maintainable*).
