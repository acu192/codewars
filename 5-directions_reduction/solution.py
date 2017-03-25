"""
https://www.codewars.com/kata/directions-reduction/python
"""

def dirReduc(arr):
    s = ''.join([d[0] for d in arr])
    while True:
        o = s
        s = s.replace('NS', '')
        s = s.replace('SN', '')
        s = s.replace('EW', '')
        s = s.replace('WE', '')
        if o == s:
            break
    lookup = {'N': 'NORTH', 'S': 'SOUTH', 'E': 'EAST', 'W': 'WEST'}
    return [lookup[c] for c in s]


if __name__ == '__main__':

    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print  dirReduc(a) == ['WEST']

    u=["NORTH", "WEST", "SOUTH", "EAST"]
    print dirReduc(u) == ["NORTH", "WEST", "SOUTH", "EAST"]
