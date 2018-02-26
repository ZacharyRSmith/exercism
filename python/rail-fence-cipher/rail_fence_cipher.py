import math


def encode(rails, message):
    rows = ['' for i in range(message)]
    for i, ch in enumerate(rails):
        crnt_idx = i % (2 * (message - 1))
        if crnt_idx >= message:
            crnt_idx = message - (crnt_idx + 2)
        rows[crnt_idx] += ch
    return ''.join(rows)


def decode(encoded_message, rails):
    rows = ['' for i in range(rails)]
    num_spots = 2 * (rails - 1)
    for i in range(rails):
        rem = len(encoded_message) % rails
        num_to_take = math.floor(len(encoded_message) / rails)
        if i < rem:
            num_to_take += 1
        # num_to_take = math.ceil((len(encoded_message) - (2 * i)) / num_spots)
        # num_to_take = math.ceil((len(encoded_message) - (2 * i)) / num_spots)
        start = sum(len(row) for row in rows)
        print(start, rows)
        row = encoded_message[start:start + num_to_take]
        rows[i] = row
        print(num_to_take, start, row)
    print(rows)
print(len('TEITELHDVLSNHDTISEIIEA'))
# 8
# 7
# 7