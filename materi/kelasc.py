# print("materi 6c")
# print("------------------")

# daftar_belanja = [
# "pisang kembung",# index 0
# "es teh desa",# index 1
# "gabin",#index 2
# "gorengan",#index 4
# ]

# # ===== PENJELASAN ===== #
# print("tas belanja:",daftar_belanja)
# # akses item dengan index
# print(daftar_belanja [1])
# # append () untuk item ke akhir lits
# daftar_belanja.append("tahu golek")
# # insert untuk menambah item ke index tertentu
# daftar_belanja.insert(1, "batagor")
# # remove() untuk menghapus item 
# daftar_belanja.remove("es teh desa")
# print("TAS BELANJA SEKARANG :", daftar_belanja) 

# # menggabungkan list + 
# jajanan_ishaq = ["olive chiken","makaroni","keripik singkong"]
# jajanan_bilal = ["nasi padang","indomie","gorengan"]
# titip_belanjaan = jajanan_bilal + jajanan_ishaq
# print("titipan belanja:",titip_belanjaan)
# # mengadakan item lits dengan *

# # lits bercabang (lits multi dimensi)
# daftar_menu = [
#  ["kopi","susu jahe","teh"] # baris 0
#  ["jus apel","jus jeruk","jus jeruk","jus mangga"] #baris 1 
#  ["es teler","es dawet"] #baris 2
# ]

# print("daftar_menu  :",daftar_menu)
# print(daftar_menu[1][2])
# print('------------')

# # tuple -> () -> berurutan,tidak berubah,boleh duplikat
# ttl = ("purworejo",21,"januari", 2009)
# print("TTL", ttl)
# print("bulan lahir ujang:",ttl[2])
# # unpacking variable (mengextak tuple ke variable baru sesuai urutan )
# tempat_lahir,tgl_lahir,bulan_lahir = ttl
# print("thn lahir")



# buah_lits = ["jeruk","durin","blewah","nanas",]
# print(buah_lits)

# for item in buah_lits:
#  print(item)



# # operasi pada lits 
# # 1. menambah data ke dalam lits
# # append 







print("kelas ke tujuh pekan ini python data structure")
print("=======================")
#set -> { } ->tidak berurutan,berubah,tidak duplikat
game_ridho = {"gensin","mlbb","delta force","free fire"}
game_imam = {"valorant","point blank","mlbb","free fire"}
# fungsi add()untuk menambahkan item ke set 
game_imam.add ("valorant") #jika ada akan di skip
game_imam.add("mlbb")
# remove .() -> untuk menghapus item dari set
game_ridho.remove("mlbb")
# len() -> menghitung jumlah item 
print("ridho ada ",len(game_ridho),"==>",game_ridho)
print("imam ada ",len(game_imam),"==>",game_imam)
# menggabungkan 2 set berbeda
game_gabungan = game_imam.union(game_ridho)
total_game = len(game_gabungan)
print("game_gabungan", total_game ,"=>", game_gabungan)
# .intersection()mencari item yg kembar dari 2 set yg berbeda 
# .diference() mencari item yg berbeda dari 2 set 
game_kembar = game_ridho.intersection(game_imam)
game_beda = game_ridho.difference(game_imam)
print("game kembar:", game_kembar)
print("game_beda:", game_beda)

# dict dictianory -> {key:value} / {kunci:isinya}
# berurutan berdasarkan key, berubah, key tidak duplikat

daftar_anime = {
    "jujutsu_kaisen": "gojo satoru",
    "one_puch_man": "saitama",
    "hunter_x_hunter": "kilua",
    "waifu": {
        "demon slayer":"mitsuri",
        "spy_x_family":"anya",
        "naruto": "tsunade,"
    }
}
print("daftar anime:",daftar_anime)
print("MC ONE PUCH MAN",daftar_anime["one_puch_man"])
print("waifu loli: ",daftar_anime["waifu"]["spy_x_family"])
#  mengubah item value berdasarkan key
daftar_anime["one_puch_man"] = "genos"
daftar_anime["waifu"]["demon_slayer"] = "nezuko"
print("waifu loli bisa gede":,daftar_anime["one_puch_man"])
print("waifu loli: ",daftar_anime["waifu"]["spy_x_family"])
#menambah item value berdasarkan key  
daftar_anime = ["wind_breaker"]