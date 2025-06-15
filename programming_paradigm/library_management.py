# library_management.py

# Book class represents individual books with availability tracking
class Book:
    def __init__(self, title, author):  # ✅ Removed the trailing comma
        self.title = title  # Public attribute: book's title
        self.author = author  # Public attribute: book's author
        self._is_checked_out = False  # Private attribute: True if book is checked out

    def check_out(self):
        """Marks the book as checked out"""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)"""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available (not checked out)"""
        return not self._is_checked_out


# Library class manages a collection of books
class Library:
    def __init__(self):  # ✅ Removed the comma
        self._books = []  # Private list storing Book instances

    def add_book(self, book):
        """Adds a Book object to the library collection"""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out the book with the given title if it's available"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break

    def return_book(self, title):
        """Returns the book with the given title if it's checked out"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                break

    def list_available_books(self):
        """Prints all books that are currently available"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
