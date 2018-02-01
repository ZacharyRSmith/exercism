

def board(input_board_array):
    if not input_board_array:
        return []
    if any(len(row) != len(input_board_array[0]) for row in input_board_array):
        raise ValueError(f'BOOM!')
    if any(cell not in ' *' for row in input_board_array
           for cell in row):
        raise ValueError(f'BOOM!')

    X, Y = len(input_board_array[0]), len(input_board_array)
    bord = [[cell for cell in row] for row in input_board_array]
    for y in range(Y):
        for x in range(X):
            if bord[y][x] == '*':
                continue
            adj_ords = [(y + i, x + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if
                        0 <= y + i < Y and 0 <= x + j < X and (i or j)]
            score = sum([bord[_y][_x] == '*' for _y, _x in adj_ords])
            bord[y][x] = str(score) if score else ' '
    return [''.join(i) for i in bord]
