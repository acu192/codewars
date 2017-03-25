"""
https://www.codewars.com/kata/the-observed-pin/python
"""

def get_pins(observed):
    adjacent = {'1': [1, 2, 4], '2': [2, 1, 3, 5], '3': [3, 2, 6], '4': [4, 1, 5, 7], '5': [5, 2, 4, 6, 8], '6': [6, 3, 5, 9], '7': [7, 4, 8], '8': [8, 5, 7, 9, 0], '9': [9, 6, 8], '0': [0, 8]}
    combos = ['']
    for ob in observed:
        combos = [combo + str(a) for combo in combos for a in adjacent[ob]]
    return combos
