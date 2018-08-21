# this one is like your scripts with argv
def print_two(*args):  # input is a tuple
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():  # this is empty (), not like void way, just empty ()!!!
    print("I got nothin'.")

print_two("Peppa", "pig")
print_two_again("Xiaozhu", "keqi")
print_one("First!")
print_none()
# print_none # without (), this is wrong!
