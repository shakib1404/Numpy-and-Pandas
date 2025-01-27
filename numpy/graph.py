import matplotlib.pyplot as plt 
import seaborn as sns 


sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()
from numpy import random

x = random.normal(size=(2, 3))

print(x)