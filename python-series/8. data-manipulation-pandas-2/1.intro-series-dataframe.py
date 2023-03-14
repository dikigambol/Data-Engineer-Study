# Bagaimana Cara Menggabungkan Pandas Series/Dataframe?
# Sebagai seorang praktisi data, pasti sering kali bertemu dengan 
# banyak file sekaligus dan data yang dibutuhkan tersebar di berbagai 
# file tersebut dan membutuhkan metode untuk menggabungkan semua 
# informasi yang dibutuhkan dari setiap file itu.

# Dengan menggunakan excel atau tools pengolah spreadsheet lain hal itu b
# isa terjadi mungkin dengan menggunakan copy paste file satu ke file 
# lainnya atau yang agak canggih menggunakan method importRange 
# di google sheets. Tetapi tentu hal itu tidak bisa diandalkan ketika 
# berurusan dengan big data yang datanya bisa miliaran rows dengan 
# informasi yang tidak terbatas, Python dan Pandas adalah satu-satunya c
# ara untuk mengatasinya.

# Terdapat beberapa metode untuk menggabungkan Series/Dataframe di Pandas, yaitu:

# append
# concat
# merge
# join

import pandas as pd
# Buat series of int (s1) dan series of string (s2)
s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series(["a","b","c","d","e","f"])
# Terapkan method append
s2_append_s1 = s1.append(s2)
print("Series - append:\n", s2_append_s1)
# Buat dataframe df1 dan df2
df1 = pd.DataFrame({'a':[1,2],
		   'b':[3,4]})
df2 = pd.DataFrame({'b':[1,2],
		   'a':[3,4]})
# Terapkan method append
df2_append_df1 = df1.append(df2)
print("Dataframe - append:\n", df2_append_df1)