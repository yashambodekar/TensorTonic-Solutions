import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    row = []
    col = []
    sum = 0 

    arr = np.array(C)
    sum = np.sum(arr)

    for i in range(0 , len(arr)):
        row.append(np.sum(arr[i]))

    temp = arr.T

    for i in range(0 , len(temp)):
        col.append(np.sum(temp[i]))


    row = np.array(row)
    col = np.array(col)

    matrix = np.outer(row , col)
    matrix = matrix / sum

    ans = np.sum((arr - matrix) ** 2 / matrix)

    result = (ans , matrix)

    return result
    
    pass