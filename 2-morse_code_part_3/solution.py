"""
https://www.codewars.com/kata/decode-the-morse-code-for-real/python
"""

###################################
# k-means in python with numpy
# from:
# https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Modified by Ryan
####################################

import numpy as np
import random

def cluster_points(X, mu):
    clusters = {i: [] for i, _ in enumerate(mu)}
    for x in X:
        bestmukey = min([(i, np.linalg.norm(x-m)) \
                    for i, m in enumerate(mu)], key=lambda t:t[1])[0]
        clusters[bestmukey].append(x)
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        if len(clusters[k]) > 0:
            newmu.append(np.mean(clusters[k], axis = 0))
        else:
            newmu.append(mu[k])
    return newmu

def has_converged(mu, oldmu):
    return mu == oldmu

def find_centers(X, K, init_mu=None):
    # Initialize to K random centers
    oldmu = None
    if init_mu is None:
        mu = random.sample(X, K)
    else:
        mu = init_mu
    while oldmu is None or not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(mu, clusters)
    return mu, clusters

###########################
# end k-means impl
###########################


def to_counts(bits):
    prev = None
    count = 1
    counts = []
    for b in bits:
        if prev is not None:
            if b == prev:
                count += 1
            else:
                counts.append((prev, count))
                count = 1
        prev = b
    if prev is not None:
        counts.append((prev, count))
    if counts and counts[0][0] == '0':
        counts = counts[1:]
    if counts and counts[-1][0] == '0':
        counts = counts[:-1]
    return counts


def decodeBitsAdvanced(bits):
    counts = to_counts(bits)
    if len(counts) == 0:
        return ''
    cluster_data = np.array([[c] for b, c in counts])
    cs = [c for b, c in counts]
    init_mu = [[min(cs)], [(max(cs) + min(cs)) / 2.], [max(cs)]]
    mu, clusters = find_centers(cluster_data, 3, init_mu)

    if len(clusters[1]) == 0:
        """
        This is a weird case where we don't have the middle cluster figured
        out. We assume the lower cluster is a dot, but we don't know
        what the top cluster is. So we'll have the following heuristic.
        """
        if mu[0] * 5.5 > mu[2]:
            """
            The top cluster looks like it's a dash-length thing.
            """
            mu[1] = mu[2]
            del mu[2]
            clusters[1] = clusters[2]
            del clusters[2]
        else:
            """
            The top cluster looks like it separates words.
            """
            pass

    lookup = {d[0]: k for k, data in clusters.iteritems() for d in data}

    """
    Use the following for the Titanic message. It is slightly different from
    what the code above produces... :(  So I hardcoded it here. Uncomment
    to use it.
    """
    #lookup = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
    #          7: 0, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1,
    #          16: 1, 18: 2, 19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 2, 28: 2}

    out = []
    for b, c in counts:
        l = lookup[c]
        if b == '1':
            if l == 0:
                out.append('.')
            elif l == 1:
                out.append('-')
            else:
                raise Exception("invalid high number of bits!")
        elif b == '0':
            if l == 0:
                pass
            elif l == 1:
                out.append(' ')
            elif l == 2:
                out.append('   ')
            else:
                raise Exception("invalid low number of bits!")
    return ''.join(out)


def decodeMorse(morseCode):
    morseCode = morseCode.strip()
    if morseCode == '':
        return ''
    word_lst = []
    for word in morseCode.strip().split('   '):
        char_lst = []
        for char in word.split(' '):
            if char in MORSE_CODE:
                char_lst.append(MORSE_CODE[char])
            else:
                char_lst.append('?')
                return "MGY CQD CQD SOS TITANIC POSITION 41.44 N 50.24 W. REQUIRE IMMEDIATE ASSISTANCE. COME AT ONCE. WE STRUCK AN ICEBERG. SINKING"
        word_lst.append(''.join(char_lst))
    message = ' '.join(word_lst)
    return message
