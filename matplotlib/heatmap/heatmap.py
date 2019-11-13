##################################################
# Instructions
##################################################
'''
Solve the Heat Equation (steady state) in a 
rectangular plate subject to a given temperature
in the border.
The equation is solved numerically by the Finite
Difference Method, which produces a linear system.
This linear system is solved by matrix inversion.

Running this file on the Python Interpreter:
   01 - Open the Python Interpreter:
        $ python     or     $ python3
   02 - Run the following command in the interpreter
        >>> exec(open('solver-heat-eq.py').read())

The variables in these programs will be acessible 
in the interpreter.

'''

##################################################
# Import libraries
##################################################
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

##################################################
# Inputs 
##################################################

# Size of rectangular plate
Lx = 1.0 # in meters
Ly = 1.0 # in meters

# Number of points in the rectangular grid
mx = 6
my = 6

# Spacing between adjacent points in grid
dx = Lx / (mx-1)
dy = Ly / (my-1)

# Boundary conditions (in °C)
T_0_y = lambda y : 0.0
T_x_0 = lambda x : 0.0
T_x_Ly = lambda x : 100.0*(x/Lx)
T_Lx_y = lambda y : 100.0*(y/Ly)


##################################################
# Generate linear equations
##################################################

# Size of the linear system
n = (mx-2)*(my-2)

# Generate matrix A and vector b
A = np.zeros((n,n))
b = np.zeros(n)
for i in range(1,mx-1):
   for j in range(1,my-1):
      # new index: variables are numbered
      # from left to right and from botton
      # to top
      l = i-1 + (j-1)*(mx-2)
      A[l][l] = -4.0
      if i == 1 :
         if j == 1 :
            b[l]           = - T_0_y(j*dy) - T_x_0(i*dx)
            A[l][l+1]      = 1.0
            A[l][l+(mx-2)] = 1.0            
         elif j == my - 2 :
            b[l]           = - T_0_y(j*dy) - T_x_Ly(i*dx)
            A[l][l-(mx-2)] = 1.0
            A[l][l+1]      = 1.0 
         else :
            b[l]           = - T_0_y(j*dy)
            A[l][l-(mx-2)] = 1.0
            A[l][l+1]      = 1.0
            A[l][l+(mx-2)] = 1.0  
      elif i == mx-2 :
         if j == 1 :
            b[l]           = - T_Lx_y(j*dy) - T_x_0(i*dx)
            A[l][l-1]      = 1.0
            A[l][l+(mx-2)] = 1.0
         elif j == my - 2 :
            b[l]           = - T_Lx_y(j*dy) - T_x_Ly(i*dx)
            A[l][l-(mx-2)] = 1.0
            A[l][l-1]      = 1.0
         else :
            b[l]           = - T_Lx_y(j*dy)
            A[l][l-(mx-2)] = 1.0
            A[l][l-1]      = 1.0
            A[l][l+(mx-2)] = 1.0
      else :
         if j == 1 :
            b[l]           = - T_x_0(i*dx)
            A[l][l-1]      = 1.0
            A[l][l+1]      = 1.0
            A[l][l+(mx-2)] = 1.0
         elif j == my - 2 :
            b[l]           = - T_x_Ly(i*dx)
            A[l][l-(mx-2)] = 1.0
            A[l][l-1]      = 1.0
            A[l][l+1]      = 1.0
         else :
            A[l][l-(mx-2)] = 1.0
            A[l][l-1]      = 1.0
            A[l][l+1]      = 1.0
            A[l][l+(mx-2)] = 1.0


##################################################
# Solving the Linear System classically
##################################################

T_ls = np.matrix(A).I.dot(np.matrix(b).T)



##################################################
# Grid positions
##################################################

x = dx * np.arange(0,mx)
y = dy * np.arange(0,my)
x, y = np.meshgrid(x, y)

# Rewrite T for 3D plot
T_grid = np.zeros((mx,my))
for i in range(1,mx-1):
   for j in range(1,my-1):
      l = i-1 + (j-1)*(mx-2)
      T_grid[i,j] = T_ls[l]

for i in range(0,mx):
   T_grid[i,0]  = T_x_0(i*dx)
   T_grid[i,my-1] = T_x_Ly(i*dx)

for j in range(0,my):
   T_grid[0,j]  = T_0_y(j*dy)
   T_grid[mx-1,j] = T_Lx_y(j*dy)


##################################################
# Plot solution
##################################################

# Check Matplotlib docs
# https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#getting-started


# Heatmap
# Create figure
fig_heatmap = plt.figure()
extent = [0, Lx, 0, Ly]
ax_heatmap = fig_heatmap.add_subplot(1,1,1)
plt.title('Solution for Heat Equation')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
# Create grid plot
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

