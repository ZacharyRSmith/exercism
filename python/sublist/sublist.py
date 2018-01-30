SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def matches_at(sameOrSmaller, sameOrBigger, idx):
    for i, elem in enumerate(sameOrSmaller):
        if sameOrBigger[i + idx] != elem:
            return False
    return True


def check_lists(first_list, second_list):
    len_diff = len(first_list) - len(second_list)
    if len_diff == 0:
        if matches_at(first_list, second_list, 0):
            return EQUAL
    elif len_diff < 0:
        for i in range(-len_diff + 1):
            if matches_at(first_list, second_list, i):
                return SUBLIST
    else:
        for i in range(len_diff + 1):
            if matches_at(second_list, first_list, i):
                return SUPERLIST
    return UNEQUAL
