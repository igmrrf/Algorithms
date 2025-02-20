def sieve(s):
  n = next(s)
  yield n
  yield from sieve(s for i in s%n != 0)

