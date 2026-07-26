def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    Set = set(recommended[:k])
    relevant = set(relevant)
    a = Set & relevant
    p = len(a) / k
    r = len(a) / len(relevant)
    return [p , r]