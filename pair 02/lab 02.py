1
a = int(input("a: "))
suma = 0
count = 0
for i in range(1, a + 1):
    if i % 3 == 0 or i % 5 == 0:
        suma += i
        count += 1

if count > 0:
    average = suma / count
    print(f"сума: {suma} ")
    print(f"кількість: {count}")
    print(f"середнє арифметичне: {average}")
else:
    print("таких чисел немає")

2
a = int(input("введіть число"))

if a == 0:
    count = 1
    total = 0
    maximum = 0
    minimum = 0
else:
    count = 0
    total = 0
    maximum = 0
    minimum = 9

    b = a
    while b > 0:
        digit = b % 10
        total += digit
        count += 1

        if digit > maximum:
            maximum = digit
        if digit < minimum:
            minimum = digit

        b = b // 10
print(f"кількість цифр: {count}")
print(f"сума цифр: {total}")
print(f"найбільша цифра: {maximum}")
print(f"найменша цифра: {minimum}")


3
a = int(input("a:"))
print("Числа щл діляться на всі свої ненульові цифри:")

for num in range(1, a + 1):
    temp = num
    good = True

    while temp > 0:
        digit = temp % 10

        if digit != 0:
            if num % digit != 0:
                good = False
                break
        temp = temp // 10

    if good:
        print(num)

4
width = int(input('ширина: '))
height = int(input('виста:'))

border = input("знак контуру: ")
inside = input("знак внутрішньої частини: ")

if width < 3 or height < 3:
    print("мінімальний розмір рамки — 3 × 3.")
else:
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    print(border, end="")
            else:
                print(inside, end="")
