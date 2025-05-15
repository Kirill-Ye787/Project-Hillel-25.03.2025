# Установи сначала geopy через: pip install geopy

from geopy.distance import geodesic
from math import atan2, radians, degrees, sin, cos

# Текущие координаты (например, корабля или машины)
current_position = (54.321, 10.123)  # Пример: Киль, Германия

# Целевая точка (например, порт назначения)
destination_position = (55.675, 12.565)  # Пример: Копенгаген, Дания

# Расчёт расстояния
distance = geodesic(current_position, destination_position).kilometers

# Расчёт направления (азимута)
def get_bearing(start, end):
    lat1, lon1 = map(radians, start)
    lat2, lon2 = map(radians, end)
    d_lon = lon2 - lon1

    x = sin(d_lon) * cos(lat2)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(d_lon)
    angle = atan2(x, y)
    bearing = (degrees(angle) + 360) % 360
    return bearing

bearing = get_bearing(current_position, destination_position)

# Вывод на экран
print(f"📍 Расстояние до цели: {distance:.2f} км")
print(f"🧭 Азимут (направление): {bearing:.1f}°")



try:
    # Код, який може викликати виняток
    result = 10 / 2
except ZeroDivisionError:
    # Код обробки винятку
    print("Error: Division by zero")
else:
    # Код, який виконується, якщо винятку не виникає
    print("Division successful")
finally:
    # Код, який виконується завжди
    print("End of try-except block")

    try:
        # Код, який може викликати виняток
        result = int("123")
    except ValueError as e:
        # Код обробки винятку
        print(f"Error: {e}")
    else:
        # Код, який виконується, якщо винятку не виникає
        print("Conversion successful")

        try:
            # Код, який може викликати виняток
            result = int("123")
        except ValueError as e:
            # Код обробки винятку
            print(f"Error: {e}")
        finally:
            # Код, який виконується завжди
            print("End of try block")

try:
    # Код, який може викликати виняток
    result = int("123")
except ValueError as e:
    # Код обробки винятку
    print(f"Error: {e}")
finally:
    # Код, який виконується завжди
    print("End of try block")

    try:
        # Код, який може викликати виняток
        result = 10 / 0
    except ZeroDivisionError:
        # Код обробки винятку
        print("Error: Division by zero")

try:
    # Код, який може викликати виняток
    result = int("123")
except ValueError as e:
    # Код обробки винятку
    print(f"Error: {e}")
finally:
    # Код, який виконується завжди
    print("End of try block")

try:
    # Код, який може викликати виняток
    result = int("123")
except ValueError as e:
    # Код обробки винятку
    print(f"Error: {e}")
else:
    # Код, який виконується, якщо винятку не виникає
    print("Conversion successful")

try:
    # Код, який може викликати виняток
    result = 10 / 2
except ZeroDivisionError:
    # Код обробки винятку
    print("Error: Division by zero")
else:
    # Код, який виконується, якщо винятку не виникає
    print("Division successful")
finally:
    # Код, який виконується завжди
    print("End of try-except block")

    try:
        # Код, який може викликати виняток
        result = 10 / 2
    except ZeroDivisionError:
        # Код обробки винятку
        print("Error: Division by zero")
    else:
        # Код, який виконується, якщо винятку не виникає
        print("Division successful")
    finally:
        # Код, який виконується завжди
        print("End of try-except block")

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception.")
except CustomError as ce:
    print(f"Custom error caught: {ce}")


# Створюємо рядок
my_string_1 = 'I like Python'
my_string_2 = "I like Python"
# Виводимо тип
print(type(my_string_1)) # виведе: <class 'str'>

# Якщо потрібні одинарні лапки всередині рядка
my_string_1 = "I 'like' Python"
print(my_string_1) # виведе: I 'like' Python

# Якщо потрібні подвійні лапки всередині рядка
my_string_1 = 'I "like" Python'
print(my_string_1) # виведе: I "like" Python

# За допомогою слеша, можна екранувати лапки
my_string_1 = "I \"like\" Python"
print(my_string_1) # виведе: I "like" Python

# Потрійні подвійні лапки використовуються тоді, коли потрібний текст із перенесенням рядків
my_string = """Python
""is""
awesome
"""

digits = str(3654)
# Виглядає як число, але це рядок
print(digits) # виведе: 3654
print(type(digits)) # виведе: <class 'str'>

digits = int(digits)
print(type(digits)) # виведе: <class 'int'>


