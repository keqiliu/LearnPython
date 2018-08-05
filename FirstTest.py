# this is a poem.
# import this
import numpy as np
import random


def main():
    """
    usually used after def func()
    """
    xx = np.array([1, 3])
    print(xx)

    print("are you 'ok'?")
    print(None)

    for i in range(3, 24, 10):
        # print(i)
        print(str(i) + ' ' + str(random.random()))

    tuple_test = (1, 2)
    # tuple_test[0] = 3 # this is wrong~~~~~~~~ TUPLE is IMMUTABLE!
    print(tuple_test)

    # list is mutable, cannot be used as dict key
    list_test = list(range(1, 15, 3))
    print(list_test[:])
    print(list_test[1:-1])
    list_test.insert(1, 'abc')
    print(list_test[::-1])

    dict_test = {'key_int': 1, 'key_str': "aha", tuple_test: "tuple can be key"}
    dict_test['key_int'] += 1
    print(dict_test)
    print(dict_test.keys())

    del dict_test['key_str']
    print(dict_test)

    dict_test[5] = "try new key type"
    print(dict_test)

    # dict_test[list_test] = 0 # thi is wrong~~~~~~~~~~ list is mutable, cannot be used as dict key

    dict_test.pop(tuple_test)
    print(dict_test)

    set_str_raw = 'this is a set'
    set_test = set(set_str_raw.split())
    # set_test[2] # this is wrong~~~~~ set does NOT support INDEXing

    for x in set_test:
        print(x, end='---')

    set_str_2nd = 'So why we use set?'
    set_test_2nd = set_test.copy()
    for x in set_str_2nd.split():
        set_test_2nd.add(x)

    test_bool = set_test_2nd.issuperset(set_test)
    print('\n', test_bool, '\n')

    print(set_test_2nd)
    set_test_2nd.remove('this')

    print(set_test_2nd & set_test)
    print(set_test_2nd | set_test)
    print(set_test_2nd ^ set_test)
    print(set_test_2nd - set(['why', 'we']))

    a = 1
    b = a
    a += 1
    print(a, b)

    a = [3, 1, 1]
    b = a
    c = a[:] # copy by full slicing!
    a[0] -= 1
    a[1] -= 1
    print('a changes:', a)
    print('WOW!! b also changes', b)
    print('But c does NOT!', c)

    return


if __name__ == '__main__':
    main()
