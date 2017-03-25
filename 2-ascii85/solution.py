"""
https://www.codewars.com/kata/ascii85-encoding-and-decoding/python
"""

import re
pattern = re.compile(r'\s+')


def encode(piece, allow_z):
    val = 0
    for p in piece:
        val <<= 8
        val += ord(p)
    output = []
    for i in range(5):
        output.append(chr((val % 85) + 33))
        val /= 85
    output = ''.join(output[::-1])
    if allow_z and output == '!!!!!':
        output = 'z'
    return output


def decode(piece):
    val = 0
    for p in piece:
        val *= 85
        val += ord(p)-33
    output = []
    for i in range(4):
        output.append(chr(val & 255))
        val >>= 8
    output = ''.join(output[::-1])
    return output


def toAscii85(data):
    padding = 0
    output = []
    for i in range(0, len(data), 4):
        piece = data[i:i+4]
        if len(piece) < 4:
            padding = 4-len(piece)
            piece = piece + '\0' * padding
        output.append(encode(piece, padding==0))
    output = ''.join(output)
    output = output[0:len(output)-padding]
    return '<~' + output + '~>'


def fromAscii85(data):
    data = data[2:len(data)-2]   # strip <~ and ~>
    data = re.sub(pattern, '', data)
    data = data.replace('z', '!!!!!')
    padding = 0
    output = []
    for i in range(0, len(data), 5):
        piece = data[i:i+5]
        if len(piece) < 5:
            padding = 5-len(piece)
            piece = piece + 'u' * padding
        output.append(decode(piece))
    output = ''.join(output)
    output = output[0:len(output)-padding]
    return output

