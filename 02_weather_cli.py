"""
=====================================================
PROYEK 2: TERMINAL LIVE WEATHER CLI (wttr.in)
RIT Academy - Pemrograman Dasar Python
=====================================================
Petunjuk:
1. Pastikan sudah menjalankan: pip install -r requirements.txt
2. Jalankan skrip ini dengan perintah: python 02_weather_cli.py
"""
import requests

nama_kota = input("Masukan nama kota:")
url = f"https://wttr.in/{nama_kota}?lang=id"

headers = {
    "User-Agent": "curl/7.68.0"  # Mengidentifikasi diri sebagai terminal client
}
response = requests.get(url, headers=headers, timeout=10)
print(response.text)