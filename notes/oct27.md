# October 27th, 2017
> I return to CS (and I'm thriving)

there is a thing called a prefix sum that is the sum of the 'prefix sums'
works like this
```python
def prefix_sum(xs):
  ps=[]
  for i in range(len(xs)):
    s = 0
    j = 0
    while j <= i:
      s += xs[i]
      j += 1
    ps.append(s)
```
running time of computing prefix sums
given a list of length `n`
each time the while loop runs, we perform one more addition than the previous step
run time is Θ(n^2), not n!.

can improve by not recomputing each time, just add on to total sum
```python
def prefix_sums(xs):
  ps = []
  s = 0
  for x in xs:
    s += x
    ps.append(s)
  return ps
```
this takes Θ(n) time

check if an array contains `True`
```python
def contains(xs, y):
  # determine whether y in xs is True
  i = 0
  while i < len(xs):
    if xs[i] == y:
      return True
    i += 1
  return False
```
Θ(n) time is worst case when index of `n = len(xs)`

### high low game
let's say we have some sorted data, but we can't see it 
we can pick something in the middle and then automatiocally rule out half of the entire list
