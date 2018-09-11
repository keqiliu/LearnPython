# I have to say, this ex41 is super cool! :)

"""
To-do list:
1. str what is casefold
2. str. isdigit() vs. isdecimal()
3. str.isindentifier
4. Run with real URL
"""

# is-a: X is-a Y --> X inherits from Y
import random
from urllib.request import urlopen  # something new
import urllib.error as NoWifi
import sys


# it's all about string
"test aha. YEAH".capitalize()  # test--> Test. All others turns lower~~yeah
"Ah?".casefold()  # Return a version of the string suitable for caseless comparisons.
"a12".isalnum()  # True
"a12".isalpha()  # False, due to 12
"12".isdecimal()  # True
"12.5".isdecimal()  # Must be all decimal!!
"125".isdigit()  # Must be all digits!! Looks like isdigit() == isdecimal()??
"classes".isidentifier()
"class".isidentifier()
"\n".isspace()
"\v".isspace()
"\vv".isspace()
"\n\t".isspace()
"how to center".center(50, 'A')  # put string in center, fill with 'A' on both sides
"how to center".center(16, '~')  # if 3 chars to fill in, 1 on left, 2 on right.
"how to ljust".ljust(30, '-')  # add '-' in the end to fill into length = 30
"I'm doing partition".partition("ing")  # case sensitive
"how to sp\nli\ttli\nnes?".splitlines()
"how to sp\nli\ttli\nnes?".splitlines(keepends=True)
"what exactly is a title".title()
"what exactly is a title".istitle()  # False
"What Exactly Is A Title".istitle()  # True
"ha? zfill?".zfill(20)  # fill in with all 0's on the left

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True  # Q: dict.values --> A: dict.keys
else:
    PHRASE_FIRST = False  # Q: dict.keys --> A: dict.values

try:
    for word in urlopen(WORD_URL).readlines():
        WORDS.append(str(word.strip(), encoding="utf-8"))
        # str(...., encoding="") is actually DEcoding!!! .... has to be bytes-like string.
except NoWifi.URLError:
    WORDS = ['Ai', 'Yo', 'Wei', 'Heng', 'Ha']


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    """
    random.sample(population, k):
    Chooses k unique random elements from a population sequence or set.
    """

    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # diff between *** and @@@:
    # *** is just one param
    # @@@ is like tuple param, *@@@, can be 1 to 3
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)  # assume some function takes 1 to 3 parameters
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # this is not real loop: just repeat same thing on snippet first, and then phrase
    for sentence in snippet, phrase:
        result = sentence[:]  # copy to new address!

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
            # count = 1, replace at most once!
        # using loop & replace count = 1
        # replace %%% one by one, for everything in class_names

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results  # by construction, a tuple with snippet + phrase


# keep try until user hits EOF
try:
    print("here we try")
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)  # cool, shuffle~~~

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"Answer:\t\t{answer}\n\n")
except KeyboardInterrupt:
    print("\nI guess it's this type of error.")
except EOFError as e:
    print("\ne")
finally:
    print("\nBye!")
    # exit(0)  # somehow in pyCharm, it still reads user input... weird
    # but in terminal, it's a real Bye!
