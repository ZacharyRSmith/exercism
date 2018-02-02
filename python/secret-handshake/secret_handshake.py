# 1 = wink
# 10 = double blink
# 100 = close your eyes
# 1000 = jump
# 10000 = Reverse the order of the operations in the secret handshake.
bin_pos_to_op = ['wink', 'double blink', 'close your eyes', 'jump']


def handshake(code):
    b = bin(code)[2:]
    should_reverse = False
    if len(b) == len('10000'):
        b = b[1:]
        should_reverse = True
    res = [bin_pos_to_op[i] for i, ch in enumerate(b[::-1]) if ch == '1']
    return res[::-1] if should_reverse else res


def secret_code(actions):
    pass
