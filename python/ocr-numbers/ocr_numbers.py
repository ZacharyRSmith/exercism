num_dict = {
    "0": [
        " _ ",
        "| |",
        "|_|",
        "   "
    ],

    "1": [
        "   ",
        "  |",
        "  |",
        "   "
    ],

    "2": [
        " _ ",
        " _|",
        "|_ ",
        "   "
    ],

    "3": [
        " _ ",
        " _|",
        " _|",
        "   "
    ],

    "4": [
        "   ",
        "|_|",
        "  |",
        "   "
    ],

    "5": [
        " _ ",
        "|_ ",
        " _|",
        "   "
    ],

    "6": [
        " _ ",
        "|_ ",
        "|_|",
        "   "
    ],

    "7": [
        " _ ",
        "  |",
        "  |",
        "   "
    ],

    "8": [
        " _ ",
        "|_|",
        "|_|",
        "   "
    ],

    "9": [
        " _ ",
        "|_|",
        " _|",
        "   "
    ]
}


def num(ocr):
    for k, v in num_dict.items():
        if v == ocr:
            return k
    return '?'


def _validate(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError(f'len(input_grid) % 4 != 0 for "{input_grid}".')
    if len(input_grid[0]) % 3 != 0:
        raise ValueError(f'len(input_grid[0]) % 3 != 0 for "{input_grid}"')


def _parse_row(row):
    for i in range(0, len(row[0]), 3):
        yield [row[j][i:i+3] for j in range(len(row))]


def _get_rows(input_grid):
    for i in range(0, len(input_grid), 4):
        yield input_grid[i:i+4]


def convert(input_grid):
    _validate(input_grid)
    return ','.join(
        ''.join([num(ocr) for ocr in _parse_row(row)])
        for row in _get_rows(input_grid)
    )
