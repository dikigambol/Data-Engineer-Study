library(pracma)

#Membaca dataset dengan read.csv dan dimasukkan ke variable data_intro
data_intro <- read.csv("https://storage.googleapis.com/dqlab-dataset/data_intro.csv", sep=";")
data_intro

# Modus merupakan nilai yang menunjukan nilai yang sering muncul. 
# Modus digunakan untuk data bertipe nominal dan ordinal.
## carilah modus untuk kolom Produk pada variable data_intro
Mode(data_intro$Produk)
## carilah modus untuk kolom Tingkat.Kepuasan pada variable data_intro
Mode(data_intro$Tingkat.Kepuasan)

# Median merupakan nilai tengah dari suatu kumpulan data. 
# median digunakan untuk data bertipe interval dan rasio.
## carilah median untuk kolom Pendapatan dari variable data_intro
median(data_intro$Pendapatan)

## carilah median untuk  kolom Harga dari variable data_intro
median(data_intro$Harga)

## carilah median untuk kolom Jumlah dari variable data_intro
median(data_intro$Jumlah)

## carilah median untuk  kolom Total dari variable data_intro
median(data_intro$Total)

# Rata-rata merupakan nilai yang menunjukan nilai rata-rata aritmatik. 
# Rata-rata/mean digunakan untuk data bertipe interval dan rasio.
## carilah mean untuk kolom Pendapatan pada variable data_intro
mean(data_intro$Pendapatan)
## carilah mean untuk kolom Harga pada variable data_intro
mean(data_intro$Harga)
## carilah mean untuk kolom Jumlah pada variable data_intro
mean(data_intro$Jumlah)
## carilah mean untuk kolom Total pada variable data_intro
mean(data_intro$Total)

# Range adalah selisih antara nilai terbesar dan nilai terendah. 
# Untuk menampilkan range dari data dapat menggunakan syntax sebagai berikut:
## carilah range untuk kolom Pendapatan pada variable data_intro
max(data_intro$Pendapatan) - min((data_intro$Pendapatan))

# Varians merupakan simpangan kuadrat data dari nilai rata-ratanya.
## Carilah varians untuk kolom Pendapatan dari variable data_intro
var(data_intro$Pendapatan)

# Simpangan baku adalah simpangan data dari nilai rata-ratanya, simpangan baku nama 
# lainnya adalah standard deviasi. Standard deviasi dapat digunakan 
# untuk melihat keakuratan dari hasil estimasi, semakin kecil standard 
# deviasi semakin akurat hasil estimasi.
## Carilah simpangan baku untuk kolom Pendapatan dari variable data_intro
sd(data_intro$Pendapatan)