import numpy as np

# Define the function to integrate
def f(x):
    return np.sin(x)  # Example function

# Implementing the trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Step size
    integral = (f(a) + f(b)) / 2.0  # Initial value with the first and last terms

    for i in range(1, n):
        integral += f(a + i * h)  # Sum the middle terms

    integral *= h  # Multiply by step size
    return integral

# Define the limits of integration and number of subintervals
a = 0  # Lower limit
b = np.pi  # Upper limit
n = 1000  # Number of subintervals

# Calculate the integral
result = trapezoidal_rule(a, b, n)
print(f"The integral of sin(x) from {a} to {b} is approximately {result:.6f}")
