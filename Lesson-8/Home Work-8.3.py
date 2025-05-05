from typing import List, Union

def find_unique_value(some_list: List[Union[int, float]]) -> Union[int, float]:
    """
    Приймає список чисел і знаходить число, яке зустрічається лише один раз.

    :param some_list: Список чисел (цілих або дробових)
    :return: Унікальне число, що зустрічається тільки один раз
    """
    for number in some_list:
        if some_list.count(number) == 1:
            return number

# Тести з виводом
print("Test1:", find_unique_value([1, 2, 1, 1]))  # Очікується 2
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'

print("Test2:", find_unique_value([2, 3, 3, 3, 5, 5]))  # Очікується 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'

print("Test3:", find_unique_value([5, 5, 5, 2, 2, 0.5]))  # Очікується 0.5
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК — всі тести пройдено успішно!")
