import re
Plain = 'abcdefghijklmnopqrstuvwxyz'
Cipher = 'zyxwvutsrqponmlkjihgfedcba'
lookup = dict(zip(Plain, Cipher))
back_lookup = dict(zip(Cipher, Plain))


def decode(ciphertext: str) -> str:
    return ''.join(back_lookup[ch] for ch in ciphertext if ch != ' ')


def encode(plaintext: str) -> str:
    encoded = ''.join(encode_ch(ch) for ch in re.sub('\W', '', plaintext))
    return ' '.join([encoded[i:i + 5] for i in range(0, len(encoded), 5)])


def encode_ch(ch: char) -> char:
    if ch.lower() not in lookup:
        return ch
    return lookup[ch.lower()]
