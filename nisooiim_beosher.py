# from datetime import datetime, timedelta
#
# today = datetime.today()
# today_delda = timedelta(days=+0)
#
# tendays_delta = timedelta(days=+10)
#
# toda_ten_del = today + tendays_delta
#
# day = toda_ten_del.strftime("%A")
# date = toda_ten_del.strftime("%d/%m/%y")
#
# print(f"{day} ,in the: {date} ")
#
# ########################################################################################################################
#
#     def choose_genre(self, genre):
#         if genre == Genre_list_enum.Science:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Fiction:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Fantasy:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Drama:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Romance:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Comedy:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Zombies:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Action:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Historical:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Horror:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.War.value:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Story_Telling:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Folklore:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Fairy_tale:
#             self._book_genres.append(genre)
#         elif genre == Genre_list_enum.Fable:
#             self._book_genres.append(genre)
#             return self._book_genres
#         else:
#             print('this genre is unknown to Shawshank facility')
########################################################################################################################

# def add_book(self, book_id: int, book_name: str, author_name: str, year_published: int, loan_type: int, genres: set, languages: set):
#     book = Book(book_id, book_name, author_name, year_published, loan_type, genres, languages)
#     capital_book: str = book_name.capitalize()
#     if capital_book in self._books:
#         if book_id in self._books[capital_book]:                  # mapping book id's as a set for each book name
#             return False
#         else:
#             self._books[capital_book].add(book_id)
#     else:
#         self._books[capital_book] = {book_id}
#     self.add_author(author_name)                                                    # adds author to authors set
#     author = Author(author_name)
#     capital_author = author_name.title()
#     if capital_author in self._authors_to_books:
#         if capital_book in self._authors_to_books[capital_author]:
#             if book_id in self._authors_to_books[capital_author][capital_book]:
#                 pass
#             else:
#                 self._authors_to_books[capital_author][capital_book].add(book_id)   # mapping author to his books
#         else:                                                                       #              and their id's
#             self._authors_to_books[capital_author][capital_book] = {book_id}
#     else:
#         self._authors_to_books[capital_author] = {capital_book:{book_id}}
#     self._blis.append(book)
########################################################################################################################

