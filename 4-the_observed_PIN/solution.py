"""
https://www.codewars.com/kata/the-observed-pin/python
"""

def get_pins(observed):
    adjacent = {'1': [1, 2, 4], '2': [2, 1, 3, 5], '3': [3, 2, 6], '4': [4, 1, 5, 7], '5': [5, 2, 4, 6, 8], '6': [6, 3, 5, 9], '7': [7, 4, 8], '8': [8, 5, 7, 9, 0], '9': [9, 6, 8], '0': [0, 8]}
    combos = ['']
    for ob in observed:
        combos = [combo + str(a) for combo in combos for a in adjacent[ob]]
    return combos


if __name__ == '__main__':
    expectations = [('8', ['5','7','8','9','0']),
                    ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                    ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

    for tup in expectations:
        print sorted(get_pins(tup[0])) == sorted(tup[1])
