#1
def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        raise ValueError("lines должно быть положительным целым числом")
    try:
        with open(file, 'r') as f:
            content = f.read().split('\n')
        while content[-1] == '':
            content.pop()
        total_lines = len(content)
        if total_lines < lines:
            start_index = 0
        else:
            start_index = total_lines - lines
        for line in content[start_index:]:
            print(line)
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
file_path = 'article.txt'
lines_to_read = 3
try:
    read_last(lines_to_read, file_path)
except Exception as e:
    print(f"Произошла ошибка: {e}")

#2
import os
def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)} /')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{sub_indent}{f}')
directory = '/path/to/your/directory'
print_docs(directory)

#3
def longest_word(file):
    with open(file, 'r') as f:
        text = f.read()
    words = text.split()
    longest_word = max(words, key=lambda w: len(w))
    return longest_word
file = 'article.txt'
word = longest_word(file)
print(f"Максимальная длина слова: {len(word)}")
print(f"Слово: {word}")

#4
def main():
    filename = input("Введите имя файла: ")
    extension = ".txt"
    full_filename = f"{filename}{extension}"
    with open(full_filename, 'w') as f:
        while True:
            line = input("Введите строку: ")
            if line == "":
                break
            f.write(line + "\n")
    print("Файл был сохранен.")
if __name__ == "__main__":
    main()

#5
import time
import csv
filename = 'rows_300.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for i in range(1, 301):
        current_time = time.time()
        seconds = int(current_time)
        microseconds = int((current_time - seconds) * 1000000)
        time.sleep(0.01)
        writer.writerow([i, seconds, microseconds])
print(f'Файл {filename} успешно создан.')

#6
from random import randint
import os
from PIL import Image, ImageDraw
def circles_generator(num_of_circles=100):
    os.makedirs('circles', exist_ok=True)
    for i in range(1, num_of_circles + 1):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        img = Image.new('RGB', (600, 600), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.ellipse((150, 150, 450, 450), fill=color)
        filename = f'circle_{i}.jpg'
        img.save(os.path.join('circles', filename))
circles_generator()