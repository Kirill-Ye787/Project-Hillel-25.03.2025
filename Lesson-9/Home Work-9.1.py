from typing import List, Dict

def popular_words(text: str, words: List[str]) -> Dict[str, int]:
    """
    Повертає словник з кількістю входжень кожного слова зі списку в тексті.
    Порівняння без урахування регістру.
    """
    text_words = text.lower().split()
    return {word: text_words.count(word) for word in words}

# Тест з прикладу
test_result = popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
)
print("Test1:", test_result)
assert test_result == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
