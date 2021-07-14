import numpy as np
import matplotlib.pylab as plt
import math as m

u = 30
g = 9.8
a = 90
angle = [a * np.pi/180]

t = np.linspace(0, 5.5, num=300)

for i in angle:
    x_ = []
    y_ = []
    for k in t:
        x = ((u*k)*np.cos(i))
        y = ((u*k)*np.sin(i))-((0.5*g)*(k**2))
        if x > 0 and y > 0:
            x_.append(x)
            y_.append(y)
            
        
    plt.plot(x_, y_)

print("Range of the Projectile = ", round(((u**2)*np.sin(2*(angle[0])))/g, 2))
print("Time of Flight of the Projectile = ", round(((u * np.sin(angle[0])))/ g, 2))
print("Maximum height of Projectile = ", round(((u * np.sin(angle[0]))**2)/g, 2))

plt.show()
