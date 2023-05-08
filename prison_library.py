# import datetime
from colors import *
from book import Book
from author import Author
from genre import Genre
from language import Language

# from address import Address
# from inmate import Inmate
# from loan import Loan


class Prison_library:
    def __init__(self):
        self._book_id_to_Book: dict[int, Book] = {}
        self._books: dict[str, set[int]] = {}
        self._authors: set = set()
        self._authors_to_books: dict[str, dict[str, set[int]]] = {}
        self._language_to_books: dict[Language, dict[str, set[int]]] = {}
        self._genre_to_books: dict[Genre, set[str]] = {}

    # self._inmates: dict[int, Inmate] = {}
    # self._loans: dict[int, dict[str, str]] = {}
    # self._inmate_loans: dict[int, dict[int, dict[str, str]]] = {}

######################################################################################################################## __len__
    def __len__(self):
        return self
######################################################################################################################## add_author
    def add_author(self, author_name: str):
        if author_name.title() not in self._authors:
            author = Author(author_name)
            self._authors.add(author.get_author_name())  # .get_author_name())
        else:
            return False
######################################################################################################################## add_book
    def add_book(self, book_id: int, book_name: str, author_name: str, year_published: int, loan_type: int, genres: set, language: str):
        self.add_author(author_name)
        book = Book(book_id, book_name, author_name, year_published, loan_type, genres, language)
        ##################################################################################             _book_id_to_Book
        if book.get_book_id() not in self._book_id_to_Book:
            self._book_id_to_Book[book.get_book_id()] = book
        else:
            return False
        ##################################################################################                       _books
        if book.get_book_name() in self._books:
            if book.get_book_id() in self._books[book.get_book_name()]:
                return False
            else:
                self._books[book.get_book_name()].add(book.get_book_id())
        else:
            self._books[book.get_book_name()] = set()
            self._books[book.get_book_name()].add(book.get_book_id())
        ##################################################################################            _authors_to_books
        if book.get_book_author() in self._authors_to_books:
            if book.get_book_name() in self._authors_to_books[book.get_book_author()]:
                if book.get_book_id() in self._authors_to_books[book.get_book_author()][book.get_book_name()]:
                    return False
                else:
                    self._authors_to_books[book.get_book_author()][book.get_book_name()].add(book.get_book_id())
            else:
                self._authors_to_books[book.get_book_author()][book.get_book_name()] = {book.get_book_id()}
        else:
            self._authors_to_books[book.get_book_author()] = {book.get_book_name(): {book.get_book_id()}}
        ###################################################################################             _genre_to_books
        for genre in book.get_book_genres():
            if genre in self._genre_to_books:
                if book.get_book_name() in self._genre_to_books[genre]:
                    return False
                else:
                    self._genre_to_books[genre].add(book.get_book_name())
            else:
                self._genre_to_books[genre] = {book.get_book_name()}
            ###################################################################################     _languages_to_books
            if book.get_book_language() in self._language_to_books:
                if book.get_book_name() in self._language_to_books[book.get_book_language()]:
                    if book.get_book_id() in self._language_to_books[book.get_book_language()][book.get_book_name()]:
                        return False
                    else:
                        self._language_to_books[book.get_book_language()][book.get_book_name()].add(book.get_book_id())
                else:
                    self._language_to_books[book.get_book_language()][book.get_book_name()] = {book.get_book_id()}
            else:
                self._language_to_books[book.get_book_language()] = {book.get_book_name(): {book.get_book_id()}}
######################################################################################################################## add_book_copy
    def add_book_copy(self, book_id: int, book_name: str, language: Language):
        for bookid, book in self._book_id_to_Book.items():
            if bookid != book_id:
                if book.get_book_name() == book_name.title():
                    self.add_book(book_id, book_name.title(), book.get_book_author(), book.get_publication_year(),
                                  book.get_loan_type(), book.get_book_genres(), language)
                    return True
                else:
                    continue
            else:
                return False
######################################################################################################################## display_books_of_author
    def display_books_of_author(self, author_name: str) -> list | bool:
        boa = []
        for author in self._authors_to_books:
            if author == author_name.title():
                boa.append(self._authors_to_books.get(author_name.title()))
            else:
                continue
            return f" books by {author_name.title()}: {boa}"
        return False
