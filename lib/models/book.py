import sqlite3
from models.__init__ import CONN, CURSOR

class Book:
    all = {}

    def __init__(self, title, genre, price, author_id, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.price = price
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.id}: Title='{self.title}', Genre='{self.genre}', Price={self.price}, Author ID={self.author_id}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre must be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be a non-negative number")

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        if isinstance(author_id, int) and author_id > 0:
            self._author_id = author_id
        else:
            raise ValueError("Author ID must be a positive integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT,
                price REAL,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors (id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS books"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO books (title, genre, price, author_id) VALUES (?, ?, ?, ?)"
        CURSOR.execute(sql, (self.title, self.genre, self.price, self.author_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE books SET title = ?, genre = ?, price = ?, author_id = ? WHERE id = ?"
        CURSOR.execute(sql, (self.title, self.genre, self.price, self.author_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM books WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, genre, price, author_id):
        book = cls(title, genre, price, author_id)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.genre = row[2]
            book.price = row[3]
            book.author_id = row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_genre(cls, genre):
        sql = "SELECT * FROM books WHERE genre = ?"
        rows = CURSOR.execute(sql, (genre,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_author(cls, author_id):
        sql = "SELECT * FROM books WHERE author_id = ?"
        rows = CURSOR.execute(sql, (author_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
