#Membaca dataset dengan read.csv dan dimasukkan ke variable penduduk.dki
penduduk.dki <- read.csv("https://storage.googleapis.com/dqlab-dataset/dkikepadatankelurahan2013.csv", sep=",")

penduduk.dki
str(penduduk.dki)
summary(penduduk.dki)

# Menggunakan argumen check.names = FALSE
#Membaca dataset dengan read.csv dan dimasukkan ke variable penduduk.dki
penduduk.dki <- read.csv("https://storage.googleapis.com/dqlab-dataset/dkikepadatankelurahan2013.csv", sep=",", check.names = FALSE)
str(penduduk.dki)
# Beberapa penjelasan terkait perbedaan hasil di atas dengan hasil pada praktek sebelumnya:
# Nama spasi tidak dijadikan titik.
# Nama yang kosong tidak diberi tanda X, ini akan menyulitkan ketika kita ingin mereferensikan 
# nama kolom kosong tersebut.
