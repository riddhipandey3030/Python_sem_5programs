# Consider the following linear equations and solve using Scipy
# 2x+3y=8
# 4x+5y=14
# Consider a scenario where two cars are moving from one point P and another point Q 
# in the same direction and meet each other after 11 hours. If they move in opposite direction 
# they will meet after 1 hr. Find out the velocity of both cars.
#------------------------------------------------------------------------------------------------
import numpy as np
from scipy.linalg import solve
A = np.array([[2, 3],[4, 5]])
B = np.array([8, 14])
solution = solve(A, B) #to solve linear eqn
print("Solution of linear equations:")
print("x =", solution[0])
print("y =", solution[1])
# Let velocity of first car = x km/hr
# Let velocity of second car = y km/hr
# Same direction: They meet after 11 hours
# D = 11(x - y)
# Opposite direction: They meet after 1 hour
# D = x + y
D = float(input("\nEnter the distance between P and Q in km: "))
# Equations:
# x - y = D/11
# x + y = D
A1 = np.array([[1, -1],[1,  1]])
B1 = np.array([D/11, D])
velocity = solve(A1, B1)
print("\nVelocity of the two cars:")
print("Velocity of first car =", velocity[0], "km/hr")
print("Velocity of second car =",velocity[1], "km/hr")