from models.author import Author
from models.book import Book
from models.borrowinghistory import BorrowingHistory
from models.library import Library
from models.category import Category
from models.user import User

def helper_1():
    print("Performing useful function#1.")

# Function to exit the program
def exit_program():
    print("Goodbye!")
    exit()

# Function to display all authors
def display_authors():
    authors = Author.get_all()  # Fetch all authors from the database
    for author in authors:
        print(author)  # Print each author

# Function to display author by name
def display_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)  # Find author by name
    print(author) if author else print(f'Author {name} not found')

# Function to create a new author
def create_author():
    name = input("Enter the author's name: ")
    try:
        author = Author.create(name)  # Create new author
        print(f'Success: Author {author.name} created')
    except Exception as exc:
        print("Error creating author:", exc)

# Function to update author details
def update_author():
    id_ = int(input("Enter Author ID: "))
    if author := Author.find_by_id(id_):  # Check if author exists
        try:
            name = input("Enter the Author's Name: ")
            author.name = name  # Update author's name
            author.update()  # Update author in the database

            print(f"Author successfully updated: {author}")
        except Exception as exc:
            print("Error Updating Author", exc)
    else:
        print(f"Author with ID: {id_} not found")

# Function to delete an author
def delete_author():
    id_ = input("Enter the author's id: ")
    if author := Author.find_by_id(id_):  # Check if author exists
        author.delete()  # Delete author from the database
        print(f'Author with ID {id_} deleted')
    else:
        print(f'Author with ID {id_} not found')

# Function to display all books
def display_books():
    books = Book.get_all()  # Fetch all books from the database
    if books:
        for book in books:
            print(book)  # Print each book
    else:
        print("No books available.")

# Function to display books by author
def display_book_by_author():
    author = input("Enter the book's author: ")
    books = Book.find_by_author(author)  # Find books by author
    if books:
        for book in books:
            print(book)  # Print each book found
    else:
        print(f'No books found by author {author}.')

# Function to create a new book
def create_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre = input("Enter the book's genre: ")
    # Input validation for year and price
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
        book = Book.create(title, author, genre, year, price)  # Create new book
        print(f'Success: Book "{book.title}" by {book.author} added')
    except Exception as exc:
        print("Error creating book:", exc)

# Function to update book details
def update_book():
    book_id = int(input("Enter Book ID: "))
    if book := Book.find_by_id(book_id):  # Check if book exists
        try:
            title = input("Enter the Book's Title: ")
            book.title = title  # Update book's title
            author = input("Enter the Book's Author: ")
            book.author = author  # Update book's author
            genre = input("Enter the Book's Genre: ")
            book.genre = genre  # Update book's genre
            year = int(input("Enter the Book's Year: "))
            book.year = year  # Update book's year
            price = float(input("Enter the Book's Price: "))
            book.price = price  # Update book's price
            book.update()  # Update book in the database

            print(f"Book successfully updated: {book}")
        except Exception as exc:
            print("Error Updating Book", exc)
    else:
        print(f"Book with ID: {book_id} not found")

# Function to delete a book
def delete_book():
    id_ = input("Enter the book's ID: ")
    if book := Book.find_by_id(id_):  # Check if book exists
        book.delete()  # Delete book from the database
        print(f'Book with ID {id_} deleted.')
    else:
        print(f'Book with ID {id_} not found.')

# Function to display all borrowing histories
def display_borrowinghistory():
    borrowing_history = BorrowingHistory.get_all()  # Fetch all borrowing histories from the database
    for history in borrowing_history:
        print(history)  # Print each borrowing history

# Function to display borrowing histories by user ID
def display_borrowinghistory_by_user_id():
    user_id = input("Enter the borrowinghistory's user_id: ")
    history = BorrowingHistory.find_by_user_id(user_id)  # Find borrowing histories by user ID
    print(history) if history else print(f' Borrowinghistory for user ID {user_id} not found')

