import numpy as np
import matplotlib.pyplot as plt

def sigmoid_membership_function(x, b, c):
    return 1 / (1 + np.exp(-c * (x - b)))

# Define the parameters for the sigmoid membership function
b = 6
c = 2

# Generate x values for the plot
x_values = np.linspace(0, 12, 100)

# Calculate the membership values for each x value
y_values = [sigmoid_membership_function(x, b, c) for x in x_values]

# Create the plot
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Sigmoid membership function')

# Annotate the center value on the x-axis
plt.annotate('b=6', xy=(b, 0.5), xytext=(b - 1, 0.5), ha='right')

plt.show()
