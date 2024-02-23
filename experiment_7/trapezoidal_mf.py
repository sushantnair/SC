import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_membership_function(x, a, b, c, d):
    if x <= a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)
    else:
        return 0

# Define the parameters for the trapezoidal membership function
a = 2
b = 4
c = 8
d = 10

# Generate x values for the plot
x_values = np.linspace(0, 12, 100)

# Calculate the membership values for each x value
y_values = [trapezoidal_membership_function(x, a, b, c, d) for x in x_values]

# Create the plot
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Trapezoidal membership function')

# Annotate the points on the x-axis
plt.annotate('a=2', xy=(a, 0), xytext=(a - 0.5, 0.1), ha='right')
plt.annotate('b=4', xy=(b, 0), xytext=(b - 0.5, 0.1), ha='right')
plt.annotate('c=8', xy=(c, 0), xytext=(c - 0.5, 0.1), ha='right')
plt.annotate('d=10', xy=(d, 0), xytext=(d - 0.5, 0.1), ha='right')

plt.show()
