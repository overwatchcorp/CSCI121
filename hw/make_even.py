def make_even(xs):
    for index, n in enumerate(xs):
        if n % 2 == 1:
            xs[index] = n - 1

