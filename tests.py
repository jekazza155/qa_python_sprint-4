import pytest

from conftest import collection
from main import BooksCollector

class TestBooksCollector:
    #Проверка добавления трех книг в словарь books_genre

    def test_add_new_book_adding_three_books_success(self, collection):
        books = ['Мёртвые души', 'Гарри Поттер', 'Король Лев']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    #Проверка установления жанра по умолчанию в добавленной книге

    def test_add_new_book_check_genre_success(self, collection):
        first_book = 'Мёртвые души'
        collection.add_new_book(first_book)
        assert collection.get_book_genre(first_book) == ''

    #Негативная проверка добавления книг с именем 0 и больше 40 символов

    @pytest.mark.parametrize('book',
                             ['', 'МёртвыеМёртвыеМёртвыеМёртвыеМёртвыеМёртвыеМёртвые']
                             )
    def test_add_new_book_add_incorrect_name_not_added(self, book, collection):
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    #Негативная проверка повторного добавления одинаковых книг

    def test_add_new_book_add_double_books_not_added(self, collection):
        books = ['Отцы и дети', 'Отцы и дети']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 1

    #Проверка добавления жанра из списка genre книге из списка books_genre

    def test_set_book_genre_added(self, collection):
        first_book = 'Гарри Поттер'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        assert collection.get_book_genre(first_book) == genre

    #Проверка изменения жанра из списка genre книге из списка books_genre

    def test_set_book_genre_changed(self, collection):
        first_book = 'Гарри Поттер'
        genre = 'Фантастика'
        other_genre = 'Детективы'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        collection.set_book_genre(first_book, other_genre)
        assert collection.get_book_genre(first_book) == other_genre

    #Негативная проверка добавления жанра не из списка genre книге из списка books_genre

    def test_set_book_genre_missing_genre_not_added(self, collection):
        first_book = 'Гарри Поттер'
        missing_genre = 'Приключения'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, missing_genre)
        assert collection.get_book_genre(first_book) == ''

    #Проверка вывода книги определенного жанра

    def test_get_books_with_specific_genre_success(self, collection_five_books):
        assert collection_five_books.get_books_with_specific_genre('Ужасы') == ['Туман']

    #Негативная проверка вывода отсутствующей книги определенного жанра

    def test_get_books_with_specific_genre_missing_book(self, collection_five_books):
        assert len(collection_five_books.get_books_with_specific_genre('Приключения')) == 0

    #Проверка вывода списка книг с жанром для детей

    def test_get_books_for_children_success(self, collection_five_books):
        children_books = collection_five_books.get_books_for_children()
        assert len(children_books) == 3 and children_books == ['Гарри Поттер', 'Король Лев', 'Кот Саймона']

    #Проверка добавления книги из списка books_genre в избранное

    def test_add_book_in_favorites_add_one_book_added(self, collection):
        first_book = 'Хоббит'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    #Негативная проверка добавления книги не из списка books_genre в избранное

    def test_add_book_in_favorites_add_missing_book_not_added(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_book_in_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    #Негативная проверка повторного добавления книги в избранное

    def test_add_book_in_favorites_add_double_books_not_added(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book

    #Проверка удаления книги из списка избранное
    def test_delete_book_from_favorites_book_deleted(self, collection):
        first_book = 'Гарри Поттер'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0

    #Вывод жанра книги по ее названию

    def test_get_book_genre_get_genre(self):
        collection = BooksCollector()
        collection.add_new_book('Туман')
        collection.set_book_genre('Туман', 'Ужасы')
        assert collection.get_book_genre('Туман') == 'Ужасы'

    #Получения словаря

    def test_get_books_genre(self, collection_five_books):
        expected_genres = {
            'Гарри Поттер': 'Фантастика',
            'Король Лев': 'Мультфильмы',
            'Кот Саймона': 'Комедии',
            'Туман': 'Ужасы',
            'Просто умереть': 'Детективы'
        }
        actual_genres = collection_five_books.get_books_genre()
        assert actual_genres == expected_genres

    def test_get_list_of_favorites_books_get_list(self, collection):
        first_book = 'Рыба меч'
        second_book = 'Сердце ангела'
        collection.add_new_book(first_book)
        collection.add_new_book(second_book)
        collection.add_book_in_favorites(first_book)
        collection.add_book_in_favorites(second_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert first_book in favorites
        assert second_book in favorites




