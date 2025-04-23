number = int(input("Введіть ціле число: "))


print("Початкове число:", number)


while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    print("Добуток цифр:", product)
    number = product


print("Результат:", number)
