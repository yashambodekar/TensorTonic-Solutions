def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    list = []
    for token in tokens:
        if not token in stopwords:
            list.append(token)
    return list