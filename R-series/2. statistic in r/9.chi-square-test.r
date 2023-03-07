# Hubungannya diantara keduanya dapat dilihat dengan menggunakan 
# tabulasi silang dan dapat juga dilihat kecenderungannya. 
# Pada hubungan antara variabel kategorik dan kategorik tersebut 
# tidak bisa diketahui seberapa kuat hubungan diantara keduanya 
# dan bagimana pengaruhnya (positif atau negatif). 
# Untuk mengetahui ada hubungan atau tidaknya menggunakan 
# uji statistik chi-square test, dengan hipotesis sebagai berikut:

# Hipotesis Nihil: tidak ada hubungan antara kedua variabel
# Hipotesis Alternatif : ada hubungan antara kedua variabel

data_intro <- read.csv("https://storage.googleapis.com/dqlab-dataset/data_intro.csv", sep=";")
## Carilah tabulasi silang antara kolom jenis produk (Produk) 
# dan tingkat kepuasan (Tingkat.Kepuasan) dari variable data_intro
a <- table(data_intro$Produk, data_intro$Tingkat.Kepuasan)

## Analisis bagaimana hubungan jenis produk dengan tingkat kepuasan mengunakan uji korelasi
chisq.test(a)

# Perintah table untuk melihat tabulasi antar variabel kategorik, 
# sedangkan perintah chisq.test digunakan untuk melihat hubungan secara statistik.

# Dengan hipotesis sebagai berikut :

# Ho : tidak ada hubungan antara jenis produk dan tingkat kepuasan.
# Ha : terdapat hubungan antara jenis produk dan tingkat kepuasan