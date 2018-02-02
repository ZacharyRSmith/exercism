def cells(matrix):
    height, width = len(matrix), len(matrix[0])
    for i in range(height):
        for j in range(width):
            yield matrix[i][j], i, j


def col(matrix, j):
    for i in range(len(matrix)):
        yield matrix[i][j]


def _validate_matrix(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError(f'rows must all be the same length.')


def saddle_points(matrix):
    _validate_matrix(matrix)
    if not matrix:
        return set()
    return set((i, j) for cell, i, j in cells(matrix)
               if max(matrix[i]) == cell and min(col(matrix, j)) == cell)
