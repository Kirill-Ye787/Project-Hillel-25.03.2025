import codecs
import re

# 1. Створення HTML-файлу (якщо його немає)
sample_html = """<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Hello, Hillel!</h1>
    <p>This is <b>your homework</b>.</p>
    <p></p>
    <footer>Good luck!</footer>
  </body>
</html>"""

with open('draft.html', 'w', encoding='utf-8') as file:
    file.write(sample_html)

print("📄 Файл draft.html успішно створено.\n")


# 2. Функція для видалення HTML-тегів
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видалення тегів <...>
    cleaned_text = re.sub(r'<[^>]*>', '', html)

    # Видалення порожніх рядків
    lines = cleaned_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    # Запис очищеного тексту у файл
    with codecs.open(result_file, 'w', 'utf-8') as output:
        for line in non_empty_lines:
            output.write(line + '\n')

    # Вивід у консоль
    print(f"✅ Текст очищено та записано у файл '{result_file}'.\n")
    print("🖨️ Вміст очищеного тексту:")
    for line in non_empty_lines:
        print(line)


# 3. 📥 ВИКЛИК ФУНКЦІЇ
delete_html_tags('draft.html')
