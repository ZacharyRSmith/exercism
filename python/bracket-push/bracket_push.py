def get_brackets(string):
    return ''.join(ch for ch in string if ch in '{[()]}')


open_to_close = {
    '{': '}',
    '[': ']',
    '(': ')'
}


def check_brackets(input_string):
    brackets = get_brackets(input_string)

    def recurse(open_bracket, rest):
        while rest:
            next_ch = rest[0]
            if next_ch in open_to_close:
                rest = recurse(next_ch, rest[1:])
            elif open_to_close[open_bracket] == next_ch:
                return rest[1:]
            else:
                return False
        return False

    if len(brackets) == 0:
        return True
    if brackets[0] in open_to_close:
        while len(brackets) > 1:
            brackets = recurse(brackets[0], brackets[1:])
            if brackets is False:
                return False
        return len(brackets) == 0
    return False
