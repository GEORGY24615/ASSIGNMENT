def trapezoidal_rule(f, a, b, n):
    """
    Approximates the definite integral of f from a to b using the trapezoidal rule.

    Parameters:
    f : function
        The function to integrate.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n : int
        The number of trapezoids (segments) to use.

    Returns:
    float : Approximation of the integral of f from a to b.
    """
    h = (b - a) / n  # width of each trapezoid
    integral = 0.5 * (f(a) + f(b))  # initialize sum with 0.5 * (f(a) + f(b))

    for i in range(1, n):
        integral += f(a + i * h)

    integral *= h
    return integral

# Example function to integrate: f(x) = x^2
def f(x):
    return x**2

# Example usage
a = 0.0  # lower limit of integration
b = 1.0  # upper limit of integration
n = 100  # number of trapezoids

approx_integral = trapezoidal_rule(f, a, b, n)
print(f"Approximated integral of f(x) from {a} to {b} using {n} trapezoids: {approx_integral}")
