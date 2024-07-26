import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def f(x):
    return np.sin(x)

# Define integration limits
a = 0
b = np.pi/2
# Perform numerical integration using quad function from scipy
result, error = quad(f, a, b)

# Print the result
print(f"Numerical integration result: {result}")
print(f"Estimated error: {error}")


