import numpy as np
import pandas as pd

df = pd.read_csv('day02_usage.csv')

# apps = ["Chat","Video","Study","Games"]
apps = np.array(df.columns)

#Part A
# arr = [df[f"{i}"].to_numpy() for i in apps]
arr = df[apps].to_numpy()

print(arr)

print(arr.shape)

#Part B

# col_sum = arr.sum(axis = 0)
per_app = arr.sum(axis=0)
# row_sum = arr.sum(axis = 1)
per_day = arr.sum(axis = 1)

print(arr[:7])

per_app_average = np.round(arr.mean(axis = 0),1)

#max 

#min

#Part C

winners = apps[arr.argmax(axis=1)]

# np.unique(winners)

values,freq = np.unique(winners,return_counts=True)

print(dict(zip(values,freq.tolist()))) #Read only once memory 

# C Printf docs 

# Part D

shares = arr/per_day[:,None]*100

'''shares2 = arr.mean(axis=1)

print(shares)

print(shares2)

 np.newaxis

shares = arr/per_day
shape
  (30,)  We cannot expand/stretch this to another column in numpy 
(30,1) 
'''

