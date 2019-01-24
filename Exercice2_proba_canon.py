# Aire du quart de cercle : π × 90 × R^2 ÷ 360

import math
import numpy as np 
import matplotlib.pyplot as plt

Acarre = 1
Acercle = math.pi/4
nbTir = 0

for i in range(100000):
    tir = np.random.random()
    if tir <= Acercle :
        nbTir += 1

print(nbTir/100000)