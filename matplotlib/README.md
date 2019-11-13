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
import numpy as np
import matplotlib.pyplot as plt
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


# Simple Line Plot

```python
# Create structure 
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


# Grid Plot


# Surface Plot


# Heatmap


# Examples

