# lib/helpers.py
from models.author import Author
from models.book import Book
from models.author import Author
from models.borrowinghistory import BorrowingHistory
from models.library import Library
from models.category import Category
from models.user import User

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def display_authors():
    # Fetch all phones from the database
    authors = Author.get_all()
    for author in authors:
        print(author)

    pass
def display_author_by_name():
    name= input("Enter the author's name: ")
    name =Author.find_by_name(name)
    print(name) if name else print(
        f' Author {name} not found')
    pass


def create_author():
    name= input("Enter the author's name: ")
    try:
        author = Author.create(name,)
        print(f'Success: Author {author.name} ')
    except Exception as exc:
        print("Error creating author:", exc)
def update_author():
    id_ = int(input("Enter Author ID: "))
    if author := Author.find_by_id(id_):
        try:
            name = input("Enter the Author's Name: ")
            author.name = name
            author.update()

            print(f"Author successfully updated: {author}")
        except Exception as exc:
            print("Error Updating Author", exc)
    else:
        print(f"Author with ID: {id_} not found")


def delete_author(): 
    id_ = input("Enter the author's id: ")
    if author := Author.find_by_id(id_):
        author.delete()
        print(f'Author in id{id_} deleted')
    else:
        print(f'Author in id {id_} not found')
    pass










def display_books():
    # Fetch all books from the database
    books = Book.get_all()
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

def display_book_by_author():
    author = input("Enter the book's author: ")
    books = Book.find_by_author(author)
    if books:
        for book in books:
            print(book)
    else:
        print(f'No books found by author {author}.')

def create_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre = input("Enter the book's genre: ")
    
    try:
        year = int(input("Enter the book's publication year: "))
        if year < 0:
            raise ValueError("Year must be a non-negative number")
    except ValueError as e:
        print(f"Invalid year input: {e}")
        return

    try:
        price = float(input("Enter the book's price: "))
        if price < 0:
            raise ValueError("Price must be a non-negative number")
    except ValueError as e:
        print(f"Invalid price input: {e}")
        return

    try:
        book = Book.create(title, author, genre, year, price)
        print(f'Success: Book "{book.title}" by {book.author} added')
    except Exception as exc:
        print("Error creating book:", exc)
def update_book():
    book_id = int(input("Enter Book ID: "))
    if book := Book.find_by_id(book_id):
        try:
            title = input("Enter the Book's Title: ")
            book.title = title
            author = input("Enter the Book's Author: ")
            book.author = author
            genre = input("Enter the Book's Genre: ")
            book.genre = genre
            year = int(input("Enter the Book's Year: "))
            book.year = year
            price = float(input("Enter the Book's Price: "))
            book.price = price
            book.update()

            print(f"Book successfully updated: {book}")
        except Exception as exc:
            print("Error Updating Book", exc)
    else:
        print(f"Book with ID: {book_id} not found")        

