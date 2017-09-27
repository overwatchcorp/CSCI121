def flipper(f):
    def thing(p1, p2):
        return f(p2, p1)
    return thing
