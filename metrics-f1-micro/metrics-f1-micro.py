
import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    elements = y_pred == y_true
    TP = np.sum(elements)
    nonTP = len(y_pred) - TP
    return (2 * TP) / (2 * TP + 2 * nonTP)