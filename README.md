# qa_python

#1) test_add_new_book_book_name_too_long_not_added - проверяет, что нельзя добавить книгу, если в длина названия больше 41 
#2) def test_set_book_genre_sets_valid_genre - проверяет, устанавливается ли жанр книги, если книга есть в books_genre и её жанр входит в список genre.
#3) def test_get_book_genre_returns_set_book_genre - проверяет, вывод жанра книги по её имени
#4) def test_get_books_with_specific_genre_returns_books_with_set_genre - проверяет, вывод списка книг с определённым жанром.  
#5) def test_get_books_genre_returns_dictionary_books_genre - проверяет, вывод словаря books_genre  
#6) def test_get_books_for_children_exclude_age_restricted_genres - проверяет, что get_books_for_children возвращает книги, которые подходят детям.
#7) def test_add_book_in_favorites_adds_book - проверяет, что add_book_in_favorites добавляет книгу в избранное 
#8) def test_delete_book_from_favorites_delete_book - проверяет, что delete_book_from_favorites удаляет книгу из избранного, если она там есть
#9) def test_get_list_of_favorities_books_returns_list_of_favorities_books - проверяет, что get_list_of_favorites_books выдает список избранный книг
# NEW 10) def test_get_books_genre_returns_books_dictionary - (позитивная проверка для get_books_genre) проверяет, что get_books_genre выдает словарь books_genre
# NEW 11) def test_get_books_genre_returns_book_dictionary_with_no_genre - (позитивная проверка для get_books_genre) проверяет, что get_books_genre выдает словарь books_genre, если у книги не задан genre 