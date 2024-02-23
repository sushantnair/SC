import matplotlib.pyplot as plt
import numpy as np

# Define the x values for the different segments of C1
x1_c1 = np.linspace(0, 1, 100)  # Linear increase from 0 to 1
x2_c1 = np.linspace(1, 4, 100)  # Constant at 0.3 from 1 to 4
x3_c1 = np.linspace(4, 5, 100)  # Linear decrease from 0.3 to 0 from 4 to 5

# Define the corresponding y values for each segment of C1
y1_c1 = np.linspace(0, 0.3, 100)
y2_c1 = np.full(100, 0.3)
y3_c1 = np.linspace(0.3, 0, 100)

# Define the x values for the different segments of C2
x1_c2 = np.linspace(3, 4, 100)  # Linear increase from 0 to 0.5
x2_c2 = np.linspace(4, 6, 100)  # Constant at 0.5 from 4 to 6
x3_c2 = np.linspace(6, 7, 100)  # Linear decrease from 0.5 to 0 from 6 to 7

# Define the corresponding y values for each segment of C2
y1_c2 = np.linspace(0, 0.5, 100)
y2_c2 = np.full(100, 0.5)
y3_c2 = np.linspace(0.5, 0, 100)

# Define the x values for the different segments of C3
x1_c3 = np.linspace(5, 6, 100)  # Linear increase from 0 to 1
x2_c3 = np.linspace(6, 7, 100)  # Constant at 1 from 6 to 7
x3_c3 = np.linspace(7, 8, 100)  # Linear decrease from 1 to 0 from 7 to 8

# Define the corresponding y values for each segment of C3
y1_c3 = np.linspace(0, 1, 100)
y2_c3 = np.full(100, 1)
y3_c3 = np.linspace(1, 0, 100)

# Plot the segments for C1
plt.plot(x1_c1, y1_c1, label='C1: y = 0 to 0.3 (0 to 1)')
plt.plot(x2_c1, y2_c1, label='C1: y = 0.3 (1 to 4)')
plt.plot(x3_c1, y3_c1, label='C1: y = 0.3 to 0 (4 to 5)')

# Plot the segments for C2
plt.plot(x1_c2, y1_c2, label='C2: y = 0 to 0.5 (3 to 4)')
plt.plot(x2_c2, y2_c2, label='C2: y = 0.5 (4 to 6)')
plt.plot(x3_c2, y3_c2, label='C2: y = 0.5 to 0 (6 to 7)')

# Plot the segments for C3
plt.plot(x1_c3, y1_c3, label='C3: y = 0 to 1 (5 to 6)')
plt.plot(x2_c3, y2_c3, label='C3: y = 1 (6 to 7)')
plt.plot(x3_c3, y3_c3, label='C3: y = 1 to 0 (7 to 8)')

# Set custom tick values for the y-axis and x-axis
plt.yticks([0, 0.25, 0.5, 0.75, 1])
plt.xticks(range(1, 9))

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Combined Graph of C1, C2, and C3')

# Add a legend
plt.legend()

# Display the combined graph
plt.grid(True)
plt.show()
