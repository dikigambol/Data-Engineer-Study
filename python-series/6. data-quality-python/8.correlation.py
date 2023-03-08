# Correlation

# Korelasi adalah cara yang tepat untuk menemukan hubungan antara 
# variabel numerik. Koefisien korelasi berkisar antara -1 hingga 1. 
# Korelasi 1 adalah korelasi positif total, korelasi -1 
# adalah korelasi negatif total dan korelasi 0 adalah korelasi non-linear.

import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

print('Korelasi quantity dengan item_price')
print(retail_raw[['quantity', 'item_price']].corr())