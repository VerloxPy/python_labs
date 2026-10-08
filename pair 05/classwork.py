#прошу вибачення, майже весь день не було світла, через що мене не було на уроці

def say_hello():
    print("Привіт, Python!")
    say_hello()

def greet(name):
    print(f"Привіт, {name}!")
    greet("Ivan")


def area_rectangle(a, b):
    return a * b
    area = area_rectangle(7, 4)
    print("Площа:", area)
width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

area_rectangle(width, height)

print(f"Площа дорівнює {S} см2")


def price_with_discount(price, discount = 0):
    return price - price * discount / 100

print(price_with_discount(1000))


def min_max(numbers):
    return min(numbers), max(numbers)
minimum, maximum = min_max([7, 2, 15, 4, 9])
print("Min:", minimum)
print("Max:", maximum)



