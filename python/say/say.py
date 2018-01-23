# def _sayGroup(number):
#     numToWord = {
#         '0': 'zero',
#         '1': 'one',
#         '2': 'two',
#         '3': 'three',
#         '4': 'four',
#         '5': 'five',
#         '6': 'six',
#         '7': 'seven',
#         '8': 'eight',
#         '9': 'nine',
#         '10': 'ten',
#         '11': 'eleven',
#         '12': 'twelve',
#         '13': 'thirteen',
#         '14': 'fourteen',
#         '15': 'fifteen',
#         '16': 'sixteen',
#         '17': 'seventeen',
#         '18': 'eighteen',
#         '19': 'nineteen'
#     }
#     tensToWord = {
#         '2': 'twenty',
#         '3': 'thirty',
#         '4': 'fourty',
#         '5': 'fifty',
#         '6': 'sixty',
#         '7': 'seventy',
#         '8': 'eighty',
#         '9': 'ninety'
#     }
#     hundreds, tens, ones = str(number).zfill(3)
#     if tens + ones in numToWord:
#         tens = numToWord[tens + ones]
#     elif tens in tensToWord:
#         tens = tensToWord[tens]
#         if ones != '0':
#             tens += f'-{numToWord[ones]}'
#     else:
#         if ones != '0' or hundreds == '0':
#             tens = numToWord[ones]
#         else:
#             tens = ''
#             # TODO handle when ones is zero and shouldn't output...eg 100

#     res = ''
#     if hundreds != '0':
#         res += f'{numToWord[hundreds]} hundred'
#         if tens:
#             res += f' and {tens}'
#     else:
#         res = tens

#     return res

# def say(number):
#     # raise ValueError('input must be a number from 0 to 999,999,999,999, but received "{number}"')

#     return _sayGroup(number)
import re
line = '12345678901'