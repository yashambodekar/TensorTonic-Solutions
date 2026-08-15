import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    for i , value in enumerate(values):
        values[i] = math.log(1 + value)

    return values