class Member:

    def __init__(self, name, email, phone, borrowed_books = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = borrowed_books if borrowed_books is not None else {}

    def borrow_book(self, isbn, due_date):
        if isbn in self.borrowed_books:
            raise ValueError("Already borrowed")
        self.borrowed_books[isbn] = due_date

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            raise ValueError("You don't have this book")
        del self.borrowed_books[isbn]

    def __str__(self):
        return self.name + " (" + self.email + ") - " + str(len(self.borrowed_books)) + " books borrowed"