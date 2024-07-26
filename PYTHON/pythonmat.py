import matplotlib.pyplot as plt

# Data to plot
labels = ['Kisumu', 'Nakuru', 'Mombasa']
sizes = [35.0, 30.0, 35.0]
colors = ['blue', 'green', 'orange']

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Title
plt.title('Population Distribution by City')

# Display the plot
plt.show()