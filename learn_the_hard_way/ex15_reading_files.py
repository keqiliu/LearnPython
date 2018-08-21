from sys import argv

script, filename = argv

txt = open(filename)  # open returns a FILE object

print(f"Here's your file {filename}:")
print(txt.read())  # read() takes no parameter!

txt.seek(0)
print("first line")
print(txt.readline())
print("the rest")
print(txt.read())

print("move to first char:")
txt.seek(0)  # move to the beginning of the text
print(txt.read())

txt.seek(10)  # move to the middle of the text
print(txt.read())


print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
