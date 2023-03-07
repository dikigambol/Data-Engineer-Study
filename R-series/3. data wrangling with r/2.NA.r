#Ketik nilai NA
NA

#Tampilkan type dari NA dengan function typeof
typeof(NA)

#Buat variable x yang diisi dengan nilai NA
x <- NA

#Pengecekan variable x dengan nilai NA menggunakan operator ==
x == NA

#Pengecekan variable x dengan nilai NA menggunakan function is.na
is.na(x)

# Variasi NA dan is.na
# NA_integer_ untuk representasi tipe data "integer"
# NA_real_ untuk representasi tipe data "double"
# NA_complex_ untuk representasi tipe data "complex"
# NA_character_ untuk representasi tipe data "character"
typeof(NA_integer_)
typeof(NA_real_)
typeof(NA_complex_)
typeof(NA_character_)
is.na(NA_integer_)
is.na(NA_real_)
is.na(NA_complex_)
is.na(NA_character_)

# Coercion pada Vector yang mengandung NA
#Membuat vector bernama isi.vector dengan isi bilangan, dimana salah satunya memiliki missing value
isi.vector <- c(1,2,3,NA,3,1)

#Mengecek keseluruhan tipe data dengan perulangan lapply dan typeof
lapply(isi.vector, typeof)

#Menggunakan is.na untuk mengecek keberadaan missing value dari tiap elemen pada vector 
is.na(isi.vector)
