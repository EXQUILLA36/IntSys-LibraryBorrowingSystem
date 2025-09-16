from database import library as db

class DisplayBooks:
    def display(self):
        books = db.get_all_books()
    
        if books:
            print("______Books available in the library______")
            for book in books:
                print(f"📕 ID: {book[0]}, 🔎Status: {book[4]} \tTitle: {book[1]}, Author: {book[2]}, Genre: {book[3]}")
        else:
            print("No books found in the library.")
        return True
    
    def show_records(self):
        books = db.get_all_records()
    
        if books:
            print("______Books borrowed in the library______")
            for book in books:
                print(f"📕 ID: {book[0]}, 🔎Book ID: {book[2]} \tBorrowedBy: {book[1]}, Borrowed Date: {book[3]}, Expected Return: {book[4]}, Returned On: {book[5]}")
        else:
            print("No books found in the library.")
        return True
    
    def show_my_records(self, userID):
        books = db.get_user_records(userID)
    
        if books:
            print("______MY RECORD______")
            for book in books:
                print(f"📕 ID: {book[0]}, 🔎Book ID: {book[2]} \tBorrowedBy: {book[1]}, Borrowed Date: {book[3]}, Expected Return: {book[4]}, Returned On: {book[5]}")
        else:
            print("No books found in the library.")
        return True
    
    def search_book(self, keyword):
        books = db.search_book(keyword)
    
        if books:
            print("______Search Results______")
            for book in books:
                print(f"📕 ID: {book[0]}, 🔎Status: {book[4]} \tTitle: {book[1]}, Author: {book[2]}, Genre: {book[3]}")
        else:
            print("No books found matching the keyword.")
        return True
    
    
class BorrowBook:
    def borrow(self, studentID, bookID):
        result =  db.borrow_book(studentID, bookID)
        if result == "success":
            print("✅ Book borrowed successfully.")
            return True
        elif result == "unavailable":
            print("⚠️ This book is already borrowed.")
        elif result == "not_found":
            print("❌ Book not found in the library.")
        else:
            print("❌ An error occurred while borrowing the book.")
        return False
        
class ReturnBook:
    def return_book(self, studentID, bookID):
        result =  db.return_book(studentID, bookID)
        if result == "success":
            print("✅ Book returned successfully.")
            return True
        elif result == "unavailable":
            print("⚠️ This book is already available.")
        elif result == "not_found":
            print("❌ Book not found in the library.")
        elif result == "not_borrowed_by_you":
            print("❌ Book is not recorded in you.")
        else:
            print("❌ An error occurred while returning the book.")
        return False
        

class AddBook:
    def add_to_db(self):
        self.bookTitle = input("Enter Book Title: ")
        self.bookAuthor = input("Enter Book Author: ")
        self.bookGenre = input("Enter Book Genre: ")
        self.bookStatus = "Available"
        
        if db.add_book(self.bookTitle, self.bookAuthor, self.bookGenre, self.bookStatus):
            print("Book added successfully.")
            return True
        return False