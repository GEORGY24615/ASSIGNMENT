import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some example data
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Create a linear regression model
model = LinearRegression()
model.fit(x, y)

# Print the model parameters
print("Intercept:", model.intercept_)
print("Slope:", model.coef_)

# Make predictions
x_new = np.array([[0], [2]])
y_predict = model.predict(x_new)

# Plot the data and the regression line
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x_new, y_predict, color='red', label='Regression line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
