# Statistik deskriptif atau summary dalam Python - Pandas, 
# dapat diperoleh dengan menggunakan fungsi describe(), yaitu:
# print([nama_df].describe())

# Function describe dapat memberikan informasi mengenai nilai rataan, 
# standar deviasi dan IQR (interquartile range).

# Ketentuan umum:
# - Secara umum function describe() akan secara otomatis mengabaikan kolom category 
# dan hanya memberikan summary statistik untuk kolom berjenis numerik.
# - Kita perlu menambahkan argument bernama include = "all" untuk mendapatkan 
# summary statistik atau statistik deskriptif dari kolom numerik dan karakter.

# yaitu :
# print([nama_df].describe(include="all"))

# Jika ingin mendapatkan summary statistik dari kolom yang tidak bernilai 
# angka, maka aku dapat menambahkan command include=["object"] pada syntax 
# describe().
# print(nilai_skor_df.describe(include=["object"]))

# Function describe() dengan include="all" akan memberikan summary statistik 
# dari semua kolom. Contoh penggunaannya:
# print(nilai_skor_df.describe(include=["all"]))

# Selanjutnya, untuk mencari rataan dari suatu data dari dataframe. 
# Aku dapat menggunakan syntax mean, median, dan mode dari Pandas.
# print([nama_df].loc[:, "nama_kolom"].mean())
# print([nama_df].loc[:, "nama_kolom"].median())
# print([nama_df].loc[:, "nama_kolom"].mode())

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())