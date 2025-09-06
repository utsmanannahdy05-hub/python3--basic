print("========== prifil digital=========")
nama = input("Masukkan Nama Lengkap: ")
umur = int(input("Masukkan Umur: "))
tahun_lahir = 2025 - umur
kelas = input("Masukkan Kelas: ")
cita_cita = input("Masukkan Cita-cita: ")
hobi = input("Masukkan Hobi: ")
waktu_belajar = input("Kamu lebih suka belajar pagi atau malam? ")

print("\n======= TIPE DIGITAL ========")
print("Pilih tipe yang paling menggambarkan kamu:")
print("1. Wibu")
print("2. Gamer")
print("3. K-Popers")
print("4. Anak Konten")
print("5. Anak Nongki")

pilihan = input("Masukkan nomor pilihan kamu (1-5): ")
print()

if pilihan == '1':
    waifu = input("Siapa waifu kamu? ")
    komentar = f"Kamu pilih waifu {waifu}? Wah, beneran wibu sejati nih! 😅"
    tipe = "Wibu"
elif pilihan == '2':
    game = input("Game favorit kamu apa? ")
    komentar = f"Wih, main {game} sambil ngoding? GG banget kamu! 🎮🔥"
    tipe = "Gamer"
elif pilihan == '3':
    bias = input("Siapa bias kamu di dunia K-Pop? ")
    komentar = f"Stan {bias}? Wah, pasti kamarnya penuh poster ya 😁"
    tipe = "K-Popers"
elif pilihan == '4':
    platform = input("Platform favorit kamu apa? TikTok? YouTube? ")
    komentar = f"Suka nonton atau bikin konten di {platform}? Kreatif banget! 🎥"
    tipe = "Anak Konten"
elif pilihan == '5':
    tempat_nongki = input("Biasanya nongkrong di mana nih? ")
    komentar = f"Nongkrong di {tempat_nongki}? Sambil ngopi-ngopi santai ya ☕"
    tipe = "Anak Nongki"
else:
    komentar = "Pilihan tidak valid. Kamu harus pilih antara 1 sampai 5 ya!"
    tipe = "Tidak Diketahui"

print("\n===== RANGKUMAN PROFIL DIGITAL =====")
print("Nama              :", nama)
print("Tahun Lahir       :", tahun_lahir)
print("Kelas             :", kelas)
print("Cita-cita         :", cita_cita)
print("Hobi              :", hobi)
print("Waktu Belajar     :", waktu_belajar)

print("\n=== TIPE DIGITAL KAMU ===")
print("Tipe Digital      :", tipe)
print("Komentar          :", komentar)

# FUN CHECK
print("\n=== FUN CHECK ===")
teman_bau = input("Eh, teman di sebelah kamu bau nggak? (Ya/Tidak): ").strip().lower()

if teman_bau == 'ya':
    print("Aduh... Kasih pewangi darurat dong! Bisa jadi masalah global nih 😁")
elif teman_bau == 'tidak':
    print("Syukurlah! Teman yang wangi bikin belajar makin semangat ")


print("=============== SELESAI! ===============")
