from typing import Generator
from inspect import isgenerator

def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Генератор простих чисел від 2 до end включно.
    """
    for num in range(2, end + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

# Тести з виводом
gen = prime_generator(1)
print("Test0:", isgenerator(gen))
assert isgenerator(gen) == True, 'Test0'

print("Test1:", list(prime_generator(10)))  # [2, 3, 5, 7]
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'

print("Test2:", list(prime_generator(15)))  # [2, 3, 5, 7, 11, 13]
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'

print("Test3:", list(prime_generator(29)))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print("Ok")
