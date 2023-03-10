import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")
# Index dari df
print('Index :', df.index)
# Column dari df
print("Columns :", df.columns)

# Untuk membuat multi index (hierarchical indexing) 
# dengan pandas diperlukan kolom-kolom mana saja yang 
# perlu disusun agar index dari dataframe menjadi 
# sebuah hirarki yang kemudian dapat dikenali.
import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")
# Set multi index df
df_x = df.set_index(['order_date', 'city', 'customer_id'])
# Perlu diketahui bahwa kumpulan index dari multi index adalah list 
# dari banyak tuples, tuples-nya merupakan kombinasi yang ada dari 
# gabungan index-index tersebut. Dari multi index tersebut juga 
# terdapat atribut levels yang menunjukkan urutan index.
# Print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level)

# menggunakan assignment untuk menset index dari suatu dataframe. 
# Untuk itu file "sample_excel.xlsx" yang digunakan. 
# Perhatikan code berikut!
import pandas as pd
df_week = pd.DataFrame({
    "day_number":[1,2,3,4,5,6,7],
    "week_type":["weekday" for i in range(5)] + ["weekend" for i in range(2)]
})
df_week.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(df_week)

# Cara yang ditunjukkan oleh baris ketujuh (ke-34) 
# pada code editor di atas hanya berlaku jika index 
# yang di-assign tersebut memiliki panjang yang sama 
# dengan jumlah baris dari dataframe.
# Jika ingin kembalikan dataframe ke index default-nya 
# yaitu dari 0 s/d jumlah baris data - 1,
# maka dapat menggunakan method .reset_index(drop=True), 
# argument drop=True bertujuan untuk menghapus index lama.

import pandas as pd
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",
                  sep="\t", 
                  nrows=10)
# Cetak data frame awal
print("Dataframe awal:\n", df)
# Set index baru
df.index = ["Pesanan ke-" + str(i) for i in range(1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df)

# Fitur ini telah dimiliki oleh setiap fungsi yang digunakan dalam 
# membaca data dengan pandas, yaitu penggunaan argumen index_col 
# pada fungsi yang dimaksud. Untuk jelasnya dapat diperhatikan 
# pada kode berikut ini.
import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv', 
                 sep='\t', 
                 index_col=["order_date"])
print("Dataframe:\n", df.head(8))
# Dari dataset sample_csv.csv, sample_tsv.tsv, atau sample_excel.xlsx
# sudah tahu bahwa kolom dataset adalah 
# 'order_id'; 'order_date'; 'customer_id'; 'city'; 'province'; 
# 'product_id'; 'brand'; 'quantity'; and 'item_price'. 
# Sehingga kode di atas digunakan langsung kolom 'order_date' 
# pada saat membaca file-nya.
# Terlihat bahwa kolom order_date sudah jadi index, dan tentunya 
# jumlah kolom dataframe berkurang satu, yaitu menjadi delapan kolom.

import pandas as pd
# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv"
                 , sep="\t", 
                 index_col=['order_date', 'order_id'])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))

import pandas as pd
df_week = pd.DataFrame({'day_number':[1,2,3,4,5,6,7],
                        'week_type':['weekday' for i in range(5)] + ['weekend' for i in range(2)]
                       })
df_week_ix = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
df_week.index = [df_week_ix, df_week['day_number'].to_list()]
df_week.index.names = ['name','num']
print(df_week.index.names)