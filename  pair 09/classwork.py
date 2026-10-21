class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    def available(self):
        return self.copies > 0

book1 = Book('Кобзар', "Тарас Шевченко" ,15)

print(book1.available())

class Counter:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1

counter1 = Counter()
counter2 = Counter()
print(counter1.value, counter2.value)

counter1.increment()
counter1.increment()
counter2.increment()
print(counter1.value, counter2.value)


class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies

    def giveone(self):
        if self.copies > 0:
            self.copies -= 1