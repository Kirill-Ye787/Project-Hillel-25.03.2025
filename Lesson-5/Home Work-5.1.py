import string
import keyword

name = input("Kirill")

def is_valid_variable_name(name):

    if name in keyword.kwlist:
        return False


    if name and name[0].isdigit():
        return False


    if any(c.isupper() for c in name):
        return False


    if any(c.isspace() for c in name):
        return False


    for c in name:
        if c in string.punctuation and c != '_':
            return False


    if set(name) == {'_'} and len(name) > 1:
        return False

    return True

print(is_valid_variable_name(name))
