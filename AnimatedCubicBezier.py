import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def cubic_bezier(t, p0, p1, p2, p3):
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

def animate(frame):
    plt.clf()
    t = frame / frames
    x, y = cubic_bezier(t, p0, p1, p2, p3)
    plt.plot(x, y, 'ro')
    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Cubic Bezier Animation')

p0 = np.array([0, 0])
p1 = np.array([1, 1])
p2 = np.array([1, 0])
p3 = np.array([2, 0])

frames = 100
ani = FuncAnimation(plt.gcf(), animate, frames=frames, interval=50)
plt.show()
