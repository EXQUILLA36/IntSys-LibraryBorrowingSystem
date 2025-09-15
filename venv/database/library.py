import sqlite3

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
                (bookID VARCHAR(15) PRIMARY KEY,
                bookTitle TEXT,
                    bookAuthor TEXT,
                    bookGenre VARCHAR(30),
                    bookStatus VARCHAR(20))''')

print("Database and table created successfully.")

def login_account(username, password):
    c.execute('SELECT * FROM studAcc WHERE studName=? AND studPsw=?', (username, password))
    result = c.fetchone()
    return result is not None
        
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
        
def add_book(bookID, bookTitle, bookAuthor, bookGenre, bookStatus):
    try:
        c.execute(
            '''INSERT INTO books (bookID, bookTitle, bookAuthor, bookGenre, bookStatus) VALUES (?, ?, ?, ?, ?)''',
            (bookID, bookTitle, bookAuthor, bookGenre, bookStatus)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    
def borrow_book(bookID):
    try:
        c.execute("UPDATE books SET bookStatus='Borrowed' WHERE bookID=?", (bookID,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

    
def close_connection():
    conn.close()