import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')
r = 1.
b= 3.
a = 4.
x0=3
y0=0

def krzywa_elipsy2(x0=0.,y0=0.,color='r',r=1.,a=2.,b=1.):
    t=np.arange(0,2*np.pi,1./100)
    x=(a-r)*np.cos(t) + r * np.cos( ((a-r)/r) * t) + x0
    y=(b-r)*np.sin(t) - r * np.sin( ((b-r)/r) * t) + y0
    return x,y

def init():
    ax.set_xlim(-2*a, 2*a)
    ax.set_ylim(-b-4., b+4.)
    return ln,

def update(frame):
    xdata.append((a-r)*np.cos(frame) + r * np.cos( ((a-r)/r) * frame) + x0)
    ydata.append((b-r)*np.sin(frame) - r * np.sin( ((b-r)/r) * frame) + y0)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True)
                    
plt.show()