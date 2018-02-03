import ast
import re

ops = [
    'plus',
    'minus',
    'multiplied',
    'divided'
]
op_dict = {
    'plus': '+',
    'minus': '-',
    'multiplied by': '*',
    'divided by': '/',
}


def by_twos(lst):
    for i in range(0, len(lst), 2):
        yield lst[i], lst[i+1]


def is_number(string):
    try:
        int(string)
    except Exception as e:
        return False
    return True


def _normalize(question):
    q = question.lower().replace('?', '')
    for k, v in op_dict.items():
        q = q.replace(f' {k} ', f' {v} ')
    q = re.split(r'\s+', q)
    q = [part for part in q if is_number(part) or part in op_dict.values()]
    if len(q) < 3:
        raise ValueError(f'No calc detected in "{q}".')
    for i in range(0, len(q), 2):
        if not is_number(q[i]):
            raise ValueError(f'Cannot calc "{q}".')
    for i in range(1, len(q), 2):
        if is_number(q[i]):
            raise ValueError(f'Cannot calc "{q}".')
    return q


def _calc(lt, op, rh):
    if op == '+':
        return lt + int(rh)
    elif op == '-':
        return lt - int(rh)
    elif op == '*':
        return lt * int(rh)
    else:  # divided
        return lt / int(rh)


def calculate(question):
    q = _normalize(question)
    # print(q)
    res = int(q[0])
    for op, num in by_twos(q[1:]):
        res = _calc(res, op, num)

    return res
