#1
def file_anal_itics(filename="text.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

        chars = len(content)
        words = len(content.split())
        lines = len(content.splitlines())

        if lines == 0:
            print("файл порожній альо")
            return

        max_len = -1
        max_num = -1
        max_text = ""

        for n, line in enumerate(lines, start=1):
            current_len = len(line)
            if current_len > max_len:
              max_len = current_len
              max_n = n
              max_text = line


        print(f"Рядків: {lines}")
        print(f"Слів: {words}")
        print(f"Символів: {chars}")
        print(f"Найдовший рядок: No{max_num}, {max_len} символів")
        print(f"Текст: {max_text}")


#2
def search():
    fragment = input("введіть фрагмент для пошуку: ")

    found = False
    with open("text.txt", "r", encoding="utf-8") as file:
        for n, line in enumerate(file, start=1):
            clean_line = line.strip()
            if fragment.lower() in clean_line.lower():
                print(f"{n}: {clean_line}")
                found = True

    if not found:
        print("нічо не знайдено")

#3

students = []
with open("students.txt", "r", encoding="utf-8") as file:
  for line in file:
    name, bal = line.strip().split(";")
    score = int(bal)

    if score > 80:
      students.append([name, score])

students.sort(reverse=True)

with open("result.txt", "w", encoding="utf-8") as file:
  for name, bal in students:
    print(f"{name};{bal}", file=file)

#4


stgrades = {}


def load_grades():
  with open("grades.txt", "r", encoding="utf-8") as file:
    for line in file:
      clean_line = line.strip()
      if not clean_line:
        continue
      name, subject, grade = clean_line.split(";")
      grade = int(grade)

      if name not in stgrades:
        stgrades[name] = []
      stgrades[name].append(grade)


def calculate_statistics(data):
  report_data = []
  for name, grades in data.items():
    average = sum(grades) / len(grades)
    report_data.append([name, len(grades), average])

  return report_data


def generate_report(report_data):
  formatted_data = []
  for name, count, average in report_data:
    formatted_data.append([average, name, count])

  formatted_data.sort(reverse=True)

  with open("report.txt", "w", encoding="utf-8") as file:
    for average, name, count in formatted_data:
      line_str = f"{name}\n{count} оцінок - середній бал: {average}"
      print(line_str, file=file)

    best_average, best_name, _ = formatted_data[0]
    best_line = f"афігенний учень: {best_name} - {best_average}"
    print(best_line, file=file)





load_grades()
stats = calculate_statistics(stgrades)
generate_report(stats)
