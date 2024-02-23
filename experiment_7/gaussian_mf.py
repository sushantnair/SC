import numpy as np
import matplotlib.pyplot as plt

def gaussian_membership_function(x, mean, sigma):
    # return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))
    return np.exp(-0.5 * ((x - mean)/sigma) ** 2)

# Define the parameters for the Gaussian membership function
mean = 10.0
sigma = 3.0

# Generate x values for the plot
x_values = np.linspace(0, 20, 100)

# Calculate the membership values for each x value
y_values = [gaussian_membership_function(x, mean, sigma) for x in x_values]

# Create the plot
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Gaussian membership function')

# Annotate the mean value on the x-axis
plt.annotate('mean=10', xy=(mean, 1), xytext=(mean - 1, 0.9), ha='right')

plt.show()
