import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    x = np.sort(x)
    sum = np.sum(x)
    mean = sum / len(x)

    counter = Counter(x)
    mode = counter.most_common(1)[0][0]

    n = len(x)
    median = 0.0
    if(n % 2 == 0):
        median = (x[n//2] + x[n//2 - 1]) / 2
    else:
        median = x[n//2]
    
    return (mean , median , mode)
    pass