# Function to create a new borrowing history
def create_borrowinghistory():
    user_id = input("Enter the user ID: ")
    book_id = input("Enter the book ID: ")
    borrowed_date = input("Enter the borrowed date (YYYY-MM-DD): ")
    return_date = input("Enter the return date (YYYY-MM-DD): ")
    try:
        history = BorrowingHistory.create(user_id, book_id, borrowed_date, return_date)  # Create new borrowing history
        print(f'Success: BorrowingHistory created for User ID {history.user_id}, '
              f'Book ID {history.book_id}, Borrowed Date {history.borrowed_date}, '
              f'Return Date {history.return_date}')
    except Exception as exc:
        print("Error creating borrowing history:", exc)

# Function to list borrowing histories for a book
def list_book_borrowing_history():
    book_id = int(input("Enter Book ID: "))
    book = Book.find_by_id(book_id)
    
    if book:
        borrowing_history = book.borrowing_history()  # Get borrowing histories for the book
        if borrowing_history:
            print(f"BorrowHistory for book :{book.title} by {book.author}")
            for history in borrowing_history:
                print(history)  # Print each borrowing history
        else:
            print(f"No borrowingHistory found for book: {book.title} by {book.author}")
    else:
        print(f"Book with ID {book_id} not found.")

# Function to list borrowing histories for a user
def list_user_borrowing_history():
    user_id = int(input("Enter User ID: "))
    user = User.find_by_id(user_id)
    
    if user:
        borrowing_history = user.borrowing_history()  # Get borrowing histories for the user
        if borrowing_history:
            print(f"BorrowHistory for user :{user.username} {user.email}")
            for history in borrowing_history:
                print(history)  # Print each borrowing history
        else:
            print(f"No borrowingHistory found for user: {user.username} {user.email}")
    else:
        print(f"User with ID {user_id} not found.")

# Function to update borrowing history details
def update_borrowinghistory():
    history_id = int(input("Enter Borrowing History ID: "))
    if history := BorrowingHistory.find_by_id(history_id):  # Check if borrowing history exists
        try:
            user_id = int(input("Enter User ID: "))
            history.user_id = user_id  # Update user ID
            book_id = int(input("Enter Book ID: "))
            history.book_id = book_id  # Update book ID
            borrowed_date = input("Enter Borrowed Date (YYYY-MM-DD): ")
            history.borrowed_date = borrowed_date  # Update borrowed date
            return_date = input("Enter Return Date (YYYY-MM-DD) or leave empty if not returned yet: ")
            history.return_date = return_date if return_date else None  # Update return date
            history.update()  # Update borrowing history in the database

            print(f"Borrowing History successfully updated: {history}")
        except Exception as exc:
            print("Error Updating Borrowing History", exc)
    else:
        print(f"Borrowing History with ID: {history_id} not found")

# Function to delete a borrowing history
def delete_borrowinghistory(): 
    id_ = input("Enter the borrowing history's id: ")
    if history := BorrowingHistory.find_by_id(id_):  # Check if borrowing history exists
        history.delete()  # Delete borrowing history from the database
        print(f'Borrowing History with ID {id_} deleted')
    else:
        print(f'Borrowing History with ID {id_} not found')

# Function to display all categories
def display_categories():
    categories = Category.get_all()  # Fetch all categories from the database
    for category in categories:
        print(category)  # Print each category

# Function to display category by name
def display_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)  # Find category by name
    print(category) if category else print(f' Category {name} not found')

# Function to create a new category
def create_category():
    name = input("Enter the category's name: ")
    try:
        category = Category.create(name)  # Create a new category
        print(f'Success: Category {category.name} created.')
    except Exception as exc:
        print("Error creating category:", exc)

# Function to update category details
def update_category():
    category_id = int(input("Enter Category ID: "))
    if category := Category.find_by_id(category_id):  # Check if category exists
        try:
            name = input("Enter the Category's Name: ")
            category.name = name  # Update category name
            category.update()  # Update category in the database

            print(f"Category successfully updated: {category}")
        except Exception as exc:
            print("Error Updating Category", exc)
    else:
        print(f"Category with ID: {category_id} not found")

# Function to delete a category
def delete_category(): 
    id_ = input("Enter the category's ID: ")
    if category := Category.find_by_id(id_):  # Check if category exists
        category.delete()  # Delete category from the database
        print(f'Category with ID {id_} deleted')
    else:
        print(f'Category with ID {id_} not found')

# Function to display all libraries
def display_libraries():
    libraries = Library.get_all()  # Fetch all libraries from the database
    for library in libraries:
        print(library)  # Print each library

