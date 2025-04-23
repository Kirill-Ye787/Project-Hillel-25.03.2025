while True:

    a = float(input("Введіть перше число: "))


    op = input("Введіть операцію (+, -, *, /): ")


    b = float(input("Введіть друге число: "))


    if op == '+':
        print("Результат:", a + b)
    elif op == '-':
        print("Результат:", a - b)
    elif op == '*':
        print("Результат:", a * b)
    elif op == '/':
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Ділення на нуль неможливе.")
    else:
        print("Невідома операція!")


    cont = input("Продовжити? (y/yes для продовження): ").strip().lower()
    if cont not in ['y', 'yes']:
        print("Роботу завершено.")
        break
