"""
https://www.codewars.com/kata/hard-sudoku-solver/python
"""

# This is my solution for the 2kyu 'Hard Sudoku Solver', which I solved
# first, prior to this 3kyu kata. I did have to modify this one _slightly_.


import copy
from collections import defaultdict


def get_possible(curr, row_avail, col_avail, grid_avail):
    possible = [[None for j in range(9)] for i in range(9)]
    for i, row in enumerate(curr):
        for j, val in enumerate(row):
            if val != 0:
                possible[i][j] = {val}
                continue
            pos = set(range(1, 10))
            pos &= row_avail[i]
            pos &= col_avail[j]
            pos &= grid_avail[i//3][j//3]
            possible[i][j] = pos
    return possible


def fill_obvious(curr, row_avail, col_avail, grid_avail, possible):
    # See if there are SUPER EASY possibilities. These are spots
    # where there is literally only one possible value to put in it.
    done = True
    for i, row in enumerate(possible):
        for j, pos in enumerate(row):
            if curr[i][j] != 0:
                continue
            if len(pos) == 0:
                return False    # NOT POSSIBLE HERE!
            elif len(pos) == 1:
                p = next(iter(pos))
                curr[i][j] = p
                row_avail[i].remove(p)
                col_avail[j].remove(p)
                grid_avail[i//3][j//3].remove(p)
                return 1         # WE MADE ONE CHANGE
            else:
                done = False
    if done:
        return "done"

    # See one logic level deeper. Are there spots with several possibilities, but
    # one of those possible values is unrepresented in all other positions on that
    # spot's row, column, or grid?
    for i, row in enumerate(curr):
        for j, val in enumerate(row):
            if val != 0:
                continue
            for p in possible[i][j]:
                # Check col:
                only = True
                for other_i in range(9):
                    if i != other_i and p in possible[other_i][j]:
                        only = False
                        break
                if not only:
                    # Check row:
                    only = True
                    for other_j in range(9):
                        if j != other_j and p in possible[i][other_j]:
                            only = False
                            break
                if not only:
                    # Check grid:
                    only = True
                    gi = i//3
                    gj = j//3
                    for other_i in range(gi*3, gi*3+3):
                        for other_j in range(gj*3, gj*3+3):
                            if (i != other_i or j != other_j) and p in possible[other_i][other_j]:
                                only = False
                                break
                if only:
                    curr[i][j] = p
                    row_avail[i].remove(p)
                    col_avail[j].remove(p)
                    grid_avail[i//3][j//3].remove(p)
                    return 1         # WE MADE ONE CHANGE

    return True    # NO CHANGES AND NOT DONE, BUT READY TO CONTINUE TO RECURSIVE STEP


def r_solve(curr, row_avail, col_avail, grid_avail, solutions):
    res = 1
    while res is not True:
        possible = get_possible(curr, row_avail, col_avail, grid_avail)
        res = fill_obvious(curr, row_avail, col_avail, grid_avail, possible)
        if res is False:
            return
        if res == "done":
            solutions.append(copy.deepcopy(curr))
            return

    # There are no more obvious moves here (i.e. res is True here).
    # That means we have to recurse.

    counts = defaultdict(list)
    for i, row in enumerate(possible):
        for j, pos in enumerate(row):
            if curr[i][j] == 0:
                counts[len(pos)].append((i, j))

    m = min(counts.keys())
    i, j = next(iter(counts[m]))

    for p in possible[i][j]:
        n_curr = copy.deepcopy(curr)
        n_row_avail = copy.deepcopy(row_avail)
        n_col_avail = copy.deepcopy(col_avail)
        n_grid_avail = copy.deepcopy(grid_avail)
        n_curr[i][j] = p
        n_row_avail[i].remove(p)
        n_col_avail[j].remove(p)
        n_grid_avail[i//3][j//3].remove(p)
        r_solve(n_curr, n_row_avail, n_col_avail, n_grid_avail, solutions)


def solve(puzzle):

    # Check size of board.
    assert len(puzzle) == 9
    for row in puzzle:
        assert len(row) == 9

    # Data structures to keep track of what is available on the rows/cols/grid-groups:
    row_avail = [set(range(1, 10)) for i in range(9)]
    col_avail = [set(range(1, 10)) for j in range(9)]
    grid_avail = [[set(range(1, 10)) for j in range(3)] for i in range(3)]

    # Insert the given numbers (and ensure for legitness).
    curr = [[0 for j in range(9)] for i in range(9)]
    for i, row in enumerate(puzzle):
        for j, val in enumerate(row):
            if val == 0:
                continue
            assert val >= 1 and val <= 9
            assert val in row_avail[i]
            assert val in col_avail[j]
            assert val in grid_avail[i//3][j//3]
            row_avail[i].remove(val)
            col_avail[j].remove(val)
            grid_avail[i//3][j//3].remove(val)
            curr[i][j] = val

    # Solve it.
    solutions = []
    r_solve(curr, row_avail, col_avail, grid_avail, solutions)
    if len(solutions) < 1:
        raise Exception("{} solutions".format(len(solutions)))
    return solutions[0]


if __name__ == '__main__':

    problem = [[9, 0, 0, 0, 8, 0, 0, 0, 1],
               [0, 0, 0, 4, 0, 6, 0, 0, 0],
               [0, 0, 5, 0, 7, 0, 3, 0, 0],
               [0, 6, 0, 0, 0, 0, 0, 4, 0],
               [4, 0, 1, 0, 6, 0, 5, 0, 8],
               [0, 9, 0, 0, 0, 0, 0, 2, 0],
               [0, 0, 7, 0, 3, 0, 2, 0, 0],
               [0, 0, 0, 7, 0, 5, 0, 0, 0],
               [1, 0, 0, 0, 4, 0, 0, 0, 7]]

    solution = [[9, 2, 6, 5, 8, 3, 4, 7, 1],
                [7, 1, 3, 4, 2, 6, 9, 8, 5],
                [8, 4, 5, 9, 7, 1, 3, 6, 2],
                [3, 6, 2, 8, 5, 7, 1, 4, 9],
                [4, 7, 1, 2, 6, 9, 5, 3, 8],
                [5, 9, 8, 3, 1, 4, 7, 2, 6],
                [6, 5, 7, 1, 3, 8, 2, 9, 4],
                [2, 8, 4, 7, 9, 5, 6, 1, 3],
                [1, 3, 9, 6, 4, 2, 8, 5, 7]]

    print solve(problem) == solution
