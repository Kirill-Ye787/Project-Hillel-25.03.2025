import string

text = input("Введіть рядок: ")


def make_hashtag(text):
    # Видаляємо пунктуацію і пробіли
    clean_text = ''.join(c for c in text if c not in string.punctuation)

    # Розбиваємо на слова та робимо кожне слово з великої літери
    words = clean_text.split()
    capitalized_words = [word.capitalize() for word in words]

    # Формуємо хештег
    hashtag = '#' + ''.join(capitalized_words)

    # Обрізаємо до 140 символів, якщо потрібно
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(make_hashtag(text))
