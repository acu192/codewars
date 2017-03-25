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


if __name__ == '__main__':

    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print cakes(recipe, available) == 2

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print cakes(recipe, available) == 0
