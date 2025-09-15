from database.library import setup_database
from models.log_reg import Login
from models.log_reg import Register
from models.books import DisplayBooks
from models.books import AddBook

login = False

def menu():
    choice = input("\n--------Welcome to the Library System--------\n1. Login\n2. Register\n3. Exit\nSelect an option: ")
    return choice

def homepage():
    if login_instance.authenticated:
        choice = input("\n--------Welcome to the Library System--------\n1. Display Books\n2. Borrow a Book\n3. Return a Book\n4. Add Book\n5. Exit\nSelect an option: ")
    else:
        menu()
    
    match choice:
        case "1":
            display_books_instance = DisplayBooks()
            display_books_instance.display()
        case "2":
            print("Borrowing a book...")
        case "3":
            print("Returning a book...")
        case "4":
            print("Adding a book...")
            add_book_instance = AddBook()
            add_book_instance.add_to_db()
        case "5":
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
                