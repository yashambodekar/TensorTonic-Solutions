import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    if x.ndim == 1:
        max_x = np.max(x , axis = 0 , keepdims = True)
        x = x - max_x
        x = math.e ** x
        sum_x = np.sum(x , axis = 0 , keepdims = True)
        x = x / sum_x
        return x
        
    max_x = np.max(x , axis = 1 , keepdims = True)
    x = x - max_x
    x = math.e ** x
    sum_x = np.sum(x , axis = 1 , keepdims = True)
    x = x / sum_x
    return x
