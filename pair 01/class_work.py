# a = 12
# b = 12.4
# c ='sting'
# d = True
#
# print( a + b)

# a = int(input("введи перше число: "))
# b = int(input("введи друге число: "))
# print(int(a) + int(b)) #конкатинація
# print(a + b)

# + -
# *, /, %, //
# **

#конкатенація
# print ('hello' * 2)

# a = int(input())
# b = int(input())
# c = int(input())
#
# a, b, c = map(int, input("введи три числа через пробіл").split())
# if a > b and a > c:
#     print(a)
# elif b > c and b > a:
#     print(b)
# elif c > a and c > b:
#     print(c)
# else:
#     print("a == b == c")









if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif a < b:
    if b > c:
        print(b)
    else:
        print(c)
elif c > a:
    if c > b:
        print(c)
    else:
        print(b)
else:
    print(a == b == c)