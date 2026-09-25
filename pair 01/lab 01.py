#1

#a
# a = int(input("введіть любе ціле число: "))
# if a % 2 == 0:
#     print("парне")
# else:
#     print("не парне")

#b
# b = int(input("введіть свій вік: "))
# if b >= 18:
#     print("Ви повнолітні!")
# elif 0 < b <= 18:
#     print("Ви неповнолітній!")
# else:
#     print("число правильно введи, дурень")

#c
# c = int(input("введіть числовий радіус кола: "))
# print(f"площа кола з радіусом {c}: {c**2 * 3.14}")
# print(f"довжина цього кола: {2 * c * 3.14}")

#d
# a, b = map(int, input('введіть 2 числа через пробіл: ').split())
# print(max(a, b))


#2

# x, y = map(int, input('координати точки A(x;y) через пробіл: ').split())
# if x > 0 and y > 0:
#     print("1 чверть")
# elif x > 0 and y < 0:
#     print("4 чверть")
# elif x < 0 and y > 0:
#     print("2 чверть")
# elif x < 0 and y < 0:
#     print("3 чверть")
# elif x == 0 and y != 0:
#     print("лежить на  Oy")
# elif y == 0 and x != 0:
#     print("Лежить на Оx")
# elif x == 0 and y == 0:
#     print("початок коoрдинат")


#3
# age = input('вкажіть ваш вік: ')
# if 120 > int(age) >0 :
#     if int(age[-1]) == 1:
#         print(f'{age} рік')
#     elif 5 > int(age[-1]) > 1:
#         print(f'{age} роки')
#     else:
#         print(f'{age} років')
# else:
#     print('-"не бреши мені, Тоні, \n  навіть не намагайся мене намахати"')