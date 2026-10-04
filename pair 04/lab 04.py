# # task 1
# digits = [12, 3, 4, 14, -12, 5, 10, 16, -4]
#
# plus = []
# minus = []
# pare = []
# krat3 = []
#
# for i in digits:
#     if i > 0:
#         plus.append(i)
#     if i < 0:
#         minus.append(i)
#     if i % 2 == 0:
#         pare.append(i)
#     if i % 3 == 0:
#         krat3.append(i)
# print("Додатні: ",plus)
# print("Віж'ємні: ",minus)
# print("Парні: ",pare)
# print("Картні 3: ",krat3)
# print(f"""
# мінімальне: {str(min(digits))}
# максимальне: {str(max(digits))}
# сума: {str(sum(digits))}
# середнє: {str(round((sum(digits) / len(digits)), 2))}""")

# task 2
#
# group1 = {'Anna','Ivan','Olha', "lol"}
# group2 = {'Ivan','Maksym','Olha'}
#
# all = ""
# peretin = ""
#
# for x in group1 | group2:
#     all += " " + x
#
# for y in group1 & group2:
#     peretin += " " + y
#
# onlyingp1 = group1 - group2
# onlyingp2 = group2 - group1
#
# print(f"Спільні: {peretin}")
# print(f"Тільки group1: {onlyingp1}")
# print(f"Тільки group2: {onlyingp2}")
# print(f"Усі: {all}")

# # task 3
# catalog = {"bread": 15, "Coke": 67, "ice cream": 13, "tea": 20}
#
#
# def find_product(name):
#     price = catalog.get(name)
#     if price is None:
#         print("Товар не знайдено")
#     else:
#         print(f"{name} - {price} грн")
#
#
# def add_or_update(name, price):
#     if catalog.get(name) is None:
#         print(f"Товар {name} додано")
#     else:
#         print(f"Ціну на {name} змінено: {catalog[name]} -> {price} грн")
#     catalog[name] = price
#
#
# def in_range(low, high):
#     found = False
#     for name, price in catalog.items():
#         if low <= price <= high:
#             print(f"{name} - {price} грн")
#             found = True
#     if not found:
#         print("У цьому діапазоні товарів немає")
#
#
# while True:
#     print("\n1 - Додати/змінити товар")
#     print("2 - Знайти товар за назвою")
#     print("3 - Товари в ціновому діапазоні")
#     print("0 - Вихід")
#     choice = input("Ваш вибір: ").strip()
#
#     if choice == "1":
#         name = input("Назва товару: ").strip()
#         if not name:
#             print("Назва не може бути порожньою")
#             continue
#         price = int(input("Ціна:  "))
#         if not name:
#             print("Назва не може бути порожньою")
#             continue
#         add_or_update(name, price)
#     elif choice == "2":
#         find_product(input("Назва товару: ").strip())
#     elif choice == "3":
#         low = int(input("Мінімальна ціна: "))
#         high = int(input("Максимальна ціна: "))
#         if low > high:
#             low, high = high, low
#         in_range(low, high)
#     elif choice == "0":
#         break
#     else:
#         print("Невірний вибір")

# # task 4
group_info = ('10-IT', '2026/2027')
journal = {}


def read_grades():
    while True:
        parts = input("Введіть 5 оцінок через пробіл: ").split()
        try:
            grades = []
            for i in parts:
                grades.append(int(i))
        except ValueError:
            print("Оцінки мають бути цілими числами")
            continue
        if len(grades) != 5:
            print("Має бути рівно 5 оцінок")
        elif not all(1 <= g <= 12 for g in grades):
            print("Оцінки мають бути в діапазоні 1–12")
        else:
            return grades


def average_grade(grades):
    return sum(grades) / len(grades)


def add_student():
    name = input("ПІБ учня: ").strip().capitalize()
    if name in journal:
        print("Такий учень уже є, оцінки буде замінено")
    journal[name] = read_grades()

def show_journal():
    print(f"{group_info[0]} — {group_info[1]}")
    if not journal:
        print("Журнал порожній")
        return
    for name, grades in journal.items():
        print(f"{name}: {' '.join(map(str, grades))}")


def show_averages():
    for name, grades in journal.items():
        print(f"{name} — {average_grade(grades):.1f}")


def show_rating():
    rating = sorted(journal.items(), key=lambda item: average_grade(item[1]), reverse=True)
    for place, (name, grades) in enumerate(rating, start=1):
        print(f"{place}. {name} — {average_grade(grades):.1f}")


def show_best():
    best_avg = max(average_grade(g) for g in journal.values())
    for name, grades in journal.items():
        if average_grade(grades) == best_avg:
            print(f"{name} — {best_avg:.1f}")


while True:
    print("1. додати учня")
    print("2. журнал")
    print("3. сер. бал кожного учня")
    print("4. рейтинг")
    print("5. найкращий учень")
    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        add_student()
    elif choice in ("2", "3", "4", "5"):
        if not journal:
            print("Журнал порожній")
        elif choice == "2":
            show_journal()
        elif choice == "3":
            show_averages()
        elif choice == "4":
            show_rating()
        else:
            print(f"{group_info[0]} — {group_info[1]}")
            show_best()

    else:
        print("Невірний вибір")