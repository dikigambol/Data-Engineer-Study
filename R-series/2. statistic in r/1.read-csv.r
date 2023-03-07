#Membaca dataset dengan read.csv dan dimasukkan ke variable data_intro
data_intro <- read.csv("https://storage.googleapis.com/dqlab-dataset/data_intro.csv", sep=";")
data_intro

#Membaca dataset dengan read.csv dan dimasukkan ke variable data_intro
str(data_intro)

## mengubah data menjadi karakter karena tidak dilakukan analisis statistik pada variabel ID Pelanggan dan nama
data_intro$ID.Pelanggan<-as.character(data_intro$ID.Pelanggan)
data_intro$Nama<-as.character(data_intro$Nama)
## melihat apakah sudah berhasil dalam mengubah variabel tersebut
str(data_intro$ID.Pelanggan)
str(data_intro$Nama)

## Mengubah data menjadi factor untuk membedakan data kualitatif dengan menggunakan functon as.factor
data_intro$Jenis.Kelamin <- as.factor(data_intro$Jenis.Kelamin)

data_intro$Produk <- as.factor(data_intro$Produk)

data_intro$Tingkat.Kepuasan <- as.factor(data_intro$Tingkat.Kepuasan)

## Melihat apakah sudah berhasil dalam mengubah variabel tersebut dengan menggunakan function str
str(data_intro$Jenis.Kelamin)
str(data_intro$Produk)
str(data_intro$Tingkat.Kepuasan)

# Modus merupakan nilai yang menunjukan nilai yang sering muncul. 
# Modus digunakan untuk data bertipe nominal dan ordinal.
library(pracma)
## carilah modus untuk kolom Produk pada variable data_intro
Mode(data_intro$Produk)
## carilah modus untuk kolom Tingkat.Kepuasan pada variable data_intro
Mode(data_intro$Tingkat.Kepuasan)