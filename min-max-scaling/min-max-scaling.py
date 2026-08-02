import numpy as np
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data = np.array(data)
    max = np.max(data , axis = 0 , keepdims = True)
    min = np.min(data , axis = 0 , keepdims = True)

    range_vals = max - min
    range_vals[range_vals == 0] = 1.0

    arr = (data - min) / range_vals
    return arr.tolist()
