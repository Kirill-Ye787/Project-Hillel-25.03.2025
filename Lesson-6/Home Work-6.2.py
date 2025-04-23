seconds = int(input("Введіть кількість секунд (від 0 до 8639999): "))

if 0 <= seconds < 8640000:

    days, remaining = divmod(seconds, 24 * 60 * 60)

    hours, remaining = divmod(remaining, 60 * 60)

    minutes, secs = divmod(remaining, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif days % 10 in [2, 3, 4] and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}")
else:
    print("Помилка: число повинно бути від 0 до 8639999.")
