"""
https://www.codewars.com/kata/the-millionth-fibonacci-kata/python
"""


def fib_iter(a, b, p, q, n):

    # Base case.
    if n == 0:
        # There are no more transformation to apply, so we're done!
        return b

    # We must apply the T_pq transformation `n` times.
    if (n % 2) == 0:
        # `n` is even, so we can T^2_pq transformation `n/2` times and
        # get the same result.
        return fib_iter(a, b, p*p + q*q, 2*p*q + q*q, n/2)
    else:
        # `n` is odd, so we'll just apply the T_pq transformation once here,
        # then recurse to do the other `n-1` T_pq transformations.
        a, b = b*q + a*q + a*p, b*p + a*q
        return fib_iter(a, b, p, q, n-1)


def pos_fib(n):
    return fib_iter(1, 0, 0, 1, n)


def fib(n):
  """Calculates the nth Fibonacci number"""
  if n == 0:
      return 0
  elif n > 0:
      return pos_fib(n)
  else:
      return pos_fib(-n) * (1 if (n % 2) == 1 else -1)


if __name__ == '__main__':
    print (fib(0) == 0)
    print (fib(1) == 1)
    print (fib(2) == 1)
    print (fib(3) == 2)
    print (fib(4) == 3)
    print (fib(5) == 5)
