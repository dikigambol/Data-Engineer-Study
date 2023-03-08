# Mengenal dan Membuat Distribusi Data dengan Histogram

# Histogram merupakan salah satu cara untuk mengidentifikasi sebaran distribusi dari data. 
# adalah grafik yang berisi ringkasan dari sebaran (dispersi atau variasi) suatu data. 
# Pada histogram, tidak ada jarak antar batang/bar dari grafik. 
# Hal ini dikarenakan bahwa titik data kelas bisa muncul dimana saja di daerah cakupan grafik. 
# Sedangkan ketinggian bar sesuai dengan frekuensi atau frekuensi relatif jumlah data di kelas. 
# Semakin tinggi bar, semakin tinggi frekuensi data. 
# Semakin rendah bar, semakin rendah frekuensi data.

# syntax : 
# nama_df[['nama_kolom']].hist(bins=jumlah_bin,
#                              by=nama_kolom,
#                              alpha=nilai_alpha,
#                              figsize=tuple_ukuran_gambar)

# Beberapa atribut penting dalam histogram pandas:
# - bins = jumlah_bins dalam histogram yang akan digunakan. 
# Jika tidak didefinisikan jumlah_bins, maka function akan 
# secara default menentukan jumlah_bins sebanyak 10.
# - by = nama kolom di DataFrame untuk di group by. 
# (valuenya berupa nama column di dataframe tersebut).
# - alpha = nilai_alpha untuk menentukan opacity dari plot di histogram. 
# (value berupa range 0.0 - 1.0, dimana semakin kecil akan semakin kecil 
#  opacity nya)
# - figsize = tuple_ukuran_gambar yang digunakan untuk menentukan ukuran 
# dari plot histogram. Contoh: figsize=(10,12)

import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# plot histogram kolom: price
order_df[['price']].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot