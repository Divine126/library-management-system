import book, member, storage, api_client, ai_recommender
from datetime import date, timedelta

class Library:

    def __init__(self):
        self.books = {}
        self.members = {}

    def load_all(self):
        self.books = storage.load_books("books.txt")
        self.members = storage.load_members("members.txt")

    def save_all(self):
        storage.save_books(self.books, "books.txt")
        storage.save_members(self.members, "members.txt")

    def add_book(self, isbn, copies_available):
        if isbn in self.books:
            raise ValueError("Book already exists")
        details = api_client.fetch_book_details(isbn)
        if details is None:
            raise ValueError(" Book details not found either because the ISBN does not exist or the book is not available in the Open Library database.")
        new_book = book.Book(details['title'], details['author'], isbn, copies_available)
        self.books[isbn] = new_book

    def list_books(self):
        return list(self.books.values())

    def search_book(self, keyword):
        keyword = keyword.lower()
        return [book for book in self.books.values()
                if keyword in book.title.lower()
                or keyword in book.author.lower()
                or keyword in book.isbn]

    def register_member(self, name, email, phone):
        if email in self.members:
            raise ValueError("Member already exists")
        self.members[email] = member.Member(name, email, phone)

    def borrow_book(self, isbn, email):
        if isbn not in self.books:
            raise ValueError("Book not found")
        if email not in self.members:
            raise ValueError("Member not found")
        self.books[isbn].mark_borrowed()
        due_date = date.today() + timedelta(days=14)
        self.members[email].borrow_book(isbn, due_date)
        return due_date

    def return_book(self, isbn, email):
        if isbn not in self.books:
            raise ValueError("Book not found")
        if email not in self.members:
            raise ValueError("Member not found")
        self.members[email].return_book(isbn)
        self.books[isbn].mark_returned()

    def check_overdue_books(self):
        overdue = []
        for member in self.members.values():
            for isbn, due_date in member.borrowed_books.items():
                if due_date < date.today():
                    title = self.books[isbn].title if isbn in self.books else "Unknown"
                    overdue.append({
                        "name": member.name,
                        "email": member.email,
                        "phone": member.phone,
                        "isbn": isbn,
                        "title": title,
                        "due_date": due_date
                    })
        return overdue

    def get_recommendation(self, user_taste):
        titles = [book.title for book in self.books.values()]
        return ai_recommender.get_recommendation(user_taste, titles)