# Create a square matrix of 4x4 order 
#1. Find out the eigen value and eigen vector of this matrix using scipy
#2. Find out permutation matrix p,lower triangular matrix l,and upper triangular matrix u of the matrix.
#-----------------------------------------------------------------------------------------------
import numpy as np
from scipy import linalg
A = np.array([[4, 1, 2, 0],
              [1, 3, 0, 1],
              [2, 0, 5, 2],
              [0, 1, 2, 4]])
# 1. Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = linalg.eig(A)
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
# 2. Find p, l and u
P, L, U = linalg.lu(A)
print("\nPermutation Matrix P:")
print(P)
print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)