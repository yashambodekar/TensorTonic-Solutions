def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    sums = {}
    counts = {}

    for cat , tar in zip(categories , targets):
        sums[cat] = sums.get(cat , 0) + tar
        counts[cat] = counts.get(cat , 0) + 1

    means = {cat : sums[cat] / counts[cat] for cat in sums}

    return [means[cat] for cat in categories]