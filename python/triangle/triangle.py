def are_triangle_sides_valid(sides):
    if any(side <= 0 for side in sides):
        # raise ValueError(f'side <= 0 found in "{sides}"')
        return False
    permutations = [
        [[0, 1], 2],
        [[0, 2], 1],
        [[1, 2], 0]
    ]
    for two_sides, side_c, in permutations:
        side_a, side_b = two_sides
        if sides[side_a] + sides[side_b] < sides[side_c]:
            # raise ValueError(f'the sum of the lengths of two sides must be greater than or equal to the length of the third side, but "{sides}".')
            return False
    return True


def is_equilateral(sides):
    if not are_triangle_sides_valid(sides):
        return False
    return len(set(sides)) == 1


def is_isosceles(sides):
    if not are_triangle_sides_valid(sides):
        return False
    return len(set(sides)) <= 2


def is_scalene(sides):
    if not are_triangle_sides_valid(sides):
        return False
    return len(set(sides)) == 3
