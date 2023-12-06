from datetime import datetime


def validate_int(number, min_n, max_n):
    try:
        number = int(number)
    except ValueError:
        return None

    if number < min_n or number > max_n:
        return None

    return number


def input_book_list(catalog, action_msg):
    books_input = None
    while books_input is None:
        books_input = input(f'Which books do you want to {action_msg} (e.g. 2,5,6,7)? ')
        books_input = list(map(lambda n: validate_int(n, 1, len(catalog.books)), books_input.split(',')))

        if all(books_input):
            print()
            return books_input

        print(f'Invalid books. Min: 1 Max: {len(catalog.books)}')


def input_int(msg, min_n, max_n):
    qty = None
    while qty is None:
        qty = validate_int(input(msg), min_n, max_n)
        if qty is None:
            print('Invalid quantity')
        else:
            return qty


def input_date(msg):
    date = None
    while date is None:
        try:
            date = datetime.strptime(input(msg), '%Y-%m-%d')
        except ValueError:
            print('Invalid date. Use format YYYY-MM-DD (e.g. 2024-02-01)')

    return date
