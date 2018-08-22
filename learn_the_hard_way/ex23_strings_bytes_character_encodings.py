# Unicode == universal encoding!!!

# how computer reads human languages?
# input file <ex23_languages.txt> is actually encoded in UTF-8.

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:  # for last line, readline() returns '', cannot pass IF check!!!
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        # hmm... kind of new recursive way, I may do it in a loop


def print_line(line, encoding, errors):  # this can come after where the function is used
    next_lang = line.strip()  # remove whitespace chars and '\n', front & bottom
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)  # cooked one is the same as already input

    print(next_lang, "===>", raw_bytes, "===>", cooked_string)


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
# what to pass in?
# input_encoding = utf-8
# error = strict


"""
The errors argument specifies the response when 
the input string can’t be converted 
according to the encoding’s rules. 

Legal values for this argument are 
- 'strict' (raise a UnicodeDecodeError exception), 
- 'replace' (use U+FFFD, REPLACEMENT CHARACTER), 
- 'ignore' (just leave the character out of the Unicode result), 
- 'backslashreplace' (inserts a \ xNN escape sequence). 
"""

0b1011010  # it's 90 = 2^6 + 2^4 + 2^3 + 2!!
ord('Z')  # Return the Unicode code point for a one-character string
chr(90)  # Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
"".join(map(chr, [23453, 23453, 21568]))

"""
bits = 1s or 0s
byte = 8 bits

bytes --> .decode() --> string
string --> .encode() --> get the bytes!
"""

