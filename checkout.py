class Checkout:
    """
    Represents a book checkout.
    """
    def __init__(self, user_id, isbn):
        """
        Initializes a Checkout object.

        Args:
            user_id (str): The ID of the user who checks out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        self.user_id = user_id
        self.isbn = isbn
