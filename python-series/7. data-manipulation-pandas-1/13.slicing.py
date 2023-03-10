# Seperti artinya slicing adalah cara untuk melakukan filter 
# ke dataframe/series berdasarkan kriteria tertentu dari nilai 
# kolomnya ataupun kriteria index-nya.

# Terdapat 2 cara paling terkenal untuk slicing dataframe, 
# yaitu dengan menggunakan method .loc dan .iloc pada variabel 
# bertipe pandas DataFrame/Series. Method .iloc ditujukan 
# untuk proses slicing berdasarkan index berupa nilai integer 
# . Akan tetapi akan lebih sering menggunakan dengan method .loc 
# lebih fleksibel. 

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df['customer_id'] == '18055') &
		          (df['product_id'].isin(['P0029','P0040','P0041']))
				 ]
print("Slice langsung berdasarkan kolom:\n", df_slice)

# menerapkan berdasarkan index. Tentu syaratnya adalah dataset 
# sudah dilakukan indexing terlebih dahulu melalui penerapan 
# method .set_index
# cara 1 method .loc
import pandas as pd
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
df = df.set_index(["order_date", "product_id"])
df_slice1 = df.loc[("2019-01-01", ["P2154","P2556"]),:]
print("Cara 1:\n", df_slice1)
# cara 2 Gunakan pd.IndexSlice sebagai varaibel untuk melakukan slicing index
idx = pd.IndexSlice
df_slice2 = df.sort_index().loc[idx["2019-01-01","P2154":"P2556"], :] 
print("Cara 2:\n", df_slice2)

import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_csv.csv')
# Set index dari df sesuai instruksi
df = df.set_index(['order_date','order_id','product_id'])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01",1612339,["P2154", "P2159"]),:]
print("Slice df:\n", df_slice)