def cells(matrix):
    if not len(matrix) or not len(matrix[0]):
        return
    height, width = len(matrix), len(matrix[0])
    for i in range(height):
        for j in range(width):
            yield matrix[i][j], i, j


def col(matrix, j):
    for i in range(len(matrix)):
        yield matrix[i][j]


def _validate_matrix(matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            raise ValueError(f'rows and cols must all be the same length.')


def saddle_points(matrix):
    _validate_matrix(matrix)
    return set((i, j) for cell, i, j in cells(matrix)
               if max(matrix[i]) == cell and min(col(matrix, j)) == cell)
