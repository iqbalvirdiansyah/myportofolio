
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

### Tugas 2

1. **Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru...**
   Gini alurnya: waktu user buka halaman `/projects/` di browser, request-nya pertama kali masuk ke `urls.py` utama milik proyek. Dari situ, request diterusin ke `urls.py` milik aplikasi `main` buat dicari rute yang pas. Kalau rutenya cocok, Django bakal manggil fungsi yang ada di `views.py` (misal `show_projects`). Di dalam *view* ini, kita minta data ke `models.py` (database). Setelah datanya dapet, *view* bakal ngelempar data tersebut (lewat *context*) ke file `projects.html` (*template*). Terakhir, *template* ini bakal nge-render HTML-nya dan dikirim balik ke browser buat ditampilin ke user.

2. **Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template?**
   Biar nggak ribet kalau mau update konten! Kalau datanya di-hardcode langsung di HTML (*template*), tiap kali mau nambah atau ngedit project, kita harus bongkar *source code* HTML-nya secara manual. Kalau disimpen di *model* (database), aplikasinya jadi lebih dinamis. Kita tinggal nambahin datanya lewat database atau admin panel, dan otomatis *template*-nya bakal nyesuain pake sintaks *looping* (perulangan). Ini bikin aplikasi jauh lebih gampang di-*maintain* dan di- *scale* ke depannya tanpa takut ngerusak layout HTML.

3. **Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh...**
   Gampangnya, `makemigrations` itu kayak bikin draf atau cetak biru (*blueprint*) dari perubahan database kita. Django nyatet perubahan apa aja yang kita lakuin di `models.py` dan disimpen ke file *migrations*. Nah, kalau `migrate`, itu fungsinya buat nge-eksekusi draf tadi langsung ke database benerannya (kayak bikin atau ngubah tabel di SQLite/PostgreSQL).
   **Contohnya:** kalau aku nambahin atribut baru `link_github = models.URLField()` di model `Project`, aku wajib jalanin `makemigrations` biar Django nyatet perubahan itu, trus jalanin `migrate` biar tabel di databasenya bener-bener ketambahan kolom `link_github`.

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

### Tugas 1 (Frontend Statis)
- **Bagian yang Dibantu AI:** Konversi teks mentah dari berkas PDF CV *Applicant Tracking System* (ATS) menjadi susunan HTML (*Experience, Projects, Skills*) dan perancangan *CSS Grid*.
- **Strategi Prompting:** Saya menyertakan seluruh profil teks dan memberikan batasan ketat ("murni HTML5 & CSS3 tanpa Tailwind") untuk mencegah pelonggaran syarat tugas.
- **Analisis Kritis & Perbaikan Manual:** AI cenderung melakukan *over-engineering* dalam mendesain (misalnya menyarankan desain kotak-kotak untuk *Experience*). Saya melakukan intervensi manual untuk mengubah spesifikasi desainnya menjadi susunan menurun bergaya *timeline* agar *User Experience* lebih profesional.

### Tugas 2 (Django MVT & Dinamis)
- **Bagian yang Dibantu AI:** Menyusun arsitektur basis data pada `models.py` (seperti pemakaian `UUIDField`), mengimplementasikan fungsi `get_object_or_404` di `views.py`, serta otomatisasi penulisan *Unit Test* dan injeksi *dummy data* melalui terminal.
- **Strategi Prompting:** Saya menyuapkan daftar *checklist* tugas (Rubrik) lalu memberikan kebebasan pada AI untuk membuat kerangka *testing*, namun saya memegang kendali arsitektur dengan instruksi spesifik ("jangan pisah halaman experience, hanya pisah projects dan buatkan halaman detailnya").
- **Analisis Kritis & Perbaikan Manual:** Tutorial bawaan menyarankan agar setiap entitas dipisah ke halamannya sendiri-sendiri, namun saya mengarahkan AI untuk melanggar kebiasaan tutorial itu demi alasan estetika. AI sempat kebingungan mengatasi masalah *routing* jika semua disatukan, jadi saya harus turun tangan mengevaluasi dan memutuskan desain *hybrid*: Model `Experience` tetap dimuat di halaman utama, sementara model `Project` diekstraksi menjadi sistem *List/Detail view* URL tersendiri. AI tidak memahami gambaran besar desain portofolio sampai saya menyelaraskan fungsi *backend*-nya secara struktural.
- **Log Prompting:** Seluruh instruksi dan *log* percakapan dengan AI tersimpan dan dapat dilacak pada histori IDE (*Workspace Agent*).
