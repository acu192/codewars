"""
https://www.codewars.com/kata/matrix-determinant/python
"""

def sub_mat(matrix, exclude_index):
    mat = [row[1:] for i, row in enumerate(matrix) if i != exclude_index]
    return mat

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    sign = 1
    for i in range(n):
        det += sign * matrix[i][0] * determinant(sub_mat(matrix, i))
        sign = -sign
    return det


if __name__ == '__main__':
    m1 = [ [1, 3], [2,5]]
    m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

    print determinant([[1]]) == 1
    print determinant(m1) == -1
    print determinant(m2) == -20
