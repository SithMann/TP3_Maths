
import numpy as np 
import matplotlib.pyplot as plt

# Graphique en python : 

#np.log(4)
#x = range(10)
#y = range(0,20,2)

#plt.plot(x,y)
#plt.title('Titre du graphique')
#plt.grid(True)
#plt.xlabel('nomaxex')
#plt.ylabel('nomaxey')
#plt.bar()
#plt.show()


z = range(100000)
d = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,}
for i in z:
    de1 = np.random.randint(1,7)
    de2 = np.random.randint(1,7)
    de3 = np.random.randint(1,7)
    de = de1 + de2 + de3

    d[de] = d[de] +1

#Histogramme
plt.title('Histogramme des tirages des dés')
plt.xlabel('Numéro tiré')
plt.ylabel('Nombre d''essais')
for i in  range(1,18):
    plt.bar(i,d[i])

plt.grid(True)
plt.show()