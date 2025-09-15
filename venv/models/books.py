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

class AddBook:
    def add_to_db(self):
        self.bookId = input("Enter Book ID: ")
        self.bookTitle = input("Enter Book Title: ")
        self.bookAuthor = input("Enter Book Author: ")
        self.bookGenre = input("Enter Book Genre: ")
        self.bookStatus = "Available"
        
        if db.add_book(self.bookId, self.bookTitle, self.bookAuthor, self.bookGenre, self.bookStatus):
            print("Book added successfully.")
            return True
        return False