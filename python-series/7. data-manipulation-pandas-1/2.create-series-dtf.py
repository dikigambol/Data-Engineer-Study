import pandas as pd
import numpy as np

# Creating series from list
ex_list = ['a',1,3,5,'c','d']
ex_series = pd.Series(ex_list)
print(ex_series)
# Creating dataframe from list of list
ex_list_of_list = [[1,'a','b','c'],
                   [2.5,'d','e','f'],
		           [5,'g','h','i'],
		           [7.5,'j',10.5,'l']]
index = ['dq','lab','kar','lan']
cols = ['float','char','obj','char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print(ex_df)

# Creating series from dictionary
dict_series = {'1':'a',
			   '2':'b',
			   '3':'c'}
ex_series = pd.Series(dict_series)
print(ex_series)
# Creating dataframe from dictionary
df_series = {'1':['a','b','c'],
             '2':['b','c','d'],
             '3':[2,3,'z']}
ex_df = pd.DataFrame(df_series)
print(ex_df)

# Creating series from numpy array (1D)
arr_series = np.array([1,2,3,4,5,6,6,7])
ex_series = pd.Series(arr_series)
print(ex_series)
# Creating dataframe from numpy array (2D)
arr_df = np.array([[1,2,3,5],
                   [5,6,7,8],
                   ['a','b','c',18]])
ex_df = pd.DataFrame(arr_df)
print(ex_df)