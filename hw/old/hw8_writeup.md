# Homework 8
> Jasper Fung

## Ordered functions
Slowest to fastest:
`3**x, 2**(x+1), 2**x, 7(x**3) + 10x, 4(x**3), x**2, x*(log(x)/log(2)), 5*x, x**0.5, (log(x)/log(10))**2, log(x)/log(3), log(x)/log(5), 1000`
## LongPalSub
```python
# reverses string, checks to see if reversed string matches input
# returns True if strings match, else returns false
def isPal (n):
    nReversed = n[::-1]
    if n == nReversed:
        return True
    else:
        return False

def longPalSub (n):
  # goes through every substring, checks to see if it is a pal.
  # returns longest pal. string
  longest = ''
  # cache previously checked palindromes
  cache = {}
  for x in range(len(n)):
      for y in range(x, len(n) + 1):
          # don't call if indexes are equal, returns no chars
          if x != y:
              testPal = n[x:y]
              if testPal not in cache:
                  testIsPal = isPal(testPal)
                  cache[testPal] = testIsPal
                  if testIsPal:
                      if len(testPal) > len(longest):
                          longest = testPal
  return longest
```
Since this program uses two nested for loops that iterate through the array, we test each possible substring.
To iterate over an array with a single for loop would take `Θ(n)` time, since it would take as long as there are `n` elements in the array.
Therefore, when we have two for loops, one that iterates over the array in `Θ(n)` time, and another one that iterates over the array inside of that, also in `Θ(n)` time, the running time of the loops is `Θ(n^2)`. However, since we have to reverse the array, which takes `n` time for `n` elements in the array , and we run isPal over every substring, we  add `Θ(n^2)` to the running time, giving us `Θ(2*n^2)`, I think.
The cache offers some performance improvement when working with very long strings as it saves us some array slicing.

## TwoSum
```python
def twoSum(ls, t):
  # if there are one or fewer elements in the array,
  # we cannot sum two elements, so return false
  if len(ls) <= 1:
      return False
  # sum each index with every other index except itself
  for i, n in enumerate(ls):
      for x, b in enumerate(ls):
          if i != x:
              if n + b == t:
                  return True
  return False
```
Since these are two for loops, nested in one another, both running with `Θ(n)` time, the time of twoSum is `Θ(n^2)`.

## ThreeSum
```python
def threeSum(ls, t):
  if len(ls) <= 2:
      return False
  for i, a in enumerate(ls):
      for y, b in enumerate(ls):
          for z, c in enumerate(ls):
              if i != z and i != y and y != z:
                  if a + b + c == t:
                      return True
  return False
```
This is the same as twoSum, except it adds another for loop. So, it runs with `Θ(n^3)` time.

## maxSublist
```python
def maxSublist (xs):
  lxs = len(xs)
  highest = 0
  highestStart = 0
  highestEnd = 0
  for x in range(lxs + 1):
      for y in range(x, lxs + 1):
          thisSum = sum(xs[x:y])
          if thisSum > highest:
            highest = thisSum
            highestStart = x
            highestEnd = y
  return xs[highestStart:highestEnd]
```
This is very similar to longPalSub, including the array slicing. The nested for loops take `Θ(n^2)` time, and the array slicing is run over every possible array slice, so it runs with `Θ(n^2)` time as well. Together, maxSublist takes `Θ(2*n^2)` time as well.
