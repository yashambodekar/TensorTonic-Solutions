import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.sum(x) / len(x)
    x = (x - mean) ** 2
    var = np.sum(x) / (len(x) - 1)
    std = var ** (0.5)
    return(var,std)
    pass