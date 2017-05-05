#import numpy as np
#import random
#print(np.random.randint(1,7, size=10))
#import random
#import numpy as np
#outcome = np.random.randint(1, 7, size=(10,10))
#print(outcome)
#%matplotlib inline
import matplotlib.pyplot as plt
from random import normalvariate
n = 1000
values = []
frequencies = {}
while len(values) < n:
    value = normalvariate(180, 30)
    if 130 < value < 230:
        frequencies[int(value)] = frequencies.get(int(value), 0) + 1
        values.append(value)
freq = list(frequencies.items())
freq.sort()
plt.plot(*list(zip(*freq)))

        




