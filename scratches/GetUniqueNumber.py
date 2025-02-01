
x = [1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9]


def get_unique(sorted_x):
    unique_list = list()
    unique_list.append(sorted_x[0])
    for i in range(1, len(sorted_x) - 1):
        if sorted_x[i] != sorted_x[i - 1]:
            unique_list.append(sorted_x[i])
    return unique_list

print(f"original sorted list {x}")
print(f"get unique {get_unique(x)}")

print(f"using set {set(x)}")

