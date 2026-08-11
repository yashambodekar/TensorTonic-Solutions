import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE
    L = []
    norm = 1
    for i in range(T):
        L.append(norm)
        curr = np.linalg.norm(W_hh , ord = 2)
        norm = norm * curr
        

    return L