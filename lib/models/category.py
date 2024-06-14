import sqlite3  # Importing the sqlite3 module for SQLite database operations
from models.__init__ import CONN, CURSOR  # Importing database connection objects from models package

class Category:
    all = {}  # Class variable to store all Category instances

    def __init__(self, name, id=None):  
        # Initializing Category instance with name and optional ID
        self.id = id  # Setting the Category ID
        self.name = name  # Setting the Category name

    def __repr__(self):  
        # Representation of Category instance
        return f"<Category {self.id}: {self.name}>"

    @property  
    # Getter method for name property
    def name(self):
        return self._name

    @name.setter  
    # Setter method for name property
    def name(self, name):
        if isinstance(name, str) and len(name):  
            # Checking if the name is a non-empty string
            self._name = name  # Setting the name
        else:
            raise ValueError("Name must be a non-empty string")  

    @classmethod  
    # Class method to create categories table in the database
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """  # SQL command to create categories table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    @classmethod  
    # Class method to drop categories table from the database
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS categories"  # SQL command to drop categories table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    def save(self):
        sql = "INSERT INTO categories (name) VALUES (?)"
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        # Method to save Category instance to the database

    def update(self):
        sql = "UPDATE categories SET name = ?  WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
        # Method to update Category instance in the database

    def delete(self):
        sql = "DELETE FROM categories WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
        # Method to delete Category instance from the database

    @classmethod  
    # Class method to create a new Category instance and save it to the database
    def create(cls, name):
        category = cls(name)
        category.save()
        return category

    @classmethod  
    # Class method to create a Category instance from a database row
    def instance_from_db(cls, row):
        category = cls.all.get(row[0])
        if category:
            category.name = row[1]
        else:
            category = cls(row[1])
            category.id = row[0]
            cls.all[category.id] = category
        return category

    @classmethod  
    # Class method to retrieve all Category instances from the database
    def get_all(cls):
        sql = "SELECT * FROM categories"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod  
    # Class method to find a Category instance by ID in the database
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM categories WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod  
    # Class method to find a Category instance by name in the database
    def find_by_name(cls, name):
        """Return a list of names corresponding to all table rows matching the specified name"""
        sql = """
            SELECT *
            FROM categories
            WHERE name = ?
        """  # SQL command to select rows with a specified name
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]  
