from typing import Callable
from inspect import isgenerator

def some_gen(begin: int, end: int, func: Callable[[int], int]):
    """
    Генератор, який створює послідовність з n+1 елемента,
    де кожен наступний обчислюється за допомогою func.
    """
    current = begin
    for _ in range(end + 1):
        yield current
        current = func(current)

def pow(x):
    return x ** 2

# Test1
gen1 = some_gen(2, 4, pow)
print("Test1:", isgenerator(gen1))  # True
assert isgenerator(gen1) == True, 'Test1'

# Test2 — новий генератор
gen2 = some_gen(2, 4, pow)
result = list(gen2)
print("Test2:", result)  # Очікується [2, 4, 16, 256, 65536]
assert result == [2, 4, 16, 256, 65536], 'Test2'

print("OK")
