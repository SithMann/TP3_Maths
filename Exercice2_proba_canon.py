# Aire du quart de cercle : π × 90 × R^2 ÷ 360

import math
import numpy as np 
import matplotlib.pyplot as plt

Acarre = 1
Acercle = math.pi/4
nbTir = 0

for i in range(100000):
    x = np.random.random()
    y = np.random.random()
    norme = np.sqrt(x*x + y*y)
    if norme <= Acarre :
        nbTir += 1

print(nbTir/100000)