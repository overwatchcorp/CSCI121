def reverse_of(xs):
    rxs = [xs[-1]] + reverse_of(xs[:-1]) if xs else []
    return rxs
