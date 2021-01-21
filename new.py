import numpy as np 
import random as r
list=[r.random() for i in range(1000)]
l=np.array(list)
print(np.mean(l),np.std(l))