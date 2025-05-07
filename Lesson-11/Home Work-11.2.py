from typing import Generator
from inspect import isgenerator

def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    """
    Генерує послідовність кубів чисел, починаючи з 2,
    поки значення куба не перевищує end.
    """
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1

# Тести з виводом
gen = generate_cube_numbers(1)
print("Test0:", isgenerator(gen))
assert isgenerator(gen) == True, 'Test0'

print("Test1:", list(generate_cube_numbers(10)))  # [8]
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'

print("Test2:", list(generate_cube_numbers(100)))  # [8, 27, 64]
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'

print("Test3:", list(generate_cube_numbers(1000)))  # [8, 27, ..., 1000]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print("OK")
