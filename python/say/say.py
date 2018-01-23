def say(number):
    # raise ValueError('input must be a number from 0 to 999,999,999,999, but received "{number}"')
    numToWord = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    tensToWord = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'fourty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }
    hundreds, tens, ones = str(number).zfill(3)
    if numberAsStr in numToWord:
        return numToWord[numberAsStr]
    res = ''
    hundreds = ''
    if len(numberAsStr) == 3:
        hundreds, tens, ones = list(numberAsStr)
    else:
        tens, ones = list(numberAsStr)
    hundreds = f'{numToWord[hundreds]} hundred' if hundreds else ''
    tens = tensToWord[tens] if tens in tensToWord else ''
    ones = '' if ones == '0' else f'-{numToWord[ones]}'
    if hundreds:
        if tens or ones:
            return ' and '.join([hundreds, f'{tens}{ones}'])
        else:
            return hundreds
    else:
        return f"{tens}{ones}"
    # group by 3s
    # if empty, "AND"
