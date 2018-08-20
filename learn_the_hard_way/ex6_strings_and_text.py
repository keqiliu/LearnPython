types_of_people = 10
x = f"There are {types_of_people} types of people."  # notice the "f" at the beginning!
xx = "There are {types_of_people} types of people."

print(x)
print(xx)

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))  # {} can be empty, without {0}.

w = "this is the left side of ..."
e = "a string with a right side."

print(w + e)
