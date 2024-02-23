import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(t, p0, p1, p2, p3):
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

radius = 2
center = np.array([0, 0])
p0 = center + np.array([radius, 0])
p1 = center + np.array([radius, radius * 4 / 3])
p2 = center + np.array([-radius, radius * 4 / 3])
p3 = center + np.array([-radius, 0])

def plot_circular_trajectory(p0, p1, p2, p3, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    x_values = []
    y_values = []
    for t in t_values:
        x, y = cubic_bezier(t, p0, p1, p2, p3)
        x_values.append(x)
        y_values.append(y)
    plt.plot(x_values, y_values, label='Circular Trajectory', color='blue')
    plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], label='Control Points', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Circular Trajectory with Cubic Bezier Curve')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_circular_trajectory(p0, p1, p2, p3)
