import sqlite3
from models.__init__ import CONN, CURSOR  # Importing necessary modules

class Book:
    all = {}  # A class variable to store all book instances
    allowed_genres = {"Fiction", "Non-Fiction", "Comics", "Fantasy", "Humor", "Romance"}  # Set of allowed genres

    def __init__(self, title, author, genre, year, price, id=None):  # Initializing a Book instance
        self.id = id  # Setting book ID
        self.title = title  # Setting book title
        self.author = author  # Setting book author
        self.genre = genre  # Setting book genre
        self.year = year  # Setting publication year
        self.price = price  # Setting book price

    def __repr__(self):  # Representation of a Book instance
        return f"<Book {self.id}: Title='{self.title}', Author='{self.author}', Genre='{self.genre}', Year={self.year}, Price={self.price}>"

    @property  # Getter for title
    def title(self):
        return self._title

    @title.setter  # Setter for title
    def title(self, title):
        if isinstance(title, str) and len(title):  # Checking if title is a non-empty string
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")  # Error message if title is invalid

    # Similar @property and @setter decorators for author, genre, year, and price properties

    @classmethod  # Class method to create books table
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                year INTEGER,
                price REAL
            )
        """
        CURSOR.execute(sql)  # Executing SQL command to create table
        CONN.commit()  # Committing changes to database

    # Class method to drop books table, similar to create_table()

    # Methods for saving, updating, and deleting book records in the database

    # Class methods to create Book instances, retrieve all books, find books by genre, author, or ID

    def borrowing_history(self):  # Method to retrieve borrowing history for a book
        from models.borrowinghistory import BorrowingHistory  # Importing BorrowingHistory model
        sql ="""
      SELECT * FROM borrowing_history WHERE book_id =?"""  # SQL query to select borrowing history for a book
        CURSOR.execute(sql,(self.id,),)  # Executing SQL query with book ID parameter
        rows =CURSOR.fetchall()  # Fetching all rows from the query result
        return[ BorrowingHistory.instance_from_db(row)for row in rows]  # Creating BorrowingHistory instances from rows
