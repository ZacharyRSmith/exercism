def is_valid_coord(coord):
    return all(0 <= x and x <= 7 for x in coord)


def _validate(white_position, black_position):
    if white_position == black_position:
        raise ValueError(f'Queens cannot be on the same position')
    if not all(is_valid_coord(coord) for coord in [white_position, black_position]):
        raise ValueError(f'Invalid position')


def board(white_position, black_position):
    _validate(white_position, black_position)
    bord = ['_'*8 for i in range(8)]
    i, j = white_position
    bord[i] = bord[i][:j] + 'W' + bord[i][j+1:]
    i, j = black_position
    bord[i] = bord[i][:j] + 'B' + bord[i][j+1:]
    return bord


def is_same_diagonal(wi, wj, bi, bj):
    return abs(wi - bi) == abs(wj - bj)


def can_attack(white_position, black_position):
    _validate(white_position, black_position)
    wi, wj = white_position
    bi, bj = black_position
    return wi == bi or wj == bj or is_same_diagonal(*white_position, *black_position)  # noqa
