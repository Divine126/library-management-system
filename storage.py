from datetime import date
from book import Book
from member import Member

def save_books(books, path):
    with open(path, "w") as file:
        for book in books.values():
            file.write(
                f"{book.title}|{book.author}|{book.isbn}|{str(book.copies_available)}\n"
            )

def load_books(path):
    books = {}

    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                if len(parts) != 4:
                    print("Skipping bad line")
                    continue

                try:
                    book = Book(
                        parts[0],
                        parts[1],
                        parts[2],
                        int(parts[3])
                    )
                    books[parts[2]] = book

                except (ValueError, TypeError):
                    print("Skipping bad line")
                    continue

    except FileNotFoundError:
        return {}
    return books

def save_members(members, path):
    with open(path, "w") as file:
        for member in members.values():
            pairs = []

            for isbn, due_date in member.borrowed_books.items():
                pairs.append(f"{isbn}:{str(due_date)}")

            joined = ";".join(pairs)

            file.write(f"{member.name}|{member.email}|{member.phone}|{joined}\n")


def load_members(path):
    members = {}

    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                if len(parts) != 4:
                    print("Skipping bad line")
                    continue

                borrowed = {}

                if parts[3] != "":
                    for piece in parts[3].split(";"):
                        isbn, due_date = piece.split(":")
                        borrowed[isbn] = date.fromisoformat(due_date)

                member = Member(
                    parts[0],
                    parts[1],
                    parts[2],
                    borrowed
                )

                members[parts[1]] = member

    except FileNotFoundError:
        return {}

    return members

