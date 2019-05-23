import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]
x, y=np.loadtxt('example.txt', delimiter=',', unpack='True')
plt.plot(x,y,label="loade from ffil1!")
plt.show()
