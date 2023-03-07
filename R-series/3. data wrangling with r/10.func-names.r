#Membaca dataset csv
penduduk.dki.csv <-read.csv("https://storage.googleapis.com/dqlab-dataset/dkikepadatankelurahan2013.csv", sep=",")

#Menggunakan names untuk variable penduduk.dki.csv
# names(penduduk.dki.csv)

# Merubah Satu Nama Kolom
names(penduduk.dki.csv)[1] <- "PERIODE"
names(penduduk.dki.csv)[2] <- "PROPINSI"
names(penduduk.dki.csv)

# Mengubah Sejumlah Nama Kolom
names(penduduk.dki.csv)[c(1:2)] <- c("PERIODE", "PROPINSI")
names(penduduk.dki.csv)

#Membuang kolom X, X.1, X.2 s/d X.11
penduduk.dki.csv <- penduduk.dki.csv[,!names(penduduk.dki.csv) %in% c("X", "X.1","X.2","X.3","X.4","X.5","X.6","X.7","X.8","X.9","X.10", "X.11")]
names(penduduk.dki.csv)

# Merubah Tipe Kolom menjadi Factor
penduduk.dki.xlsx$NAMA.PROVINSI <- as.factor(penduduk.dki.xlsx$NAMA.PROVINSI)
str(penduduk.dki.xlsx)

# Mengambil Kolom Laki.Laki / Perempuan dengan grep
#Tampilkan nama-nama kolom yang mengandung kata "perempuan".
pola_nama_perempuan <- grep(pattern="perempuan", x = names(penduduk.dki.xlsx), ignore.case=TRUE)
names(penduduk.dki.xlsx[pola_nama_perempuan])

#Tampilkan nama-nama kolom yang mengandung kata "laki-laki"
pola_nama_laki_laki <- grep(pattern="laki-laki", x = names(penduduk.dki.xlsx), ignore.case=TRUE)
names(penduduk.dki.xlsx[pola_nama_laki_laki])

# Menambahkan kolom Penjumlahan
#Tampilkan nama-nama kolom yang mengandung kata "perempuan".
pola_nama_perempuan <- grep(pattern="perempuan", x = names(penduduk.dki.xlsx), ignore.case=TRUE)
penduduk.dki.xlsx$PEREMPUAN35TAHUNKEATAS <- rowSums(penduduk.dki.xlsx[pola_nama_perempuan])
