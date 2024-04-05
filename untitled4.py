import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.subplots import make_subplots

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

# Create a 3D scatter plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

trace = go.Surface(x=X, y=Y, z=Z, colorscale='viridis')

fig.add_trace(trace)

# Customize the appearance of the plot
fig.update_layout(scene=dict(
    xaxis_title='X-axis',
    yaxis_title='Y-axis',
    zaxis_title='Z-axis'
))

# Show the interactive 3D plot
fig.show()
