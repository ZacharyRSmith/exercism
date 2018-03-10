def is_isogram(string=''):
    '''Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.

    Examples of isograms:

    - lumberjacks
    - background
    - downstream

    The word *isograms*, however, is not an isogram, because the s repeats.
    '''
    for i in range(ord('a'), ord('z')):
        if string.lower().count(chr(i)) > 1:
            return False
    return True
