import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    x = (math.e ** (x) - math.e ** (-1 * x)) / (math.e ** (x) + math.e ** (-1 * x))
    return x
