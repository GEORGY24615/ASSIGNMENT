import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the model function
def model_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate example data
x_data = np.linspace(0, 4, 50)
y_data = model_func(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(x_data))

# Fit the model to the data
popt, pcov = curve_fit(model_func, x_data, y_data)

# Print optimal parameters
print("Optimal parameters:", popt)

# Plot data and fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model_func(x_data, *popt), color='red', label='Fitted curve')
plt.legend()
plt.show()
