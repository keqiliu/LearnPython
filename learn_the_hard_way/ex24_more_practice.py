print("Some practice")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tI'm so tired
\n\t\t and sleepy
"""

print("-----------")
print(poem)
print("-----------")

five = 10 - 5
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_benas = started * 500
    jars = jelly_benas / 1000
    crates = jars / 100
    return jelly_benas, jars, crates


start_point = 10000
beans, jar, crate = secret_formula(start_point)
print(f"We'd have {beans} beans,")
print("and {} jars, and {} crates".format(jar, crate))

start_point /= 10
print("We could even do string in this way!!")
formula = secret_formula(start_point)
# the cool way!!!!
print("We got {}, {}, {}".format(*formula))


