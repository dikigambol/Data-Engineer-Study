# Di dalamnya aku diminta untuk meneliti popularitas antara buah salak dan
# buah jeruk berdasarkan judul artikel yang muncul di majalah Buah Sehat.
# Aku mulai menyiapkan susunan kodeku:

judul_artikel = [
    "Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium",
    "Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat",
    "Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang",
    "Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi",
    "Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes",
    "Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
    "Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik",
    "Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
    "Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak",
    "Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
jumlah_artikel_jeruk = 0
jumlah_artikel_salak = 0
for judul in judul_artikel:
    if judul.count('Jeruk') > 0:
        jumlah_artikel_jeruk += 1
    if judul.count('Salak') > 0:
        jumlah_artikel_salak += 1
print(jumlah_artikel_jeruk)
print(jumlah_artikel_salak)

# Setelah selesai menghitung jumlah kemunculan kata, aku mencoba 
# berpikir dari sudut pandang si 
# pemilik majalah. Kalau aku jadi mereka, 
# tentunya aku juga ingin tahu apakah kata yang muncul 
# itu bermuatan positif atau tidak. Nah ini!

# Dengan cepat, aku mendeklarasikan daftar bernama kata_positif yang 
# berisi nuansa kata positif untuk menghitung jumlah kemunculan kata_positif 
# bagi tiap artikel jeruk dan salak, seperti ini:

kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kata_positif_jeruk = 0
kata_positif_salak = 0
for judul in judul_artikel:
    for kata in kata_positif:
        if judul.count('Jeruk') > 0 and judul.count(kata) > 0:
            kata_positif_jeruk += 1
        if judul.count("Salak") > 0 and judul.count(kata) > 0:
            kata_positif_salak += 1
print(kata_positif_jeruk)
print(kata_positif_salak)
