import math
import numpy as np 
import matplotlib.pyplot as plt

n = 1000000
somme = 0

plt.title('Calcul de pi')
plt.xlabel('Essai n°')
plt.ylabel('Valeur')

t=[]

for i in range(1,n) :

    x = np.random.rand()
    somme += np.sqrt(1-x*x)
    t.append(somme*4*(1/i))
    plt.plot(t)
    plt.pause(0.001)

print(somme*4*(1/n))