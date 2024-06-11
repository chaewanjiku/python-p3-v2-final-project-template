# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()

import click
from app.models import Session, create_author, get_all_authors, find_author_by_id, update_author, delete_author, create_book, get_all_books, find_book_by_id, update_book, delete_book

session = Session()

@click.group()
def cli():
    pass

# Author commands
@cli.group()
def author():
    pass

@author.command()
@click.option('--name', prompt='Author name')
def add(name):
    author = create_author(name)
    click.echo(f'Author "{author.name}" added.')

@author.command()
def list():
    authors = get_all_authors()
    for author in authors:
        click.echo(f'{author.id}: {author.name}')

# Book commands
@cli.group()
def book():
    pass

@book.command()
@click.option('--title', prompt='Book title')
@click.option('--author-id', prompt='Author ID', type=int)
def add(title, author_id):
    book = create_book(title, author_id)
    click.echo(f'Book "{book.title}" added.')

@book.command()
def list():
    books = get_all_books()
    for book in books:
        click.echo(f'{book.id}: {book.title} (Author ID: {book.author_id})')

if __name__ == '__main__':
    cli()
