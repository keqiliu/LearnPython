from ex25_even_more_practice import *
# try help(ex25)
# If need to reload the module:
# from importlib import reload
# reload(ex25_even_more_practice)

sentence = "All good things come to those who wait."

words = break_words(sentence)
print(words)

sorted_words = sort_words(words)
print(sorted_words)

print_first_word(words)  # popped out!
print(words)
print_first_word(words)
print(words)

print_last_word(words)
print(words)

print_first_word(sorted_words)
print(sorted_words)
print_last_word(sorted_words)
print(sorted_words)

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
