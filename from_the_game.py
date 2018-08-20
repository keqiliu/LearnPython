# real copy
a = 1
b = a
a += 1
print(a, b)

a = [3, 1, 1]
b = a
c = a[:]  # copy by full slicing!
d = a.copy()

a[0] -= 1
a[1] -= 1
print('a changes:', a)
print('WOW!! b also changes', b)
print('But c does NOT!', c)
print('d does not change!', d)


# arrays
# https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
arr = [[]] * 3  # refer to the same address 3 times!!!
arr[0].append(7)
print(arr)  # you will see three 7's ~~~ wow!!!

x = (0, 1, 2)
(a, b, c) = x
[a1, b1] = (a, b)

