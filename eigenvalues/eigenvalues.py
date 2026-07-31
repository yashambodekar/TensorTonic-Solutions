import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    if  not(matrix) or not any(matrix) or get_dimension(matrix) < 2 or (len(matrix) != len(matrix[0]))   :
        return None
    matrix = np.array(matrix)
    eigenvalues , eigenvectors = np.linalg.eig(matrix)
    return eigenvalues


def get_dimension(matrix):
    dim = 0
    current = matrix
    
    # Keep diving into the first element if it is a list
    while isinstance(current, list):
        dim += 1
        if len(current) > 0:
            current = current[0]
        else:
            break  # Stop if an empty list is encountered
            
    return dim