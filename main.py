numbers = [0, 1, 7, 2, 4, 8]

if len(numbers) == 0:
    result = 0
else:
    i = 0
    s = 0
    while i < len(numbers):
        s = s + numbers[i]
        i = i + 2
    result = s * numbers[-1]

print(result)
