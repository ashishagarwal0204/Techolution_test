class Book:
    """
    Represents a book.
    """
    def __init__(self, title, author, isbn):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
