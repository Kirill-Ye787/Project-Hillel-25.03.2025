num1 = float(input("Введіть перше число: "))
operator = input("Введіть дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
if operator == "+":
    result = num1 + num2
    print("Результат:", result)
elif operator == "-":
    result = num1 - num2
    print("Результат:", result)
elif operator == "*":
    result = num1 * num2
    print("Результат:", result)
elif operator == "/":
    if num2 == 0:
        print("Помилка: Ділення на нуль неможливе!")
    else:
        result = num1 / num2
        print("Результат:", result)
else:
    print("Невідома дія. Введіть один із символів: +, -, *, /")
