from typing import Union

def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Повертає різницю між максимальним і мінімальним числом серед аргументів.
    Якщо аргументів немає — повертає 0.
    """
    if not args:
        return 0
    return round(max(args) - min(args), 2)

# Тести з виводом
print("Test1:", difference(1, 2, 3))  # Очікується 2
assert difference(1, 2, 3) == 2, 'Test1'

print("Test2:", difference(5, -5))  # Очікується 10
assert difference(5, -5) == 10, 'Test2'

print("Test3:", difference(10.2, -2.2, 0, 1.1, 0.5))  # Очікується 12.4
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'

print("Test4:", difference())  # Очікується 0
assert difference() == 0, 'Test4'

print("OK")
