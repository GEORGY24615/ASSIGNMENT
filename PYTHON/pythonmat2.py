import matplotlib.pyplot as plt

# Data to plot
labels = ['FORD', 'BMW', 'AUDI', 'MERCEDES', 'JAGUAR', 'TESLA']
sizes = [20, 15, 15, 25, 10, 15]  # Hypothetical proportions for each brand
colors = ['green', 'orange', 'blue', 'brown', 'red', 'purple']

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Title
plt.title('Proportions of Listings of Different Car Brands')

# Display the plot
plt.show()