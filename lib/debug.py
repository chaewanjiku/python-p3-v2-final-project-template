#!/usr/bin/env python3
# lib/debug.py

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

    Author.drop_table()
    Author.create_table()

    Category.drop_table()
    Category.create_table()

    User.drop_table()
    User.create_table()

    BorrowingHistory.drop_table()
    BorrowingHistory.create_table()

    Library.drop_table()
    Library.create_table()

    # Create seed data for authors
    Author.create("F. Scott Fitzgerald")
    Author.create("Harper Lee")
    Author.create("Allan Moore")
    Author.create("Neil Gaiman")
    Author.create("J.R.R Tolkien")
    Author.create("J.K Rowling")
    Author.create("Douglas Adams")
    Author.create("Neil Teddy")
    Author.create("Jane Austen")
    Author.create("Diana Gabaldon")



    # Create seed data for categories
    fiction = Category.create("Fiction")
    comics = Category.create("Comics")
    fantasy = Category.create("Fantasy")
    humor = Category.create("Humor")
    romance = Category.create("Romance")

    # Create seed data for books
    Book.create("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 19.25)
    Book.create("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 14.99)
    Book.create("Watchmen", "Alan Moore", "Comics", 1986, 29.99)
    Book.create("The Sandman: Preludes & Nocturnes", "Neil Gaiman", "Comics", 1989, 24.99)
    Book.create("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, 15.99)
    Book.create("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, 20.99)
    Book.create("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Humor", 1979, 12.99)
    Book.create("Good Omens", "Neil Teddy", "Humor", 1990, 14.99)
    Book.create("Pride and Prejudice", "Jane Austen", "Romance", 1813, 9.99)
    Book.create("Outlander", "Diana Gabaldon", "Romance", 1991, 16.99)

    
    # Create seed data for users
    User.create("Alice", "alice@example.com", "password123")
    User.create("Bob", "bob@example.com", "password123")
    User.create("Charlie", "charlie@example.com", "password123")
    User.create("David", "david@example.com", "password123")
    User.create("Eve", "eve@example.com", "password123")
    User.create("Frank", "frank@example.com", "password123")
    User.create("Grace", "grace@example.com", "password123")
    User.create("Hannah", "hannah@example.com", "password123")


    # Create seed data for borrowing history
    BorrowingHistory.create(1, 1, datetime.now(), None)

    # Create seed data for library
    Library.create("Main Library", "123 Library St")
    Library.create("Central Library", "456 Central Ave")
    Library.create("Westside Branch", "789 Westside Blvd")
    Library.create("Eastside Branch", "101 Eastside Rd")
    Library.create("North Branch", "202 North St")
    Library.create("South Branch", "303 South Ave")


reset_database()
ipdb.set_trace()