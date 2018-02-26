# translate English to pig latin
# Pig Latin is a made-up children's language that's intended to be
# confusing.
# See <http://en.wikipedia.org/wiki/Pig_latin> for more details.

# - **Rule 1**: If a word begins with a vowel sound, add an "ay" sound to
#   the end of the word.
# - **Rule 2**: If a word begins with a consonant sound, move it to the
#   end of the word, and then add an "ay" sound to the end of the word.
def _translate_word(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if word[0] in vowels:
        return f'{word}ay'
    else:
        return f'{word[1:]}{word[0]}ay'


def translate(text):
    return ''.join(_translate_word(word) for word in text.split(' '))
