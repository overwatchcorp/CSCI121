is_even = lambda i: True if i % 2 == 0 else False

def conditional_print(test):
    return lambda toPrint: print(toPrint) if test(toPrint) else None

print_evens = conditional_print(is_even)
