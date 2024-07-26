import numpy as np
from scipy.interpolate import interp1d

# Given data points
x = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Create a linear interpolation function
linear_interp = interp1d(x, y, kind='linear')

# Calculate the value of y at x = 4.0
x_new = 4.0
y_new = linear_interp(x_new)

print(f"The value of y at x = {x_new} is {y_new:.2f}")