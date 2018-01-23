import collections


def _isIter(item):
    return isinstance(item, collections.Iterable) and type(item) != str


def flatten(iterable):
    res = []

    for item in iterable:
        if item is None:
            continue
        if _isIter(item):
            res.extend(flatten(item))
        else:
            res.append(item)

    return res
