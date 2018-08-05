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

    return


if __name__ == '__main__':
    main()
