import numpy as np 
import matplotlib.pyplot as plt

z = range(100000)
d = {}
for i in z:
    de1 = np.random.randint(1,7)
    de2 = np.random.randint(1,7)
    de3 = np.random.randint(1,7)
    de = de1 + de2 + de3

    if de in d :
        d[de] = d[de] + 1
    else :
        d[de] = 1
print(d)


#Histogramme
plt.title('Histogramme des tirages des dés')
plt.xlabel('Numéro tiré')
plt.ylabel('Nombre d''essais')
plt.bar(d.keys(),d.values())
plt.grid(True)
plt.show()