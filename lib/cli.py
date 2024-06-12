from helpers import (
    exit_program,
    display_authors,
    display_author_by_name,
    create_author,
    delete_author,
)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            author_menu()
        elif choice == "2":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("Welcome to Library Management System (LMS)")
    print("Please select a category:")
    print("1. Author Records")
    print("2. Exit the system")

def author_menu():
    while True:
        print("\nAuthor Records Menu:")
        print("1. Display all authors")
        print("2. Display author by name")
        print("3. Create author")
        print("4. Delete author")
        print("5. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_authors()
        elif choice == "2":
            display_author_by_name()
        elif choice == "3":
            create_author()
        elif choice == "4":
            delete_author()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
