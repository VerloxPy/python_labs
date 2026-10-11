#4
from random import *



def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(randint(1, 12))

    return grades


def average_grade(grades):
    return sum(grades) / len(grades)


def get_level(average):
    if average >= 10:
        return "відмінник"
    elif average >= 7:
        return "норм"
    elif average >= 4:
        return "домохозяйка"
    else:
        return "лох"