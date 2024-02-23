import numpy as np
import matplotlib.pyplot as plt

def triangular_membership_function(x, a, b, c):
    if x <= a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)
    else:
        return 0

# Define the parameters for the triangular membership function
a = 2
b = 6
c = 10

# Generate x values for the plot
x_values = np.linspace(0, 12, 100)

# Calculate the membership values for each x value
y_values = [triangular_membership_function(x, a, b, c) for x in x_values]

# Create the plot
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Triangular membership function')

# Annotate the points on the x-axis
plt.annotate('a=2', xy=(a, 0), xytext=(a - 0.5, 0.1), ha='right')
plt.annotate('b=6', xy=(b, 1), xytext=(b - 0.5, 0.9), ha='right')
plt.annotate('c=10', xy=(c, 0), xytext=(c - 0.5, 0.1), ha='right')

plt.show()
