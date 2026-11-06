"""
=====================================================
PROYEK 1: TERMINAL ASCII QR CODE GENERATOR
RIT Academy - Pemrograman Dasar Python
=====================================================
"""

import qrcode

print("TERMINAL QR CODE GENERATOR")
print("Ubah link web atau pesan teksmu menjadi QR Code instan!\n")

input_link = input("Masukkan teks atau link URL: ").strip()

if not input_link:
    input_link = "https://github.com/RIT-Base"
    print(f"Input kosong, pakai default: {input_link}")

# 1) Buat objek QR
qr = qrcode.QRCode(version=1, box_size=1, border=2)

# 2) Masukkan data
qr.add_data(input_link)

# 3) Bangun matriks QR
qr.make(fit=True)

# 4) Cetak sebagai ASCII
qr.print_ascii(invert=True)