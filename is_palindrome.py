import re

is_letter = r"[a-zA-Z]"


class BasicString:
    def __init__(self, string):
        self.string = string

    @classmethod
    def reverse(cls, string):
        """To get the reverse version"""
        return string[::-1]

    def remove_non_letter(self):
        something_letter = ''
        for x in self.string:
            if re.match(is_letter, x):   # if x.isalpha():
                something_letter += x
        return something_letter


class Palindrome(BasicString):
    def is_palindrome(self):
        only_letter_to_lower = BasicString.remove_non_letter(self).lower()
        return only_letter_to_lower == BasicString.reverse(only_letter_to_lower)


print("string to check is:")
magic_test = "Rise to vote, sir"
print(magic_test)

print("pure revert is:", BasicString.reverse(magic_test))

test = Palindrome(magic_test)
print("chunk into pure letter:", test.remove_non_letter())

print("so, is it Palindrome? \n\n", test.is_palindrome())

# the use of __doc__
print(BasicString.reverse.__doc__)
