import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_init_default_list_of_genres_true(self, library):
        default_genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        default_genres_age_rating = ['Ужасы', 'Детективы']
        assert library.genre == default_genres
        assert library.genre_age_rating == default_genres_age_rating


    @pytest.mark.parametrize('unsupported_book_name',['a'*41, ''])
    def test_add_new_book_name_name_invalid_len_false(self, library, unsupported_book_name):
        library.add_new_book(unsupported_book_name)
        assert not unsupported_book_name in library.books_genre.keys()

    def test_add_new_book_name_name_alreay_added_genre_not_empty(self, one_book):
        one_book.add_new_book('Оно')
        assert one_book.books_genre['Оно'] == 'Ужасы'


    @pytest.mark.parametrize(
            'book_name,book_genre',
            [
                ['Оно', 'Ужасы'],
                ['Десять негритят', 'Детективы'],
                ['Ревизор','Комедии']
            ]
    )
    def test_set_book_genre_book_added_and_genre_default_true(self, library, book_name, book_genre):
        library.add_new_book(book_name)
        library.set_book_genre(book_name, book_genre)
        assert library.books_genre[book_name] == book_genre

    def test_set_book_genre_book_added_and_genre_not_default_true(self, library):
        library.add_new_book('Мартин Иден')
        library.set_book_genre('Мартин Иден','Романы')
        assert library.books_genre['Мартин Иден'] == ''


    def test_get_book_genre_book_with_genre_true(self, one_book):
        assert one_book.get_book_genre('Оно') == 'Ужасы'


    def test_get_books_with_specific_genre_fantastic_dict_of_two_fantastic_books(self, five_books):
        fantastic_books = five_books.get_books_with_specific_genre('Фантастика')
        assert len(fantastic_books) == 2
        assert 'Дюна' in fantastic_books
        assert 'Автостопом по Галактике' in fantastic_books

    def test_get_books_with_specific_genre_romance_empty_list(self, five_books):
        romance_books = five_books.get_books_with_specific_genre('Роман')
        assert len(romance_books) == 0


    def test_get_books_genre_one_book_all_added_books_dict(self, one_book):
        books_dict = one_book.get_books_genre()
        assert isinstance(books_dict, dict)
        assert books_dict['Оно'] == 'Ужасы'


    def test_get_books_for_children_five_books_dict_of_three_books_without_disallowed_genre(self, five_books):
        children_books = five_books.get_books_for_children()
        assert len(children_books) == 3
        assert 'Автостопом по Галактике' in children_books
        assert 'Ревизор' in children_books
        assert 'Дюна' in children_books


    def test_add_book_in_favorites_one_book_one_book_in_favorites(self, one_book):
        one_book.add_book_in_favorites('Оно')
        assert len(one_book.favorites) == 1
        assert one_book.favorites[0] == 'Оно'

    def test_add_book_in_favorites_one_book_in_favorites_one_book_favorites(self, one_book):
        one_book.add_book_in_favorites('Оно')
        one_book.add_book_in_favorites('Оно')
        assert len(one_book.favorites) == 1
        assert one_book.favorites[0] == 'Оно'

    def test_add_book_in_favorites_one_book_not_in_dict_empty_favorites_list(self, one_book):
        one_book.add_book_in_favorites('Дюна')
        assert len(one_book.favorites) == 0


    def test_delete_book_from_favorites_one_book_in_favorites_empty_favorites_list(self, one_book):
        one_book.add_book_in_favorites('Оно')
        one_book.delete_book_from_favorites('Оно')
        assert len(one_book.favorites) == 0

    def test_delete_book_from_favorites_one_book_not_in_favorites_empty_favorites_list(self, one_book):
        one_book.add_book_in_favorites('Оно')
        one_book.delete_book_from_favorites('Дюна')
        assert len(one_book.favorites) == 1
        assert one_book.favorites[0] == 'Оно'


    def test_get_list_of_favorites_books_five_books_three_books_in_favorites(self, five_books):
        five_books.add_book_in_favorites('Оно')
        five_books.add_book_in_favorites('Дюна')
        five_books.add_book_in_favorites('Ревизор')
        list_of_favorites_books = five_books.get_list_of_favorites_books()
        assert len(list_of_favorites_books) == 3
        assert isinstance(list_of_favorites_books, list)