
class Author:
    def __init__(self, author_name: str):
        self._author_name: str = author_name

    def get_author_name(self) -> str:
        return self._author_name.title()

    def __str__(self) -> str:
        return self.get_author_name()

    def __repr__(self):
        return self.get_author_name()


if __name__ == '__main__':
    gugu = Author('gugu')