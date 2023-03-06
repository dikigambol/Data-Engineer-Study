import pandas as pd
import numpy as np
from sklearn import preprocessing

# X merupakan matriks yang berisi fitur dataset yang akan digunakan dalam machine learning, baik untuk regresi, klasifikasi, pengklusteran, atau normalisasi
# Pada kasus kita, X berisi fitur-fitur yang digunakan untuk dinormalisasi dengan teknik min-max scaler
csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")
array = csv_data.values

X = array[:,2:5]
Y = array[:,0:1]

dataset=pd.DataFrame({"Customer ID":array[:,0],"Gender":array[:,1],"Age":array[:,2],"Income":array[:,3],"Spending Score":array[:,4]})
print("dataset sebelum dinormalisasi :")
print(dataset.head(10))

min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data = min_max_scaler.fit_transform(X)
dataset = pd.DataFrame({"Age":data[:,0],"Income":data[:,1],"Spending Score":data[:,2],"Customer ID":array[:,0],"Gender":array[:,1]})

print("dataset setelah dinormalisasi :")
print(dataset.head(10))