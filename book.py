class Book:

    def __init__(self, title, author, isbn, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def mark_borrowed(self):
        if self.copies_available == 0:
            raise ValueError("No copies available")
        self.copies_available = self.copies_available - 1

    def mark_returned(self):
        self.copies_available = self.copies_available + 1

    def __str__(self):
        return self.title + " by " + self.author + " (" + self.isbn + ") - " + str(self.copies_available) + " copies available"