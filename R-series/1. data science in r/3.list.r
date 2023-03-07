# List merupakan jenis data di R yang mirip dengan vector. 
# Perbedaannya adalah list dapat menyimpan lebih dari satu 
# data dasar di setiap elemennya. Untuk memasukkan isi 
# ke dalam struktur data ini kita gunakan function list.

# List disimpan dalam variable dengan nama list_random
list_random <- list(2, "Budi", 4)

# Menampilkan isi list
list_random 

# List disimpan dalam variable dengan nama dati2
dati2 <- list(nama = "Denpasar", propinsi = "Bali")

# Menampilkan isi list dati2
dati2 

# Buat variable kota sesuai permintaan soal
kota <- list(nama_kota = "Makassar", propinsi = "Sulawesi Selatan", luas_km2 = 199.3)

# Tampilkan isi variable list kota
kota

# Membentuk list dengan 2 angka dan 1 character
list_saya <- list(2, "Budi", 4)

# Menampilkan index kedua dengan aksesor kurung siku tunggal 
list_saya[2]

# Menampilkan index kedua dengan aksesor kurung siku ganda
list_saya[[2]]

# Menampilkan index kedua s/d ketiga
list_saya[2:3]

list_satu <- list(1, "Online", TRUE)

list_satu[1]