######################################################################################################################## display_book_by_id
    def display_book_by_id(self, book_id: int) -> Book | bool:
        for bookid in self._book_id_to_Book.keys():
            if bookid == book_id:
                return self._book_id_to_Book[bookid]
            else:
                continue
        return False
######################################################################################################################## display_book_ids_by_name
    def display_book_ids_by_name(self, book_name: str) -> str | bool:
        capital_book = book_name.title()
        separator = (" , ")
        if capital_book in self._books:
            bid = self._books.get(capital_book)
            return f"{get_red(bid)}"
        else:
            return False
######################################################################################################################## display_books_by_genre
    def display_books_by_genre(self, genre: Genre) -> list | bool:
        bbg = []
        for gen in self._genre_to_books:
            if gen == genre:
                bbg.append(self._genre_to_books[genre])
            else:
                continue
            return f" books by the genre: {genre}: {bbg}"
        return False
######################################################################################################################## display_genres_of_book
    def display_genres_of_book(self, book_name: str) -> set:
        for bookid, book in self._book_id_to_Book.items():
            if book.get_book_name() == book_name.title():
                return f"{get_blue_bolt_and_line(self._book_id_to_Book[bookid].get_book_name())} {get_black_bolt('-->  ')}{get_yelow_bolt_and_line('Genres:')} \t{get_red(self._book_id_to_Book[bookid].get_book_genres())}"
        return False
######################################################################################################################## display_books_by_language
    def display_books_by_language(self, language: Language) -> list | bool:
        bbl = []
        for langu in self._language_to_books:
            if langu == language:
                bbl.append(self._language_to_books.get(language))
            else:
                continue
            return f" books in {language}: {bbl}"
        return False
######################################################################################################################## display_languages_of_book
    def display_languages_of_book(self, book_name: str) -> set:
        book_langs = set()
        separator = (" , ")
        for bookid, book in self._book_id_to_Book.items():
            if book.get_book_name() == book_name.title():
                book_langs.add(self._book_id_to_Book[bookid].get_book_language())
        return f"{get_blue_bolt_and_line(book_name.title())} {get_black_bolt('-->  ')}{get_yelow_bolt_and_line('Languages:')} \t{get_red(separator.join(book_langs))}"
######################################################################################################################## display_books_by_loan_type
    def display_books_by_loan_type(self, loan_type: int):
        books = set()
        separator =('\n ~\t')
        for bookid, book in self._book_id_to_Book.items():
            if book.get_loan_type() == loan_type:
                books.add(book.get_book_name())
            else:
                continue
        return f" {get_yellow_bolt_and_line('books with loan type:')} {get_red_bolt(loan_type)} {get_black_bolt('-->')}\n{get_blue(' ~  ')}{get_blue(separator.join(books))}"
######################################################################################################################## display_books_by_publication_year
    def display_books_by_publication_year(self, publication_year: int):
        books = set()
        separator =('\n ~\t')
        for bookid, book in self._book_id_to_Book.items():
            if book.get_publication_year() == publication_year:
                books.add(book.get_book_name())
            else:
                continue
        return f" {get_yellow_bolt_and_line('books published in:')} {get_red_bolt(publication_year)} {get_black_bolt('-->')}\n{get_blue(' ~  ')}{get_blue(separator.join(books))}"
######################################################################################################################################################################


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |___ main___|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

