class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

    def print_sentence(self):
        print(str.capitalize(self.subject), self.verb+'s', self.object+'.')


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]  # show the type of the 1st word
    else:
        return None


# peek does not change word_list, match pops 1st one
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')  # like adding the default subject
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


x = parse_sentence([('verb', 'run'), ('direction', 'up')])
x.print_sentence()

# x = parse_sentence([('verb', 'run'), ('verb', 'up')])  # to raise an error
# x.print_sentence()

x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
x.print_sentence()
