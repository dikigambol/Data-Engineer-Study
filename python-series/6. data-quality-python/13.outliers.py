# Outliers merupakan data observasi yang muncul dengan nilai-nilai ekstrim.
# Yang dimaksud dengan nilai-nilai ekstrim dalam observasi adalah nilai
# yang jauh atau beda sama sekali dengan sebagian besar nilai lain
# dalam kelompoknya.

# Cara treatment terhadap outliers antara lain:

# 1. Remove the outliers (dibuang)
# 2. Filling the missing value (imputasi)
# 3. Capping
# 4. Prediction

# Pada umumnya, outliers dapat ditentukan dengan metric
# IQR (interquartile range).

# Rumus dasar dari IQR: Q3 - Q1, dan data suatu observasi
# dapat dikatakan outliers jika memenuhi kedua syarat dibawah ini:

# - < Q1 - 1.5 * IQR
# - > Q3 + 1.5 * IQR


# Syntax di Python:
# Q1 = nama_df.quantile(0.25)
# Q3 = nama_df.quantile(0.75)
# IQR = Q3 - Q1

# Kemudian untuk membuang outliers-nya:
# nama_df = nama_df[~((nama_df < (Q1 - 1.5*IQR)) | (nama_df > (Q13 + 1.5*IQR)))]

import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

# Q1, Q3, dan IQR
Q1 = retail_raw['quantity'].quantile(0.25)
Q3 = retail_raw['quantity'].quantile(0.75)
IQR = Q3 - Q1

# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('Shape awal: ', retail_raw.shape)

# Removing outliers
retail_raw = retail_raw[~((retail_raw['quantity'] < (Q1 - 1.5*IQR)) | (retail_raw['quantity'] > (Q3 + 1.5*IQR)))]

# Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', retail_raw.shape)
