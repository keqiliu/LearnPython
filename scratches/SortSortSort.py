# insertion sort, merge sort, quick sort
def insert_sort(x):
    for i in range(1, len(x)):
        z = x[i]
        natural_end = True
        for j in range(i-1,-1,-1):
            if x[j] > z:
                x[j+1] = x[j]
            else:
                # at j, x[j] <= z, so z should be put onto j+1
                natural_end = False
                break
        if natural_end:
            x[0] = z
        else:
            x[j+1] = z
    return x


def merge_sort(x):
    if len(x) <= 1:
        # need to consider len(x) = 0 case
        return x
    idx_half = int(len(x)/2)
    first_half = merge_sort(x[:idx_half])
    second_half = merge_sort(x[idx_half:])
    i = 0
    j = 0
    idx = 0
    # e.g. merge[3, 27, 38, 43] and [9, 10, 43, 82]
    while i < len(first_half) or  j < len(second_half):
        while i < len(first_half) and first_half[i] <= second_half[j]:
            x[idx] = first_half[i]
            idx += 1
            i += 1
        if i == len(first_half):
            while j < len(second_half):
                x[idx] = second_half[j]
                idx += 1
                j += 1

        while j < len(second_half) and second_half[j] < first_half[i]:
            x[idx] = second_half[j]
            idx += 1
            j += 1
        if j == len(second_half):
            while i < len(first_half):
                x[idx] = first_half[i]
                idx += 1
                i += 1
    return x


def quick_sort(x):
    if len(x) <= 1:
        return x

    # pick last element to compare against
    z = x[-1]

    # then, try to swap positions for array left/right to z
    # to avoid creating new spaces
    i = -1

    # exclude the last point in j's range
    for j in range(len(x)-1):
        if x[j] <= z:
            i += 1
            # trigger above line first to make i at least to 0
            # also use i+1 to count how many we have checked who is <= z
            x[j], x[i] = x[i], x[j]
            # move anything <= z to the left
    x[i+1], x[-1] = x[-1], x[i+1]
    # now i+1 saves the number to compare

    locate_z = i+1
    x[:locate_z] = quick_sort(x[:locate_z])
    x[locate_z+1:] = quick_sort(x[locate_z+1:])

    return x


# sort once
xx = [38, 27, 43, 3, 9, 82, 10, 43]
print(f'original list = {xx}')
print(f'insertion sort: {insert_sort(xx)}')
print(f'original list has also changed = {xx}')
print('-' * 50)

# sort twice
xx = [38, 27, 43, 3, 9, 82, 10, 43]
print(f'original list = {xx}')
print(f'merge sort: {merge_sort(xx)}')
print(f'original list has also changed = {xx}')
print('-' * 50)

# sort thrice (is "thrice" a real word?)
xx = [38, 27, 43, 3, 9, 82, 10, 43]
print(f'original list = {xx}')
print(f'quick sort: {quick_sort(xx)}')
print(f'original list has also changed = {xx}')
print('-' * 50)
