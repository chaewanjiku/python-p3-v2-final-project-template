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

def delete_author(): 
    id_ = input("Enter the author's id: ")
    if author := Author.find_by_id(id_):
        author.delete()
        print(f'Author in id{id_} deleted')
    else:
        print(f'Author in id {id_} not found')
    pass










def display_books():
    # Fetch all phones from the database
    book = Book.get_all()
    for book in book:
        print(book)

    pass
def display_book_by_author():
    author= input("Enter the books author: ")
    book =Book.find_by_author(author)
    print(book) if book else print(
        f' Author {author} not found')
    pass


def create_book():
    name= input("Enter the book's name: ")
    try:
        book = Book.create(name,)
        print(f'Success: Book {book.name} ')
    except Exception as exc:
        print("Error creating book:", exc)

def delete_book(): 
    id_ = input("Enter the book's id: ")
    if author := Author.find_by_id(id_):
        author.delete()
        print(f'Author in id{id_} deleted')
    else:
        print(f'Author in id {id_} not found')
    pass


