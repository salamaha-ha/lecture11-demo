from .utils.data_validation import validate_book_data

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        book = {"title": title, "author": author, "genre": genre}
        if validate_book_data(book):
            self.books.append(book)
        else:
            raise ValueError("Некорректные данные книги.")

    def remove_book(self, title):
        before = len(self.books)
        self.books = [b for b in self.books if b["title"] != title]
        return before != len(self.books)

    def find_books(self, *, title=None, author=None, genre=None):
        results = self.books
        if title:
            results = [b for b in results if title.lower() in b["title"].lower()]
        if author:
            results = [b for b in results if author.lower() in b["author"].lower()]
        if genre:
            results = [b for b in results if genre.lower() in b["genre"].lower()]
        return results

    def list_books(self):
        return list(self.books)
