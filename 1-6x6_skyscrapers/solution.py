"""
https://www.codewars.com/kata/6-by-6-skyscrapers/python
"""

from collections import defaultdict


N = 6
"""
We're using a 6x6 board.
"""


def count_clues(clues, check_i, check_j):
    """
    This function counts how many clues the given row and/or column has.
    In some puzzles, many of the clues are missing, so this function
    is a handy way to query for a given row and/or column, how many
    clues does it have.
    This is used in the function `get_visit_order()` to help know
    which rows/columns should be filled in first. Rows/columns with
    more clues should be filled in first because that will create a
    smaller search space.
    """
    c1 = clues[check_j]                   # columns from the top
    c2 = clues[N + check_i]               # rows from the right
    c3 = clues[N + N + (N-1-check_j)]     # columns from the bottom
    c4 = clues[N + N + N + (N-1-check_i)] # rows from the left
    c1 = 1 if c1!=0 else 0                # has clue or not
    c2 = 1 if c2!=0 else 0                # has clue or not
    c3 = 1 if c3!=0 else 0                # has clue or not
    c4 = 1 if c4!=0 else 0                # has clue or not
    total = 0
    if check_i is not False:
        total += c2 + c4
    if check_j is not False:
        total += c1 + c3
    return total


def get_visit_order(clues):
    """
    We want to search the possibilities by filling in rows/columns
    with clues FIRST. That will allow the search space to be pruned
    more and allow our whole search to terminate MUCH faster. So, this
    function will give us an order on which to fill in cells so that
    the search tree is smallish.

    THIS FUNCTION CAN BE OPTIMIZED MORE! BUT IT DOES SEEM THAT THIS
    IMPL DOES AN OKAY JOB GIVING A REASONABLY FAST VISITATION ORDER.
    I'M SURE IT CAN BE IMPROVED THOUGH.
    """
    # Get a list of row indexes, order by visit first-to-last.
    counts = {i: count_clues(clues, i, False) for i in range(N)}
    weights = defaultdict(list)
    for i, s in counts.iteritems():
        weights[s].append(i)
    keys = sorted(weights.keys())[::-1]
    rows = []
    for key in keys:
        rows.extend(weights[key])
    row_sum = sum(keys)

    # Get a list of column indexes, order by visit first-to-last.
    counts = {j: count_clues(clues, False, j) for j in range(N)}
    weights = defaultdict(list)
    for i, s in counts.iteritems():
        weights[s].append(i)
    keys = sorted(weights.keys())[::-1]
    cols = []
    for key in keys:
        cols.extend(weights[key])
    col_sum = sum(keys)

    # It helps to explore EITHER a whole row at a time or a whole column at a time.
    # So depending on if rows are generally better or if columns are generally better,
    # we'll choose one over the other to be our order.
    if row_sum <= col_sum:
        final = [(i, j) for i in rows for j in range(N)]
    else:
        final = [(i, j) for j in cols for i in range(N)]
    return final


def count(lst):
    """
    This function counts the number of visible building in the list
    of building heights given. The given list might have zeros in it
    meaning we don't yet have a building in that position.
    This function computes the minimum possible visible buildings AND
    the maximum possible visible buildings, two values which might
    be different depending on what building are put into the missing spots.

    THIS FUNCTION MIGHT BE WRONG! BUT IT DOES SEEM TO PASS THE TESTS.

    This function simply puts building in the missing spots in increasing order
    THEN in decreasing order and counts the number of visible building in each
    arrangement. You would think that putting them in decreasing order would
    minimize the visible buildings, but that's not the case. Similarly, you'd
    think that putting them in increasing order would maximize the visible
    buildings, but that's also not the case. I do believe that these two arrangements
    give the min and max, it's just not clear which will be which ahead of time.
    Here's a weird example to show my point:

        me   -> looking this way ->    1 3 4 - 6 -
    """
    avail_inc = sorted(list(set(range(1, N+1)) - set(lst)))
    avail_dec = avail_inc[::-1]

    l = 0
    c = 0
    for v in lst:
        if v == 0:
            v = avail_inc.pop()
        if v > l:
            l = v
            c += 1
    option_a = c

    l = 0
    c = 0
    for v in lst:
        if v == 0:
            v = avail_dec.pop()
        if v > l:
            l = v
            c += 1
    option_b = c

    return min(option_a, option_b), max(option_a, option_b)


