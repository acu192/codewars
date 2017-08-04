def cut_log(p, n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]

    if (n == 0):
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_log(p, n-i, cache))

    cache[n] = q
    return q

