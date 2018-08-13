"""
insert sort
selection sort
bubble sort
quick sort
merge sort
"""

import random
import timeit


# insert sort
def insert_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
    return l


# selection sort
def select_sort(l):
    for i in range(len(l)-1):
        idx_min_rest = i
        for j in range(i+1, len(l)):
            if l[j] < l[idx_min_rest]:
                idx_min_rest = j
        if idx_min_rest > i:
            l[i], l[idx_min_rest] = l[idx_min_rest], l[i]
    return l


# bubble sort
def bubble_sort(l):
    while 1:
        does_sort = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                does_sort = True
        if not does_sort:
            break
    return l


# quick sort
def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]  # pick first one
    while 1:
        i = 1
        while i < len(l) and l[i] < pivot:
            i += 1
        j = len(l) - 1
        while j > 0 and l[j] >= pivot:
            j -= 1
        if i >= j:  # j is the idx to put in pivot
            break
        l[i], l[j] = l[j], l[i]
    if j == 0:
        l[j+1:] = quick_sort(l[j+1:])
    elif j == len(l) - 1:
        l[0], l[j] = l[j], l[0]
        l[:j] = quick_sort(l[:j])
    else:
        l[0], l[j] = l[j], l[0]
        l[:j] = quick_sort(l[:j])
        l[j+1:] = quick_sort(l[j+1:])
    return l


# merge sort
def merge_sort_sub(l, idx_left, idx_right, idx_end):
    part1 = l[idx_left:idx_right]
    part2 = l[idx_right:idx_end]
    sort_l = []
    i = 0
    j = 0
    while i < len(part1) and j < len(part2):
        if part1[i] == part2[j]:
            sort_l.append(part1[i])
            sort_l.append(part2[j])
            i += 1
            j += 1
            continue
        while i < len(part1) and part1[i] < part2[j]:
            sort_l.append(part1[i])
            i += 1
        if i < len(part1):
            while j < len(part2) and part2[j] < part1[i]:
                sort_l.append(part2[j])
                j += 1
    if i < len(part1):
        sort_l.extend(part1[i:])
    if j < len(part2):
        sort_l.extend(part2[j:])
    return sort_l


def merge_sort(l):
    width = 1
    while width < len(l):
        for i in range(0, len(l), 2*width):
            l[i:min(i+width*2, len(l))] = merge_sort_sub(l, i, min(i+width, len(l)), min(i+width*2, len(l)))
        width *= 2
    return l


def check_input(l):
    return all(list(map(lambda x: type(x) in [int, float], l)))


# main test and compare time
N = 100
raw_list = [random.randint(1, N) for i in range(N)]

if not check_input(raw_list):
    raise Exception("list must be numbers")

timing = {}
name = ['built-in', 'insert', 'select', 'bubble', 'quick', 'merge']
for i in range(6):
    copy = raw_list.copy()
    t_start = timeit.default_timer()
    print('\n', name[i])
    if i == 0:
        copy.sort()
        benchmark = copy
    elif i == 1:
        insert_sort(copy)
    elif i == 2:
        select_sort(copy)
    elif i == 3:
        bubble_sort(copy)
    elif i == 4:
        quick_sort(copy)
    else:
        merge_sort(copy)
    print(copy)
    t_end = timeit.default_timer()
    timing[name[i]] = (t_end - t_start)
    if i > 0 and copy != benchmark:
        raise Exception('{0} sort is wrong'.format(name[i]))

# sorted, does NOT change original value in t
for k, v in sorted(timing.items(), key=lambda x: x[1]):
    print('{0}: t = {1}'.format(k, v))

"""
N = 10000
built-in: t = 0.0083113929999854
merge: t = 0.11466931300000738
quick: t = 4.38856896599998
select: t = 6.084492812999997
bubble: t = 21.13758963699999
insert: t = 29.102735595000013
"""