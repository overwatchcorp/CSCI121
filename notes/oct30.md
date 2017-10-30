# October 30th, 2017 the year of our lord
> Just Thriving

## how to check to see if a list contains a number
given a list of unsorted numbers and the list with the numbers sorted
we can start with a number about in the middle, check to see if it's it
if no, then check if greater or less than targer number, which allows us to eliminate an entire half of the list
contains 27?
1,4,5,*7*,10,19,27,100
27 > 7, so new list
10,19,27,100
repeat, pick one, let's say position 2, 19
27>19, so new lsit
27, 100
let's say we pick 27 🎉 we did it

this is called *binary search*, and it is a term.
pros of binary search
- recursive
cons
- binary as in gender binary hmm

jim's description: if the list has a length of n, then the worst case number of elements we have to check is n/2.
### basic code for binary search
```python
def binary_search(y, xs):
  if len(xs) == 0:
    return False
  else:
    m = (len(xs) - 1) // 2
    if xs[m] == y:
      return True
    else:
      if y < xs[m]:
        return binary_search(y, xs[:m]) # left half
      else:
        return binary_search(y, xs[m+1:]) # right half
```
runs in linear time because the array slicing takes a lot of time when it has to apportion more memory
okay so it takes log base 2 ha ha yeah 
logarithms... like.... log base b (n) / log base a (b) = log base a (n)

## MORE BINARY SEARCH
```python
# l, r is the slice we think it's in xs[l:r+1]
def binary_search(y, xs, l, r):
  # if l is greater than r, that means that the search points have crossed each other and the list does not contain y
  if l > r:
    return False
  else:
    middle = (l+r) // 2
    if xs[m] == y:
      return True
    elif y < xs[m]:
      return binary_search(y, xs, l, m-1)
    else:
      return binary_search(y, xs, m+1, r)
```
this runs in Θ(ln(n)) time, because there is no arry slicing that takes more time

## THE CLASSICAL WAY OF WRITING THIS ALGORITHM WITHOUT RECURSION
> still thriving btw
```python
def search(y, xs):
  l = 0
  r = len(xs) - 1
  while l <= r:
    m = (l + r) // 2
    if xs[m] == y:
      return True
    elif: y < xs[m]:
```
