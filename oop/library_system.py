# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize the base Book class with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the Book."""
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook class with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"{self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook class with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"{self.title} by {self.author}, Pages: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
