from helpers import (
    exit_program,
    display_authors,
    display_author_by_name,
    create_author,
    update_author,
    delete_author,
    display_books,
    display_book_by_author,
    create_book,
    update_book,
    delete_book,
    display_borrowinghistory,
    display_borrowinghistory_by_user_id,
    list_book_borrowing_history,
    list_user_borrowing_history,
    create_borrowinghistory,
    update_borrowinghistory,
    delete_borrowinghistory,
    display_categories,
    display_category_by_name,
    create_category,
    update_category,
    delete_category,
    display_libraries,
    display_library_by_name,
    create_library,
    update_library,
    delete_library,
    display_users,
    display_user_by_username,
    create_user,
    update_user,
    delete_user,
    

)
def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            author_menu()
        elif choice == "2":
            book_record()
        elif choice =="3":
            category_record()
        elif choice =="4":
            borrowinghistory_record()    
        elif choice == "5":
            library_record() 
        elif choice == "6":
            user_record()    

        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("Welcome to Library Management System (LMS)")
    print("Please select a category:")
    print("1. Author Records")
    print("2. Book Records")
    print("3. Category Records")
    print("4. BorrowingHistory Records")
    print("5. Library Records")
    print("6. User Records")
    print("7. Exit the system")

def author_menu():
    while True:
        print("\nAuthor Records Menu:")
        print("1. Display all authors")
        print("2. Display author by name")
        print("3. Create author")
        print("4.Update  author")
        print("5. Delete author")
        print("6. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_authors()
        elif choice == "2":
            display_author_by_name()
        elif choice == "3":
            create_author()
        elif choice =="4":
            update_author()    
        elif choice == "5":
            delete_author()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def book_record():
     while True:
        print("\nBook Records Menu:")
        print("1. Display all books")
        print("2. Display book by author")
        print("3. Create book")
        print("4. Update book")
        print("5. Delete book")
        print("6. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_books()
        elif choice == "2":
            display_book_by_author()
        elif choice == "3":
            create_book()
        elif choice == "4":
            update_book()    
        elif choice == "5":
            delete_book()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
        
def category_record():
     while True:
        print("\nCategory Records Menu:")
        print("1. Display all category")
        print("2. Display category by name")
        print("3. Create category")
        print("4. Update catergory")
        print("5. Delete category")
        print("6. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_categories()
        elif choice == "2":
            display_category_by_name()
        elif choice == "3":
            create_category()
        elif choice =="4":
            update_category()
        elif choice == "5":
           delete_category  ()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def library_record():
    while True:
        print("\nLibrary Records Menu:")
        print("1. Display all libraries")
        print("2. Display library by name")
        print("3. Create library")
        print("4. Upadate library")
        print("5. Delete library")
        print("6. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_libraries()
        elif choice == "2":
            display_library_by_name()
        elif choice == "3":
            create_library()
        elif choice=="4":
            update_library()    
        elif choice == "5":
            delete_library()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")  
def user_record():
     while True:
        print("\nUser Records Menu:")
        print("1. Display all users")
        print("2. Display user by username")
        print("3. Create user")
        print("4. Update user")
        print("5. Delete user")
        print("6. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_users()
        elif choice == "2":
            display_user_by_username()
        elif choice == "3":
            create_user()
        elif choice=="4":
            update_user()   
        elif choice == "5":
           delete_user()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
def borrowinghistory_record():
     while True:
        print("\nBorrowingHistory Records Menu:")
        print("1. Display all borrowinghistories")
        print("2. Display borrowinghistory by user_id")
        print("3. List all borrowinghistories  for a book")
        print("4. List all borrowinghistories  for a user")
        print("5. Create borrowinghistoy")
        print("6. Update borrowhistory")
        print("7. Delete borrowinghistory")
        print("8. Return to main menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_borrowinghistory()
        elif choice == "2":
            display_borrowinghistory_by_user_id()
        elif choice =="3":
            list_book_borrowing_history()  
        elif choice =="4":
            list_user_borrowing_history()      
        elif choice == "5":
            create_borrowinghistory()
        elif choice =="6":
            update_borrowinghistory()    
        elif choice == "7":
            delete_borrowinghistory()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")
                    


# Start the program
if __name__ == "__main__":
    main()
