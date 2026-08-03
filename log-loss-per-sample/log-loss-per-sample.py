import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    p = np.clip(y_pred , eps , 1 - eps) 
    loss = -1 * (y_true * np.log(p) + (1 - y_true) * np.log(1 - p))
    return loss.tolist()