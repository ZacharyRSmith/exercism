def distance(a, b):
    if len(a) != len(b):
        raise ValueError("Hamming Distance is only defined for strands of equal length")

    distance = 0

    for pair in zip(list(a), list(b)):
        if pair[0] != pair[1]:
            distance += 1

    return distance
