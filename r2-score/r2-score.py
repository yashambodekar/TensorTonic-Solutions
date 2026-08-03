import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    SSR = (y_pred - y_true)**2
    y_avg = np.mean(y_true)
    SST = (y_true - y_avg)**2
    if np.sum(SST) == 0 :
        if np.sum(SSR) == 0:
            return 1.0
        else :
            return 0.0
    return 1 - np.sum(SSR) / np.sum(SST)