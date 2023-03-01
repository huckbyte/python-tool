class Book:
    def __init__(self, title, author, pages,content):
        self.title = title
        self.author = author
        self.page = pages
        self.content = content


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except:
            return "No such book"

    def add_book(self, book):
        self.books.append(book)


class Person:
    def __init__(self, name):
        self.name = name


class Reader(Person):
    def __init__(self, name, current_book):
        super().__init__(name)
        self.current_book = current_book
        self.current_page = None

    def turn_page(self, page):
        if self.current_page:
            self.current_page += 1
            return
        self.current_page = 1

class Formatter:
    def format(self, book):
        return book.content


class Printer:
    def get_book(self, book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


b = Book("Ethic's","Forbiden","Hezron",41)
f = Formatter()
p = Printer()

print(p.get_book(b, f))
