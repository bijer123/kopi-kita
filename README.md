# Kopi Kita ☕

Website katalog kopi modern berbasis Django. Dibuat untuk memenuhi tugas akhir mata kuliah *Algoritma dan Pemrograman Lanjut*, dengan fitur lengkap CRUD, login/logout, tampilan responsif, dan dark mode.

---

## 🔧 Fitur Utama

* ✅ **CRUD** kopi (tambah, lihat, edit, hapus)
* ✅ **Login & Logout** menggunakan sistem autentikasi Django
* ✅ **Upload gambar kopi** dari form atau tampil otomatis
* ✅ **Dark Mode toggle**
* ✅ **Search bar** untuk filter nama kopi
* ✅ **Modal detail** interaktif
* ✅ **Tampilan responsive** dan modern

---

## 🗂️ Struktur Proyek

```
kopi_kita/
├── katalog/                # App utama
│   ├── migrations/
│   ├── static/             # File CSS, gambar
│   ├── templates/
│   │   └── katalog/        # HTML templates
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── kopi_kita/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3              # Database SQLite
└── manage.py
```

---

## 🚀 Cara Menjalankan

### 1. Clone Repository (jika pakai Git)

```bash
git clone https://github.com/username/kopi-kita.git
cd kopi-kita
```

### 2. Buat dan Aktifkan Virtual Environment

```bash
python -m venv env
source env/bin/activate       # Linux / Mac
.\env\Scripts\activate        # Windows
```

### 3. Install Dependency

```bash
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, cukup:

```bash
pip install django pillow
```

### 4. Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Jalankan Server

```bash
python manage.py runserver
```

Buka di browser: `http://127.0.0.1:8000/`

### 6. (Opsional) Buat Superuser

```bash
python manage.py createsuperuser
```

---

## 📌 Akun Login (jika dibutuhkan)

| Username | Password                     |
| -------- | ---------------------------- |
| admin    | admin123 (contoh, sesuaikan) |

---

## 📷 Contoh Tampilan

![homepage](static/img/preview-homepage.png)

---

## 🧑‍💻 Pembuat

Nama  : \[Multazam An Nasri]
NIM   : \[240604073]
Kelas : \[TK C]

---

## 📄 Lisensi

Proyek ini dibuat hanya untuk keperluan tugas akademik. Tidak untuk tujuan komersial.

---

> Dibuat dengan ❤️ menggunakan Django 5.2.3
