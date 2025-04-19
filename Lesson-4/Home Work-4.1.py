import random

# Створюємо список з випадковою кількістю елементів від 3 до 10
length = random.randint(3, 10)
my_list = [random.randint(1, 100) for _ in range(length)]

# Створюємо новий список з потрібних елементів
result = [my_list[0], my_list[2], my_list[-2]]

# Виводимо обидва списки
print("Початковий список:", my_list)
print("Результат:", result)
