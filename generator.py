def infinite(base, mult):
    i = 0
    while i < mult:
        base *= mult
        print(base)
        i += 1
        print(i)
    yield base


gen = next(infinite(1, 10))


print(gen)
