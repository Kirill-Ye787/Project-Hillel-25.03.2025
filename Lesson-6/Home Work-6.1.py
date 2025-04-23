import string

range_input = input("Введіть дві літери через дефіс (наприклад a-c): ")

start_char, end_char = range_input.split('-')

all_letters = string.ascii_letters

start_index = all_letters.index(start_char)
end_index = all_letters.index(end_char)

result = all_letters[start_index:end_index + 1]

print(result)
