# grades = [10, 8, 9]
# numbers = []
# numbers_new = list()
#
# grades[1] = 12
# print(grades)
#
# numbers.append(10)
# numbers.append([11, 4]) # додає один обєкт
# numbers.insert(1, [5, 6])
# numbers.extend([1,2,3,4,7]) #додає декілька обєктів
# numbers.remove(7) #видаленни за значенням
# numbers.pop(1) #видалення за індексом
# print(numbers)
# del numbers[0]
# print(numbers)
#
# len()
# min()
# max()
# sum()
# print(min("a", "b"))
#
# print(numbers)
#
#
# numbers = [1, 4, 6, 8, 3]
# numbers.sort(reverse = True)
# print(numbers)
#
# #tuple - кортежі -
# point = (-10, 12)
# rgb = (255, 0, 0)
# data = ()
# student = "oleksi", "lox"
# print(student)
# a = (10,)

# функції сета:
# немає дублікатів,
# немає індексного доступу,
# на порядок елементів пох,
# у множині елементи можна додавати, видатяти



name = ["Ivan", "Oleg", "Olha", "Ivan", "Maria", "Maria"]
unique_names = set(name)
print(unique_names)

group1 = {"Ivan", "Oleg", "Olha"}
group2 = {"Ivan", "Maria", "Ann"}


group4 = group1 & group2
group5 = group1 | group2

student= {
    "name": "Ivan",
    "grade": 11}


print(student.get("age", "Такого немає"))
if "grade" in student:
    print(student.get("grade"))

if "Ivan" in student.values():
    print(student.get("name"))

print(student.items())
