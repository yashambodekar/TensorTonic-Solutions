import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.sort(x)
    # print(x)

    index = len(x)
    
    arr = []
    
    for i in q:
        if(i == 0):
            arr.append(x[0])
            continue
        if(i == 100):
            arr.append(x[len(x) - 1])
            continue
        curr = (index - 1) * i / 100
        start = (int)(curr // 1 )
        end = start + 1
        if(start == index - 1):
            end = start
        temp = x[start] + (x[end] - x[start]) * (curr - start)
        print(curr , start , end , sep=" ")
        arr.append(temp)

    ans = np.array(arr)
    return ans
    
    pass