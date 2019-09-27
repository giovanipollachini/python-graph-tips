##################################################
# Instructions
##################################################
'''
Example for creating a graph from an empty graph using the 
library NetworkX.
Reference for NetworkX: https://networkx.github.io/

Running this file on the Python Interpreter:
   01 - Open the Python Interpreter
        $ python   or   $ python3
   02 - Run the following command in the interpreter
        >>> exec(open('graph_from_empty.py').read())

The variables in these programs will be acessible in the interpreter
after executing the program.

'''

# Import libraries
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np



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
plt.savefig('graph_from_empty_circular.png', format='png')
plt.clf()
plt.cla()
plt.close()


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
plt.savefig('graph_from_empty_custom.png', format='png')
plt.clf()
plt.cla()
plt.close()

