"""
https://www.codewars.com/kata/alphabetic-anagrams/python
"""

from collections import Counter


def r_max_word_order(counter, cache):
    """
    Computes the zero-based index of the max word represented by the counter.
    This function is so that we can cache this specific counter configuration.
    E.g. r_max_word_order({'y': 5, 'z': 8}) == r_max_word_order({'a': 5, 'b': 8})
    """

    cache_key = tuple(sorted(counter.values()))
    if cache_key in cache:
        return cache[cache_key]

    max_word = ''.join(ch*count for ch, count in counter.iteritems() if count > 0)
    max_word = ''.join(sorted(max_word, reverse=True))
    index = r_word_order(max_word, cache)

    cache[cache_key] = index
    return index


def r_word_order(word, cache):
    """
    Returns the zero-based index of the word.
    """

    if len(word) == 0:
        return 0
    if len(word) == 1:
        return 0

    counter = Counter(word)

    if word in cache:
        return cache[word]

    order = sorted(counter.keys())   # sorted unique letters
    first = word[0]
    rest  = word[1:]

    index = r_word_order(rest, cache)

    for o in order:
        if o == first:
            break
        counter[o] -= 1
        index += r_max_word_order(counter, cache) + 1
        counter[o] += 1

    cache[word] = index
    return index


def word_order(word):
    """
    Returns the one-based index of the word.
    """
    cache = {}
    return r_word_order(word, cache) + 1


def listPosition(word):
    """Return the anagram list position of the word"""
    return word_order(word)

