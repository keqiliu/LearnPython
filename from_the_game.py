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

