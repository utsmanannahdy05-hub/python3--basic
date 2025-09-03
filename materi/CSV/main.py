import csv

# baca semua data dari csv

with open("keuangan.csv", newline="", encoding="utf-8") as f:
   reader = csv.DictReader(f)
   data = list(reader)
print(data)

# 1. tampilkan semua data 
print("semua data: ")
for row in data:
    print(f"{row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} ")

# 2. hitung total pengeluaran 

total = sum(int(row['Jumlah']) for row in data)
print(f"total pengeluaran: RP.{total}")