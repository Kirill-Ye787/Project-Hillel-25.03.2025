def is_even(number: int) -> bool:
    """ Перевірка на парність без використання %, //, /, divmod """
    return (number & 1) == 0

# Тести з простим виводом
n1 = 2494563894038**2
print("Test1:", n1, is_even(n1))
assert is_even(n1) == True, 'Test1'

n2 = 1056897**2
print("Test2:", n2, is_even(n2))
assert is_even(n2) == False, 'Test2'

n3 = 24945638940387**3
print("Test3:", n3, is_even(n3))
assert is_even(n3) == False, 'Test3'

print("OK")

