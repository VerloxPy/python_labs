# n = int(input())
#
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1
#
# n = int(input())
# suma = 0
#
# for i in range(1, n + 1):
#     suma += i
#     print(f'сума дорівнює {suma}')
#
# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count += 1
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     print(n)
#
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# n = 1234
#igit_last = n %10
# digit_first = n % 100

# while n > 0:
#     digit = n % 10
#     print(f'остання цифра {digit}')
#     # n = n // 10
#     n //= 10

n = 1934
max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10
print(max_digit)

