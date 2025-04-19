import random

length = random.randint(3, 10)
my_list = [random.randint(1, 100) for _ in range(length)]


result = [my_list[0], my_list[2], my_list[-2]]


print("Початковий список:", my_list)
print("Результат:", result)
