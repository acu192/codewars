"""
https://www.codewars.com/kata/pete-the-baker/python
"""

def cakes(recipe, available):

    # if stuff in recipe that we don't have, return 0
    if set(recipe.keys()) - set(available.keys()):
        return 0

    # the answer is the minimum of the available multiples
    mults = {k: available[k] / recipe[k] for k in recipe}
    return min(mults.values())

