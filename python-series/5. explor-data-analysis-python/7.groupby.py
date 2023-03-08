# Kegunaan .groupby adalah mencari summary dari 
# data frame dengan menggunakan aggregate dari kolom tertentu.

# Penggunaan groupby:
# df["Score"].groupby([df['Name']]).mean()

# Penjelasan: komputasi diatas menggunakan kolom ‘Name’ 
# sebagai aggregate dan kemudian menggunakan menghitung mean dari 
# kolom ‘Score’ pada tiap - tiap aggregate tersebut.

# Contoh lainnya:
# df["Score"].groupby([df['Name']], df['Exam']).sum()

# Penjelasan: komputasi diatas menggunakan kolom ‘Name’ dan ‘Exam’ 
# sebagai aggregate dan kemudian menggunakan 
# menghitung sum dari kolom ‘Score’ pada 
# tiap - tiap aggregate tersebut.

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)