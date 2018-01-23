def _flatten(iterable):
    while iterable:
        part = iterable.pop(0)

        if isinstance(part, list):
            iterable = part + iterable
        elif part or part == 0:
            yield part


def flatten(iterable):
    return [i for i in _flatten(iterable)]
