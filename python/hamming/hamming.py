def distance(a, b):
    if len(a) != len(b):
        raise ValueError("Hamming Distance is only defined for strands of " +
                         "equal length")

    return sum(1 for pair in zip(list(a), list(b))
               if pair[0] != pair[1])
