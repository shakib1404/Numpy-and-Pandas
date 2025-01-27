from numpy import random
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

x=random.randint(100)
print(x)
x=random.rand()
print(x)
x=random.randint(100,size=5)
print(x)
x=random.randint(100,size=(3,5))
print(x)
x=random.rand(5)
print(x)
x=random.choice([1,3,4,5,7])
print(x)
x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
x=random.choice([1,3,4,5,7], p=[.1,.5,.4,.0,.0], size=(10))
print(x)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)
arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr) 
rr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr)) 


