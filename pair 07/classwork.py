import os

print("Створення файлу")

with open('hello.txt', "w", encoding="utf-8") as file:
    file.write("сир ковбаса хліб\n")

# r - читання, файл існує
# w - перезаписує існуючий файл, автоматично закриває файл після завершення роботи
# a - додай в кінець, не стирається минуле, файл має існувати
# x - новий файл, але такого файла не має існувати до того

if not os.path.exists('text.txt'):
    with open('text.txt', "w", encoding="utf-8") as file:
        file.write("тумба юмба")
        file.write("тумба юумба")
        file.write("румба тумба")

if not os.path.exists('numbers.csv'):
    with open('numbers.txt', "w", encoding="utf-8") as file:
        file.write('12\n8\n1\n25\n16')

if not os.path.exists('students.txt'):
    with open('students.txt', "w", encoding="utf-8") as file:
        file.write('Ivanenko Anna; 91')
        file.write('Leshchenko Ivan; 76')
        file.write('Komarova Sophie; 97')
        file.write('Bondarenko Ivan; 94')

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text)
with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines() #cписок вісіх рядків ще не прочитаних

#перебіп файлів
with open("text.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        print(f"{number}. {clean_line}")