def delete_book():
    id_ = input("Enter the book's ID: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'Book with ID {id_} deleted.')
    else:
        print(f'Book with ID {id_} not found.')



def display_borrowinghistory():
    # Fetch all phones from the database
    borrowing_history = BorrowingHistory.get_all()
    for borrowing_history in borrowing_history:
        print(borrowing_history)

    pass
def display_borrowinghistory_by_user_id():
    user_id= input("Enter the borrowinghistory's user_id: ")
    borrowinghistory =BorrowingHistory.find_by_user_id(user_id)
    print(borrowinghistory) if borrowinghistory else print(
        f' Borrowinghistory {borrowinghistory} not found')
    pass

def create_borrowinghistory():
    user_id = input("Enter the user ID: ")
    book_id = input("Enter the book ID: ")
    borrowed_date = input("Enter the borrowed date (YYYY-MM-DD): ")
    return_date = input("Enter the return date (YYYY-MM-DD): ")
    try:
        borrowing_history = BorrowingHistory.create(user_id, book_id, borrowed_date, return_date)
        print(f'Success: BorrowingHistory created for User ID {borrowing_history.user_id}, '
              f'Book ID {borrowing_history.book_id}, Borrowed Date {borrowing_history.borrowed_date}, '
              f'Return Date {borrowing_history.return_date}')
    except Exception as exc:
        print("Error creating borrowing history:", exc)

def list_book_borrowing_history():
    book_id = int(input("Enter Book ID: "))
    book= Book.find_by_id(book_id)
    
    if book:
        borrowing_history = book.borrowing_history()
        if borrowing_history:
            print(f"BorrowHistory for book :{book.author} {book.genre}")
            for borrowing_history in borrowing_history :
                print(borrowing_history)
               
        else:
            print(f"No borrowingHistory found for book: {book.author} {book.genre}")
    else:
        print(f"Book with ID {book_id} not found.")

def list_user_borrowing_history():
    user_id = int(input("Enter User ID: "))
    user= User.find_by_id(user_id)
    
    if user:
        borrowing_history = user.borrowing_history()
        if borrowing_history:
            print(f"BorrowHistory for user :{user.username} {user.email}")
            for borrowing_history in borrowing_history :
                print(borrowing_history)
               
        else:
            print(f"No borrowingHistory found for user: {user.username} {user.email}")
    else:
        print(f"User with ID {user_id} not found.")       
def update_borrowinghistory():
    history_id = int(input("Enter Borrowing History ID: "))
    if history := BorrowingHistory.find_by_id(history_id):
        try:
            user_id = int(input("Enter User ID: "))
            history.user_id = user_id
            book_id = int(input("Enter Book ID: "))
            history.book_id = book_id
            borrowed_date = input("Enter Borrowed Date (YYYY-MM-DD): ")
            history.borrowed_date = borrowed_date
            return_date = input("Enter Return Date (YYYY-MM-DD) or leave empty if not returned yet: ")
            history.return_date = return_date if return_date else None
            history.update()

            print(f"Borrowing History successfully updated: {history}")
        except Exception as exc:
            print("Error Updating Borrowing History", exc)
    else:
        print(f"Borrowing History with ID: {history_id} not found")        
def delete_borrowinghistory(): 
    id_ = input("Enter the category's id: ")
    if borrowinghistory := BorrowingHistory.find_by_id(id_):
        borrowinghistory.delete()
        print(f'BorrowingHistory in id{id_} deleted')
    else:
        print(f'BorrowingHistory in id {id_} not found')
    pass       














def display_categories():
    # Fetch all phones from the database
    category = Category.get_all()
    for category in category:
        print(category)

    pass
def display_category_by_name():
    name= input("Enter the category's name: ")
    category =Category.find_by_name(name)
    print(category) if category else print(
        f' Category {category} not found')
    pass

def create_category():
    name= input("Enter the category's name: ")
    try:
        category = Category.create(name,)
        print(f'Success: Category {category.name} ')
    except Exception as exc:
        print("Error creating category:", exc)
def update_category():
    category_id = int(input("Enter Category ID: "))
    if category := Category.find_by_id(category_id):
        try:
            name = input("Enter the Category's Name: ")
            category.name = name
            category.update()

            print(f"Category successfully updated: {category}")
        except Exception as exc:
            print("Error Updating Category", exc)
    else:
        print(f"Category with ID: {category_id} not found")        
def delete_category(): 
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        category.delete()
        print(f'Category in id{id_} deleted')
    else:
        print(f'Category in id {id_} not found')
    pass       










def display_libraries():
    # Fetch all phones from the database
    library = Library.get_all()
    for library in library:
        print(library)

    pass
def display_library_by_name():
    name= input("Enter the library name: ")
    name =Library.find_by_name(name)
    print(name) if name else print(
        f' Library {name} not found')
    pass


def create_library():
    name = input("Enter the library's name: ")
    location = input("Enter the library's location: ")
    try:
        library = Library.create(name, location)
        print(f'Success: Library {library.name}, Location: {library.location}')
    except Exception as exc:
        print("Error creating library:", exc)

def update_library():
    library_id = int(input("Enter Library ID: "))
    if library := Library.find_by_id(library_id):
        try:
            name = input("Enter the Library's Name: ")
            library.name = name
            location = input("Enter the Library's Location: ")
            library.location = location
            library.update()

            print(f"Library successfully updated: {library}")
        except Exception as exc:
            print("Error Updating Library", exc)
    else:
        print(f"Library with ID: {library_id} not found")
    

def delete_library(): 
    id_ = input("Enter the library's id: ")
    if library := Library.find_by_id(id_):
        library.delete()
        print(f'Library in id{id_} deleted')
    else:
        print(f'Library in id {id_} not found')
    pass

def display_users():
    # Fetch all users from the database
    user = User.get_all()
    for user in user:
        print(user)

    pass
def display_user_by_username():
    username= input("Enter the user username: ")
    user=User.find_by_username(username)
    print(user) if user else print(
        f' User {user} not found')
    pass


def create_user():
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    try:
        user = User.create(username, email, password)
        print(f'Success: User {user.username}, Email: {user.email} ,Password{user.password}')
    except Exception as exc:
        print("Error creating user:", exc)


def update_user():
    user_id = int(input("Enter User ID: "))
    if user := User.find_by_id(user_id):
        try:
            username = input("Enter the User's Username: ")
            user.username = username
            email = input("Enter the User's Email: ")
            user.email = email
            password = input("Enter the User's Password: ")
            user.password = password
            user.update()

            print(f"User successfully updated: {user}")
        except Exception as exc:
            print("Error Updating User", exc)
    else:
        print(f"User with ID: {user_id} not found")
    

def delete_user(): 
    id_ = input("Enter the user's id: ")
    if user:= User.find_by_id(id_):
        user.delete()
        print(f'User in id{id_} deleted')
    else:
        print(f'User in id {id_} not found')
    pass








