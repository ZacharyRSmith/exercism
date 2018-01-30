SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def matches_at(sameOrSmaller, sameOrBigger, idx):
    return sameOrSmaller == sameOrBigger[idx:len(sameOrSmaller)+idx]


def is_sublist(smaller, bigger):
    for i in range(len(bigger) - len(smaller) + 1):
        if smaller == bigger[i:len(smaller) + i]:
            return True
    return False


def check_lists(first_list, second_list):
    len_diff = len(first_list) - len(second_list)
    if len_diff == 0:
        if first_list == second_list:
            return EQUAL
    elif len_diff < 0:
        if is_sublist(smaller=first_list, bigger=second_list):
            return SUBLIST
    else:
        if is_sublist(smaller=second_list, bigger=first_list):
            return SUPERLIST
    return UNEQUAL
