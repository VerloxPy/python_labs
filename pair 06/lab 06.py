#1

import math


radius = float(input("hflsec: "))
catets = list(map(float, input("введіть два катити: ").split(",")))
items = int(input("кількість упаковок: "))
pack = int(input("в упаковці: "))

area = math.pi * radius ** 2
hypotenuse = math.sqrt(catets[0] ** 2 + catets[1] ** 2)
packs = math.ceil(items / pack)

print("площя круга:", round(area, 2))
print("гіпотенза:", round(hypotenuse, 2))
print("потрібно упаковок:", packs)

#2


import random
import statistics

s = int(input("кількість оцінок: "))
grades = []

while s <= 0:
    s = int(input("додатнє число введи олух: "))
for i in range(s):
    grades.append(random.randint(1, 12))

count = 0

for grade in grades:
    if grade >= 10:
        count += 1

print("оцінки:", grades)
print("Min:", min(grades))
print("Max:", max(grades))
print("середнє:", round(statistics.mean(grades), 2))
print("медіана :", statistics.median(grades))
print("оцінок 10 – 12:", count)

#3

from datetime import*

day = int(input("день: "))
month = int(input("місяць: "))
year = int(input("рік: "))

party = date(year, month, day)
today = date.today()

days = (party - today).days

if days > 0:
    print(f" {days} днів до дня Х")
if days < 0:
    print(f"день Х пройшов {abs(days)} днів тому")
if days == 0:
    print("АОАОАОА ДЕНЬ Х")