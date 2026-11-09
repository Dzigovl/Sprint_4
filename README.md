# qa_python
---
Проверка наличия жанров стандартного списка при инициализации объекта
__test_init_default_list_of_genres_true__
---
Проверка граничных значений длины названия добавляемой книги, 41 символ
__test_add_new_book_name_name_invalid_len_false__
---
Проверка неизменности жанра у книги добавленной повторно
__test_add_new_book_name_name_alreay_added_genre_not_empty__
---
Проверка установки жанра добавленной книге
__test_set_book_genre_book_added_and_genre_default_true__
---
Проверка невозможности установки нестандартного жанра
__test_set_book_genre_book_added_and_genre_not_default_true__
---
Проверка получения жанра добавленной книги
__test_get_book_genre_book_with_genre_true__
---
Проверка фильтрации по стандартному жанру (Фантастика)
__test_get_books_with_specific_genre_fantastic_dict_of_two_fantastic_books__
---
Проверка фильтрации по нестандартного жанру (Роман)
__test_get_books_with_specific_genre_romance_empty_list__
---
Проверка получения словаря добавленных книг
__test_get_books_genre_one_book_all_added_books_dict__
---
Проверка возврата книг, подходящих для детей, без запрещенных жанров
__test_get_books_for_children_five_books_dict_of_three_books_without_disallowed_genre__
---
Проверка добавления книги, уже присутсвующей в словаре, в Избранное
__test_add_book_in_favorites_one_book_one_book_in_favorites__
---
Проверка добавления книги, уже добавленной в Избранное, в Избранное
__test_add_book_in_favorites_one_book_in_favorites_one_book_favorites__
---
Проверка не добавления книги, отсутствующей в словаре, в Избранное
__test_add_book_in_favorites_one_book_not_in_dict_empty_favorites_list__
---
Проверка удаления книги из Избранного
__test_delete_book_from_favorites_one_book_in_favorites_empty_favorites_list__
---
Проверка удаления книги, отсутствующей в Избранном, из Избранного
__test_delete_book_from_favorites_one_book_not_in_favorites_empty_favorites_list__
---
Получение списка Избранных книг
__test_get_list_of_favorites_books_five_books_three_books_in_favorites__
---