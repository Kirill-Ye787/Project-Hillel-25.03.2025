import re

def first_word(text: str) -> str:
    """ Пошук першого слова з урахуванням апострофів, крапок і ком """
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group()
    return ""

# Тести з виводом результатів
test1 = first_word("Hello world")
print("Test1:", test1)
assert test1 == "Hello", 'Test1'

test2 = first_word("greetings, friends")
print("Test2:", test2)
assert test2 == "greetings", 'Test2'

test3 = first_word("don't touch it")
print("Test3:", test3)
assert test3 == "don't", 'Test3'

test4 = first_word(".., and so on ...")
print("Test4:", test4)
assert test4 == "and", 'Test4'

test5 = first_word("hi")
print("Test5:", test5)
assert test5 == "hi", 'Test5'

test6 = first_word("Hello.World")
print("Test6:", test6)
assert test6 == "Hello", 'Test6'

print("OK")

