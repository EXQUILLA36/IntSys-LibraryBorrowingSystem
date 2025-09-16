from datetime import datetime, timedelta
import sqlite3


#           __________-------____                 ____-------__________
#           \------____-------___--__---------__--___-------____------/
#            \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/
#              \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/
#                --//// / /  /  //|| (O)\ /(O) ||\\  \  \ \ \\\\--
#                     ---__/  // /| \_  /V\  _/ |\ \\  \__---
#                          -//  / /\_ ------- _/\ \  \\-
#                            \_/_/ /\---------/\ \_\_/
#                                ----\   |   /----
#                                     | -|- |
#                                    /   |   \
#                                    ---- \___|


conn = sqlite3.connect('Library.db')
c = conn.cursor()

print("Database connected successfully.")

def setup_database():
    c.execute('''CREATE TABLE IF NOT EXISTS studAcc
            (
                id VARCHAR(15) PRIMARY KEY,
                studName TEXT,
                studPsw VARCHAR(50)
            )''')

    c.execute('''CREATE TABLE IF NOT EXISTS books
                (
                    bookID INTEGER PRIMARY KEY AUTOINCREMENT,
                    bookTitle TEXT,
                    bookAuthor TEXT,
                    bookGenre VARCHAR(30),
                    bookStatus VARCHAR(20))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS borrowRecord
                (
                    recordID INTEGER PRIMARY KEY AUTOINCREMENT,
                    studentID VARCHAR(15),
                    bookID VARCHAR(15),
                    borrowDate TEXT,
                    returnDate TEXT,
                    returnActualDate TEXT,
                    FOREIGN KEY (bookID) REFERENCES books(bookID),
                    FOREIGN KEY (studentID) REFERENCES studAcc(id)
                )''')
    

print("Database and table created successfully.")

def login_account(username, password):
    c.execute('SELECT * FROM studAcc WHERE studName=? AND studPsw=?', (username, password))
    result = c.fetchone()
    return result
        
def register_account(studId, studName, studPsw):
    try:
        c.execute(
            '''INSERT INTO studAcc (id, studName, studPsw) VALUES (?, ?, ?)''',
            (studId, studName, studPsw)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False    
    
def get_all_books():
    try:
        c.execute("SELECT * FROM books")
        rows = c.fetchall()
        return rows
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    
def get_all_records():
    try:
        c.execute("SELECT * FROM borrowRecord")
        rows = c.fetchall()
        return rows
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    
def borrow_book(studentID, bookID):
    try:
        
        c.execute("SELECT bookStatus FROM books WHERE bookID=?", (bookID,))
        row = c.fetchone()

        if not row:
            return "not_found"
        elif row[0] == "Borrowed":
            return "unavailable"
        
        borrow_date = datetime.now()
        return_date = borrow_date + timedelta(days=4)

        borrow_date_str = borrow_date.strftime("%Y-%m-%d")
        return_date_str = return_date.strftime("%Y-%m-%d")

        c.execute(
            "INSERT INTO borrowRecord (studentID, bookID, borrowDate, returnDate) VALUES (?, ?, ?, ?)",
            (studentID, bookID, borrow_date_str, return_date_str)
        )
        c.execute("UPDATE books SET bookStatus='Borrowed' WHERE bookID=?", (bookID,))
        conn.commit()
        return "success"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "error"
    
def return_book(studentID, bookID):
    try:
        
        c.execute("""
            SELECT * FROM borrowRecord 
            WHERE studentID=? AND bookID=? AND returnActualDate IS NULL
        """, (studentID, bookID))
        record = c.fetchone()

        if not record:
            return "not_borrowed_by_you"
        
        return_date = datetime.now()
        return_date_str = return_date.strftime("%Y-%m-%d")
        
        c.execute("SELECT bookStatus FROM books WHERE bookID=?", (bookID,))
        row = c.fetchone()

        if not row:
            return "not_found" ""

        c.execute("""
            UPDATE borrowRecord SET returnActualDate=? WHERE studentID=? AND bookID=? AND returnActualDate IS NULL""", 
            (return_date_str, studentID, bookID)
        )
        c.execute("UPDATE books SET bookStatus='Available' WHERE bookID=?", (bookID,))
        conn.commit()
        return "success"
    except Exception as e:
        print(f"Error occurred: {e}")
        return "error"
        
def add_book(bookTitle, bookAuthor, bookGenre, bookStatus):
    try:
        c.execute('''INSERT INTO books (bookTitle, bookAuthor, bookGenre, bookStatus) VALUES (?, ?, ?, ?)''', (bookTitle, bookAuthor, bookGenre, bookStatus))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    
def get_user_records(studentID):
    try:
        c.execute("SELECT * FROM borrowRecord WHERE studentID=?", (studentID,))
        rows = c.fetchall()
        return rows
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    
def search_book(search_term):
    try:
        normalized_input = search_term.replace(" ", "").upper()

        c.execute("SELECT * FROM books")
        rows = c.fetchall()

        matches = []
        for row in rows:
            book_title = row[1]
            normalized_title = book_title.replace(" ", "").upper()

            if normalized_input in normalized_title:
                matches.append(row)

        return matches
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    
def drop_book_tables():
    try:
        c.execute("DROP TABLE IF EXISTS books")
        c.execute("DROP TABLE IF EXISTS borrowRecord")

        conn.commit()
        print("All tables dropped successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

    
def close_connection():
    conn.close()