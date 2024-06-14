from models.__init__ import CONN, CURSOR  # Importing database connection objects from models package

class Library:
    all = {}  # Class variable to store all Library instances

    def __init__(self, name, location, id=None):  
        # Initializing Library instance with name, location, and optional ID
        self.id = id  # Setting the Library ID
        self.name = name  # Setting the Library name
        self.location = location  # Setting the Library location

    def __str__(self):  
        # String representation of Library instance
        return f"Library Name: {self.name}, Location: {self.location}"

    def __repr__(self):  
        # Representation of Library instance
        return f'Library(name={self.name}, location={self.location})'
    
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

    @property  
    # Getter method for location property
    def location(self):
        return self._location

    @location.setter  
    # Setter method for location property
    def location(self, location):
        if isinstance(location, str) and len(location):  
            # Checking if the location is a non-empty string
            self._location = location  # Setting the location
        else:
            raise ValueError("Location must be a non-empty string")

    @classmethod  
    # Class method to create libraries table in the database
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS libraries (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """  # SQL command to create libraries table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    @classmethod  
    # Class method to drop libraries table from the database
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS libraries"  # SQL command to drop libraries table
        CURSOR.execute(sql)  # Executing the SQL command
        CONN.commit()  # Committing changes to the database

    def save(self):
        sql = "INSERT INTO libraries (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        # Method to save Library instance to the database

    def update(self):
        sql = "UPDATE libraries SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()
        # Method to update Library instance in the database

    def delete(self):
        sql = "DELETE FROM libraries WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
        # Method to delete Library instance from the database

    @classmethod  
    # Class method to create a new Library instance and save it to the database
    def create(cls, name, location):
        library = cls(name, location)
        library.save()
        return library

    @classmethod  
    # Class method to create a Library instance from a database row
    def instance_from_db(cls, row):
        library = cls.all.get(row[0])
        if library:
            library.name = row[1]
            library.location = row[2]
        else:
            library = cls(row[1], row[2], row[0])
            cls.all[library.id] = library
        return library

    @classmethod  
    # Class method to retrieve all Library instances from the database
    def get_all(cls):
        sql = "SELECT * FROM libraries"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod  
    # Class method to find a Library instance by name in the database
    def find_by_name(cls, name):
        sql = "SELECT * FROM libraries WHERE name = ?"
        rows = CURSOR.execute(sql, (name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod  
    # Class method to find a Library instance by location in the database
    def find_by_location(cls, location):
        sql = "SELECT * FROM libraries WHERE location = ?"
        rows = CURSOR.execute(sql, (location,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod  
    # Class method to find a Library instance by ID in the database
    def find_by_id(cls, id_):
        CURSOR.execute('SELECT * FROM libraries WHERE id = ?', (id_,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
