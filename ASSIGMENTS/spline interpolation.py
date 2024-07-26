import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

# Create a cubic spline interpolation of the data
cs = CubicSpline(x, y)

# Generate new x values for a smooth curve
x_new = np.linspace(0, 5, 100)
y_new = cs(x_new)

# Plot the original data points and the interpolated curve
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new, '-', label='Cubic spline interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.show()

