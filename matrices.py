#Define two matrices(A,B) of 3x3 order using numpy.Perform the following operations
# on these matrices.
#1. Find out the inverse of matrix A
#2. Find out the determinant of matrix B
#3. Print the result of (A.A-1) i.e, A.A inverse.
#------------------------------------------------------------------------------------
import numpy as np
A = np.array([[1, 2, 3],[0, 1, 4],[5, 6, 0]])
B = np.array([[2, 1, 3],[1, 0, 2],[4, 1, 1]])
A_inverse = np.linalg.inv(A)
print("Inverse of Matrix A:")
print(A_inverse)
det_B = np.linalg.det(B)
print("\nDeterminant of Matrix B:")
print(det_B)
result = np.dot(A, A_inverse)
print("\n A×A-1:")
print(result)