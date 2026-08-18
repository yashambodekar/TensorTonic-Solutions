def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    L = []
    for i in range(len(values) - window_size + 1):
        sum = 0
        for k in range(window_size):
            sum += values[i + k]
        L.append(sum / window_size)

    return L
        