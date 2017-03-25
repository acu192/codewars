"""
https://www.codewars.com/kata/nim/python
"""

def choose_move(game_state):
    """Chooses a move to play given a game state"""
    # https://en.wikipedia.org/wiki/Nim#Winning_positions
    nim_sum = 0
    for val in game_state:
        nim_sum ^= val
    if nim_sum == 0:
        raise Exception("You can't win because the nim sum is zero.")
    for i, val in enumerate(game_state):
        if (val ^ nim_sum) < val:
            return (i, val - (val ^ nim_sum))
    raise Exception("You can't win because no pile is suitable.")

