def index_gen(coord, shape):
    neighbors_ = (-1, 0, 1)
    for dx in neighbors_:
        for dy in neighbors_:
            if not (dx == 0 and dy == 0):
                new_x, new_y = coord[0] + dx, coord[1] + dy
                if 0 <= new_x < shape[0] and 0 <= new_y < shape[1]:
                    yield (new_x, new_y)
    raise StopIteration


def validate(cell, i, j):
    if cell not in ' *':
        raise ValueError(f'invalid cell encountered: {cell}')


def validate_shape(matrix):
    if min(len(row) for row in matrix) != max(len(row) for row in matrix):
        raise ValueError(f'all rows must be of same size')


def each_cell(matrix, fn):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            fn(cell, i, j)


def board(input_board_array):
    if not input_board_array:
        return []
    if input_board_array == list():
        return []
    each_cell(input_board_array, validate)
    validate_shape(input_board_array)
    output_board_array = [[0 if cell == ' ' else cell for cell in row]
                          for row in input_board_array]

    def incr_adj_cells_if_self_is_mine(cell, i, j):
        shape = (len(input_board_array), len(input_board_array[0]))
        if cell != '*':
            return
        for i1, j1 in index_gen((i, j), shape):
            if output_board_array[i1][j1] == '*':
                continue
            output_board_array[i1][j1] += 1

    each_cell(input_board_array, incr_adj_cells_if_self_is_mine)

    return [''.join(str(y) if y != 0 else ' ' for y in x)
            for x in output_board_array]
