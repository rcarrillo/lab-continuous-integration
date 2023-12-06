class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __repr__(self):
        return f'Book(\'{self.title}\', \'{self.author}\', {self.available})'


class Catalog:
    def __init__(self):
        self.books = []
        self.books_to_checkout = []
        self.books_to_return = []

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, number):
        return self.books[number - 1]

    def checkout_book(self, number, qty):
        self.books_to_checkout.append((number, qty))

    def confirm_checkout(self):
        for number, qty in self.books_to_checkout:
            self.get_book(number).available -= qty
        self.books_to_checkout = []

    def return_book(self, number, qty):
        self.books_to_return.append((number, qty))

    def confirm_return(self):
        for number, qty in self.books_to_return:
            self.get_book(number).available += qty
        self.books_to_return = []

    def show(self, books=None):
        for i, book in enumerate(books or self.books, start=1):
            if isinstance(book, int):
                book = self.get_book(book)
            print(f'{i}) {book.title} by {book.author} | Available: {book.available}')
