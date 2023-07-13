class Book:

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def info(self):
        print("{}, {} ({}), {}".format(self.title, self.author, self.year, self.genre))


my_favourite_book = Book("Гарри Поттер", "Дж. К. Роулинг", 1997, "Фэнтези")
my_favourite_book.info()