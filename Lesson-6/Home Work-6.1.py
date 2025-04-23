import string

# Введення рядка від користувача, наприклад: "a-c"
range_input = input("Введіть дві літери через дефіс (наприклад a-c): ")

# Розділяємо на дві літери
start_char, end_char = range_input.split('-')

# Отримуємо всі літери латиницею (малі + великі)
all_letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Знаходимо індекси обох літер
start_index = all_letters.index(start_char)
end_index = all_letters.index(end_char)

# Виводимо діапазон включно: від start до end
result = all_letters[start_index:end_index + 1]

print(result)
