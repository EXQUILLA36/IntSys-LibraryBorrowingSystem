from database.library import setup_database
from models.log_reg import Login
from models.log_reg import Register
from models.books import DisplayBooks
from models.books import AddBook
from models.books import BorrowBook
from models.books import ReturnBook
import database.library as db

login = False
current_user = None

def menu():
    choice = input("\n--------Welcome to the Library System--------\n1. Login\n2. Register\n3. Exit\nSelect an option: ")
    return choice

def homepage():
    if login_instance.authenticated:
        choice = input("\n--------Welcome to the Library System--------\n1. Display Books\n2. Search Book\n3. Borrow a Book\n4. Return a Book\n5. My Borrow Record\n6. Borrowing record\n7. Add Book\n8. Delete Everything\n9. Exit\nSelect an option: ")
    else:
        menu()
    
    match choice:
        case "1":
            display_books_instance = DisplayBooks()
            display_books_instance.display()
        case "2":
            bookSearch = input("Search Title: ")
            display_books_instance = DisplayBooks()
            display_books_instance.search_book(bookSearch)
        case "3":
            bookID = input("Enter the Book ID to borrow: ")
            borrow_book_instance = BorrowBook()
            borrow_book_instance.borrow(current_user, bookID)
        case "4":
            bookID = input("Enter the Book ID to return: ")
            borrow_book_instance = ReturnBook()
            borrow_book_instance.return_book(current_user, bookID)
        case "5":
            display_books_instance = DisplayBooks()
            display_books_instance.show_my_records(current_user)
        case "6":
            display_books_instance = DisplayBooks()
            display_books_instance.show_records()
        case "7":
            print("Adding a book...")
            add_book_instance = AddBook()
            add_book_instance.add_to_db()
        case "8":
            print("Dropping Tables...")
            db.drop_book_tables()
        case "9":
            print("Exiting to main menu...")
            global login
            login = False
            menu()
    return choice

def user_login(name=None, pwd=None):
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    return username, password

def user_register(id=None, name=None, pwd=None):
    id = input("Enter your id: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return id, username, password

if __name__ == "__main__":
    setup_database()
    while True:
        if login == True:
            homepage()
        else:
            match menu():
                case "1":
                    username, password = user_login()
                    login_instance = Login(username, password)
                    if login_instance.authenticated:
                        current_user = login_instance.studId
                        print("Login successful. Welcome to the library!")
                        login = True
                    else:
                        print("Login failed. Invalid credentials.")
                case "2":
                    id, username, password = user_register()
                    register_instance = Register(id, username, password)
                case "3":
                    print("Exiting the system. Goodbye!")
                    break
                case _:
                    print("Invalid option. Please select 1 or 2.")
                