import string

text = input("Введіть рядок: ")


def make_hashtag(text):

    clean_text = ''.join(c for c in text if c not in string.punctuation)


    words = clean_text.split()
    capitalized_words = [word.capitalize() for word in words]


    hashtag = '#' + ''.join(capitalized_words)


    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(make_hashtag(text))
