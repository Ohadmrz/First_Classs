# import random
from genre import Genre
from language import Language
from colors import *




class Book:
    def __init__(self, book_id: int, book_name: str, author_name: str, publication_year: int, loan_type: int, genres: set, language):
        self._book_id: int = book_id                                 #  random.randint(1000, 10000) #
        self._book_name: str = book_name
        self._author_name: str = author_name
        self._publication_year: int = publication_year
        self._loan_type: int = loan_type
        self._book_genres: set = genres
        self._book_language = language

    def get_book_id(self) -> int:                                        # get -   id
        return self._book_id

    def get_book_name(self) -> str:                                      # get -   name
        return self._book_name.title()

    def set_book_name(self, new_name: str) -> None:                      # set -   name
        self._book_name = new_name.title()

    def get_book_author(self) -> str:                                   # get -    author
        return self._author_name.title()

    def get_publication_year(self) -> int:                              # get -  publication year
        return self._publication_year

    def set_publication_year(self, new_year: int) -> None:              # set -  publication year
        self._publication_year = new_year

    def get_loan_type(self) -> int:                                     # get -   loan type
        return self._loan_type
        # try:
        #     if self._loan_type == 1:
        #         return f"\033[4;34;33mLoan type:\033[00m  {get_red_bolt(self._loan_type)}   \033[2;30;41m 10 days MAX \033[00m"
        #     elif self._loan_type == 2:
        #         return f"\033[4;34;33mLoan type:\033[00m  {get_red_bolt(self._loan_type)}   \033[2;30;41m 5 days MAX \033[00m"
        #     elif self._loan_type == 3:
        #         return f"\033[4;34;33mLoan type:\033[00m  {get_red_bolt(self._loan_type)}   \033[2;30;41m 2 days MAX \033[00m"
        # except:
        #     raise

    def set_loan_type(self, new_type: int) -> None:                     # set -   loan type
        self._loan_type = new_type

    def get_book_genres(self) -> set:                                   # get -   genre
        return self._book_genres

    def add_book_genres(self, *genres) -> None:                         # add -   genre
        for genre in genres:
            self._book_genres.add(genre)

    def del_book_genres(self, *genres_to_delete: str) -> None:          # del -   genre
        genre_del = set()
        for genre_to_delete in genres_to_delete:
            genre_del.add(genre_to_delete)
        self._book_genres.intersection(genre_del)

    def get_book_language(self) -> str:                            # get -  languages
        return self._book_language

    def set_book_language(self, new_language) -> None:        # set -  language
        self._book_language = new_language

    def __str__(self):
        return f"\n{get_black_bolt_and_line('___________________________________________________________')}\n \033[4;94m \033[1;94m{self.get_book_name()} \033[00m        \033[5;31;40m\033[00m\033[5;31;40m {get_yelow_line('ISBN')}{get_yelow_inside_black(':')}\033[1;91;40m {self.get_book_id()} \033[00m\n    {get_yelow_bolt('~ by ~')} \n  {get_blue(self.get_book_author())}  \n{get_yelow_line('Publication Year:')}  {get_red_bolt(self.get_publication_year())} \n{get_yelow_line('Genres:')}   {get_red(self.get_book_genres())} \n{get_yelow_line('Language:')} {get_red(self._book_language)} \n{get_yelow_line('Loan Type:')}  {get_red(self.get_loan_type())} \n{get_black_bolt_and_line('___________________________________________________________')}"

    def __repr__(self):
        return f" \r <| ID: {get_red(self.get_book_id())}  |  name: {get_blue_line_brighter(self.get_book_name())} |>\n"


if __name__ == '__main__':
    book1 = Book(33053, 'The Hitchhikers Guide to the Galaxy', 'Douglas Adams', 1956, 2, {Genre.Historical.value}, str(Language.Hebrew.value))
    book2 = Book(99598, 'fields of weedreams', 'Dr.Anir-Hak imzih Azak', 1420, 3, {Genre.Science.value, Genre.Historical.value}, Language.Portuguese.value)

    book1.add_book_genres(Genre.Drama.value, Genre.Zombies.value, Genre.Action.value)
    print(book1.get_book_genres())

    print(book1)
    print(book2)

