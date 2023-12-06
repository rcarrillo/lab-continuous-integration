from books import Book, Catalog
from utils import validate_int, input_book_list, input_int, input_date
from data import books_d


def print_catalog(title, catalog, book_numbers=None, ):
    print(title)
    print('-' * 80)
    catalog.show(book_numbers)
    print()


def checkout(catalog):
    books_to_checkout = input_book_list(catalog, 'checkout')

    print_catalog('Books to checkout', catalog, books_to_checkout)

    for number in books_to_checkout:
        book = catalog.get_book(number)
        print(f'Checkout: {book} | Available units: {book.available}')
        qty = input_int('How many copies? ', 1, book.available)
        catalog.checkout_book(number, qty)
        print('-')

    catalog.confirm_checkout()


def returns(catalog):
    books_to_return = input_book_list(catalog, 'return')

    print_catalog('Books to return', catalog, books_to_return)

    for number in books_to_return:
        book = catalog.get_book(number)
        print(f'Return: {book} | Available units: {book.available}')
        qty = input_int('How many copies? ', 1, book.available)
        catalog.return_book(number, qty)
        print('-')

    return_date = input_date('How many days? ')

    catalog.confirm_return()


def main():
    catalog = Catalog()
    for book_d in books_d:
        catalog.add_book(Book(**book_d))

    print_catalog('Catalog', catalog)

    checkout_ok = False
    while not checkout_ok:
        checkout(catalog)
        if len(catalog.books_to_checkout) > 10:
            print('Checkout exceeded 10 books')
        else:
            checkout_ok = True

    returns(catalog)

    print_catalog('Final catalog', catalog)


if __name__ == '__main__':
    main()
