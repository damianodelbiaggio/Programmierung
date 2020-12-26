import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 25)     #25 è il numero di punti da stampare, 0 e 2pi sono il wertebereich
y = np.sin(x)


plt.plot(x,y,'k-')                  #punkte mit 'ko'    Dreiecke mit 'k^-'
plt.plot(x,y, 'ro')
plt.show()