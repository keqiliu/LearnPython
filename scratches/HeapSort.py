"""
What is Heap Sort?

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements.
It has a time complexity of O( n log(n) ) in all cases (worst, average, and best),
making it one of the most efficient sorting algorithms.

It is also an in-place algorithm, meaning it doesn’t require extra memory.

No need to really build a tree, use index to find

for each idx:
left = 2 * idx + 1
right = 2* idx + 2
"""

def heapify(arr, n, i):
    # start by taking current node as largest, and then check if this is true
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than the current node
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the current node, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # largest still saves either left or right child index
        heapify(arr, n, largest)


def build_max_heap(arr, n):
    """
    step 1. build the max heap
    [4, 10, 3, 5, 1]
            4
          /   \
         10    3
        /  \
       5    1

    Heapify Each Non-Leaf Node:
    Heapify: Ensure that the current node is greater than or equal to its children.
    If not, swap it with the larger child and recursively heapify the affected subtree.

    [10, 5, 3, 4, 1]
             10
           /   \
          5    3
        /  \
       4    1
    """

    # Start from the last non-leaf node and move upwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    """
    step 2. sort the heap
    1) Swap the root (maximum element) with the last element in the heap.
    2) Reduce the heap size by 1 (ignore the last element, which is now in its correct sorted position).
    3) Heapify the root to restore the max-heap property.
    4) Repeat this process until the heap is empty.

    [10, 5, 3, 4, 1] --> [1, 5, 3, 4, 10]
    [1, 5, 3, 4] --> [5, 4, 3, 1] 
             5
           /   \
          4    3
        /
       1 
    """

    n = len(arr)
    # Step 1: Build a max-heap
    build_max_heap(arr, n)

    # Step 2: Sort the heap
    for i in range(n-1, 0, -1):
        # Swap the root (maximum element) with the last element
        arr[0], arr[i] = arr[i], arr[0]
        # heapify the new element on index 0
        # but the new length is i (ignoring the last one)
        heapify(arr, i, 0)
    # in-place sort, so do not need to return anything


# test case
xx = [38, 27, 43, 3, 9, 82, 10, 43]
print(f'original list = {xx}')
heap_sort(xx)
print(f'Heap sort: {xx}')
print('-' * 50)
