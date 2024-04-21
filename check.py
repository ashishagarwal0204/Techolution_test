from storage import JSONStorage

class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn

class CheckoutManager:
    def __init__(self, filename):
        self.storage = JSONStorage(filename)
        self.checkouts = self.storage.load_data()

    def checkout_book(self, user_id, isbn):
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        self.storage.save_data([checkout.__dict__ for checkout in self.checkouts])

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(f"User ID: {checkout.user_id}, ISBN: {checkout.isbn}")
