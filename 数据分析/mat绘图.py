from matplotlib import pyplot as plt 
import numpy as np 

x=np.arange(-20,20)
y=x**2
plt.title('y=x^2')
plt.plot(x,y)
plt.show()