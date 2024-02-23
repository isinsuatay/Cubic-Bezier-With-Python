import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(t, p0, p1, p2, p3):
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

def plot_reverse_curve(p0_start, p1_start, p2_start, p3_start, p0_end, p1_end, p2_end, p3_end, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    x_values = []
    y_values = []
    for t in t_values:
        p0 = (1-t) * p0_end + t * p0_start
        p1 = (1-t) * p1_end + t * p1_start
        p2 = (1-t) * p2_end + t * p2_start
        p3 = (1-t) * p3_end + t * p3_start
        x, y = cubic_bezier(t, p0, p1, p2, p3)
        x_values.append(x)
        y_values.append(y)
    plt.plot(x_values, y_values, label='Reverse Curve', color='blue')
    plt.scatter([p0_start[0], p1_start[0], p2_start[0], p3_start[0]], [p0_start[1], p1_start[1], p2_start[1], p3_start[1]], label='Start Control Points', color='red')
    plt.scatter([p0_end[0], p1_end[0], p2_end[0], p3_end[0]], [p0_end[1], p1_end[1], p2_end[1], p3_end[1]], label='End Control Points', color='green')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Reverse Curve with Cubic Bezier')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

p0_start = np.array([1, 0])
p1_start = np.array([1, 0.552])
p2_start = np.array([0.552, 1])
p3_start = np.array([0, 1])

p0_end = np.array([0, 0])
p1_end = np.array([2, 0])
p2_end = np.array([2, 2])
p3_end = np.array([0, 2])

plot_reverse_curve(p0_start, p1_start, p2_start, p3_start, p0_end, p1_end, p2_end, p3_end)
