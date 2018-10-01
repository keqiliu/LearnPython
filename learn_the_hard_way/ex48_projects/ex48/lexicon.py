dict_direction = {'north', 'south',  'east', 'west', 'down', 'up', 'left', 'right', 'back'}
dict_verbs = {'go', 'stop', 'kill', 'eat'}
dict_stop = {'the', 'in', 'of', 'from', 'at', 'it'}
dict_nouns = {'door', 'bear', 'princess', 'cabinet'}


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(stuff):
    words = stuff.split()
    sentence = []
    for raw_word in words:
        word = str.lower(raw_word)
        if word in dict_direction:
            sentence.append(('direction', word))
        elif word in dict_verbs:
            sentence.append(('verb', word))
        elif word in dict_stop:
            sentence.append(('stop', word))
        elif word in dict_nouns:
            sentence.append(('noun', word))
        elif convert_number(word) is not None:
            sentence.append(('number', convert_number(word)))
        else:
            sentence.append(('error', raw_word))
    return sentence
