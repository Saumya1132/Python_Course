# using numpy calculate the inverse of the 2 x 2 matrix

import numpy as np

def calculate_inverse(matrix):
    determinant = np.linalg.det(matrix)
    if determinant == 0:
        print("Matrix is singular, cannot calculate inverse.")
        return None
    
    inverse = np.linalg.inv(matrix)
    return inverse

matrix = np.array([[1, 2], [3, 4]])

inverse = calculate_inverse(matrix)

if inverse is not None:
    print("Inverse of the matrix:")
    print(inverse)
    print("Product of the matrix and its inverse:")
    print(np.dot(matrix, inverse))
    print("Product of the inverse and the matrix:")
