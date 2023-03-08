import numpy as np
import pandas as pd

# read csv or excel dengan pandas 
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Melihat struktur kolom dan baris dari data frame
print(order_df.shape)

# Melihat preview data dari data frame
# konten teratas default 5
print(order_df.head(10))
# konten terbawah default 5
print(order_df.tail())