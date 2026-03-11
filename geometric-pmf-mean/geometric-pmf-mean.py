import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k)
    ans = []
    for i in k:
        sum = ((1 - p) ** (i - 1)) * p
        ans.append(sum)
    mean = 1 / p
    res = (np.array(ans) , mean)
    return res
    pass