import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection

def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture
def collection_five_books(collection):
    collect = collection
    books = ['Гарри Поттер', 'Король Лев', 'Туман', 'Кот Саймона', 'Просто умереть']
    genre = ['Фантастика', 'Мультфильмы', 'Ужасы', 'Комедии', 'Детективы']
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])

    return collect