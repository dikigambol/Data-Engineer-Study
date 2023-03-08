# Sorting adalah sebuah metode mengurutkan data berdasarkan syarat 
# kolom tertentu dan biasanya digunakan untuk melihat nilai maksimum 
# dan minimum dari dataset. Library Pandas sendiri menyediakan 
# fungsi sorting sebagai fundamental dari exploratory data analysis.

# Syntax untuk operasi sorting pada Pandas:
# nama_df.sort_values(by="nama_kolom")

# Function tersebut akan secara default mengurutkan 
# secara ascending (dimulai dari nilai terkecil), 
# untuk dapat mengurutkan secara descending 
# (nilai terbesar lebih dahulu), dapat menggunakan 
# properti tambahan:

# nama_df.sort_values(by="nama_kolom", ascending=False)
# Fungsi sorting di Pandas juga dapat dilakukan menggunakan lebih dari 
# satu kolom sebagai syarat. Contohnya pada skenario di bawah, akan 
# mencoba mengaplikasikan fungsi sorting menggunakan Age dan Score 
# sekaligus:

# nama_df.sort_values(by=["nama_kolom1", "nama_kolom2"], ascending=[True, False])

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)