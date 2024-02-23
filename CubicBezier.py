import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(t, p0, p1, p2, p3):
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

def plot_cubic_bezier(p0, p1, p2, p3, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    x_values = []
    y_values = []
    for t in t_values:
        x, y = cubic_bezier(t, p0, p1, p2, p3)
        x_values.append(x)
        y_values.append(y)
    plt.plot(x_values, y_values, label='Cubic Bezier Curve', color='blue')
    plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], label='Control Points', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cubic Bezier Curve')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Control points
p0 = np.array([0, 0])
p1 = np.array([1, 3])
p2 = np.array([4, -1])
p3 = np.array([5, 2])

plot_cubic_bezier(p0, p1, p2, p3)
