# Vector merupakan tipe data sederhana di R yang menyimpan 
# deretan nilai (lebih dari satu nilai) dengan tipe data sama 
# untuk setiap elemennya. Maksudnya, jika tipe datanya berupa 
# teks maka seluruh elemennya harus bertipe teks. Demikian juga 
# jika tipenya angka maka seluruh elemennya berisi angka semua.

# Vector didefinisikan dengan nama function yang memilki satu huruf 
# saja: c, yang telah kamu pelajari dan praktikkan sebelumnya. 
# Sebagai contoh untuk membuat vector yang isinya angka dengan 
# nilai 2, 5, dan 7, maka perintahnya adalah c(2, 5, 7).

# Ini adalah contoh vector untuk angka numerik dengan 3 data c(4, 5, 6)

c(4, 5, 6)

# Variable bernama angka dengan input berupa vector
angka <- c(4, 5, 6)

# Tampilkan isi variable angka dengan fungsi print
print(angka)

# Deretan Nilai dengan Operator ":" (Titik Dua)
angka1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(angka1)

angka2 <- c(1:10)
print(angka2)

# Vector dengan Isi Teks
# Variable nama_mahasiswa dengan input character
nama_mahasiswa <- c("Amira", "Budi", "Charlie")

print(nama_mahasiswa)

# Selain dengan angka, indeks pada vector juga dapat dilengkapi dengan 
# nama untuk tiap elemennya dengan menggunakan 
# format penulisan name=value. Penggunaan format 
# name=value disebut dengan named vector.

#Membuat named vector dengan nama nilai
nilai <- c(statistik = 89, fisika = 95, ilmukomunikasi = 100)

#Menampilkan isi variable nilai
print(nilai)

#Menampilkan isi dengan nama fisika
print(nilai["fisika"])

#Buat variable profil sesuai permintaan soal
profil <- c(nama = "Budi", tempat_tinggal = "Jakarta", tingkat_pendidikan = "S1")

#Tampilkan variable profil
print(profil)


# Index dan Accessor pada Vector
# Buat vector variable bernama angka yang isinya 20 s/d 30
angka <- c(20:30)
print(angka)

# Tampilkan isi variable angka pada posisi ke 3
print(angka[3])


# Tampilkan isi variable angka pada posisi ke 5 gunakan kurung siku ganda
print(angka[[5]])


# Tampilkan isi variable angka pada posisi ke 4 s/d 6
print(angka[4:6])

# Buat vector teks dengan nama kode_prodi yang diisi sesuai petunjuk soal
kode_prodi <- c("DKV","ILKOM","ICT")

# Tampilkan isi indeks ketiga dari kode_prodi
print(kode_prodi[3])


