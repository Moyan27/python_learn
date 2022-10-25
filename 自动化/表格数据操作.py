import pandas as pd 
import os 

path=os.path.dirname(__file__)
new_path1=path+'/1.xlsx'
df1=pd.read_excel(new_path1,sheet_name='Sheet1')
new_path2=path+'/1.csv'
df2=pd.read_csv(new_path2)


print(df2)