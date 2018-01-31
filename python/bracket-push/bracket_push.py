# simple solution not fulfilling all requirements
def check_brackets(input_string):
    num_square_open = 0
    num_curly_open = 0
    num_parens_open = 0
    for ch in input_string:
        if ch == '[':
            num_square_open += 1
        elif ch == '{':
            num_curly_open += 1
        elif ch == '(':
            num_parens_open += 1
        elif ch == ']':
            if num_square_open == 0:
                return False
            else:
                num_square_open -= 1
        elif ch == '}':
            if num_curly_open == 0:
                return False
            else:
                num_curly_open -= 1
        elif ch == ')':
            if num_parens_open == 0:
                return False
            else:
                num_parens_open -= 1
    if num_square_open > 0 or num_curly_open > 0 or num_parens_open > 0:
        return False
    return True
