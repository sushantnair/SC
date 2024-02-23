import numpy as np
import matplotlib.pyplot as plt

def gbellmf(x, a, b, c):
    return 1 / (1 + ((x - c) / a) ** (2 * b))

# Define the parameters for the generalized bell-shaped membership function
a = 2
b = 3
c = 10

# Generate x values for the plot
x_values = np.linspace(0, 20, 100)

# Calculate the membership values for each x value
y_values = [gbellmf(x, a, b, c) for x in x_values]

# Create the plot
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Generalized bell-shaped membership function')

# Annotate the center value on the x-axis
plt.annotate('c=10', xy=(c, 1), xytext=(c - 1, 0.9), ha='right')

plt.show()
