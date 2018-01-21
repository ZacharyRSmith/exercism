def is_armstrong(number: int) -> bool:
    digits = str(number)
    numDigits = len(digits)

    return sum(
        [int(digit) ** numDigits
            for digit in digits]
        ) == number
