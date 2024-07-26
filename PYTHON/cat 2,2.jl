X = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
Y = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]
from scipy import interpolate

# Given data points
X = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
Y = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]

# Target x value
x_target = 4.0

# Perform linear spline interpolation
interp_func = interpolate.interp1d(X, Y, kind='linear')

# Evaluate the interpolation function at x_target
y_target = interp_func(x_target)

print(f"The interpolated value of y at x = {x_target} is {y_target}")
