import  chezafile
from math import *
from math import sqrt

import statistics as st
import random
from datetime import *

a = 81
print(sqrt(a))
grades = [10, 7, 9, 7,  2, 11, 2]
print(f'Средній бал: {st.mean(grades)}')
print(f'мода:{st.mode(grades)}')
print(f'медіана: {st.median(grades)}')

radius = 5
print(f'circle area: {round((pi * pow(radius, 2)), 2)} ')

b = 2.559939938823
print(ceil(b))
print(floor(b))

balls = 25
items = 6
print(f'Повністю заповнені коробки: {floor(balls / items)}')
print(f'Коробок потрібно всього:{ceil(balls / items)}')

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)
print(random.choice(numbers))
print(f'Сьогодні: {datetime.today()}')
print(f'Now: {datetime.now()}')


year = 2026
day = 31
month = 12

user_day = datetime.today()
print(datetime(year, month, day) - user_day)


year = 2026
day = 31
month = 12

print(chezafile.squre(5))
grades2 = [10, 7, 9, 2, 11, 2]
print(chezafile.average(grades2))



from tkinter import *

def text():
    message = "Welcome to the game"
    label2["text"] = message

def clear():
    label2["text"] = ""


window = Tk()
window.title("my program")
window.geometry("500x500")
window.resizable(width=False, height=False)
window["bg"] = "#2633E3"

label = Label(
    window,
    text="My program",
    bg="#2633E3",
    font=("Arial", 25)
)
label.grid(row=0, column=0, columnspan=2)

btn1 = Button(
    window,
    text="ok",
    font=("Arial", 20),
    width=8,
    activebackground="#CF0A9E",
    command=text
)
btn2 = Button(
    window,
    text="cancel",
    font=("Arial", 20),
    width=8,
    activebackground="#CF0A9E",
    command=clear
)

btn1.grid(row=1, column=0, pady=20, padx=10)
btn2.grid(row=1, column=1, pady=20, padx=10)

label2 = Label(
    window,
    text="",
    bg="#0A28CF",
    font=("Arial", 16)
)
label2.grid(row=2, column=0, columnspan=2, pady=10)
window.mainloop()