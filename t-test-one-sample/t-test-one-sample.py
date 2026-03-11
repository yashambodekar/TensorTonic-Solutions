import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.array(x)
    n = len(x)

    mean = np.sum(x) / n
    curr = (x - mean) ** 2
    
    std = (np.sum(curr) / (n - 1)) ** 0.5
    den = std / ((n) ** 0.5)
    t = (mean - mu0) / den
    
    return float(t)
    pass