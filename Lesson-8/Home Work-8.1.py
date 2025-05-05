from typing import List

def add_one(some_list: List[int]) -> List[int]:
    """
    Приймає список цифр, перетворює їх на число, додає 1,
    і повертає результат знову у вигляді списку цифр.

    :param some_list: Список цифр числа (наприклад, [1, 2, 3])
    :return: Список цифр після додавання 1 (наприклад, [1, 2, 4])
    """
    number = int(''.join(map(str, some_list)))
    number += 1
    return [int(digit) for digit in str(number)]

# Юніт-тести з виводом результатів
print("Test1:", add_one([1, 2, 3, 4]))  # Очікується [1, 2, 3, 5]
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'

print("Test2:", add_one([9, 9, 9]))  # Очікується [1, 0, 0, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'

print("Test3:", add_one([0]))  # Очікується [1]
assert add_one([0]) == [1], 'Test3'

print("Test4:", add_one([9]))  # Очікується [1, 0]
assert add_one([9]) == [1, 0], 'Test4'

print("ОК — всі тести пройдено успішно!")

