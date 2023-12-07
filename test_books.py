import pytest

from books import Book, Catalog


def test_book_creation():
    book = Book('Title', 'Author', 20)
    assert book.title == 'Title'
    assert book.author == 'Author'
    assert book.available == 20


def test_catalog():
    catalog = Catalog()
    book1 = Book('Title1', 'Author', 20)
    book2 = Book('Title2', 'Author', 20)
    catalog.add_book(book1)
    catalog.add_book(book2)
    assert len(catalog.books) == 2


def test_checkout():
    catalog = Catalog()
    book1 = Book('Title1', 'Author', 20)
    book2 = Book('Title2', 'Author', 10)
    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.checkout_book(1, 5)
    catalog.checkout_book(2, 3)
    assert len(catalog.books) == 2
    assert catalog.get_book(1).available == 20
    assert catalog.get_book(2).available == 10
    catalog.confirm_checkout()
    assert catalog.get_book(1).available == 15
    assert catalog.get_book(2).available == 7


def test_return():
    catalog = Catalog()
    book1 = Book('Title1', 'Author', 20)
    book2 = Book('Title2', 'Author', 10)
    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.return_book(1, 5)
    catalog.return_book(2, 3)
    assert len(catalog.books) == 2
    assert catalog.get_book(1).available == 20
    assert catalog.get_book(2).available == 10
    catalog.confirm_return()
    assert catalog.get_book(1).available == 25
    assert catalog.get_book(2).available == 13
