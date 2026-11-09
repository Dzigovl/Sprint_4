import pytest

from main import BooksCollector


@pytest.fixture
def library():

    library = BooksCollector()
    return library

@pytest.fixture
def one_book(library):

    library.add_new_book("Оно")
    library.set_book_genre("Оно", 'Ужасы')
    return library

@pytest.fixture
def five_books(one_book):
    one_book.add_new_book('Автостопом по Галактике')
    one_book.set_book_genre('Автостопом по Галактике', 'Фантастика')
    one_book.add_new_book('Десять негритят')
    one_book.set_book_genre('Десять негритят', 'Детективы')
    one_book.add_new_book('Ревизор')
    one_book.set_book_genre('Ревизор', 'Комедии')
    one_book.add_new_book('Дюна')
    one_book.set_book_genre('Дюна', 'Фантастика')
    return one_book