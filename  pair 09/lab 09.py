# #1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def info(self):
#         print(f'ширина - {self.width}  висота - {self.height}  площа - {self.area()}  периметр - {self.perimeter()}')
#
# rect1 = Rectangle(6, 9)
# rect2 = Rectangle(3, 4)
#
# rect1.info()
# rect2.info()

# #2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if grade > 0 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print('оцінки мають 12ти бальну систему')
#
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {round(self.average(),2)}'
# student = Student('Ivan Petrenko')
# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9)
# print(student)
#

## 3
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self, grade):
#         if grade > 0 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print('оцінки мають 12ти бальну систему')
#
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {round(self.average(),2)}'
#
# students = [
#     Student("Piter", [6,7,2,7,10]),
#     Student("Leha", [7,2,7,6,10]),
#     Student("Kaleka", [11,12,10,10,11]),
#     Student("Anton", [10,10,11, 11, 12]),
#     Student("Antonio", [4,8,2,5,9,12]),
# ]

# best_students = []
#
# def best(score):
#     for student in students:
#         if student.average() == score:
#             best_students.append(student.name)
#     return best_students
#
# average = []
#
# for student in students:
#     print(f'{student.name} - {student.average()}')
#     average.append(student.average())
#
# print(f'найкращий результат: {",".join(best(max(average)))} - {max(average)}')

#4
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("на карту меньше однієї гривні не кидають")
        else:
            self.balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            print("не обманюй систему олух, ти не можеш зняти відємне значення коштів чи 0")
        elif amount > self.balance:
            print("не так бистро кавбой, на рахунку немає стікі грошей")
        else:
            self.balance -= amount

    def info(self):
        print(f'{self.owner}: баланс: {self.balance}')

ivan = BankAccount('Misha',400)
ivan.deposit(500)
ivan.withdraw(100)
ivan.withdraw(2000)
olha = BankAccount('Stesha',67)
olha.withdraw(200)
olha.deposit(100)
olha.deposit(-100)

ivan.info()
olha.info()