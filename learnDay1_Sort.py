"""
bubble sort
insert sort
selection sort
"""

l = [1, 2, 5, 0.6, 'a']

def check_input(l):
    return all(list(map(lambda x: type(x) in [int, float], l)))


print(check_input(l))


