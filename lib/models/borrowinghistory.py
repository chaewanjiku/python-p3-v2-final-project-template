from datetime import datetime  # Importing the datetime module for date-related functionality
from models import CONN, CURSOR  # Importing database connection objects from models package
from models.book import Book  # Importing the Book class from models package
from models.user import User  # Importing the User class from models package

class BorrowingHistory:
    all = {}  # Class variable to store all BorrowingHistory instances

    def __init__(self, user_id, book_id, borrowed_date, return_date, id=None):  
        # Initializing BorrowingHistory instance with user ID, book ID, borrowed date, return date, and optional ID
        self.id = id  # Setting the BorrowingHistory ID
        self.user_id = user_id  # Setting the user ID associated with the borrowing
        self.book_id = book_id  # Setting the book ID associated with the borrowing
        self.borrowed_date = borrowed_date  # Setting the borrowing date
        self.return_date = return_date  # Setting the return date

    def __str__(self):  
        # String representation of BorrowingHistory instance
        return (f'User ID: {self.user_id}, Book ID: {self.book_id}, '  
                f'Borrowed Date: {self.borrowed_date}, Return Date: {self.return_date}')

    def __repr__(self):  
        # Representation of BorrowingHistory instance
        return (f'BorrowingHistory(user_id={self.user_id}, book_id={self.book_id}, '
                f'borrowed_date={self.borrowed_date}, return_date={self.return_date})')

    # Property and setter decorators for id, user_id, book_id, borrowed_date, and return_date properties

    @classmethod  
    # Class method to create borrowing_history table
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS borrowing_history (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                book_id INTEGER,
                borrowed_date TEXT,
                return_date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
        """  # SQL command to create borrowing_history table with foreign key constraints
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    @classmethod  
    # Class method to drop borrowing_history table
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS borrowing_history"  # SQL command to drop borrowing_history table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    def save(self):
        sql = "INSERT INTO borrowing_history (user_id, book_id, borrowed_date, return_date) VALUES (?, ?, ?, ?)"
        CURSOR.execute(sql, (self.user_id, self.book_id, self.borrowed_date, self.return_date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        # Method to save BorrowingHistory instance to the database

    def update(self):
        sql = "UPDATE borrowing_history SET user_id = ?, book_id = ?, borrowed_date = ?, return_date = ? WHERE id = ?"
        CURSOR.execute(sql, (self.user_id, self.book_id, self.borrowed_date, self.return_date, self.id))
        CONN.commit()
        # Method to update BorrowingHistory instance in the database

    def delete(self):
        sql = "DELETE FROM borrowing_history WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
        # Method to delete BorrowingHistory instance from the database

    @classmethod  
    # Class method to create a new BorrowingHistory instance and save it to the database
    def create(cls, user_id, book_id, borrowed_date, return_date=None):
        history = cls(user_id, book_id, str(borrowed_date), return_date)
        history.save()
        return history

    @classmethod  
    # Class method to create a BorrowingHistory instance from a database row
    def instance_from_db(cls, row):
        history = cls.all.get(row[0])
        if history:
            history.user_id = row[1]
            history.book_id = row[2]
            history.borrowed_date = row[3]
            history.return_date = row[4]
        else:
            history = cls(row[1], row[2], row[3], row[4], row[0])
            cls.all[history.id] = history
        return history

    @classmethod  
    # Class method to retrieve all BorrowingHistory instances from the database
    def get_all(cls):
        sql = "SELECT * FROM borrowing_history"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod  
    # Class method to find BorrowingHistory instances by user ID in the database
    def find_by_user_id(cls, user_id):
        sql = "SELECT * FROM borrowing_history WHERE user_id = ?"
        rows = CURSOR.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod  
    # Class method to find a BorrowingHistory instance by ID in the database
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM borrowing_history WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
