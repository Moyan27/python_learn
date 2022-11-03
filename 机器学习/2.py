import sklearn.preprocessing as sp 
import numpy as np 

raw_samples=np.array([
    [17,90,4000],
    [20,80,5000],
    [23,75,5550]
])

result=sp.scale(raw_samples)
print(result)