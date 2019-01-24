import math
import numpy as np 
import matplotlib.pyplot as plt

n = range(100000)
somme = 0
for i in n :
    somme += np.sqrt(1-i*i)

print(somme*4*(1/n))