#1

def area_circle(radius):
    return 3.14159 * radius ** 2

def area_rectangle(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    shape = input("фігура: ").strip().lower()
    if shape == "круг":
        r = float(input("рдіус:"))
        print(f"Площа круга:{area_circle(r)}")
    elif shape == "прямокутник":
        w = float(input("ширина: "))
        h = float(input("висота: "))
        print(f"площа прямокутника: {area_rectangle(w, h)}")
    elif shape == "трикутник":
        b = float(input("основа: "))
        h = float(input("висота: "))
        print(f"площа трикутника: {area_triangle(b, h)}")
    else:
        print("напиши нормально (круг | прямокутник | трикутник)")

# main()

#2
def is_prime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


def main():
    n = int(input("n = "))

    prime_status = "так" if is_prime(n) else "ні"
    print(f"просте число: {prime_status}")
    print(f"дільники: {divisors(n)}")
    print(f"сума цифр: {digit_sum(n)}")


# main()

def average(grades):
    return sum(grades) / len(grades)

def count_above(grades, value):
    count = 0
    for g in grades:
        if g > value:
            count += 1
    return count


def main():
    grades = [10, 8, 12, 9, 11]
    value = 9

    print(f"середній бал: {average(grades)}")
    print(f"мінімальна: {min(grades)}")
    print(f"максимальна: {max(grades)}")
    print(f"вище {value}: {count_above(grades, value)}")


# main()

#4
def check_length(password):
    return len(password) >= 8


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False

def validate_password(password):
    errors = []
    if not check_length(password):
        errors.append("менше 8 символів")
    if not has_digit(password):
        errors.append("немає цифри")
    if not has_upper(password):
        errors.append("немає великої літери")
    if not has_lower(password):
        errors.append("немає малої літери")
    if not has_special(password):
        errors.append("немає спеціального символу")

    if len(errors) == 0:
        return True, errors
    else:
        return False, errors


def main():
    password = input("password: ")
    is_valid, errors = validate_password(password)

    if is_valid:
        print("пароль надійний!")
    else:
        print("пароль не відповідає вимогам.")
        for error in errors:
            print(f"не виконано: {error}")


main()
