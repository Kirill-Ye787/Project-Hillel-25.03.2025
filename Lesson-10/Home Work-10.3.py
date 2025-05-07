def is_even(digit: int) -> bool:
    """ Перевірка чи є парним число """
    return digit % 2 == 0

# Тести з виводом
test1 = is_even(2)
print("Test1:", test1)
assert test1 == True, 'Test1'

test2 = is_even(5)
print("Test2:", test2)
assert test2 == False, 'Test2'

test3 = is_even(0)
print("Test3:", test3)
assert test3 == True, 'Test3'

print('OK')
