def is_armstrong(number):
    sum = 0
    digits = str(number)
    numDigits = len(digits)

    for digit in digits:
        sum += int(digit)**numDigits

    return sum == number
