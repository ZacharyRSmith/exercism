import re


def decode(arg):
    res = ''
    for elt in re.findall(r'\d*[^\d]', arg):
        if re.search('\d', elt) is None:
            res += elt
        else:
            res += int(re.findall(r'\d*', elt)[0]) * elt[-1]
    return res

# def decode(arg):
#     res = ''
#     ary = re.split('([^\d])', arg)

#     for i in xrange(0, len(ary) - 1, 2):
#         run_len = ary[i]
#         run_char = ary[i + 1]

#         if run_len.isdigit():
#             res += run_char * int(run_len)
#         else: # is an empty str, so add run_char only once
#             res += run_char

#     return res

def encode(arg):
    res = ''
    compile_to_repeats = re.compile(r'(.)\1*')
    ary = [match.group() for match in compile_to_repeats.finditer(arg)]

    for elt in ary:
        if len(elt) is 1:
            res += elt[0]
        else:
            res += str(len(elt)) + elt[0]

    return res
