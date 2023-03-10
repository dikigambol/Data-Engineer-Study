import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak info dari df
print(df.info())

# mengetahui berapa banyak nilai hilang dari tiap kolom di dataset tersebut dengan 
# menerapkan chaining method pada dataframe yaitu .isna().sum(). Method .isna() 
# digunakan untuk mengecek berapa data yang bernilai NaN dan .sum() menjumlahkannya 
# secara default untuk masing-masing kolom dataframe.

# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print("\nJumlah missing value per kolom:\n", mv)

# Terdapat beberapa cara untuk mengatasi missing value, antara lain:

# - dibiarkan saja,
# - hapus value itu, atau
# - isi value tersebut dengan value yang lain (biasanya interpolasi, mean, median, etc)

# Sekarang dapat menerapkan dua aksi yaitu

# Membiarkannya saja
# Menghapus kolom
 
# Treatment pertama (membiarkannya saja) seperti pada kolom confirmed, death, dan recovered. 
# Akan tetapi jika tidak ada yang terkonfirmasi, meninggal dan sembuh sebenarnya dapat menukar 
# value ini dengan angka nol. Meskipun ini lebih make sense dalam representasi datanya, tetapi 
# untuk sub bab ini ketiga kolom tersebut diasumsikan dibiarkan memiliki nilai missing value.

# Treatment kedua yaitu dengan menghapus kolom, yang mana ini digunakan jika seluruh kolom dari 
# dataset yang dipunyai semua barisnya adalah missing value. Untuk itu dapat menerapkan 
# method .dropna() pada dataframe, bagaimana caranya?

# nama_dataframe.dropna(axis=1, how="all")

# Pada method .dropna() ada dua keyword argumen yang harus diisikan yaitu axis dan how. 
# Keyword axis digunakan untuk menentukan arah dataframe yang akan dibuang angka 1 untuk 
# menyatakan kolom (column-based) atau dapat ditulis dalam string "column". 
# Jika digunakan angka 0 berarti itu dalam searah index (row-based) atau dapat ditulis dalam string "index".

# Sementara, keyword how digunakan untuk bagaimana cara membuangnya. Opsi yang dapat diterimanya (dalam string) adalah
# "all" artinya jika seluruh data di satu/beberapa kolom atau di satu/beberapa baris adalah missing value.
# "any" artinya jika memiliki 1 saja data yang hilang maka buanglah baris/kolom tersebut.

import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak ukuran awal dataframe
print("Ukuran awal df: %d baris, %d kolom." % df.shape)
# Drop kolom yang seluruhnya missing value dan cetak ukurannya
df = df.dropna(axis=1, how="all")
print("Ukuran df setelah buang kolom dengan seluruh data missing: %d baris, %d kolom." % df.shape)
# Drop baris jika ada satu saja data yang missing dan cetak ukurannya
df = df.dropna(axis=0, how="any")
print("Ukuran df setelah dibuang baris yang memiliki sekurangnya 1 missing value: %d baris, %d kolom." % df.shape)

# Sekarang, akan melakukan treatment ketiga untuk melakukan handle missing value pada dataframe. 
# Treatment ini dilakukan dengan cara mengisi missing value dengan nilai lain, yang dapat berupa :

# nilai statistik seperti mean atau median
# - interpolasi data
# - text tertentu
 
# Akan mulai pada kolom yang missing yang tipe datanya adalah berupa object. 
# Kolom tersebut adalah province_state, karena tidak tahu secara persis province_state mana yang 
# dimaksud, bisa menempatkan string "unknown" sebagai substitusi missing value. Meskipun keduanya 
# berarti sama-sama tidak tahu tetapi berbeda dalam representasi datanya.

import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak unique value pada kolom province_state
print("Unique value awal:\n", df['province_state'].unique())
# Ganti missing value dengan string "unknown_province_state"
df['province_state'] = df['province_state'].fillna('unknown_province_state')
# Cetak kembali unique value pada kolom province_state
print("Unique value setelah fillna:\n", df['province_state'].unique())

# mengganti missing value dengan nilai statistik kolom bersangkutan, 
# baik median atau mean (nilai rata-rata). Misalnya akan menggunakan kolom active. 
# Dengan mengabaikan terlebih dahulu sebaran berdasarkan negara (univariate), 
# jika mengisi dengan nilai rata-rata maka harus melihat terlebih dahulu data 
# apakah memiliki outliers atau tidak. Jika ada outliers dari data maka 
# menggunakan nilai tengah (median) data adalah cara yang lebih safe.

# Untuk itu diputuskan dengan mengecek nilai median dan nilai mean kolom active 
# juga nilai min dan max-nya. Jika data pada kolom active terdistribusi normal 
# maka nilai mean dan median akan hampir sama.

# Terlihat data memiliki distribusi yang skewness, karena nilai mean dan median 
# yang cukup jauh serta range data yang cukup lebar. Di sini pada kolom active 
# data memiliki outliers. Jadi akan mengisi missing value dengan median.

import pandas as pd
# Baca file "https://storage.googleapis.com/dqlab-dataset/datacovid19.csv"
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
# Cetak nilai mean dan median awal 
print("Awal: mean = %f, median = %f." % (df["active"].mean(), df["active"].median()))
# Isi missing value kolom active dengan median
df_median = df["active"].fillna(df["active"].median())
# Cetak nilai mean dan median awal setelah diisi dengan median
print("Fillna median: mean = %f, median = %f." % (df_median.mean(), df_median.median()))
# Isi missing value kolom active dengan mean
df_mean = df["active"].fillna(df["active"].mean())
# Cetak nilai mean dan median awal setelah diisi dengan mean
print("Fillna mean: mean = %f, median = %f." % (df_mean.mean(), df_mean.median()))

# menggunakan teknik interpolasi dalam mengisi nilai missing value 
# pada suatu dataset.

# Data yang menggunakan interpolasi untuk mengisi data yang 
# hilang adalah time series data, yang secara default akan 
# diisi dengan interpolasi linear.

# Perhatikan kode berikut:

import numpy as np
import pandas as pd
# Data
ts = pd.Series({
   "2020-01-01":9,
   "2020-01-02":np.nan,
   "2020-01-05":np.nan,
   "2020-01-07":24,
   "2020-01-10":np.nan,
   "2020-01-12":np.nan,
   "2020-01-15":33,
   "2020-01-17":np.nan,
   "2020-01-16":40,
   "2020-01-20":45,
   "2020-01-22":52,
   "2020-01-25":75,
   "2020-01-28":np.nan,
   "2020-01-30":np.nan
})
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi linier
print("Setelah diisi missing valuenya:\n", ts)