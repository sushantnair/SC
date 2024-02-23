import numpy as np
import matplotlib.pyplot as plt

def identity(x):
    return x

def binary_step(x):
    return np.where(x >= 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def bipolar_sigmoid(x):
    return (1 - np.exp(-x)) / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def get_user_weights():
    weights = {}
    i = 1
    while True:
        weight_str = input(f"Enter weight for input {i} (or 'stop' to finish): ")
        if weight_str.lower() == 'stop':
            break
        try:
            weight = float(weight_str)
            weights[i] = weight
            i += 1
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

    return weights

# Get user-defined input weights
input_weights = get_user_weights()

# Number of inputs
num_inputs = len(input_weights)

# Generate input values
min_weight = min(input_weights.values())
max_weight = max(input_weights.values())
x_range = abs(max_weight - min_weight) * 1.2  # Adding some padding
x_center = (max_weight + min_weight) / 2
x = np.linspace(x_center - x_range / 2, x_center + x_range / 2, 400)

# Compute output values for each activation function
y_identity = identity(x)
y_binary_step = binary_step(x)
y_sigmoid = sigmoid(x)
y_bipolar_sigmoid = bipolar_sigmoid(x)
y_relu = relu(x)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Plot each activation function with user-defined input weights
axes[0, 0].plot(x, y_identity)
axes[0, 0].set_title("Identity")

axes[0, 1].plot(x, y_binary_step)
axes[0, 1].set_title("Binary Step")

axes[0, 2].plot(x, y_sigmoid)
axes[0, 2].set_title("Sigmoid")

axes[1, 0].plot(x, y_bipolar_sigmoid)
axes[1, 0].set_title("Bipolar Sigmoid")

axes[1, 1].plot(x, y_relu)
axes[1, 1].set_title("ReLU")

# Remove empty subplot
fig.delaxes(axes[1, 2])

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
