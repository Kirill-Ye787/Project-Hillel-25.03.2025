import string
import keyword

name = input("Kirill")

def is_valid_variable_name(name):
    # 1. Якщо ім’я є зареєстрованим ключовим словом
    if name in keyword.kwlist:
        return False

    # 2. Якщо ім’я починається з цифри
    if name and name[0].isdigit():
        return False

    # 3. Якщо є великі літери
    if any(c.isupper() for c in name):
        return False

    # 4. Якщо є пробіли
    if any(c.isspace() for c in name):
        return False

    # 5. Якщо є заборонені знаки пунктуації (окрім "_")
    for c in name:
        if c in string.punctuation and c != '_':
            return False

    # 6. Якщо ім’я складається лише з підкреслень — їх має бути не більше одного
    if set(name) == {'_'} and len(name) > 1:
        return False

    return True

print(is_valid_variable_name(name))
