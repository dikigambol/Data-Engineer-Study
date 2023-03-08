# Untuk memprosesnya bisa dilakukan dengan cara berikut:

# 5. Mengetahui kolom yang memiliki outliers! 
# Gunakan visualisasi dengan boxplot pada dataframe uncleaned_raw.

import pandas as pd
import numpy as np
import io
import pandas_profiling
import matplotlib.pyplot as plt

plt.style.use('default')

uncleaned_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv')
uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(uncleaned_raw['Quantity'].mean())

#Mengetahui kolom yang memiliki outliers!
uncleaned_raw.boxplot()
plt.show()

#Check IQR
Q1 = uncleaned_raw['UnitPrice'].quantile(0.25)
Q3 = uncleaned_raw['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1

#removing outliers
uncleaned_raw = uncleaned_raw[~((uncleaned_raw[['UnitPrice']] < (Q1 - 1.5*IQR)) | (uncleaned_raw[['UnitPrice']] > (Q3 + 1.5*IQR)))]

#check for duplication
print(uncleaned_raw.duplicated(subset=None))

#remove duplication
uncleaned_raw = uncleaned_raw.drop_duplicates()