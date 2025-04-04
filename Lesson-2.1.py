number = int(input("Введіть 4-значне число: "))

d1, r = divmod(number, 1000)
d2, r = divmod(r, 100)
d3, d4 = divmod(r, 10)

print(d1)
print(d2)
print(d3)
print(d4)

