#@author Simranjit Singh
import pandas as pd
dict={'col1':[1,2,3,4,5,6],
      'col2':[7,8,9,10,11,12],
      'col3':[11,12,13,14,15,16],
      'col4':[16,17,18,19,20,21],
      'col5':[22,23,24,25,26,27],
      'name':['sim','dso','er','rfe','wef','drge']}

df= pd.DataFrame(dict)
print(df)
print(df.dtypes)
print(df['col1'][2])
print(df.tail(2))
print(df.index)
df=df.set_index('name')
print(df)

