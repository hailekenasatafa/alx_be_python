class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.check_out():
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.return_book():
                return True
        return False

    def list_available_books(self):
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

