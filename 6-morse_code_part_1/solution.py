"""
https://www.codewars.com/kata/decode-the-morse-code/python
"""

def decodeMorse(morseCode):
    word_lst = []
    for word in morseCode.strip().split('   '):
        char_lst = []
        for char in word.split(' '):
            char_lst.append(MORSE_CODE[char])
        word_lst.append(''.join(char_lst))
    return ' '.join(word_lst)

