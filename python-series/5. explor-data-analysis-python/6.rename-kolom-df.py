# Pada bagian ini, aku belajar cara mengganti nama kolom dataframe 
# menggunakan Pandas. Mengganti nama kolom pada Pandas dapat dilakukan 
# dengan 2 cara:

# 1. Menggunakan nama kolom.
# 2. Menggunakan indeks kolom.

# 1. Rename menggunakan nama kolom
# Syntax:
# nama_df.rename(columns={"kolom_nama_sebelumnya":"kolom_nama_baru"}, inplace=True)

# 2. Rename menggunakan indeks kolom
# Syntax:
# nama_df.columns.values['no_idx_kolom'] = "kolom_nama_baru"

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={'freight_value': 'shipping_cost'}, inplace=True)
print(order_df)