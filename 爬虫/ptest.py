import numpy as np

a=[[1,2,3,4],[5,6,7,8],[9,10]]
b=[]
for i in a:
    b+=i[0:len(i)+1]
    print(i[0:-1])
    
print(b)