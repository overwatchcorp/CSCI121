# August 30th, 2017

#### taking user input
```python
name = input("what's your name?")
print("Hello there, " + name + "!")
```
input *always* returns a string. it's the "raw" input.
also, note the string concatenation using the "+" signs. the interpreter will return an error if `name` is note of type `String`.

say though, that you wanted to have a number. you can do this:
```python
pi = 3.14159
radius = float(input("input the radius"))
area = pi(radius ** 2)
```
Amazing! you can multiply a string to have it repeat! for example: `"csci121 is the best class! " * 1000000` will print "csci121 is the best class! " many times.
