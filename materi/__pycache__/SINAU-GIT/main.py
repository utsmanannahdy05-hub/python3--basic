import json

print("MATERI 12  - JSON")
print("----------------------")
file_json_path = r"C:\Users\User\Documents\Python\__pycache__\SINAU-GIT\rukun_islam.json"
with open(file_json_path, "r") as file_json:
  data_json = json.load(file_json)
  print(f"judul file: {data_json['judul']}")
  print(f"jumlah ruku islam: {data_json['judul']}")
  print(f"daftar rukun islam")
  for item_rukun in data_json['rukun']:
    print(item_rukun)
  print("-" * 30) # buat garis panjang 
  print("daftar 3 surat di al-qur'an")
  print("-" * 30)
  # tampilkan surat sebagai tabel garis sedehana
  # keys: nomor, nama, jumlah_ayat, tempat_turun
  print("|NO| NAMA | JUMLAH AYAT | TEMPAT TURUN |")
  print("-" * 45)
for surah in data_json['surah']:
  print(f"| {surah['nomor']} | {surah['nama']} | {surah['jumlah_ayat']} | {surah['tempat_turun']}| ")