# Function to display library by name
def display_library_by_name():
    name = input("Enter the library's name: ")
    library = Library.find_by_name(name)  # Find library by name
    print(library) if library else print(f' Library {name} not found')

# Function to create a new library
def create_library():
    name = input("Enter the library's name: ")
    location = input("Enter the library's location: ")
    try:
        library = Library.create(name, location)  # Create a new library
        print(f'Success: Library {library.name} created at {library.location}')
    except Exception as exc:
        print("Error creating library:", exc)

# Function to update library details
def update_library():
    library_id = int(input("Enter Library ID: "))
    if library := Library.find_by_id(library_id):  # Check if library exists
        try:
            name = input("Enter the Library's Name: ")
            library.name = name  # Update library name
            location = input("Enter the Library's Location: ")
            library.location = location  # Update library location
            library.update()  # Update library in the database

            print(f"Library successfully updated: {library}")
        except Exception as exc:
            print("Error Updating Library", exc)
    else:
        print(f"Library with ID: {library_id} not found")

# Function to delete a library
def delete_library(): 
    id_ = input("Enter the library's ID: ")
    if library := Library.find_by_id(id_):  # Check if library exists
        library.delete()  # Delete library from the database
        print(f'Library with ID {id_} deleted')
    else:
        print(f'Library with ID {id_} not found')

# Function to display all users
def display_users():
    users = User.get_all()  # Fetch all users from the database
    for user in users:
        print(user)  # Print each user

# Function to display user by username
def display_user_by_username():
    username = input("Enter the user's username: ")
    user = User.find_by_username(username)  # Find user by username
    print(user) if user else print(f' User {username} not found')

# Function to create a new user
def create_user():
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    try:
        user = User.create(username, email, password)  # Create a new user
        print(f'Success: User {user.username} created with email {user.email}')
    except Exception as exc:
        print("Error creating user:", exc)

# Function to update user details
def update_user():
    user_id = int(input("Enter User ID: "))
    if user := User.find_by_id(user_id):  # Check if user exists
        try:
            username = input("Enter the User's Username: ")
            user.username = username  # Update username
            email = input("Enter the User's Email: ")
            user.email = email  # Update email
            password = input("Enter the User's Password: ")
            user.password = password  # Update password
            user.update()  # Update user in the database

            print(f"User successfully updated: {user}")
        except Exception as exc:
            print("Error Updating User", exc)
    else:
        print(f"User with ID: {user_id} not found")

# Function to delete a user
def delete_user(): 
    id_ = input("Enter the user's ID: ")
    if user := User.find_by_id(id_):  # Check if user exists
        user.delete()  # Delete user from the database
        print(f'User with ID {id_} deleted')
    else:
        print(f'User with ID {id_} not found')

# The main function that runs the program
# The main function that runs the program
def main():
    while True:
        main_menu()  # Display the main menu
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_authors()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            manage_borrowing_history()
        elif choice == '4':
            manage_categories()
        elif choice == '5':
            manage_libraries()
        elif choice == '6':
            manage_users()
        elif choice == '7':
            exit_program()
        else:
            print("Invalid choice. Please enter a valid option.")

# Function to display the main menu options
def main_menu():
    print("\n=== Main Menu ===")
    print("1. Manage Authors")
    print("2. Manage Books")
    print("3. Manage Borrowing History")
    print("4. Manage Categories")
    print("5. Manage Libraries")
    print("6. Manage Users")
    print("7. Exit Program")

# Function to manage author-related operations
def manage_authors():
    while True:
        author_menu()  # Display author menu
        choice = input("Enter your choice: ")
        if choice == '1':
            display_authors()
        elif choice == '2':
            display_author_by_name()
        elif choice == '3':
            create_author()
        elif choice == '4':
            update_author()
        elif choice == '5':
            delete_author()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Function to display the author menu options
def author_menu():
    print("\n=== Author Menu ===")
    print("1. Display All Authors")
    print("2. Display Author by Name")
    print("3. Create New Author")
    print("4. Update Author")
    print("5. Delete Author")
    print("6. Back to Main Menu")

# Similarly, you can define functions for managing books, borrowing history, categories, libraries, and users.

if __name__ == "__main__":
    main()  # Call the main function to start the program



