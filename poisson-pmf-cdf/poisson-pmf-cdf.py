import numpy as np
import math
def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    e = math.e
    pmf = (e ** (-lam)) * ((lam) ** k) / math.factorial(k)

    cdf = 0.0

    for i in range(0 , k + 1):
        cdf += (e ** (-lam)) * ((lam) ** i) / math.factorial(i)

    return(pmf , cdf)
    pass