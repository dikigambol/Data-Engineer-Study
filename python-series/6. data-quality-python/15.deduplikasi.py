# Duplikasi data merupakan data dengan kondisi pada row-row tertentu 
# memiliki kesamaan data di seluruh kolomnya. Tentunya ada data yang 
# duplikat dalam dataset yang dimiliki. Kondisi duplikasi harus diatasi 
# dengan jalan mengeliminir baris yang mengalami duplikasi, sehingga 
# proses ini dikenal dengan deduplikasi.

# Untuk mengecek duplikasi data:
# nama_df.duplicated(subset=None)

# Syntax untuk membuang duplikasi:
# nama_df.drop_duplicates()

import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Check ukuran (baris dan kolom) sebelum data duplikasi dibuang
print('Shape awal: ', retail_raw.shape)

# Buang data yang terduplikasi
retail_raw.drop_duplicates(inplace=True)

# Check ukuran (baris dan kolom) setelah data duplikasi dibuang
print('Shape akhir: ', retail_raw.shape)
