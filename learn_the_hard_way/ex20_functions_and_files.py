from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def go_to_end(f):
    f.seek(0, 2)  # the only format allowed for text files


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First, let's print whole thing:\n")
print_all(current_file)  # file reaches to end, after this function!
print("file position:", current_file.tell())

print("now, let's remind, like a tape:")
rewind(current_file)
print("file position:", current_file.tell())

print("now, let's go to end directly:")
go_to_end(current_file)
print("file position:", current_file.tell())

print("let's remind again!\n")
rewind(current_file)

print("Let's print 3 lines:")
current_line = 1
print_a_line(current_line, current_file)
print_a_line(current_line, current_file)  # intentionally read another line, the line_count is kind of fake

current_line += 1
print_a_line(current_line, current_file)  # in input file, this is an empty line.

current_line += 1
print_a_line(current_line, current_file)