def check_clues(clues, curr_soln, check_i, check_j):
    """
    The way this function is now is a huge win for speed. Here's the key:
    When you change one cell, you only need to check the clues of that cell's
    row and columns (at most four possible clues). No other clues need to be
    checked; if the other clues were satisfied before this cell was changed,
    they will remain satisfied now.

    So, this function only checks at most 4 clues: the ones of the cell
    which was just modified.

    Next thing which makes this fast. When it encounters a row/column with
    missing buildings, it computes (using the `count()` function above) what
    the min and max possible visible building are; if it looks at one of these
    rows/cols and discovers that it's not possible to satisfy a corresponding clue,
    it returns False immediately so that this part of the search tree is pruned
    away and no more searching is done on this inevitably doomed path.
    """
    r = True   # <- default to "all clues are fully satisfied here"

    clue = clues[check_j]   # column from the top
    if clue != 0:
        min_pos, max_pos = count([curr_soln[i][check_j] for i in range(N)])
        if min_pos > clue or max_pos < clue:
            return False   # <- this branch is impossible and should be pruned
        elif min_pos != max_pos:  # <- there is more to be explored here, make note of it
            r = None   # <- means "clue is not yet satisfied, but more exploring is needed"

    clue = clues[N + check_i]  # row from the right
    if clue != 0:
        min_pos, max_pos = count([curr_soln[check_i][j] for j in range(N-1, -1, -1)])
        if min_pos > clue or max_pos < clue:
            return False
        elif min_pos != max_pos:
            r = None

    clue = clues[N + N + (N-1-check_j)]  # column from the bottom
    if clue != 0:
        min_pos, max_pos = count([curr_soln[i][check_j] for i in range(N-1, -1, -1)])
        if min_pos > clue or max_pos < clue:
            return False
        elif min_pos != max_pos:
            r = None

    clue = clues[N + N + N + (N-1-check_i)]  # row from the left
    if clue != 0:
        min_pos, max_pos = count([curr_soln[check_i][j] for j in range(N)])
        if min_pos > clue or max_pos < clue:
            return False
        elif min_pos != max_pos:
            r = None

    return r


def r_solve_puzzle(clues, curr_soln, col_avail, row_avail, visit_order, curr_visit_index, pi=0, pj=0):
    """
    This recursive function does the exploring of the solution space. At every step
    it calls the `check_clues()` function above to ensure that this exploration
    path is still valid and should be explored further. It only ever checks the most
    recent change, but inductively if it does this for every change we're good (see
    the slightly longer explanation in the `check_clues()` function). It knows when
    it gets to the end, and if it's at the end and all clues are satisfied now (and
    inductively all in the past as well), then WE HAVE A SOLUTION!
    """
    c = check_clues(clues, curr_soln, pi, pj)   # check the previous change
    if c is True and curr_visit_index == len(visit_order):
        return tuple(tuple(row) for row in curr_soln)   # we have a solution!
    elif c is False:
        return False        # we're at a dead end -- there is no solution along this pathway
    else:  # c is None
        pass  # this condition means we're not finished, but we're not at a dead-end yet either.
    i, j = visit_order[curr_visit_index]
    for v in range(1, N+1):
        if v in col_avail[j] and v in row_avail[i]:
            col_avail[j].remove(v)
            row_avail[i].remove(v)
            curr_soln[i][j] = v
            res = r_solve_puzzle(clues, curr_soln, col_avail, row_avail, visit_order, curr_visit_index+1, i, j)
            curr_soln[i][j] = 0
            col_avail[j].add(v)
            row_avail[i].add(v)
            if res is not False:
                return res
    return False


def solve_puzzle(clues):
    """
    Kick it all off. We keep track of the current board-state, which values are
    available for each row and each column, and which cell we're exploring at
    each step along the exploration path. We then call our recursive function
    to do the exploring.
    """
    curr_soln = [[0 for j in range(N)] for i in range(N)]
    col_avail = [set(range(1, N+1)) for i in range(N)]
    row_avail = [set(range(1, N+1)) for i in range(N)]
    visit_order = get_visit_order(clues)
    return r_solve_puzzle(clues, curr_soln, col_avail, row_avail, visit_order, 0)


if __name__ == '__main__':
    clues = ( 3, 2, 2, 3, 2, 1,
              1, 2, 3, 3, 2, 2,
              5, 1, 2, 2, 4, 3,
              3, 2, 1, 2, 2, 4)
    expected = (( 2, 1, 4, 3, 5, 6 ),
                ( 1, 6, 3, 2, 4, 5 ),
                ( 4, 3, 6, 5, 1, 2 ),
                ( 6, 5, 2, 1, 3, 4 ),
                ( 5, 4, 1, 6, 2, 3 ),
                ( 3, 2, 5, 4, 6, 1 ))
    actual = solve_puzzle(clues)
    print actual == expected

    clues = ( 0, 0, 0, 2, 2, 0,
              0, 0, 0, 6, 3, 0,
              0, 4, 0, 0, 0, 0,
              4, 4, 0, 3, 0, 0)
    expected = (( 5, 6, 1, 4, 3, 2 ),
                ( 4, 1, 3, 2, 6, 5 ),
                ( 2, 3, 6, 1, 5, 4 ),
                ( 6, 5, 4, 3, 2, 1 ),
                ( 1, 2, 5, 6, 4, 3 ),
                ( 3, 4, 2, 5, 1, 6 ))
    actual = solve_puzzle(clues)
    print actual == expected

    clues = ( 0, 3, 0, 5, 3, 4,
              0, 0, 0, 0, 0, 1,
              0, 3, 0, 3, 2, 3,
              3, 2, 0, 3, 1, 0)
    expected = (( 5, 2, 6, 1, 4, 3 ),
                ( 6, 4, 3, 2, 5, 1 ),
                ( 3, 1, 5, 4, 6, 2 ),
                ( 2, 6, 1, 5, 3, 4 ),
                ( 4, 3, 2, 6, 1, 5 ),
                ( 1, 5, 4, 3, 2, 6 ))
    actual = solve_puzzle(clues)
    print actual == expected
