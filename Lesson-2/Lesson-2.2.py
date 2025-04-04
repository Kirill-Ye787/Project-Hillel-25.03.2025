number = int(input("Введіть 5-значне число: "))


d1, r = divmod(number, 10000)
d2, r = divmod(r, 1000)
d3, r = divmod(r, 100)
d4, d5 = divmod(r, 10)


reversed_number = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1
print("Перевернуте число:", reversed_number)
