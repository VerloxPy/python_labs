#1.
# text = input("Введіть текст: ")
# golosni = "aeiouyаеєиіїоуюя"
#
# total_chars = len(text)
# letters_count = 0
# digits_count = 0
# spaces_count = 0
# vowels_count = 0
#
# for i in text:
#     if i.isalpha():
#         letters_count += 1
#         if i.lower() in golosni:
#             vowels_count += 1
#     elif i.isdigit():
#         digits_count += 1
#     elif i.isspace():
#         spaces_count += 1
#
# words_count = len(text.split())
#
#
# print(f"cимволи: {total_chars}")
# print(f"літери: {letters_count}")
# print(f"цифри: {digits_count}")
# print(f"Пробіли: {spaces_count}")
# print(f"голосні: {vowels_count}")
# print(f"слова: {words_count}")


# 2
# name = input("Введіть ПІБ: ")
# parts = name.split()
#
# if len(parts) == 3:
#     firstname = parts[0].capitalize()
#     initial = parts[1][0].upper()
#     last_initial = parts[2][0].upper()
#
#     formatted_name = f"{firstname} {initial}.{last_initial}."
#     print(formatted_name)
# else:
#     print("нормально своє ПІБ введи, олух (Прізвище, Ім'я, По батькові).")

# 3/
# s1 = input()
# s2 = input()
#
# n1 = s1.replace(" ", "").lower()
# n2 = s2.replace(" ", "").lower()
#
# if sorted(n1) == sorted(n2):
#     print(f"Рядки '{n1}' та '{n2}' є анаграмами.")
# else:
#     print(f"Рядки '{n1}' та '{n2}' не є анаграмами.")
#

4.
text = input('введіть текст')

words = text.split()
clean_words = []

for w in words:
    cw = w.strip(".,!?:;\"'()[]{}")
    if cw:
        clean_words.append(cw)


shortest = [clean_words[0]]
longest = [clean_words[0]]

for w in clean_words[1:]:
    if len(w) < len(shortest[0]):
        shortest = [w]
    elif len(w) == len(shortest[0]) and w not in shortest:
        shortest.append(w)

    if len(w) > len(longest[0]):
        longest = [w]
    elif len(w) == len(longest[0]) and w not in longest:
        longest.append(w)

unique_words = []
for w in clean_words:
    if w.lower() not in unique_words:
        unique_words.append(w.lower())

print("Найдовші:", ", ".join(longest))
print("Найкоротші:", ", ".join(shortest))
print("Унікальних слів:", len(unique_words))

old_w = input()
new_w = input()

res = []
for w in words:
    cw = w.strip(".,!?:;\"'()[]{}")
    if cw.lower() == old_w.lower():
        res.append(w.replace(cw, new_w))
    else:
        res.append(w)

print("Після заміни:", " ".join(res))