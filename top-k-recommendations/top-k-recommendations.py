def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    d = {}
    for i , score in enumerate(scores):
        if i not in rated_indices:
            d[i] = score


    sorted_item = sorted(d.items() , key = lambda x : (-x[1] , x[0]))
    L = [item[0] for item in sorted_item[:k]]
    return L
    # Write code here