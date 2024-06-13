from models.__init__ import CONN, CURSOR
from models.book import Book
from models.user import User

class BorrowingHistory:
    all = {}

    def __init__(self, user_id, book_id, borrowed_date, return_date=None, id=None):
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.borrowed_date = borrowed_date
        self.return_date = return_date
        
    def __str__(self):
        return (f'User ID: {self.user_id}, Book ID: {self.book_id}, '
                f'Borrowed Date: {self.borrowed_date}, Return Date: {self.return_date}')

    def __repr__(self):
        return (f'BorrowingHistory(user_id={self.user_id}, book_id={self.book_id}, '
                f'borrowed_date={self.borrowed_date}, return_date={self.return_date})')
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value > 0:
            self._id = value
        else:
            raise ValueError("ID must be a positive integer")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and User.find_by_id(user_id):
            self._user_id = user_id
        else:
           raise ValueError("user_id must be a reference a user in the database")


    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, book_id):
        if isinstance(book_id, int) and Book.find_by_id(book_id):
            self._book_id = book_id
        else:
            raise ValueError("book_id must be a reference a book in the database")

    @property
    def borrowed_date(self):
        return self._borrowed_date

    @borrowed_date.setter
    def borrowed_date(self, value):
        if isinstance(value, str) and len(value):
            self._borrowed_date = value
        else:
            raise ValueError("Borrowed date must be a non-empty string")

    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        if value is None or (isinstance(value, str) and len(value)):
            self._return_date = value
        else:
            raise ValueError("Return date must be a non-empty string or None")
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS borrowing_history (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                book_id INTEGER,
                borrowed_date TEXT,
                return_date TEXT
                FOREIGN KEY(user_id)REFERENCES users(id)
                FOREIGN KEY(book_id)REFERENCES books(id)

            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS borrowing_history"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO borrowing_history (user_id, book_id, borrowed_date, return_date) VALUES (?, ?, ?, ?)"
        CURSOR.execute(sql, (self.user_id, self.book_id, self.borrowed_date, self.return_date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE borrowing_history SET user_id = ?, book_id = ?, borrowed_date = ?, return_date = ? WHERE id = ?"
        CURSOR.execute(sql, (self.user_id, self.book_id, self.borrowed_date, self.return_date, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM borrowing_history WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, user_id, book_id, borrowed_date, return_date=None):
        history = cls(user_id, book_id, borrowed_date, return_date)
        history.save()
        return history

    @classmethod
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
    def get_all(cls):
        sql = "SELECT * FROM borrowing_history"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_user_id(cls, user_id):
        sql = "SELECT * FROM borrowing_history WHERE user_id = ?"
        rows = CURSOR.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM borrowing_history WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
