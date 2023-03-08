# Varians dan standar deviasi juga merupakan suatu ukuran dispersi atau variasi. 
# Standar deviasi merupakan ukuran dispersi yang paling banyak dipakai. 
# Hal ini mungkin karena standar deviasi mempunyai satuan ukuran yang sama dengan 
# satuan ukuran data asalnya. Sedangkan varians memiliki satuan kuadrat dari data asalnya (misalnya cm^2).

# Syntax dari standar deviasi dan varians pada Pandas:
# print(order_df.loc[:, "nama_kolom"].std())
# print(order_df.loc[:, "nama_kolom"].var())

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Standar variasi kolom product_weight_gram
order_df.loc[:, 'product_weight_gram'].std()
# Varians kolom product_weight_gram
order_df.loc[:, 'product_weight_gram'].var()