def saddle_points(matrix):
    def _validate_matrix():
        for i in range(len(matrix)):
            if len(matrix[i]) != len(matrix):
                raise ValueError(f'rows and cols must all be the same length.')

    def _gteAllOnRow(i, j, val):
        for otherJ in range(len(matrix[0])):
            if otherJ == j:
                continue
            if val < matrix[i][otherJ]:
                return False
        return True

    def _lteAllOnCol(i, j, val):
        for otherI in range(len(matrix)):
            if otherI == i:
                continue
            if val > matrix[otherI][j]:
                return False
        return True

    _validate_matrix()
    results = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = matrix[i][j]
            if _gteAllOnRow(i, j, val) and _lteAllOnCol(i, j, val):
                results.add((i, j))

    return results
