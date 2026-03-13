import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here

    if rng is None:
        rng = np.random.default_rng()

    x = np.array(x)
    n = len(x)

    boot_means = []
  

    for _ in range (n_bootstrap):
        sample = rng.choice(x , size=n , replace=True)
        boot_means.append(np.mean(sample))

    boot_means = np.array(boot_means)

    a = (1 - ci) / 2

    lower = np.quantile(boot_means,a)
    upper = np.quantile(boot_means,1-a)

    return (boot_means,lower,upper)
        
    pass
