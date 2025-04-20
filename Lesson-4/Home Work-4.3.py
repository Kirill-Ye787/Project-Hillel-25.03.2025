import random


length = random.randint(3, 10)
numbers = []

i = 0
while i < length:
    num = random.randint(1, 100)
    numbers.append(num)
    i = i + 1


new_list = [numbers[0], numbers[2], numbers[-2]]

print("Початковий список:", numbers)
print("Новий список:", new_list)
