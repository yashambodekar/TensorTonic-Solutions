def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    L = []
    for i in x:
        if i <= 0:
            curr = alpha * (math.e ** i - 1)
            L.append(curr)
        else :
            L.append(i)

    return L