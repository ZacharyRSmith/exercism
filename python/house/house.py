LINES = [
    "the horse and the hound and the horn\nthat belonged to ",
    "the farmer sowing his corn\nthat kept ",
    "the rooster that crowed in the morn\nthat woke ",
    "the priest all shaven and shorn\nthat married ",
    "the man all tattered and torn\nthat kissed ",
    "the maiden all forlorn\nthat milked ",
    "the cow with the crumpled horn\nthat tossed ",
    "the dog\nthat worried ",
    "the cat\nthat killed ",
    "the rat\nthat ate ",
    "the malt\nthat lay in ",
    "the house that Jack built.",
]


def rhyme():
    return "\n\n".join(verse(n) for n in range(12))


def verse(v):
    return ''.join(["This is "] + LINES[-v-1:])
