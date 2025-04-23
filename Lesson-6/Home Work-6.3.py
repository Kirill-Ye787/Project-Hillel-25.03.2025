number = int(input("Введіть ціле число: "))

# Виводимо стартове значення
print("Початкове число:", number)

# Поки число більше 9 — продовжуємо множити цифри
while number > 9:
    product = 1
    for digit in str(number):
        product *= int(digit)
    print("Добуток цифр:", product)
    number = product

# Виводимо фінальний результат
print("Результат:", number)
