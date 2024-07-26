import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x**3 + 2*x**2 + 5*x + 7

# Differentiate the function with respect to x
f_prime = sp.diff(f, x)

# Print the original function and its derivative
print("Original function f(x):", f)
print("Derivative f'(x):", f_prime)
