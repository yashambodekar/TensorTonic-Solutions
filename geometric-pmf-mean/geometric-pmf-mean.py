import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k)
    ans = ((1 - p) ** (k - 1)) * p
    mean = 1 / p
    res = (np.array(ans) , mean)
    return res
    pass