if __name__ == '__main__':
    shawshank = Prison_library()

    shawshank.add_book(30584, 'fields of weedreams', 'imzih Azak', 1420, 3,{Genre.Science.value, Genre.Historical.value}, Language.Thai.value)
    shawshank.add_book_copy(66606, 'fields of weedreams', Language.Hebrew.value)
    shawshank.add_book(78003, 'od sefer lama lo', 'imzih Azak', 1421, 3, {Genre.Drama.value, Genre.Romance.value}, Language.Hebrew.value)
    shawshank.add_book_copy(78004, 'od sefer lama lo', Language.French.value)
    shawshank.add_book(30888, 'the Hitchhikers guide to the galaxy', 'dougles adams', 1956, 2, {Genre.Historical.value}, Language.Hebrew.value)
    shawshank.add_book_copy(66722, 'the Hitchhikers guide to the galaxy', Language.English.value)
    shawshank.add_book_copy(67722, 'the Hitchhikers guide to the galaxy', Language.Turkish.value)
    shawshank.add_book_copy(66822, 'the Hitchhikers guide to the galaxy', Language.Thai.value)
    shawshank.add_book_copy(80722, 'the Hitchhikers guide to the galaxy', Language.German.value)
    shawshank.add_book_copy(62722, 'the Hitchhikers guide to the galaxy', Language.Hebrew.value)
    shawshank.add_book_copy(62723, 'the Hitchhikers guide to the galaxy', Language.Arabic.value)
    shawshank.add_book(16722, 'sahar tabaot', 'dougles adams', 1949, 1, {Genre.Story_Telling.value}, Language.English.value)
    shawshank.add_book_copy(16727, 'sahar tabaot', Language.Russian.value)
    shawshank.add_book_copy(86722, 'sahar tabaot', Language.Japanese.value)
    shawshank.add_book_copy(55522, 'sahar tabaot', Language.German.value)
    shawshank.add_book_copy(33333, 'Sahar Tabaot', Language.Ancient_Egyptian.value)
    shawshank.add_book_copy(22222, 'Sahar Tabaot', Language.Thai.value)

    shawshank.add_book(56722, 'batyam 90210', 'shimi shchunot', 2002, 1, {Genre.Fantasy.value}, Language.Ancient_Egyptian.value)
    shawshank.add_book_copy(46722, 'batyam 90210', Language.Portuguese.value)
    shawshank.add_book_copy(86722, 'batyam 90210', Language.French.value)

    shawshank.add_book(33883, 'haniagarot sheli', 'pipica ciasla', 2020, 3, {Genre.Drama.value, Genre.Romance.value}, Language.Dutch.value)
    shawshank.add_book_copy(55343, 'haniagarot sheli', Language.Yiddish.value)

    shawshank.add_book(55553, 'as zir root', 'pipica ciasla', 2021, 3, {Genre.Comedy.value, Genre.Romance.value}, Language.Hebrew.value)
    shawshank.add_book(33553, 'petite m catshop', 'david ben gurion', 1951, 3, {Genre.Action.value, Genre.Historical.value}, Language.Turkish.value)
    shawshank.add_book(89586, 'living in Shoshis forgivness', 'batya memories', 1779, 2, {Genre.Folklore.value}, Language.Chinese.value)
    shawshank.add_book(56443, 'How to paste Bakestries', 'Esh Diran', 2011, 3, {Genre.Folklore.value, Genre.Romance.value}, Language.Italian.value)
    shawshank.add_book(51563, 'hater of N', 'Ha rambaMMM', 2002, 1, {Genre.Zombies.value, Genre.Story_Telling.value}, Language.French.value)

    print(f"_books:\n{shawshank._books}\n")
    print(f"search_book_id's_by_name:\n{shawshank.display_book_ids_by_name('sahar tabaot')}\n")
    print(f"search_a_book_by_id:{shawshank.display_book_by_id(55553)}")
    print(f"book_id_to_Book:\n{shawshank._book_id_to_Book}\n")
    print(f"_authors:\n{shawshank._authors}\n")
    print(f"display_books_of_author:\n{shawshank.display_books_of_author('dougles adams')}\n")
    print(f"authors_to_books:\n{shawshank._authors_to_books}\n")

    print(shawshank.display_genres_of_book('haniagarot sheli'))
    print(shawshank.display_languages_of_book('haniagarot sheli'))
    print(shawshank._language_to_books)
    print(f"display_books_by_language:\n{shawshank.display_books_by_language(Language.Hebrew.value)}\n")

    print(shawshank._genre_to_books)
    print(shawshank.display_books_by_genre(Genre.Drama.value))

    print(shawshank.display_books_by_loan_type(3))

    print(shawshank.display_books_by_publication_year(2002))