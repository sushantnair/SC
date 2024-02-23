import matplotlib.pyplot as plt
import numpy as np

# Define the x values for the different segments
x1 = np.linspace(0, 1, 100)  # Linear increase from 0 to 1
x2 = np.linspace(1, 4, 100)  # Constant at 0.3 from 1 to 4
x3 = np.linspace(4, 5, 100)  # Linear decrease from 0.3 to 0 from 4 to 5

# Define the corresponding y values for each segment
y1 = np.linspace(0, 0.3, 100)
y2 = np.full(100, 0.3)
y3 = np.linspace(0.3, 0, 100)

# Plot the segments
plt.plot(x1, y1, label='y = 0 to 0.3 (0 to 1)')
plt.plot(x2, y2, label='y = 0.3 (1 to 4)')
plt.plot(x3, y3, label='y = 0.3 to 0 (4 to 5)')

# Draw a dotted line at y = 0.3
plt.axhline(y=0.3, color='red', linestyle='--', label='y = 0.3')

# Set custom tick values for the y-axis and x-axis
plt.yticks([0, 0.25, 0.5, 0.75, 1])
plt.xticks(range(1, 9))

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph Based on Provided Information')

# Add a legend
plt.legend()

# Display the graph
plt.grid(True)
plt.show()
