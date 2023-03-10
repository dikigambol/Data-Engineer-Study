# Transform adalah ketika mengubah dataset yang ada menjadi entitas baru, 
# dapat dilakukan dengan:

# konversi dari satu data type ke data type yang lain,
# transpose dataframe, atau yang lainnya.
# Hal yang biasa dilakukan pertama kali setelah data dibaca adalah mengecek 
# tipe data di setiap kolomnya apakah sesuai dengan representasinya. 
# Untuk itu dapat menggunakan atribut .dtypes pada dataframe yang telah kita baca tadi,

# [nama_dataframe].dtypes 
 
# Untuk konversi tipe data, secara default system akan mendeteksi data yang tidak bisa 
# di render as date type or numeric type sebagai object yang basically string. 
# bisa di render oleh system ini karena berbagai hal, mungkin karena formatnya asing 
# dan tidak dikenali oleh python secara umum (misal: date type data → '2019Jan01').

# Data contoh tersebut tidak bisa di render karena bulannya Jan tidak bisa di translate 
# menjadi in form of number (00-12) dan tidak ada ‘-’ di antara tahun, bulan dan harinya. 
# Jika seluruh data pada kolom di order_date sudah tertulis dalam bentuk 'YYYY-MM-DD' 
# maka ketika dibaca, kolom order_date sudah langsung dinyatakan bertipe data datetime.

# Untuk merubah kolom date_order yang sebelumnya bertipe object menjadi kolom bertipe datetime, 
# cara pertama yang dapat dilakukan adalah menggunakan:

# pd.to_datetime(argumen) 
# dengan argumen adalah isi kolom dari dataframe yang akan dirubah tipe datanya, 
# misal dalam format umum.
# nama_dataframe["nama_kolom"]

# Sehingga lengkapnya dapat ditulis sebagai:
# nama_dataframe["nama_kolom"] = pd.to_datetime(nama_dataframe["nama_kolom"]) 

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom order_date menjadi datetime
df["order_date"] = pd.to_datetime(df["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)

# Ubah tipe data kolom quantity menjadi tipe data numerik float
df["quantity"] = pd.to_numeric(df["quantity"], downcast="float")
# Ubah tipe data kolom city menjadi tipe data category
df["city"] = df["city"].astype("category")
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)

# Method .apply() digunakan untuk menerapkan suatu fungsi python 
# (yang dibuat dengan def atau anonymous dengan lambda) pada 
# dataframe/series atau hanya kolom tertentu dari dataframe. 
# Cetak 5 baris teratas kolom brand
print("Kolom brand awal:\n", df["brand"].head())

# Gunakan method apply untuk merubah isi kolom menjadi lower case
df["brand"] = df["brand"].apply(lambda x: x.lower())

# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah apply:\n", df["brand"].head())

# Gunakan method map untuk mengambil kode brand yaitu karakter terakhirnya
df["brand"] = df["brand"].map(lambda x: x[-1])

# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah map:\n", df["brand"].head())

# menggunakan method .applymap pada dataframe.
import numpy as np
import pandas as pd
# number generator, set angka seed menjadi suatu angka, bisa semua angka, supaya hasil random nya selalu sama ketika kita run
np.random.seed(1234)
# create dataframe 3 baris dan 4 kolom dengan angka random
df_tr = pd.DataFrame(np.random.rand(3,4)) 
# Cetak dataframe
print("Dataframe:\n", df_tr)
# Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x
df_tr1 = df_tr.applymap(lambda x:  x**2 + 3*x + 2) 
print("\nDataframe - cara 1:\n", df_tr1)
# Cara 2 dengan define function 
def qudratic_fun(x):
	return  x**2 + 3*x + 2
df_tr2 = df_tr.applymap(qudratic_fun)
print("\nDataframe - cara 2:\n", df_tr2)