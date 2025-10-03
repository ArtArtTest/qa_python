import pytest
from main import BooksCollector

class TestBooksCollector:
    
    def test_add_new_book_book_name_too_long_not_added(self):
        collector = BooksCollector()    
        long_book_name = "Z" * 41
        collector.add_new_book(long_book_name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize("genre",['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_sets_valid_genre(self,genre):
        collector = BooksCollector()
        book = "Властелин колец"
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_returns_set_book_genre(self):
        collector = BooksCollector()
        book = "Властелин колец"
        collector.add_new_book(book)
        collector.set_book_genre(book, 'Фантастика')
        assert collector.get_book_genre(book) == 'Фантастика'
    
    def test_get_books_with_specific_genre_returns_books_with_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_new_book("Звездные войны")
        collector.set_book_genre("Властелин колец", 'Фантастика')
        collector.set_book_genre("Звездные войны", 'Комедии')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ["Властелин колец"]
    
    def test_get_books_genre_returns_dictionary_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", 'Фантастика')
        books = collector.get_books_genre()
        assert books == {"Властелин колец":'Фантастика'}

    def test_get_books_for_children_exclude_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_new_book("Чук и Гек")
        collector.set_book_genre("Оно",'Ужасы')
        collector.set_book_genre("Чук и Гек", 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert "Чук и Гек" in children_books
        assert "Оно" not in children_books

    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        book = "Властелин колец"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        book = "Звездные войны"
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorities_books_returns_list_of_favorities_books(self):
        collector = BooksCollector()
        collector.add_new_book("Звездные войны")
        collector.add_book_in_favorites("Звездные войны")
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        favorities_books = collector.get_list_of_favorites_books()
        assert favorities_books == ["Звездные войны", "Властелин колец"]

