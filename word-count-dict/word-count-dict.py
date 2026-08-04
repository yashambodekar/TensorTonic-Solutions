def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    d = dict()
    for i in sentences:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1

    return d