import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x);
    x = x * (1 / (1 + math.e ** (-1 * x)))
    return x 