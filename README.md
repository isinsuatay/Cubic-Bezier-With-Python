# Cubic Bezier Curves

Cubic Bezier curves are smooth curves widely used in computer graphics and graphic design. They are defined by four control points and expressed by a third-degree polynomial. The curve is shaped by two control points (P1 and P2) between the starting and ending points (P0 and P3).

The equation of a Cubic Bezier curve is given by:

B(t) = (1-t)^3 * P0 + 3*(1-t)^2 * t * P1 + 3*(1-t) * t^2 * P2 + t^3 * P3

Here, the parameter t varies between 0 and 1, representing any point on the curve. P0 and P3 represent the starting and ending points of the curve, while P1 and P2 represent the control points shaping the curve.

## Relation between Python and Cubic Bezier

Calculating and using Cubic Bezier curves in Python is straightforward. Libraries like numpy can be used for mathematical operations required to construct these curves. Additionally, Python's graphic libraries such as matplotlib, PyQtGraph, Plotly, etc., can be utilized to draw and visualize Cubic Bezier curves.

## Applications

- **Creating Circular Trajectories:** Four control points can be used to create circular trajectories using Cubic Bezier curves.
- **Creating Spline Curves:** Bezier curves can be employed to create spline curves, which are piecewise-connected curves used to create smooth shapes.
- **Metamorphosis Curves:** Cubic Bezier curves are useful for creating smooth transitions between different shapes.
- **Backtracking Curves:** By altering control points, backtracking curves can be generated, which are useful for creating smooth animations.

## Running the Python Code

To run the provided Python scripts and examples, follow these steps:

1. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. Install the required libraries. You can install them using pip, Python's package manager. For example:
    ```
    pip install numpy matplotlib
    ```

3. Clone or download this repository to your local machine.

4. Navigate to the directory containing the Python scripts.

5. Run the desired script using Python. For example:
    ```
    python draw_cubic_bezier_curve.py
    ```
This repository contains examples and implementations of Cubic Bezier curves in Python, along with applications in various fields like computer graphics, animation, and design. Explore the provided scripts and examples to understand how Cubic Bezier curves can be effectively utilized in your projects.
