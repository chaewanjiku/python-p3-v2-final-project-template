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
    Book.create("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 20)
    Book.create("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 15)
    Book.create("1984", "George Orwell", "Fiction", 1949, 25)
    Book.create("Pride and Prejudice", "Jane Austen", "Fiction", 1813, 30)
  

   
    # Add more book entries as needed...

    Author.drop_table()
    Author.create_table()

    # Create seed data for authors
    Author.create("F. Scott Fitzgerald")
    Author.create("Harper Lee")
    Author.create("George Orwell")
    Author.create("Jane Austen")
    # Add more author entries as needed...

    Category.drop_table()
    Category.create_table()

    # Create seed data for categories
    Category.create("Fiction")
    Category.create("Non-Fiction")
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
    BorrowingHistory.create(1, 1, datetime.now(), None)
    # Add more borrowing history entries as needed...

    Library.drop_table()
    Library.create_table()

    # Create seed data for library
    Library.create("Main Library", "123 Library St", "Librarian Name")
    # Add more library entries as needed...

reset_database()
ipdb.set_trace()
