import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    arr = np.array(x)
    arr = 1 / (1 + (math.e ** (-1 * arr)))
    return arr