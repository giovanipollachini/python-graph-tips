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
