# Aku pun mengutak-atik dataku kembali selama hampir setengah jam dan menemukan jika missing value aku ada pada kolom item_price
# “Ah, akhirnya!” Dengan cepat aku melengkapi missing value tersebut dengan mean dari item_price. Berikut caranya:

import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

print(retail_raw['item_price'].fillna(retail_raw['item_price'].mean()))