# Description

This document shows how to plot graphs using the library Matplotlib. Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

Reference: https://matplotlib.org/users/index.html

# Install Matplotlib

Installation using PIP:
```shell
python -m pip install -U matplotlib
```

# Import Library

```python
# NumPy
import numpy as np
# Matplotlib
import matplotlib.pyplot as plt
# For 3-D graphs
from mpl_toolkits.mplot3d import axes3d
# Colormaps
from matplotlib import cm
```

# Useful References

Unicode characters: useful for labels and titles of graphs.
Link: https://pythonforundergradengineers.com/unicode-characters-in-python.html 

Marker styles.
Link: https://matplotlib.org/3.1.1/api/markers_api.html

Line styles.
Link https://stackoverflow.com/questions/33936134/are-there-really-only-4-matplotlib-line-styles 

Color map (for heatmaps).
https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html

Some 3-D plots.
Link: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#getting-started


# Line Plot

```python
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define values
X = np.array([0, 1, 2, 3, 4, 5])
Y1 = X
Y2 = X * X

# Create figure for plot
fig = plt.figure()
graph = fig.add_subplot(1,1,1)
graph.set_xlabel('x label')
graph.set_ylabel('y label')
graph.set_title('Title')

# Insert plots
plt.plot(X,Y1,'ro-',label='Plot Y1')
plt.plot(X,Y2,'go-',label='Plot Y2')

# Show legend
plt.legend()

# Save figure
plt.savefig('lineplot.png')
plt.savefig('lineplot.pdf')

# Show plot in interactive window
plt.show()

# Close figure
plt.clf()
plt.cla()
plt.close()
```
Result:
![lineplot](https://github.com/giovanipollachini/python-graph-tips/blob/master/matplotlib/lineplot/lineplot.png)

Example: 

# Wireframe (3-D)
Example: plotting the temperature (z axis) over a square plate (x and y axes) in stationary state with a given distribution of temperature on the edges. 
```python
# Grid plot
# Create figure
fig_grid = plt.figure()
ax_grid = fig_grid.add_subplot(111, projection='3d')
ax_grid.set_xlabel('x (m)')
ax_grid.set_ylabel('y (m)')
ax_grid.set_zlabel('T (°C)')
plt.title('Solution for Heat Equation')
# Create wireframe
grid = ax_grid.plot_wireframe(x, y, T_grid, rstride=1, cstride=1)
# Show plot in interactive window
plt.show(grid)
# Close figure
plt.clf()
plt.cla()
plt.close()
```
Result:
![wireframe](https://github.com/giovanipollachini/python-graph-tips/blob/master/matplotlib/wireframe/wireframe.png)


# Surface Plot (3-D)
Example: plotting the temperature (z axis) over a square plate (x and y axes) in stationary state with a given distribution of temperature on the edges. 
```python
# 3-D Surface Plot
# Create figure
fig_surf = plt.figure()
ax_surf = fig_surf.gca(projection='3d')
ax_surf.set_xlabel('x (m)')
ax_surf.set_ylabel('y (m)')
ax_surf.set_zlabel('T (°C)')
plt.title('Solution for Heat Equation')
# Create surface plot
surf = ax_surf.plot_surface(x, y, T_grid, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig_surf.colorbar(surf, shrink=0.8, aspect=5, label='T (°C)')
# Save figure in file
plt.savefig('surfplot.png')
plt.savefig('surfplot.pdf')
# Show plot in interactive window
plt.show(surf)
# Close figure
plt.clf()
plt.cla()
plt.close()
```
Result:
![surfplot](https://github.com/giovanipollachini/python-graph-tips/blob/master/matplotlib/surfplot/surfplot.png)

# Heatmap
Example: plotting the temperature (as a heatmap) over a square plate (x and y axes) in stationary state with a given distribution of temperature on the edges. 

```python
# Heatmap
# Create figure
fig_heatmap = plt.figure()
extent = [0, Lx, 0, Ly]
ax_heatmap = fig_heatmap.add_subplot(1,1,1)
plt.title('Solution for Heat Equation')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
# Create heatmap
heatmap = plt.imshow(T_grid, extent=extent, cmap=cm.coolwarm, origin='lower')
plt.colorbar(heatmap, shrink=0.6, aspect=5, label='T (°C)')
# Save figure in file
plt.savefig('heatmap.png')
plt.savefig('heatmap.pdf')
# Show plot in interactive window
plt.show(heatmap)
# Close figure
plt.clf()
plt.cla()
plt.close()
```
Result:
![heatmap](https://github.com/giovanipollachini/python-graph-tips/blob/master/matplotlib/heatmap/heatmap.png)


# Other Examples

Examples: Matplotlib - mplot3d
Source: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#getting-started
Link: [examples-mplot3d](https://github.com/giovanipollachini/python-graph-tips/tree/master/matplotlib/examples-mplot3d)
