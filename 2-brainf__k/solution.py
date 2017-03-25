"""
https://www.codewars.com/kata/my-smallest-code-interpreter-aka-brainf-star-star-k/python
"""

from collections import defaultdict


def inc(x):
    if x == 255:
        return 0
    return x+1


def dec(x):
    if x == 0:
        return 255
    return x-1


def brain_luck(code, inpt):

    open_stack = []

    matching_pos = {}

    for i, instruction in enumerate(code):
        if instruction == '[':
            open_stack.append(i)
        elif instruction == ']':
            open_position = open_stack.pop()
            close_position = i
            matching_pos[open_position] = close_position
            matching_pos[close_position] = open_position


    if len(open_stack) > 0:
        raise Exception("unclosed brackets!")

    mem = defaultdict(int)
    tape_pos = 0

    code_pos = 0

    output = []
    inpt_pos = 0

    while code_pos < len(code):

        instruction = code[code_pos]

        if instruction == '>':
            tape_pos += 1
            code_pos += 1

        elif instruction == '<':
            tape_pos -= 1
            code_pos += 1

        elif instruction == '+':
            mem[tape_pos] = inc(mem[tape_pos])
            code_pos += 1

        elif instruction == '-':
            mem[tape_pos] = dec(mem[tape_pos])
            code_pos += 1

        elif instruction == '.':
            output.append(chr(mem[tape_pos]))
            code_pos += 1

        elif instruction == ',':
            mem[tape_pos] = ord(inpt[inpt_pos])
            inpt_pos += 1
            code_pos += 1

        elif instruction == '[':
            if mem[tape_pos] == 0:
                code_pos = matching_pos[code_pos]+1
            else:
                code_pos += 1

        elif instruction == ']':
            if mem[tape_pos] != 0:
                code_pos = matching_pos[code_pos]+1
            else:
                code_pos += 1

        else:
            raise Exception("unknown instruction")

    return ''.join(output)


if __name__ == '__main__':
    # Echo until byte(255) encountered
    print brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'

    # Echo until byte(0) encountered
    print brain_luck(',[.[-],]', 'Codewars' + chr(0)) == 'Codewars'

    # Two numbers multiplier
    print brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) == chr(72)
