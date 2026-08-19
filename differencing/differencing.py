def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here(
    L = series
    for i in range(order):
        curr = []
        for j in range(1 , len(L)):
            curr.append(L[j] - L[j - 1])
        L = curr
    return L