"""
https://www.codewars.com/kata/moving-zeros-to-the-end/python
"""

def move_zeros(array):
    def is_zero(val):
        if isinstance(val, bool): return False
        if isinstance(val, (int, float)): return val == 0
        return False
    a = [val for val in array if not is_zero(val)]
    diff = (len(array) - len(a))
    return a + [0] * diff


if __name__ == '__main__':
    print move_zeros([1,2,0,1,0,1,0,3,0,1]) == [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
    print move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    print move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
    print move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
    print move_zeros(["a","b"]) == ["a","b"]
    print move_zeros(["a"]) == ["a"]
    print move_zeros([0,0]) == [0,0]
    print move_zeros([0]) == [0]
    print move_zeros([]) == []
