def distance(a, b):
    if len(a) != len(b):
        raise ValueError("Hamming Distance is only defined for strands of " +
                         "equal length. like woah!")

    return sum(a != b for a, b in zip(list(a), list(b)))
