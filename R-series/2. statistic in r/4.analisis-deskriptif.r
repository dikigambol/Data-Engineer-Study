data_intro <- read.csv("https://storage.googleapis.com/dqlab-dataset/data_intro.csv", sep=";")

## carilah summary data dari data_intro
summary(data_intro)
# Function summary akan menampilkan kesimpulan pada variabel masing-masing. 
# Untuk variabel bertipe character akan menampilkan panjang datanya. 
# Variabel bertipe factor akan menampilkan jumlah data pada masing-masing kelas. 
# Sedangkan untuk variabel bertipe numerik akan memunculkan nilai minimum, 
# Q1,Q2 (median), Q3, mean, dan maximum.

# Pengertian dari masing-masing istilah itu adalah sebagai berikut :

# 1. Minimum adalah nilai observasi terkecil.
# 2. Kuartil pertama (Q1), yang memotong 25 % dari data terendah.
# 3. Median (Q2) atau nilai pertengahan.
# 4. Kuartil ketiga (Q3), yang memotong 25 % dari data tertinggi.
# 5. Maksimum adalah nilai observasi terbesar.

# plot digunakan untuk variabel bertipe Factor - function ini menghasilkan grafik Bar Plot.
# hist untuk variabel bertipe numerik seperti int - function ini menghasilkan grafik Histogram.
# Tujuan dari plot dan hist adalah untuk mengetahui sebaran data.
## Carilah sebaran data kolom Jenis.Kelamin dari variable data_intro
data_intro$Jenis.Kelamin <- as.factor(data_intro$Jenis.Kelamin)
plot(data_intro$Jenis.Kelamin)

## Carilah sebaran data dari Pendapatan dari variable data_intro
hist(data_intro$Pendapatan)
