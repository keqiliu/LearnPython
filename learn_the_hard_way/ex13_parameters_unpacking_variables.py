from sys import argv   # the MODULE!

script, first, second, third = argv  # "unpack"
# it must be 4 args in total, 3 is wrong, 5 is wrong!!!

print("The script is called:", script)  # argv[0] is this script name
print("1st variable is:", int(first))
print("2nd variable is:", second)
print("3rd variable is", third)

print("also try input: ", input())

# in edit config part, only pass 3
# as while running in terminal it should be:
# python 3 this_file.py first second third
# that's why argv[0] is this script name
