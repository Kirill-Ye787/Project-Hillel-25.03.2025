import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    """Зчитує файл, видаляє html-теги та записує очищений текст у інший файл."""

    # Зчитування вхідного HTML-файлу
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видалення всіх тегів <...>
    cleaned_text = re.sub(r'<[^>]*>', '', html)

    # Розбиваємо текст на рядки
    lines = cleaned_text.splitlines()

    # Додатково: видаляємо порожні рядки або рядки лише з пробілами
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    # Запис очищеного тексту у файл
    with codecs.open(result_file, 'w', 'utf-8') as output:
        for line in non_empty_lines:
            output.write(line + '\n')
