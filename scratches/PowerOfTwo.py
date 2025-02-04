"""
number to binary: bin()

binary str to number: int(bin_str, 2)

"""

# check if it's a power of two
def check_power_of_two (x):
    return "Yes!!" if x & (x-1) == 0 else "Nope"

x = 1024
print(f'{x} is power of two? {check_power_of_two(x)}\n')
x = 1111
print(f'{x} is power of two? {check_power_of_two(x)}')


"""
understand << better
"""
x = 5
print(f'{x} in binary is {bin(x)[2:]}')
print(f'use << by n means adding n zeroes into binary str')
print(f'like x << 2 = {bin(x)[2:]}00')
print(f'essentially it means x * 2^n')
print(f'validating: .... \nbit shift left operator (x << 2) = {x << 2}')
print(f'binary string {bin(x)[2:]}00 to number = {int(bin(x)[2:]+"00", 2)}')


def multiply_7 (x):
    return (x << 3) - x

x = 11
print(f'{x} x 7 = {multiply_7(x)}')




