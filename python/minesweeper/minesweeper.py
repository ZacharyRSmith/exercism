valid_chars = " *12345678"
tt = str.maketrans(' 1234567', '12345678')


def rows_to_board(row_strings):
    return [list(r) for r in row_strings]


def board_to_rows(board):
    return [''.join(r) for r in board]


def neighbors(board, x, y):
    w, h = len(board[0]), len(board)
    min_y, max_y = max(y-1, 0), min(y+2, h)
    min_x, max_x = max(x-1, 0), min(x+2, w)
    for y2 in range(min_y, max_y):
        for x2 in range(min_x, max_x):
            if (x2 == x and y2 == y):
                continue
            yield x2, y2, board[y2][x2] or '1'


def each_cell(board, pred=lambda cell, i, j: True):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if not pred(cell, i, j):
                continue
            yield cell, i, j


def validate(board):
    def validate_cell(cell):
        if cell not in ' *':
            raise ValueError(f'each cell must be ` ` or `*` but received `{cell}`')  # noqa
    for cell, i, j in each_cell(board):
        validate_cell(cell)
    if min(len(row) for row in board) != max(len(row) for row in board):
        raise ValueError('All rows must be of the same length.')


def each_mine(board):
    for cell, i, j in each_cell(board, lambda cell, i, j: cell == '*'):
        yield cell, i, j


def board(row_strings):
    if not row_strings:
        return []
    board = rows_to_board(row_strings)
    validate(board)
    for mine, i, j in each_mine(board):
        for nx, ny, cell in neighbors(board, j, i):
            board[ny][nx] = cell.translate(tt)
    return board_to_rows(board)
