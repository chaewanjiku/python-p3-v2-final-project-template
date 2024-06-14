import sqlite3  # Import the sqlite3 library for database operations
from models.__init__ import CONN, CURSOR  # Import CONN and CURSOR from the models package

class Author:  # Define the Author class
    all = {}  # Initialize an empty dictionary to store all Author instances

    def __init__(self, name, id=None):  # Define the constructor for Author instances
        self.id = id  # Initialize the id attribute
        self.name = name  # Initialize the name attribute

    def __repr__(self):  # Define the __repr__ method to represent Author instances as strings
        return f"<Author {self.id}: {self.name}>"  # Return a string representation of the Author instance

    @property  # Define a property for the name attribute
    def name(self):  # Getter method for name
        return self._name  # Return the private _name attribute

    @name.setter  # Setter method for name
    def name(self, name):  # Setter method for name attribute
        if isinstance(name, str) and len(name):  # Check if name is a non-empty string
            self._name = name  # Set the private _name attribute
        else:
            raise ValueError("Name must be a non-empty string")  # Raise an error for invalid name

    @classmethod  # Define a class method for creating the authors table in the database
    def create_table(cls):  # Class method to create the authors table
        sql = """
            CREATE TABLE IF NOT EXISTS authors (  # SQL statement to create the authors table if not exists
                id INTEGER PRIMARY KEY,  # Define the id column as primary key
                name TEXT  # Define the name column as TEXT type
            )
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    @classmethod  # Define a class method for dropping the authors table from the database
    def drop_table(cls):  # Class method to drop the authors table
        sql = "DROP TABLE IF EXISTS authors"  # SQL statement to drop the authors table if exists
        CURSOR.execute(sql)  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    def save(self):  # Method to save Author instance to the database
        sql = "INSERT INTO authors (name) VALUES (?)"  # SQL statement to insert author name into authors table
        CURSOR.execute(sql, (self.name,))  # Execute the SQL statement with author name parameter
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Get the last inserted row id and assign it to self.id
        type(self).all[self.id] = self  # Add the Author instance to the class dictionary

    def update(self):  # Method to update Author instance in the database
        sql = "UPDATE authors SET name = ?  WHERE id = ?"  # SQL statement to update author name by id
        CURSOR.execute(sql, (self.name, self.id))  # Execute the SQL statement with author name and id parameters
        CONN.commit()  # Commit the changes to the database    

    def delete(self):  # Method to delete Author instance from the database
        sql = "DELETE FROM authors WHERE id = ?"  # SQL statement to delete author by id
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement with author id parameter
        CONN.commit()  # Commit the changes to the database
        del type(self).all[self.id]  # Delete the Author instance from the class dictionary
        self.id = None  # Set the id attribute to None

    @classmethod  # Define a class method for creating an Author instance and saving it to the database
    def create(cls, name):  # Class method to create an Author instance
        author = cls(name)  # Create a new Author instance with the given name
        author.save()  # Save the Author instance to the database
        return author  # Return the created Author instance

    @classmethod  # Define a class method for creating an Author instance from a database row
    def instance_from_db(cls, row):  # Class method to create an Author instance from a database row
        author = cls.all.get(row[0])  # Get the Author instance from class dictionary by id
        if author:  # If Author instance exists
            author.name = row[1]  # Update the author name
        else:  # If Author instance does not exist
            author = cls(row[1])  # Create a new Author instance with name from row
            author.id = row[0]  # Set the author id from row
            cls.all[author.id] = author  # Add the Author instance to the class dictionary
        return author  # Return the Author instance

    @classmethod  # Define a class method for getting all Author instances from the database
    def get_all(cls):  # Class method to get all Author instances
        sql = "SELECT * FROM authors"  # SQL statement to select all authors from authors table
        rows = CURSOR.execute(sql).fetchall()  # Execute the SQL statement and fetch all rows
        return [cls.instance_from_db(row) for row in rows]  # Return a list of Author instances

    @classmethod  # Define a class method for finding Author instances by name
    def find_by_name(cls, name):  # Class method to find Author instances by name
        sql = """
            SELECT *
            FROM authors
            WHERE name = ?
        """  # SQL statement to select authors by name
        rows = CURSOR.execute(sql, (name,)).fetchall()  # Execute the SQL statement with name parameter
        return [cls.instance_from_db(row) for row in rows]  # Return a list of Author instances

    @classmethod  # Define a class method for finding an Author instance by id
    def find_by_id(cls, id_):  # Class method to find an Author instance by id
        CURSOR.execute('SELECT * FROM authors WHERE id = ?', (id_,))  # SQL statement to select author by id
        row = CURSOR.fetchone()  # Fetch the first row
        return cls.instance_from_db(row) if row else None  # Return Author instance if row exists, else None
