# Create a matrix of 4x4 order and find out the transpose of the matrix 
# and the rank of the matrix using scipy.
#--------------------------------------------------------------------------
import numpy as np
from scipy import linalg
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
transpose = A.T
print("Original Matrix:")
print(A)
print("\nTranspose of Matrix:")
print(transpose)

print("\nRank of Matrix:")
print(np.linalg.matrix_rank(A))