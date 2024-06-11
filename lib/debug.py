#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from datetime import datetime
from models.book import Book
from models.author import Author
from models.borrowinghistory import BorrowingHistory
from models.library import Library
from models.category import Category
from models.user import User
import ipdb


def reset_database():
    Book.drop_table()
    Book.create_table()

    # Create seed data for books
    fitzgerald_name = Author.create("F. Scott Fitzgerald")
    lee_name = Author.create("Harper Lee")
    orwell_name = Author.create("George Orwell")
    austen_name = Author.create("Jane Austen")
    
    # Ensure that the genre parameter is a non-empty string
    fiction = Category.create("Fiction")
    if not fiction:
        raise ValueError("Failed to create 'Fiction' category")

    non_fiction = Category.create("Non-Fiction")
    if not non_fiction:
        raise ValueError("Failed to create 'Non-Fiction' category")

    # Make sure genre values are non-empty strings
    Book.create("The Great Gatsby", fitzgerald_name, fiction, 1925, 19.25)
    Book.create("To Kill a Mockingbird", lee_name, fiction, 1960, 19.60)
    Book.create("1984", orwell_name, fiction, 1949, 19.49)
    Book.create("Pride and Prejudice", austen_name, fiction, 1813, 18.13)

    # Add more book entries as needed...

    # Add more book entries as needed...


    # Add more book entries as needed...

    # Add more author entries as needed...

    # Add more category entries as needed...

    User.drop_table()
    User.create_table()

    # Create seed data for users
    User.create("Alice", "alice@example.com", "password123")
    User.create("Bob", "bob@example.com", "password123")
    User.create("Charlie", "charlie@example.com", "password123")
    # Add more user entries as needed...

    BorrowingHistory.drop_table()
    BorrowingHistory.create_table()

    # Create seed data for borrowing history
    BorrowingHistory.create(user_id=1, book_id=1, borrowed_date=datetime.now(), returned_date=None)
    # Add more borrowing history entries as needed...

    Library.drop_table()
    Library.create_table()

    # Create seed data for library
    Library.create("Main Library", "123 Library St", "Librarian Name")
    # Add more library entries as needed...

reset_database()
ipdb.set_trace()
