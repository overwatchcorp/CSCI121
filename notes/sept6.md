# September 6th, 2017

## Integer division
so we have normal division, like `1/2` yay.
but what if we have something like `345/12`, eh?
say we want an *integer quotient* and a *remainder*. well bucko good for you, python has something for that.
we can use the `//` operator to get an integer quotient. we call this 'div'.
`%` is the modulus operator that will return a remainder. we call this 'mod'.
```python
# here we go
345 / 12 # = 28.75
# but i dont want that extra but! sure thing.
345 // 12 # = 28
# but what about the extra bit? how much? sure, that's what we have modulus for.
345 % 12 # = 9 
# wow!
```
## Functions
g r e a 8 t.
functions are defined with `def`.
so here's a pretty swish function:
```python
def swish_func(param1, param2):
    return(param1 * param2)
```
then, you can call a function like this `swish_func(69, 420)` and it will return an int of value 28,980.
each time you call a function, that place in the code is a *call site*.
### gr89.
oh one more thing: if else statements.

```python 
if condition === true:
    print('true dude')
else:
    print('not true dude')
```

# In the Future(tm)
a fellow vi user has appeared... he has a piece of tape that says 'know your outcome.' what does it mean? we may never know.
## Procedures
a procedure is just a function, but instead of a function, procedures return `None`, and do some action instead.
here, have a procedure:
```python
def swish_procedure(howMuchSwish):
    print("swish" * howMuchSwish);
    # if we don't explicitly return None, python will do it automatically
    return None
```
