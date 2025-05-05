from typing import Any

def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом — без урахування регістру і знаків пунктуації.

    :param text: Вхідний рядок
    :return: True, якщо рядок паліндром, інакше False
    """
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# Тести з виводом
print("Test1:", is_palindrome('A man, a plan, a canal: Panama'))  # True
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'

print("Test2:", is_palindrome('0P'))  # False
assert is_palindrome('0P') == False, 'Test2'

print("Test3:", is_palindrome('a.'))  # True
assert is_palindrome('a.') == True, 'Test3'

print("Test4:", is_palindrome('aurora'))  # False
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")

