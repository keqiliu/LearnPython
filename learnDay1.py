"""
a = 15
b = a ** 2
c = _ + 2 --> in the console, _ to present previous answer
"""

import decimal

print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Fibonacci series:
# the sum of two elements defines the next
a, b = 1, 1
while a < 60:
    a, b = b, a + b
    print(a, end=',')
print('\n\n')

"""Day 1"""
# float v.s. decimal
print(0.1 + 0.2)
x = 9.99 + 0.005
print(x)
print(type(x))
print(round(x, 2))  # float is slightly smaller than 9.995

x_decimal = decimal.Decimal(9.995)
print(x_decimal)  # the exact value how real 9.995 should be saved
print(round(x_decimal, 2))
print(type(x_decimal))

# str functions
t = '  nothing can stop me   '
print(t.capitalize())
print(t.split())
print(t.replace(' ', '-'))
print(t.strip())  # remove blank
print(t.strip('me   '))

# list functions
l = [1, 2, 3.14, 'test']
l.append(4)
print(l)
l.append([5, 6])  # add this LIST as the element
print(l)
l.extend([7, 'ahahah'])  # add everything in this list as ELEMENTS
print(l)
l.reverse()
print(l)
print(l.remove('ahahah'))
print(l)
l[-2:] = []  # remove a few elements by slicing
print(l)


# calculate sum of even numbers from 1 to 20
sum_num = 0
for i in range(2, 21, 2):
    sum_num += i
print(sum_num)


# as long as default values are put at last, there could be multiple
def test_multi_default(x1, x2=3, x3=10):
    return max(x1, x2, x3), x2


print(test_multi_default(4))


# files
file = open('daydayup.txt', 'w')
file.write('Hello again. \n')
file.write('Nice to have')
file.write(' you here. :)') # if not provide blank, right next to above line's chars
file.write('\n another \n few \n lines')
file.close()


with open('daydayup.txt', 'r') as f:  # mode 'a' can not be READ!!!
    # print(f.read(10))  # read first 10 chars
    # print(f.readline()) # read 1 line
    print(f.readlines())  # new line '\n' will be shown in this way, in the list of several lines char

with open('daydayup.txt', 'r') as f:
    print(f.read())  # read in eyeball's way, no '\n' sign

with open('daydayup.txt', 'r+') as f:  # mode 'r+', write at the beginning
    f.write('now I\'m replacing chars at the beginning.\n')

with open('daydayup.txt', 'r') as f:
    for line in f:
        print(line, end='')  # same as above f.read()

with open('daydayup.txt', 'a') as f:  # mode 'a', add at last
    f.write('\t\tnow I\'m adding new lines in the end\n')

with open('daydayup.txt', 'r') as f:
    print(f.read())  # read in eyeball's way, no '\n' sign


# open existing file
file_name = r'/Users/keqiliu/desktop/Dissertation-48962.txt'
with open(file_name, 'w') as f:
    f.write('this is baobao\'s distinction work!')


# Target 3
fab_list = [1, 1]
for i in range(8):
    fab_list.append(fab_list[-1] + fab_list[-2])
print(fab_list[::-1])