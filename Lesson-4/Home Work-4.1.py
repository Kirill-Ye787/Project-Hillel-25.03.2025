numbers = [0, 1, 0, 12, 3]

i = 0
for j in range(len(numbers)):
    if numbers[j] != 0:
        numbers[i] = numbers[j]
        i = i + 1

while i < len(numbers):
    numbers[i] = 0
    i = i + 1

print(numbers)
