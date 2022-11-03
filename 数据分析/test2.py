import pandas as pd 
import os

path =os.path.dirname(__file__)

data=pd.read_csv('{}/1.csv'.format(path))
print(data)