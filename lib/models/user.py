import sqlite3  # Importing the sqlite3 library
from models.__init__ import CONN, CURSOR  # Importing database connection objects from models package

class User:
    all = {}  # Class variable to store all User instances

    def __init__(self, username, email, password, id=None):
        # Initializing User instance with username, email, password, and optional ID
        self.id = id  # Setting the User ID
        self.username = username  # Setting the username
        self.email = email  # Setting the email
        self.password = password  # Setting the password

    def __repr__(self):
        # Representation of User instance
        return f"<User {self.id}: Username='{self.username}', Email='{self.email}'>"

    @property
    # Getter method for username property
    def username(self):
        return self._username

    @username.setter
    # Setter method for username property
    def username(self, username):
        if isinstance(username, str) and len(username):  # Checking if the username is a non-empty string
            self._username = username  # Setting the username
        else:
            raise ValueError("Username must be a non-empty string")

    @property
    # Getter method for email property
    def email(self):
        return self._email

    @email.setter
    # Setter method for email property
    def email(self, email):
        if isinstance(email, str) and len(email):  # Checking if the email is a non-empty string
            self._email = email  # Setting the email
        else:
            raise ValueError("Email must be a non-empty string")

    @property
    # Getter method for password property
    def password(self):
        return self._password

    @password.setter
    # Setter method for password property
    def password(self, password):
        if isinstance(password, str) and len(password):  # Checking if the password is a non-empty string
            self._password = password  # Setting the password
        else:
            raise ValueError("Password must be a non-empty string")

    @classmethod
    # Class method to create users table in the database
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password TEXT
            )
        """  # SQL command to create users table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    @classmethod
    # Class method to drop users table from the database
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS users"  # SQL command to drop users table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    def save(self):
        sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.username, self.email, self.password))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        # Method to save User instance to the database

    def update(self):
        sql = "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?"
        CURSOR.execute(sql, (self.username, self.email, self.password, self.id))
        CONN.commit()
        # Method to update User instance in the database

    def delete(self):
        sql = "DELETE FROM users WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
        # Method to delete User instance from the database

    @classmethod
    # Class method to create a new User instance and save it to the database
    def create(cls, username, email, password):
        user = cls(username, email, password)
        user.save()
        return user

    @classmethod
    # Class method to create a User instance from a database row
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user.username = row[1]
            user.email = row[2]
            user.password = row[3]
        else:
            user = cls(row[1], row[2], row[3], row[0])
            cls.all[user.id] = user
        return user

    @classmethod
    # Class method to retrieve all User instances from the database
    def get_all(cls):
        sql = "SELECT * FROM users"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    # Class method to find a User instance by username in the database
    def find_by_username(cls, username):
        sql = "SELECT * FROM users WHERE username = ?"
        rows = CURSOR.execute(sql, (username,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    # Class method to find a User instance by email in the database
    def find_by_email(cls, email):
        sql = "SELECT * FROM users WHERE email = ?"
        rows = CURSOR.execute(sql, (email,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    # Class method to find a User instance by ID in the database
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM users WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None

    def borrowing_history(self):
        from models.borrowinghistory import BorrowingHistory
        sql = """
            SELECT * FROM borrowing_history WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [BorrowingHistory.instance_from_db(row) for row in rows]
