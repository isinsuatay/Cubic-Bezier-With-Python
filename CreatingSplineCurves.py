import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(t, p0, p1, p2, p3):
    return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3

def plot_spline_curve(points, num_points=100):
   
    if len(points) % 2 != 0:   
        raise ValueError("Control points must be even.")

    spline_points = []
    for i in range(0, len(points), 2):
        p0, p1, p2, p3 = points[i:i+4]
        t_values = np.linspace(0, 1, num_points)
        x_values = []
        y_values = []
        for t in t_values:
            x, y = cubic_bezier(t, p0, p1, p2, p3)
            x_values.append(x)
            y_values.append(y)
        spline_points.extend(list(zip(x_values, y_values)))
    
    spline_x, spline_y = zip(*spline_points)
    plt.plot(spline_x, spline_y, label='Spline Curve', color='blue')
    plt.scatter([point[0] for point in points], [point[1] for point in points], label='Control Points', color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Spline Curve with Cubic Bezier Segments')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

control_points = [
    (0, 0), (1, 3), (2, -1), (3, 2), 
    (4, 2), (5, 0), (6, 4), (7, 1)     
]

plot_spline_curve(control_points)
