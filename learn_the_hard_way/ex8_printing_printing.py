formatter = "{} {} {} {}"  # see? no need to put 0 1 2 3 inside

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", 3, "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))  # lots of empty {} printed
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about that"
))
