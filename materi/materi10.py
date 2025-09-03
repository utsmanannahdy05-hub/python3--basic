import csv

print("==== MATERI 10 C ==== ")
print("--------------------------")
# file extension/ekstensi yg membedakan
# jenis suatu file, lihat di akhir nama file
# .py (python), doc (document) txt (text file)
# cari posisi detail file yang mau di buka 
file_path = r"C:\Users\User\Documents\Python\pesan.txt"
# buka file target dengan mode tertentu 
file_pesan = open(file_path, "r")  # r = read only
# fungsi read() membaca semua isi file 
baca_pesan = file_pesan.read()
print(f"isi pesanya: {baca_pesan}")
# tutup file
file_pesan.close()

print("----- OPEN CSV -----")
csv_alamat_path = r"C:\Users\User\Documents\Python\alamat.csv"
with open(csv_alamat_path, "r") as file_alamat:
    baca_alamat = csv.reader(file_alamat)
    lits_alamat = list(baca_alamat)  # UBAH CSV OBJECT KE LIST
    print(f"daftar alamat: {lits_alamat}")

print("---------------ADD ROW CSV------------------")
alamat_khalid = [9, "khalid sukabumi"]
print(f"alamat baru: {alamat_khalid}")

# Buka file CSV dengan mode 'a' untuk menambahkan baris baru
with open(csv_alamat_path, "a", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat)
    tulis_alamat.writerow(alamat_khalid)

print("selesai menambah baris baru ke csv")







print("-----update row CSV -----")
# open -> baca file -> ambil datanya , jadikan lits 
# ekstrak data dengan for loop (edit/hapus)
# buat ulang semua baris file csv dgn mode 'w'
csv_alamat_path = r"C:\Users\User\Documents\Python\alamat.csv"
# buat lits kosong untuk menampung data dari csv 
data_alamat = []
with open(csv_alamat_path, "r") as file_alamat:
  baca_alamat = csv.reader(file_alamat)
  for item_alamat in baca_alamat:
    data_alamat.append(item_alamat)


# ekstak lits data almat dgn for loop 
for item in data_alamat:
  # cek kolom nama (index 1)
  print(item)
  if item[1] == 'surya':

   print("data surya di temukan , ganti alamatnya ...")
   item[2] = "bandung" # index 2 (kolom alamat))
else:
    print("skip... bukan surya ")

 

 # ubah data alamat (index 2 ) 
print(f"lits data alamat: {data_alamat}")
# for item in data_alamat:
#   print(item)


# hapus data  alamat index 
del data_alamat[1]
# ubah data alamat (index 2)
print(f"lits data alamat: {data_alamat}")
# buka file dengan mode "w" (write) -> menulis ulang semua 
# beserta newline/baris barunya kosong atau ""
with open(csv_alamat_path, "w", newline="") as file_alamat:
   tulis_alamat = csv.writer(file_alamat) # targetkan file 
   tulis_alamat.writerows(data_alamat) # tambah garis baru
print("--> selesai membuat ulang data csv")


