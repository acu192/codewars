"""
https://www.codewars.com/kata/4-by-4-skyscrapers/python
"""

N = 4


def count(lst):
    l = 0
    c = 0
    for v in lst:
        if v > l:
            l = v
            c += 1
    return c


def check_clues(clues, curr_soln):
    visible = []
    for j in range(N):
        c = count([curr_soln[i][j] for i in range(N)])
        visible.append(c)
    for i in range(N):
        c = count([curr_soln[i][j] for j in range(N-1, -1, -1)])
        visible.append(c)
    for j in range(N-1, -1, -1):
        c = count([curr_soln[i][j] for i in range(N-1, -1, -1)])
        visible.append(c)
    for i in range(N-1, -1, -1):
        c = count([curr_soln[i][j] for j in range(N)])
        visible.append(c)
    for viz, clue in zip(visible, clues):
        if clue != 0:
            if viz != clue:
                return False
    return True


def r_solve_puzzle(clues, curr_soln, col_avail, row_avail, i, j):
    if i == N:
        if check_clues(clues, curr_soln):
            return tuple(tuple(row) for row in curr_soln)
        else:
            return None
    ni = i+1 if j == N-1 else i
    nj = 0 if j == N-1 else j+1
    for v in range(1, N+1):
        if v in col_avail[j] and v in row_avail[i]:
            col_avail[j].remove(v)
            row_avail[i].remove(v)
            curr_soln[i][j] = v
            res = r_solve_puzzle(clues, curr_soln, col_avail, row_avail, ni, nj)
            curr_soln[i][j] = 0
            col_avail[j].add(v)
            row_avail[i].add(v)
            if res is not None:
                return res


def solve_puzzle (clues):
    curr_soln = [[0 for j in range(N)] for i in range(N)]
    col_avail = [set(range(1, N+1)) for i in range(N)]
    row_avail = [set(range(1, N+1)) for i in range(N)]
    return r_solve_puzzle(clues, curr_soln, col_avail, row_avail, 0, 0)


if __name__ == '__main__':
    clues = (
        ( 2, 2, 1, 3,
          2, 2, 3, 1,
          1, 2, 2, 3,
          3, 2, 1, 3 ),
        ( 0, 0, 1, 2,
          0, 2, 0, 0,
          0, 3, 0, 0,
          0, 1, 0, 0 )
        )

    outcomes = (
        ( ( 1, 3, 4, 2 ),
          ( 4, 2, 1, 3 ),
          ( 3, 4, 2, 1 ),
          ( 2, 1, 3, 4 ) ),
        ( ( 2, 1, 4, 3 ),
          ( 3, 4, 1, 2 ),
          ( 4, 2, 3, 1 ),
          ( 1, 3, 2, 4 ) )
        )

    print solve_puzzle(clues[0]) == outcomes[0]
    print solve_puzzle(clues[1]) == outcomes[1]
