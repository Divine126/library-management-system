# Library Management System

A Python console application for managing a small library — books, members,
borrowing, returning, overdue tracking, and AI-powered reading recommendations.

## Group 34
- Divine Uzong (Leader)
- Khadijah Aliyu
- Timothy Otor
- Umar Abimbola
- Toheeb Adisa
- Hope Ayuba
- Hassan Yusuf

## Features
1. Add book (auto-fetches title/author by ISBN)
2. View all books
3. Search books
4. Register member
5. Borrow book
6. Return book
7. Get an AI book recommendation
8. Check overdue books
9. Save and exit

## Tech Stack
- Python 3
- Open Library API (book lookup)
- Google Gemini API (recommendations)
- Plain text file storage

## Setup
1. Clone the repo.
2. Install dependencies: pip install -r requirements.txt
3. Create a `.env` file in the project root with your Gemini API key: GEMINI_API_KEY=your_key_here
4. Run the program: python main.py

   
## Project Files
| File | Purpose |
|---|---|
| `book.py` | Book class |
| `member.py` | Member class (tracks borrowed books with due dates) |
| `library.py` | Library class (core logic, including overdue checks) |
| `validators.py` | Input validation (regex) |
| `storage.py` | Save/load text files |
| `api_client.py` | Open Library API integration |
| `ai_recommender.py` | Gemini AI integration |
| `main.py` | Program entry point / menu |
