class User:
    """
    Represents a user.
    """
    def __init__(self, name, user_id):
        """
        Initializes a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id
