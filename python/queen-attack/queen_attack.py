def is_valid_coord(coord):
    return all(0 <= x and x <= 7 for x in coord)


def _validate_positions(w_pos, b_pos):
    if w_pos == b_pos:
        raise ValueError(f'Queens cannot be on the same position')
    if not all(is_valid_coord(coord) for coord in [w_pos, b_pos]):
        raise ValueError(f'Invalid position')


def board(w_pos, b_pos):
    _validate_positions(w_pos, b_pos)
    _board = [['_']*8 for _ in range(8)]
    _board[w_pos[0]][w_pos[1]] = 'W'
    _board[b_pos[0]][b_pos[1]] = 'B'
    return [''.join(row) for row in _board]


def is_same_diagonal(wi, wj, bi, bj):
    return abs(wi - bi) == abs(wj - bj)


def can_attack(w_pos, b_pos):
    _validate_positions(w_pos, b_pos)
    wi, wj = w_pos
    bi, bj = b_pos
    return wi == bi or wj == bj or is_same_diagonal(*w_pos, *b_pos)
