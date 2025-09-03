Jadwal_Piket = [
"bilal",
"tegar",
"harun",
"gozzy"]
print("Jadwal Piket harian")
  
for jadwal in Jadwal_Piket :
    print("-",jadwal)

print("===================")

daftar_rukun_islam = ("syahadat","shalat","zakat","puasa","haji bagi yg mampu")
print(" rukun islam ada 5 (lima)",daftar_rukun_islam)   

for index in range(len(daftar_rukun_islam)):
   print(f"{index + 1}. {daftar_rukun_islam[index]}")

print("=====================")

kitab_pelajaran = {'Kitab Tajwid', 'Kitab Fiqh', 'Kitab Aqidah','kitab aby','kitab nahwu'}
print("kitab kitab yg saya pelajari =")
for kitab in kitab_pelajaran:
    print("-",kitab)

print("=======================")

biodata = {'nama': 'utsman annahdyy', 'kelas': '10 SMA', 'hafalan juz': 30 }

for key, value in biodata.items():
    print(f"{key} : {value}")         


def tambah(angkapertama, angkakedua):
    return angkapertama + angkakedua   




