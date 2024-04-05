import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for x and y values
x = np.linspace(-1, 1, 100)
y = np.linspace(0, 300, 100)
a_1 = 0.7
b_1 = -2
a_2 = 1.7
b_2 = -1.4
a_3 = 2
b_3 = 1.1

alpha = 2.2
beta = 0

# Create a grid of x and y values
X, Y = np.meshgrid(x, y)

# Define the function for the surface plot
# You can change this function to plot different surfaces
Z = np.exp(a_2 + b_2 * X) / (np.exp(a_1 + b_1 * X) + np.exp(a_2 + b_2 * X) + np.exp(a_3 + b_3 * X))

# Create the 3D surface plot using Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # Specify 3D projection

# Customize the appearance of the plot
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and a colorbar
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Enable interactive mode for 3D plot
plt.ion()

# Show the interactive 3D plot using Axes3D
plt.show()

# To keep the plot window open after execution, you can add input:
# input("Press Enter to close the plot...")
