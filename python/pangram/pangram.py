from string import ascii_lowercase


def is_pangram(input):
    return all(ltr in input.lower() for ltr in ascii_lowercase)
