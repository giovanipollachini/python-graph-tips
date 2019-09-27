# Description

The package provides classes for graph
objects, generators to create standard graphs, IO routines for reading in existing datasets, algorithms to analyze the
resulting networks and some basic drawing tools.

References: [https://networkx.github.io/](https://networkx.github.io/)

# Install NetworkX

On terminal, type:
```terminal
pip install networkx
```
If you prefer, install it on a virtual environment:
```terminal
# Move to the directory you want to use to create the virtual environment
# (often created inside the home directory)
cd My/virtual/env/here
# Create virtual environment 
virtualenv name_of_virtual_env
```
```terminal
# Activate virtual environment (cd to the directory 
# in which the virtual environment was installed)
source name_of_virtual_env/bin/activate
# Dectivate virtual environment
deactivate
```

# Import libraries

```python
# Import libraries
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
```

# Create graph from empty

```python
# Create graph from empty graph
G = nx.Graph()
node_color = []
node_position = {}

G.add_node('N1') # node label can take types other than str
node_color += [0.8] # node color is a number from vmin to vmax if the heatmap
                    # option is chosen (select style difining cmap on options)
                    # otherwise, node color can be a string such as 'blue' 
                    # or '#0000FF'
node_position['N1'] = (0,1)            
G.add_node('N2') 
node_color += [0.2]
node_position['N2'] = (1,0)
G.add_node('N3') 
node_color += [0.2]
node_position['N3'] = (1,1)
G.add_node('N4') 
node_color += [0.2]
node_position['N4'] = (1,2)
G.add_node('N5') 
node_color += [0.2]
node_position['N5'] = (1,3)
G.add_edge('N1','N2')
G.add_edge('N1','N3')
G.add_edge('N1','N4')
G.add_edge('N1','N5')
G.add_edge('N2','N3')
```

# Create graph from adjacency matrix

```python
# Define adjacency matrix
A = np.array([[0 , 1 , 1 , 1 , 1 ],
              [0 , 0 , 1 , 0 , 0 ],
              [0 , 0 , 0 , 0 , 0 ],
              [0 , 0 , 0 , 0 , 0 ],
              [0 , 0 , 0 , 0 , 0 ]])

# Create graph from adjacency matrix
G = nx.from_numpy_matrix(A)
```

# Plot graph (png file)

```python
# Plot circular graph
options_circular = {
   'node_color': node_color,  
   'node_size': 500,
   'font_size': 7,
   'alpha': 1.0,
   'cmap': 'Blues',
   'vmin': 0.0,
   'vmax': 1.0,
   'width': 2,
   'with_labels' : True}
   # Check NetworkX Reference Chapter 10. Drawing for more options
nx.draw_circular(G,**options_circular)
plt.axis('equal')
plt.savefig('graph_from_adjacency_matrix_circular.png', format='png')
plt.clf()
plt.cla()
plt.close()
```
![graph_from_empty_circular](https://github.com/giovanipollachini/python-graph-tips/blob/master/networkx/graph-from-empty/graph_from_empty_circular.png)

```python
# Plot graph with defined positions
options_custom = {
   'node_color': node_color,  
   'node_size': 500,
   'font_size': 7,
   'alpha': 1.0,
   'cmap': 'Blues',
   'vmin': 0.0,
   'vmax': 1.0,
   'pos': node_position,
   'width': 2,
   'with_labels' : True}
   # Check NetworkX Reference Chapter 10. Drawing for more options
nx.draw(G,**options_custom)
plt.savefig('graph_from_adjacency_matrix_custom.png', format='png')
plt.clf()
plt.cla()
plt.close()
```
![graph_from_empty_custom](https://github.com/giovanipollachini/python-graph-tips/blob/master/networkx/graph-from-empty/graph_from_empty_custom.png)


# Examples

- [Create graph from empty](https://github.com/giovanipollachini/python-graph-tips/tree/master/networkx/graph-from-empty)
- [Create graph from adjacency matrix](https://github.com/giovanipollachini/python-graph-tips/tree/master/networkx/graph-from-adjacency-matrix)
