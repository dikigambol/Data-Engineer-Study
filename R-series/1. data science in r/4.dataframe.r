# Data frame merupakan jenis struktur data yang dirancang 
# untuk representasi tabel, yang terdiri dari atas kolom 
# dengan tiap kolom berisi list ataupun vector dengan 
# jumlah data yang sama.

#Membuat dua variable vector
fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)

#Membuat data frame dari kedua vector di atas
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa)

#Melihat isi data frame
info_mahasiswa

#Buat vector baru sebagai representasi akreditasi
akreditasi <- c("A","A","B","A","A")

#Buat data frame dari ketiga vector di atas
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa, akreditasi)

info_mahasiswa

#Membuat tiga variable vector
fakultas <- c("Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain")
jumlah_mahasiswa <- c(260, 28, 284, 465, 735)
akreditasi <- c("A","A","B","A","A")

#Membuat data frame dari kedua vector di atas
info_mahasiswa <- data.frame(fakultas, jumlah_mahasiswa, akreditasi)

#Menampilkan kolom jumlah_mahasiswa
info_mahasiswa$jumlah_mahasiswa

#Menampilkan kolom fakultas
info_mahasiswa$fakultas
