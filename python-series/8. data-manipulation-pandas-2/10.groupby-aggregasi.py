# Pada subbab ini akan menerapkan groupby dan fungsi aggregasi 
# mean dan std untuk menentukan nilai rata-rata dan standar 
# deviasi dari masing-masing kelompok data dari dataset

import pandas as pd
# Load data global_air_quality.csv
gaq = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv")
# Create variabel pollutant 
pollutant = gaq[['country','city','pollutant','value']].pivot_table(index=['country','city'],columns='pollutant').fillna(0)
print('Data pollutant (5 teratas):\n', pollutant.head())
# [1] Group berdasarkan country dan terapkan aggregasi mean
pollutant_mean = pollutant.groupby('country').mean()
print('Rata-rata pollutant (5 teratas):\n', pollutant_mean.head())
# [2] Group berdasarkan country dan terapkan aggregasi std
pollutant_std = pollutant.groupby('country').std().fillna(0)
print('Standar deviasi pollutant (5 teratas):\n', pollutant_std.head())
# [3] Group berdasarkan country dan terapkan aggregasi sum
pollutant_sum = pollutant.groupby('country').sum()
print('Total pollutant (5 teratas):\n', pollutant_sum.head())
# [4] Group berdasarkan country dan terapkan aggregasi nunique
pollutant_nunique = pollutant.groupby('country').nunique()
print('Jumlah unique value pollutant (5 teratas):\n', pollutant_nunique.head())
# [5] Group berdasarkan country dan terapkan aggregasi min
pollutant_sum = pollutant.groupby('country').min()
print('Nilai min pollutant (5 teratas):\n', pollutant_sum.head())
# [6] Group berdasarkan country dan terapkan aggregasi max
pollutant_nunique = pollutant.groupby('country').max()
print('Nilai max pollutant (5 teratas):\n', pollutant_nunique.head())
# Group berdasarkan country dan terapkan aggregasi first
pollutant_first = pollutant.groupby('country').first()
print('Item pertama pollutant (5 teratas):\n', pollutant_first.head())
# Group berdasarkan country dan terapkan aggregasi last
pollutant_last = pollutant.groupby('country').last()
print('Item terakhir pollutant (5 teratas):\n', pollutant_last.head())