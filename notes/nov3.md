# November 3rd, 2017 The Year Of Our Lord

## Mergesort
1. Split the list in half
2. Sort each halves
3. Merge each list by comparing the same index on both lists (the smallest position in that one half list), then seeing which one is smallest and putting that first
```python
def mergesort (xs):
  if len(xs) > 1:
    middle = len(xs) // 2
    lefts = xs[:middle]
    rights = xs[middle:]
    mergesort(lefts)
    mergesort(rights)
    merge(lefts,rights,xs)

def merge (ls,rs,xs):
  # indexes
  # xi: position in list, li: position in left index, ri: position in right index
  xi, li, ri = 0, 0, 0
  while xi < len(xs):
    # ensure that left index is not out of range
    if ls[li] <= rs[ri] or ls[li] <= rs[ri]:
      xs[xi] = ls[li]
      li += 1
    else:
      xs[xi] = rs[ri]
      ri += 1
    xi += 1
```
## Quicksort
does work before calling self recursively
picks value called pivot value, could be value on the left, could be random, take median of left, middle, and right
place values less than pivot value before pivot and larger after, sort each list and then it's all sorted
### how to partitition
`[pivot value][less than][greater than][unsorted values]`
if value v is less than or equal to p, swap leftmost greater than value with v's position to put it at end of less than list
if it is greater than, then we don't need to do anything
quicksort doesn't need to create more arrays with this partitioning method, so it uses less memory
```python
def quicksort (xs):
  quicksort_helper(xs, 0, len(xs)-1)

def quicksort_helper (xs, left, right):
  if left < right:
    pivot = partition(xs, left, right)
    quicksort_helper(xs, left, pivot - 1)
    quicksort_helper(xs, pivot + 1, right)

def partition (xs, first, last):
  pivot, pivot_value, = first, xs[first]
  i = first + 1
  while i <= last:
    if xs[i] <= pivot_value:
      xs[pivot +1], xs[i] = xs[i], xs[pivot+1]
      pivot = pivot + 1
    i += 1
  xs[first],xs[pivot] = xs[pivot],xs[first]
  return pivot
```
