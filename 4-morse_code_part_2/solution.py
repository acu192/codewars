"""
https://www.codewars.com/kata/decode-the-morse-code-advanced/python
"""


def to_counts(bits):
    prev = None
    count = 1
    counts = []
    for b in bits:
        if prev is not None:
            if b == prev:
                count += 1
            else:
                counts.append((prev, count))
                count = 1
        prev = b
    if prev is not None:
        counts.append((prev, count))
    if counts and counts[0][0] == '0':
        counts = counts[1:]
    if counts and counts[-1][0] == '0':
        counts = counts[:-1]
    return counts


def decodeBits(bits):
    counts = to_counts(bits)
    min_high = None
    max_high = None
    for b, c in counts:
        min_high = min(min_high, c) if min_high is not None else c
        max_high = max(max_high, c) if max_high is not None else c
    bit_rate = min_high
    out = []
    for b, c in counts:
        if b == '1':
            if c / bit_rate == 1:
                out.append('.')
            elif c / bit_rate == 3:
                out.append('-')
            else:
                raise Exception("invalid high number of bits!")
        elif b == '0':
            if c / bit_rate == 1:
                pass
            elif c / bit_rate == 3:
                out.append(' ')
            elif c / bit_rate == 7:
                out.append('   ')
            else:
                raise Exception("invalid low number of bits!")
    return ''.join(out)


def decodeMorse(morseCode):
    word_lst = []
    for word in morseCode.strip().split('   '):
        char_lst = []
        for char in word.split(' '):
            char_lst.append(MORSE_CODE[char])
        word_lst.append(''.join(char_lst))
    return ' '.join(word_lst)
