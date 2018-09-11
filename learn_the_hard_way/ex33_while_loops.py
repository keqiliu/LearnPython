i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)  # Zed, this line should be before i++

    print(f"At the bottom i is {i}")

print("The numbers: ")
for num in numbers:
    print(num, end='---')
