import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    # vocab = np.array(vocab)
    d = {word: index for index, word in enumerate(vocab)}
    a = np.zeros(len(vocab) , dtype = int)
    for i in tokens:
        if i in vocab:
            a[d[i]] += 1
    return a