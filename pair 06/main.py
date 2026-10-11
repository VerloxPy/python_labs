import tkinter as tk
from tkinter import messagebox
import student_utils as st

students = ["Anna", "Ivan", "Olha"]

def report():
    value = entry.get().strip()

    if not value.isdecimal() or not 1 <= int(value) <= 20:
        messagebox.showerror("помилка", "введіть 1-20")
        return

    report = ""
    for name in students:
        grades = st.generate_grades(int(value))
        avg = st.average_grade(grades)
        level = st.get_level(avg)
        report += f"{name}: \n    оцінки - {grades}  \n    середнє - {avg:.1f} \n    рівень - {level}\n"

    print(report)
    result.delete("1.0", tk.END)
    result.insert(tk.END, report)

app = tk.Tk()
app.title("статістік оф стюдентс")
app.geometry("500x400")

tk.Label(app, text="кількість оцінок (1-20):").pack()
entry = tk.Entry(app)
entry.insert(0, "5")
entry.pack()
tk.Button(app, text="доклад", command=report).pack()
result = tk.Text(app, height=12, width=55)
result.pack()

app.mainloop()