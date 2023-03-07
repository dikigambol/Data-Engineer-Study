# Hubungannya diantara keduanya dapat dilihat dengan membandingkan 
# rata-rata pada setiap kategori. Jika nilai rata-ratanya berbeda 
# maka kedua variabel memiliki hubungan. Pada hubungan antara variabel 
# kategorik dan numerik tidak bisa diketahui seberapa kuat hubungan 
# diantara keduanya dan bagimana pengaruhnya (positif atau negatif).

# Untuk mengetahui ada hubungan atau tidaknya menggunakan 
# uji statistik t-test, dengan hipotesis sebagai berikut

# Hipotesis Nihil: tidak ada hubungan antara kedua variabel
# Hipotesis Alternatif: ada hubungan antara kedua variabel

data_intro <- read.csv("https://storage.googleapis.com/dqlab-dataset/data_intro.csv", sep=";")

## carilah boxplot antara variabel jenis kelamin dengan total belanja
boxplot(Total~Jenis.Kelamin, data = data_intro)

## analisis bagaimana hubungan jenis kelamin dengan total belanja mengunakan uji statistik t-test
t.test(Total~Jenis.Kelamin, data = data_intro)
