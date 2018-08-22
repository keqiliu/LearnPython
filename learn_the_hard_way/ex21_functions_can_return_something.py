def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


def substract(a, b):
    print(f"Substracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Dividing {a} \ {b}")  # under f"", can type \ directly! not escaping char!
    return a / b


print("Let's do some math")

age = add(29, -1)
height = substract(90, 8)
weight = multiply(11, 6)
iq = divide(300, 2)

print(f"Age: {age}, height: {height}, weight"
      f": {weight}, IQ: {iq}")

print("Here's a puzzle.")
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print(f"That becomes: {what}. Right? :)")
