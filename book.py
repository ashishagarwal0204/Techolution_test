from storage import JSONStorage

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class BookManager:
    def __init__(self, filename):
        self.storage = JSONStorage(filename)
        self.books = self.storage.load_data()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.storage.save_data([book.__dict__ for book in self.books])

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
