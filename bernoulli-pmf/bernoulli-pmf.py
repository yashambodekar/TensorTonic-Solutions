import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    arr = []
    for i in x:
        if(i == 0):
            arr.append(1 - p)
        else:
            arr.append(p)

    mean = p
    variance = p * (1 - p)

    pmf = np.array(arr)

    ans = (pmf , mean , variance)
    return ans
    
    pass