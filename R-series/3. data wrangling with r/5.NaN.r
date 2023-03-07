#Hitung kalkulasi 0 dibagi dengan 0
0/0

#Hitung logaritma dari angka -1000
log(-1000)

#Buat variable contoh.nan
contoh.nan <- 0/0

#Periksa dengan function is.nan
is.nan(contoh.nan)

# Seluruh nilai NaN dapat diperiksa dengan fungsi is.na, sehingga hasilnya mengembalikan TRUE.
# Semua nilai NA tidak akan mengembalikan nilai TRUE jika diperiksa dengan fungsi is.nan
is.na(NaN)
is.nan(NA)

#Masukkan code di bawah ini sesuai permintaan soal
isi.vector <- c(1,2,NA,4,5,NaN,6)
sum(is.na(isi.vector) == TRUE)
