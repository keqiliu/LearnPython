print("I am 6'2\" tall.")  # escape " in ""
print('I am 6\'2" tall.')  # escape ' in ''

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."  # escape \

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print()
print()

print('\\')  # Backslash (\)
print('\'')  # Single-quote (')
print('\"')  # Double-quote (")
print('\a')  # ASCII bell (BEL)
print('\b')  # ASCII backspace (BS)
print('\f')  # ASCII formfeed (FF)
print('\n')  # ASCII linefeed (LF)
# print('\N{ah}')  # Character named ah in the Unicode database (Unicode only)
print('\r')  # Carriage return (CR)
print('\t')  # Horizontal tab (TAB)
print('\u1234')  # Character with 16-bit hex value 1234
# print('\U12341234')  # Character with 32-bit hex value 12341234
print('\v')  # ASCII vertical tab (VT)
print('\000')  # Character with octal value 000
print('\xab')  # Character with hex value ab

x = '''
three single quote is also fine
'''
print(x)