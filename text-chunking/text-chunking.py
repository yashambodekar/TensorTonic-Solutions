def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    L = []
    i = 0 
    while i < len(tokens) - overlap :
        curr = []
        flag = True
        for k in range(chunk_size):
            curr.append(tokens[i])
            i += 1
            if(i >= len(tokens)):
                flag == False
                break
        L.append(curr)
        if flag == False :
            break
        i -= overlap

    return L