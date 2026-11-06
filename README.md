# 🧪 RIT Pemrograman Dasar (menggunakan Python)

Repositori resmi latihan mahasiswa **RIT Academy (Republic of Information Technology)** untuk mempelajari alur kerja instalasi dependensi pihak ketiga, mengeksekusi proyek Python di komputer lokal, serta membaca dan mengeksplorasi dokumentasi fitur.

---

## 📋 Prasyarat Sistem
* Sudah terpasang **Python (minimal versi 3.8 keatas)** di komputermu.
* Text editor **VS Code** (atau editor teks lain pilihanmu).
* Koneksi internet aktif untuk mengunduh library awal.

---

## 🚀 Langkah 1: Persiapan Lingkungan Kerja

### 1. Unduh Kode ke Laptop
* Di GitHub, klik tombol hijau **`<> Code`** di kanan atas, lalu pilih **Download ZIP**.
* Ekstrak file ZIP tersebut ke folder dokumenmu (misal di `Documents/` atau `Downloads/`).
* Buka folder tersebut menggunakan **VS Code** (*File ➔ Open Folder...*).

### 2. Buka Terminal di VS Code
Tekan shortcut keyboard: `Ctrl + ~` (atau menu *Terminal ➔ New Terminal*).

### 3. Pasang Dependensi Proyek (PIP)
Jalankan satu perintah ini di terminal untuk mengunduh seluruh library yang dibutuhkan:
```bash
pip install -r requirements.txt
```

---

## 🎯 Lab 1: Terminal ASCII QR Code Generator

Aplikasi pembuat QR Code ASCII yang dapat dipindai langsung menggunakan kamera smartphone dari layar monitor. Menggunakan library `qrcode` python. Cek dokumentasi: [python-qrcode](https://github.com/lincolnloop/python-qrcode)

1. Jalankan program di terminal:
   ```bash
   python 01_qr_generator.py
   ```
2. Masukkan link website portofoliomu (contoh: `https://namamu.github.io`).
3. QR yang tampil di terminal bisa langsung dipakai.

---

## 🎯 Lab 2: Live Weather CLI (wttr.in Client)

Aplikasi pemantau cuaca dunia *real-time* yang berkomunikasi langsung dengan layanan API publik eksternal. Cek dokumentasi: [wttr.in](https://github.com/chubin/wttr.in)

1. Jalankan program di terminal:
   ```bash
   python 02_weather_cli.py
   ```
2. Ketik nama kota (contoh: `Garut`, `Bandung`, `Tokyo`).
3. Laporan cuaca akan muncul di terminal.

---

## 🌐 Lab 3: Eksplorasi Proyek Nyata Tingkat Lanjut (Vercel Flask)

Setelah menguasai instalasi dan eksekusi kode mini tersebut, coba jalankan server web backend resmi dengan arsitektur flask Python berikut ini:

* **Tautan Repositori:** [`Flask App Template (untuk di deploy di Vercel)`](https://github.com/putuwaw/flask-app-vercel)

---

## 📄 Lisensi
Didistribusikan di bawah lisensi MIT. Bebas digunakan, dipelajari, dan dimodifikasi untuk kepentingan edukasi mahasiswa RIT Academy.
