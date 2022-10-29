import pandas as pd 
import os 

path=os.path.dirname(__file__)

# df=pd.read_csv('{}/1.csv'.format(path))
# print(df)

df1= pd.read_excel('{}/1.xlsx'.format(path),sheet_name='Sheet1')
print(df1)
print()