# Consider the following equation:-
# 3x=5y+10
# 4x-2y=7
#Find the value of x and y using numpy package
#----------------------------------------------------

import numpy as np
A = np.array([[3, -5],[4, -2]]) #taking both eqn L.H.S
B = np.array([10, 7]) # taking R.H.S
x, y = np.linalg.solve(A, B) # Solves matrix equations,simple way to solve simultaneous linear eqn
print("Value of x:", x)
print("Value of y:", y)
