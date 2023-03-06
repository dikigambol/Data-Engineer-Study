import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

# print data 
print(csv_data)

# akses head
print(csv_data.head())

# akses melalui kolom 
print(csv_data["Age"])

# akses melalui baris 
print(csv_data.iloc[5])

# Menampilkan suatu data dari baris dan kolom tertentu
print(csv_data["Age"].iloc[1])
print("Cuplikan Dataset:")
print(csv_data.head())

# Menampilkan data dalam range tertentu
print("Menampilkan data ke 5 sampai kurang dari 10 dalam satu baris:")
print(csv_data.iloc[5:10])

# Menampilkan informasi statistik dengan Numpy
print(csv_data.describe(exclude=["O"]))

