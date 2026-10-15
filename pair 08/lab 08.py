#1
# try:
#     a = int(input("число 1: "))
#     b = int(input("число 2: "))
# except ValueError:
#     print("ЧИСЛО блін введи!")
# else:
#     try:
#         operation = input("Choose action (+, -, *, /): ")
#
#         if operation == "+":
#             print(a + b)
#         elif operation == "-":
#             print(a - b)
#         elif operation == "*":
#             print(a * b)
#         elif operation == "/":
#             print(a / b)
#         else:
#             print(" дано лише операції (+, -, *, /) ")
#     except ZeroDivisionError:
#         print('ну хто на нуль ділить')
# №2
# def input_grade():
#
#     while True:
#         try:
#             grade = int(input("введіть оінку за 12ти бальною шкалою"))
#
#             if grade < 1 or grade > 12:
#                 raise ValueError("неправильна оцінка")
#             return grade
#
#         except ValueError:
#             print('ValueError')
#
# grade = input_grade()
# print(f"ваша оцінкка: {grade}")

# №3
#
# with open("students.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#
# students = []
# grades = {}
#
# for student in text.splitlines():
#     try:
#         name, grade = student.split(";")
#         if int(grade) > 100 or int(grade) < 1:
#             raise ValueError
#     except ValueError:
#         continue
#
#     students.append(name)
#     grades[name] = grade
#
# try:
#     n = int(input("1 - пошук учня за індексом \n 2 - оцінка за ім'ям: "))
#
#     if n == 1:
#         index = int(input("номер: "))
#         print("yчень:", students[index])
#     elif n == 2:
#         name = input("імя: ")
#         print(f"оцінка: {grades[name]}")
#     else:
#         print("ну тий тугодууууууум")
#
# except IndexError:
#     print("нема учня з таким номером")
# except KeyError:
#     print("немає нікого з учнів з таким іменем")
# except ValueError:
#     print("неправильне число")

# №4

def process_students():
    valid = []
    valid_count = 0
    skipped = 0

    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            for n, line in enumerate(file, start=1):
                line = line.strip()
                try:
                    name, grade = line.split(";")
                except ValueError:
                    print(f"рядок {n} пропущено через неправильнц структуру або відсутність роздільника.")
                    skipped += 1
                    continue

                try:
                    grade = int(grade)
                except ValueError:
                    print(f"рядок {n} пропущно бо балл не є числом.")
                    skipped += 1
                    continue

                if not (0 <= grade <= 100):
                    print(f"рядок {n} пропущено оскільки балл поза діапазоном.")
                    skipped += 1
                    continue

                valid.append((name, grade))
                valid_count += 1

        valid.sort(reverse=True)

        with open("report.txt", "w", encoding="utf-8") as report_file:
            for name, grade in valid:
                report_file.write(f"{name};{grade}\n")

        print(f"правильних записів: {valid_count}")
        print(f"пропущено: {skipped}")

    except FileNotFoundError:
        print("Помилка: файл students.txt відсутній.")


process_students()