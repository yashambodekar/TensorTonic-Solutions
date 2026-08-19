def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    L = []
    ema = values[0]
    L.append(ema)
    for i in range(1 , len(values)):
        ema = alpha * values[i] + (1 - alpha) * ema
        L.append(ema)

    return L

    