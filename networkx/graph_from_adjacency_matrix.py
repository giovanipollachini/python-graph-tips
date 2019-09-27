##################################################
# Instructions
##################################################
'''
Example for creating a graph from adjacency matrix using the 
library NetworkX.
Reference for NetworkX: https://networkx.github.io/

Running this file on the Python Interpreter:
   01 - Open the Python Interpreter
        $ python   or   $ python3
   02 - Run the following command in the interpreter
        >>> exec(open('graph_from_adjacency_matrix.py').read())

The variables in these programs will be acessible in the interpreter
after executing the program.

'''

# Import libraries
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# Define adjacency matrix
A = np.array([[0 , 1 , 1 , 1 , 1 ],
              [0 , 0 , 1 , 0 , 0 ],
              [0 , 0 , 0 , 0 , 0 ],
              [0 , 0 , 0 , 0 , 0 ],
              [0 , 0 , 0 , 0 , 0 ]])



# Create graph from adjacency matrix
G = nx.from_numpy_matrix(A)


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


# Define position
node_position = [(0,1),(1,0),(1,1),(1,2),(1,3)]

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
